import cv2
import numpy as np
from abc import ABC, abstractmethod

class CornerDetector(ABC):

    @abstractmethod
    def detect_corners(self, image):
        pass


class HarrisCornerDetector(CornerDetector):
    def __init__(self, k=0.04, block_size=2, ksize=3):
        self.k = k
        self.block_size = block_size
        self.ksize = ksize

    def detect_corners(self, image):
        image_copy = np.copy(image)

        gray = cv2.cvtColor(image_copy, cv2.COLOR_RGB2GRAY)
        gray = np.float32(gray)
        
        # Apply Harris corner detection
        corners = cv2.cornerHarris(gray, self.block_size, self.ksize, self.k)

        # Threshold the corners to keep only strong corners
        corners = cv2.dilate(corners, None)
        image_copy[corners > 0.01 * corners.max()] = [0, 255, 0]

        return (image_copy,corners)
    

class ShiTomasiCornerDetector(CornerDetector):
    def __init__(self, max_corners=100, quality_level=0.01, min_distance=10):
        self.max_corners = max_corners
        self.quality_level = quality_level
        self.min_distance = min_distance

    def detect_corners(self, image):
        
        image_copy = np.copy(image)
        
        # Convert the image to grayscale
        gray = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)
        
        # Apply Shi-Tomasi corner detection
        corners = cv2.goodFeaturesToTrack(
            gray, self.max_corners, self.quality_level, self.min_distance
        )

        # Convert the corners to integer coordinates
        corners = np.int0(corners)

        # Draw circles around the detected corners
        for corner in corners:
            x, y = corner.ravel()
            cv2.circle(image_copy, (x, y), 3, 255, -1)

        return (image_copy, corners)
