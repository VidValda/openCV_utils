from handling.image_handling import ImageHandling

if __name__ == "__main__":

    handler = ImageHandling()

    image = handler.extract_image("https://64.media.tumblr.com/tumblr_lt88wwEn1s1qildlio1_500.jpg")

    handler.display_image()
