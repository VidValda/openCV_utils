from handling.image_handling import ImageHandling
from segmentation.segmentation_strategies.thresholding_strategies import *

if __name__ == "__main__":

    handler = ImageHandling()
    handler.set_extract_strategy("urllist")
    images = handler.extract_image(
        [
            "https://64.media.tumblr.com/tumblr_lt88wwEn1s1qildlio1_500.jpg",
            "https://i.pinimg.com/736x/57/cf/98/57cf9899961fb683a2dbb0b37fa3cd42.jpg",
            "https://64.media.tumblr.com/147809bcd562f7f90b2dfc3b8d71b0f9/tumblr_inline_o5kahcXjgh1tvkjl5_500.png"
        ]
    )
    handler.set_display_strategy("single")
    handler.display_image(images[0],figsize=(8,3),text="Imagen")

    imageSegmented = []

    imageSegmented.append( BinarizationTh().segment(images[0],125))

    imageSegmented.append( AdaptativeTh().segment(images[0],255,9,10))

    imageSegmented.append( OtsuTh().segment(images[0]))

    imageSegmented.append( WatershedTh().segment(images[0]))

    handler.set_display_strategy("grid",1,4)
    handler.display_image(imageSegmented,figsize=(8,8))



