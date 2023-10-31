import cv2
import numpy as np
from collections import Counter
from scipy.fftpack import idct


class JPEGCompression:
    def __init__(self, quality=70):
        self.quality = quality

    def compress(self, image):
        # Step 1: Convert from RGB to YCrCb
        ycrcb_image = cv2.cvtColor(image, cv2.COLOR_RGB2YCR_CB)
        

        # Step 2: Downsample Cb and Cr channels (if required)
        #ycrcb_image[:, :, 1] = cv2.resize(ycrcb_image[:, :, 1], (0, 0), fx=0.5, fy=0.5)
        #ycrcb_image[:, :, 2] = cv2.resize(ycrcb_image[:, :, 2], (0, 0), fx=0.5, fy=0.5)

        height, width, _ = ycrcb_image.shape
        self.new_height = height - (height % 8)
        self.new_width = width - (width % 8)
        ycrcb_image = ycrcb_image[:self.new_height, :self.new_width]
        self.ycrcb = ycrcb_image

        # Step 3: Divide the image into 8x8 segments
        height, width, _ = ycrcb_image.shape
        segments = []
        for y in range(0, height, 8):
            for x in range(0, width, 8):
                segment = ycrcb_image[y:y+8, x:x+8]
                segments.append(segment)

        # Step 4: Normalize each segment
        segments = [(segment - 128).astype(np.float32) for segment in segments]

        # Step 5: Apply DCT to each segment
        dct_segments = []
        for segment in segments:
            dct_channels = [cv2.dct(segment[:, :, i]) for i in range(3)]
            dct_segments.append(np.stack(dct_channels, axis=-1))

        # Step 6: Quantization
        quantized_segments = []
        for segment in dct_segments:
            quantized_channels = []
            for i in range(3):
                quantization_table = self.get_quantization_table(i, segment.shape[0], segment.shape[1])
                quantized_channel = np.round(segment[:, :, i] / quantization_table * self.quality).astype(np.int16)
                quantized_channels.append(quantized_channel)
            quantized_segments.append(np.stack(quantized_channels, axis=-1))


        # Step 7: Zigzag symbol encoder
        encoded_segments = [self.zigzag_encode(segment) for segment in quantized_segments]

        # Step 8: Run-Length Encoding
        rle_encoded_segments = [self.run_length_encode(segment) for segment in encoded_segments]

        return rle_encoded_segments

    def decompress(self, compressed_data):
        # Inverse of all the compression steps, reconstruct the image

        # Perform reverse Run-Length Decoding
        decoded_segments = [self.run_length_decode(segment) for segment in compressed_data]

        # Perform reverse Zigzag Decoding
        dezigzag_segments = [self.zigzag_decode(segment) for segment in decoded_segments]

        # Reverse Quantization
        dequantized_segments = [self.inverse_quantize(segment) for segment in dezigzag_segments]
        idct_segments = [self.inverse_dct(segment) for segment in dequantized_segments]

        # Denormalize each segment
        denormalized_segments = [(segment + 128).astype(np.uint16) for segment in idct_segments]

        # Reconstruct the 8x8 segments into the original image
        #height, width = denormalized_segments[0].shape[0] * 8, denormalized_segments[0].shape[1] * 8
        height = self.new_height
        width = self.new_width
        decoded_image = np.zeros((height, width, 3), dtype=np.uint16)
        for i in range(len(dezigzag_segments)):
            for j in range(len(dezigzag_segments[i])):
                y, x = i * 8, j * 8
                decoded_image[y:y+8, x:x+8] = denormalized_segments[i][j]




        # Convert YCrCb back to RGB
        decoded_image = cv2.cvtColor(decoded_image, cv2.COLOR_YCrCb2RGB)

        return decoded_image
    
    def inverse_quantize(self, quantized_segment):
        dequantized_segment = np.round(quantized_segment / self.quality).astype(np.float32)
        return dequantized_segment

    def inverse_dct(self, dct_segment):
        idct_channels = [idct(dct_segment[:, :, i], norm='ortho') for i in range(3)]
        idct_segment = np.stack(idct_channels, axis=-1)
        return idct_segment



    def get_quantization_table(self, channel, height, width):
        # Define custom quantization tables for different channels
        if channel == 0:  # Y channel
            quantization_table = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
                                          [12, 12, 14, 19, 26, 58, 60, 55],
                                          [14, 13, 16, 24, 40, 57, 69, 56],
                                          [14, 17, 22, 29, 51, 87, 80, 62],
                                          [18, 22, 37, 56, 68, 109, 103, 77],
                                          [24, 35, 55, 64, 81, 104, 113, 92],
                                          [49, 64, 78, 87, 103, 121, 120, 101],
                                          [72, 92, 95, 98, 112, 100, 103, 99]])
        else:  # Cb and Cr channels
            quantization_table = np.array([[17, 18, 24, 47, 99, 99, 99, 99],
                                          [18, 21, 26, 66, 99, 99, 99, 99],
                                          [24, 26, 56, 99, 99, 99, 99, 99],
                                          [47, 66, 99, 99, 99, 99, 99, 99],
                                          [99, 99, 99, 99, 99, 99, 99, 99],
                                          [99, 99, 99, 99, 99, 99, 99, 99],
                                          [99, 99, 99, 99, 99, 99, 99, 99],
                                          [99, 99, 99, 99, 99, 99, 99, 99]])[:height, :width]
        return quantization_table


    def zigzag_encode(self, data):
        z = np.zeros((64, 3), dtype=np.int16)
        for channel in range(3):
            index = 0
            for i in range(8):
                for j in range(8):
                    z[index, channel] = data[i][j][channel]
                    index += 1
        return z



    def zigzag_decode(self, data):
        z = np.zeros((8, 8, 3), dtype=np.int16)
        index = 0
        for i in range(8):
            for j in range(8):
                if index < len(data):
                    z[i, j] = data[index]
                    index += 1
        return z

    def run_length_encode(self, data):
        rle_encoded = []
        for channel in range(3):
            rle_channel = []
            run = []
            for i in range(64):
                if i == 0:
                    run = [data[i, channel]]
                elif data[i, channel] == data[i - 1, channel]:
                    run.append(data[i, channel])
                else:
                    rle_channel.append((len(run), run[0]))
                    run = [data[i, channel]]
            rle_channel.append((len(run), run[0]))
            rle_encoded.append(rle_channel)
        return rle_encoded


    def run_length_decode(self, data):
        decoded = []
        for channel_data in data:
            for item in channel_data:
                if len(item) == 2:
                    value, count = item
                    decoded.extend([value] * count)
                elif len(item) == 1:
                    value = item[0]
                    decoded.append(value)
                else:
                    raise ValueError("Invalid run-length encoded data")
        return np.array(decoded)


