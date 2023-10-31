from segmentation_method import Thresholding

class ThresholdingStrategy(Thresholding):
    
    def segment(self,image):
        pass


class BinarizationTh(ThresholdingStrategy):

    def segment(self, image):
        pass

class AdaptativeTh(ThresholdingStrategy):

    def segment(self, image):
        pass

class OtsuTh(ThresholdingStrategy):

    def segment(self, image):
        pass

class SplitMergeTh(ThresholdingStrategy):

    def segment(self, image):
        pass

class WatershedTh(ThresholdingStrategy):

    def segment(self, image):
        pass

class RegionGrowingTh(ThresholdingStrategy):

    def segment(self, image):
        pass