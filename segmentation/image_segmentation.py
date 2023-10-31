
from .segmentation_strategies.segmentation_method import Thresholding, RegionBased, EdgeBased, ClusteringBased, ArtificialBased
from .segmentation_strategies.thresholding_strategies import BinarizationTh, AdaptativeTh, OtsuTh, SplitMergeTh, WatershedTh, RegionGrowingTh
from .segmentation_strategies.region_based_strategy import CountoursRb


class ImageSegmentation:
    def __init__(self,image):
        self.image = image
        self.segmentedImage = None

        self.segmentatiomethod = Thresholding()

        self.thresholdingMethod = BinarizationTh()
        self.regionBasedMethod = CountoursRb()
        self.edgeBasedMethod = None
        self.clusteringMethod = None
        self.artificialMethod = None
    
    def set_image(self,image):
        self.image = image

    def set_segmentation_method(self,strategy):
        if strategy == "thresholding":
            self.segmentatiomethod = Thresholding()
        elif strategy == "regionBased":
            self.segmentatiomethod = RegionBased()
        elif strategy == "EdgeBased":
            self.segmentatiomethod = EdgeBased()
        elif strategy == "clustering":
            self.segmentatiomethod = ClusteringBased()
        elif strategy == "artificial":
            self.segmentatiomethod = ArtificialBased()

    def set_thresholding_method(self,method):
        if method == "binarization":
            self.thresholdingMethod = BinarizationTh()
        elif method == "adaptativeThresholding":
            self.thresholdingMethod = AdaptativeTh()
        elif method == "otsu":
            self.thresholdingMethod = OtsuTh()
        elif method == "splitMerge":
            self.thresholdingMethod = SplitMergeTh()
        elif method == "watershed":
            self.thresholdingMethod = WatershedTh()
        elif method == "regionGrowing":
            self.thresholdingMethod = RegionGrowingTh()

            