import cv2
import numpy as np

class BinarizationTh:
    def segment(self, image, threshold_value):
        """
        Segment an image using a global threshold.

        Args:
            image (numpy.ndarray): The input image.
            threshold_value (int): The threshold value for binarization.

        Returns:
            numpy.ndarray: The binary segmented image.
        """
        if len(image.shape) == 3:
            image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        _, binary_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)
        return binary_image

class AdaptativeTh:
    def segment(self, image, max_value, block_size, C):
        """
        Segment an image using adaptive thresholding.

        Args:
            image (numpy.ndarray): The input image.
            max_value (int): The maximum value for thresholding 255 recomended.
            block_size (int): The size of the neighborhood area.
            C (int): Constant subtracted from the mean.

        Returns:
            numpy.ndarray: The binary segmented image.
        """
        if len(image.shape) == 3:
            image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        binary_image = cv2.adaptiveThreshold(image, max_value, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, block_size, C)
        return binary_image

class OtsuTh:
    def segment(self, image):
        """
        Segment an image using Otsu's thresholding method.

        Args:
            image (numpy.ndarray): The input image.

        Returns:
            numpy.ndarray: The binary segmented image.
        """
        if len(image.shape) == 3:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, binary_image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        return binary_image

class SplitMergeTh:
    def segment(self, image):
        """
        Segment an image using the Split and Merge algorithm.

        Args:
            image (numpy.ndarray): The input image.

        Returns:
            numpy.ndarray: The segmented image.
        """
        if len(image.shape) == 3:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Implement Split and Merge segmentation algorithm using OpenCV
        # You may need to write a custom function for this

        # For example:
        # segmented_image = split_and_merge(image)

        # return segmented_image
        pass 

class WatershedTh:
    def segment(self, image):
        """
        Segment an image using the Watershed algorithm.

        Args:
            image (numpy.ndarray): The input image.

        Returns:
            numpy.ndarray: The segmented image with marked boundaries in blue.
        """
        if len(image.shape) == 3:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret, markers = cv2.connectedComponents(gray_image)

        # Apply the watershed algorithm
        markers = cv2.watershed(image, markers)
        image[markers == -1] = [0, 0, 255]  # Mark boundaries in blue

        return image

class RegionGrowingTh:
    def segment(self, image, seed_point):
        """
        Segment an image using the Region Growing algorithm.

        Args:
            image (numpy.ndarray): The input image.
            seed_point (tuple): The seed point for region growing.

        Returns:
            numpy.ndarray: The segmented image.
        """
        if len(image.shape) == 3:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Implement Region Growing segmentation algorithm using OpenCV
        # You may need to write a custom function for this

        # For example:
        # segmented_image = region_growing(image, seed_point)

        # return segmented_image
        pass
