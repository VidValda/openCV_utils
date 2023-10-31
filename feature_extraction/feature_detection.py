import cv2
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod

class FeatureExtractor(ABC):

    @abstractmethod
    def extract_features(self, image):
        pass


    @abstractmethod
    def match_features(self, query_descriptors, train_descriptors):
        pass

    @abstractmethod
    def match_images(self, query_image, train_image):
        pass

class ORBFeatureExtractor:
    def __init__(self, n_keypoints=500, scale_factor=1.2, n_levels=8, edge_threshold=31, patch_size=31):
        self.n_keypoints = n_keypoints
        self.scale_factor = scale_factor
        self.n_levels = n_levels
        self.edge_threshold = edge_threshold
        self.patch_size = patch_size

        # Initialize the ORB detector
        self.orb = cv2.ORB_create(
            nfeatures=n_keypoints,
            scaleFactor=scale_factor,
            nlevels=n_levels,
            edgeThreshold=edge_threshold,
            patchSize=patch_size
        )

    def extract_features(self, image):
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        keypoints, descriptors = self.orb.detectAndCompute(gray_image, None)
        return keypoints, descriptors

    def match_features(self, query_descriptors, train_descriptors):
        # Create a BFMatcher (Brute-Force Matcher)
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        
        # Perform feature matching
        matches = bf.match(query_descriptors, train_descriptors)
        
        # Sort the matches by distance (shortest distances first)
        matches = sorted(matches, key=lambda x: x.distance)

        return matches
    
    def match_images(self, query_image, train_image):
        # Extract ORB features from query and train images
        query_keypoints, query_descriptors = self.extract_features(query_image)
        train_keypoints, train_descriptors = self.extract_features(train_image)

        matches = self.match_features(query_descriptors,train_descriptors)

        return self.get_image(query_image,query_keypoints,train_image,train_keypoints, matches)

    def get_image(self,query_image, query_keypoints, train_image, train_keypoints, matches):
        matched_image = cv2.drawMatches(query_image, query_keypoints, train_image, train_keypoints, matches, None)
        return matched_image
    

class SIFTFeatureExtractor(FeatureExtractor):

    def __init__(self):
        self.query_keypoints = None
        self.query_descriptors = None

    def extract_features(self, image):
        # Create an SIFT detector
        sift = cv2.SIFT_create()

        # Detect keypoints and compute descriptors
        keypoints, descriptors = sift.detectAndCompute(image, None)

        self.query_keypoints = keypoints
        self.query_descriptors = descriptors

        return keypoints, descriptors

    def match_features(self, query_descriptors, train_descriptors):
        # Create a BFMatcher (Brute Force Matcher) with default params
        bf = cv2.BFMatcher()
        # Match descriptors using KNN (k-nearest neighbors)
        matches = bf.knnMatch(query_descriptors, train_descriptors, k=2)

        # Apply ratio test to filter good matches
        good_matches = []
        for m, n in matches:
            if m.distance < 0.75 * n.distance:
                good_matches.append(m)

        return good_matches

    def match_images(self, query_image, train_image):
        # Extract features from both query and train images
        query_keypoints, query_descriptors = self.extract_features(query_image)
        train_keypoints, train_descriptors = self.extract_features(train_image)

        # Match the extracted features
        matches = self.match_features(query_descriptors, train_descriptors)

        return self.get_image(query_image,query_keypoints,train_image,train_keypoints, matches)

    def get_image(self,query_image, query_keypoints, train_image, train_keypoints, matches):
        matched_image = cv2.drawMatches(query_image, query_keypoints, train_image, train_keypoints, matches, None)
        return matched_image