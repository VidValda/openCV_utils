
from .segmentation_strategies.segmentation_method import Thresholding, RegionBased, EdgeBased, ClusteringBased, ArtificialBased
from .segmentation_strategies.thresholding_strategies import BinarizationTh, AdaptativeTh, OtsuTh, SplitMergeTh, WatershedTh, RegionGrowingTh
from .segmentation_strategies.region_based_strategy import CountoursRb


class ImageSegmentation:
    def __init__(self,image):
        self.image = image
        self.segmentedImage = None

        self.segmentatiomethod = Thresholding()

    def segment(self,image = None):
        imagen = self.image
        if image is not None:
            imagen = image
        self.segmentedImage = self.segmentatiomethod.segment(imagen)
        return self.segmentedImage
    
    def set_image(self,image):
        self.image = image

    def get_method(self,method):
        if method == "thresholding":
            self.segmentatiomethod = Thresholding()
        elif method == "regionBased":
            self.segmentatiomethod = RegionBased()
        elif method == "EdgeBased":
            self.segmentatiomethod = EdgeBased()
        elif method == "clustering":
            self.segmentatiomethod = ClusteringBased()
        elif method == "artificial":
            self.segmentatiomethod = ArtificialBased()
        return self.segmentatiomethod


            