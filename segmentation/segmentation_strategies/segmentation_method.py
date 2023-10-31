from abc import ABC,abstractmethod

from .thresholding_strategies import BinarizationTh, AdaptativeTh, OtsuTh, SplitMergeTh, WatershedTh, RegionGrowingTh


class SegmentationMethod(ABC):

    @abstractmethod
    def set_strategy(self,strategy):
        pass

    @abstractmethod
    def segment(self, image):
        pass


class Thresholding(SegmentationMethod):

    """
    A class for performing image segmentation using different thresholding methods.

    This class allows you to set a thresholding strategy and then use that strategy
    to segment an input image.

    Attributes:
        thresholding_method: The selected thresholding strategy.

    Methods:
        segment(image):
            Segment the input image using the selected thresholding strategy.

        set_strategy(strategy):
            Set the thresholding strategy to be used for segmentation.

    Thresholding Strategies:
        - "binarization": Binary thresholding using BinarizationTh.
        - "adaptiveThresholding": Adaptive thresholding using AdaptativeTh.
        - "otsu": Otsu's method thresholding using OtsuTh.
        - "splitMerge": Split and merge thresholding using SplitMergeTh.
        - "watershed": Watershed-based segmentation using WatershedTh.
        - "regionGrowing": Region growing-based segmentation using RegionGrowingTh.
    """

    def segment(self, image):
        """
        Segment the input image using the selected thresholding strategy.

        Args:
            image (numpy.ndarray): The input image to be segmented.

        Returns:
            numpy.ndarray: The segmented image.
        """
        return self.thresholding_method.segment(image)

    def set_strategy(self, strategy):
        """
        Set the thresholding strategy to be used for segmentation.
        Thresholding Strategies:
            - "binarization": Binary thresholding using BinarizationTh.
            - "adaptiveThresholding": Adaptive thresholding using AdaptativeTh.
            - "otsu": Otsu's method thresholding using OtsuTh.
            - "splitMerge": Split and merge thresholding using SplitMergeTh.
            - "watershed": Watershed-based segmentation using WatershedTh.
            - "regionGrowing": Region growing-based segmentation using RegionGrowingTh.

        Args:
            strategy (str): The selected thresholding strategy.
                Should be one of the supported thresholding methods.

        Returns:
            SegmentationMethod: An instance of the selected thresholding strategy.
        
        """
        self.thresholding_method = strategy
        if self.thresholding_method == "binarization":
            return BinarizationTh()
        elif self.thresholding_method == "adaptativeThresholding":
            return AdaptativeTh()
        elif self.thresholding_method == "otsu":
            return OtsuTh()
        elif self.thresholding_method == "splitMerge":
            return SplitMergeTh()
        elif self.thresholding_method == "watershed":
            return WatershedTh()
        elif self.thresholding_method == "regionGrowing":
            return RegionGrowingTh()



class RegionBased(SegmentationMethod):

    def segment(self, image):
        return self.method.segment(image)

class EdgeBased(SegmentationMethod):

    def segment(self, image):
        return self.method.segment(image)

class ClusteringBased(SegmentationMethod):

    def segment(self, image):
        return self.method.segment(image)

class ArtificialBased(SegmentationMethod):

    def segment(self, image):
        return self.method.segment(image)