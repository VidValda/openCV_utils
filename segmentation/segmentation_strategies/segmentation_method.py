from abc import ABC, abstractclassmethod

class SegmentationMethod(ABC):

    @abstractclassmethod
    def segment(self, image):
        pass

    
#"thresholding":"regionBased":"EdgeBased":"clustering":"artificial":

class Thresholding(SegmentationMethod):

    def segment(sefl,image):
        pass

class RegionBased(SegmentationMethod):

    def segment(sefl,image):
        pass

class EdgeBased(SegmentationMethod):

    def segment(sefl,image):
        pass

class ClusteringBased(SegmentationMethod):

    def segment(sefl,image):
        pass

class ArtificialBased(SegmentationMethod):

    def segment(sefl,image):
        pass