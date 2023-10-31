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
        image_copy = np.copy(image)
        self.image_copy = image_copy

        gray_image = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

        thresh  = cv2.adaptiveThreshold(gray_image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,499,9)

        kernel = np.ones((5,5),np.uint8)
        opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel,iterations=3)

        kernel = np.ones((3,3),np.uint8)
        opening = cv2.dilate(opening,kernel)

        kernel = np.ones((5,5),np.uint8)
        sure_bg = cv2.dilate(opening,kernel,iterations=3)

        dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,cv2.DIST_MASK_PRECISE)
        ret, sure_fg = cv2.threshold(dist_transform,0.3*dist_transform.max(),255,cv2.THRESH_BINARY)

        sure_fg = np.uint8(sure_fg)
        unknown = cv2.subtract(sure_bg,sure_fg)

        ret, markers = cv2.connectedComponents(sure_fg)
        markers = markers+1
        markers[unknown==255] = 0

        markersW = cv2.watershed(image_copy,markers)
        image_copy[markersW == -1] = [255,0,0]
        self.num_objects = len(markersW)
        self.image_watershed = image_copy
        self.markersW = markersW
        
        return image_copy

    def add_centroids(self):
        centroids = []
        image_copy = np.copy(self.image_copy)
        for label in range(1, self.markersW.max() + 1):
            mask = (self.markersW == label).astype(np.uint8)
            moments = cv2.moments(mask)
            centroid_x = int(moments["m10"] / moments["m00"])
            centroid_y = int(moments["m01"] / moments["m00"])
            if label != 1:
                centroids.append((centroid_x, centroid_y))
        
        for centroid in centroids:
            cv2.circle(image_copy, centroid, 5, (0, 255, 0), -1)

        return image_copy

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
