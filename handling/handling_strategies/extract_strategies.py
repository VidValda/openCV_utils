from abc import ABC, abstractmethod
import cv2
import urllib.request
import numpy as np

class ImportStrategy:
    """
    Abstract base class for image import strategies.

    Attributes:
        None
    """

    @abstractmethod
    def import_image(self, source):
        """
        Import an image from a given source.

        Args:
            source: The source of the image data, which can be a file path, URL, or other source.

        Returns:
            An image in a format suitable for further processing.
        """
        pass

class FilePathImportStrategy(ImportStrategy):
    """
    Image import strategy for importing images from a local file path.

    Attributes:
        None
    """

    def import_image(self, source):
        """
        Import an image from a file path.

        Args:
            source: The file path to the image.

        Returns:
            An image in RGB format.
        """
        image = cv2.imread(source)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return image

class UrlImportStrategy(ImportStrategy):
    """
    Image import strategy for importing images from a URL.

    Attributes:
        None
    """

    def import_image(self, source):
        """
        Import an image from a URL.

        Args:
            source: The URL of the image.

        Returns:
            An image in RGB format.
        """
        response = urllib.request.urlopen(source)
        image_array = np.asarray(bytearray(response.read()), dtype=np.uint8)
        image = cv2.imdecode(image_array, -1)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return image

class NumpyImportStrategy(ImportStrategy):
    """
    Image import strategy for importing images from a NumPy array.

    Attributes:
        None
    """

    def import_image(self, source):
        """
        Import an image from a NumPy array.

        Args:
            source: The NumPy array representing the image.

        Returns:
            The input NumPy array representing the image.
        """
        return source

class RandomImportStrategy(ImportStrategy):
    """
    Image import strategy for generating random images.

    Attributes:
        width: The width of the generated image.
        height: The height of the generated image.
    """

    def __init__(self, width, height):
        """
        Initialize a RandomImportStrategy with the specified width and height.

        Args:
            width: The width of the generated image.
            height: The height of the generated image.
        """
        self.width = width
        self.height = height

    def import_image(self, source=None):
        """
        Generate a random image.

        Args:
            source: This parameter is not used in this strategy.

        Returns:
            A randomly generated image as a NumPy array (grayscale).
        """
        image = np.random.randint(0, 256, (self.height, self.width), dtype=np.uint8)
        return image


class URLListStrategy(ImportStrategy):
    """
    Image import strategy for importing images from a list of URLs.

    Attributes:
        None
    """

    def import_image(self, source):
        """
        Import an image from a list of URLs.

        Args:
            source: A list of URLs of the images.

        Returns:
            A list of images in RGB format.
        """
        images = []
        for url in source:
            response = urllib.request.urlopen(url)
            image_array = np.asarray(bytearray(response.read()), dtype=np.uint8)
            image = cv2.imdecode(image_array, -1)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            images.append(image)
        return images

class PathListStrategy(ImportStrategy):
    """
    Image import strategy for importing images from a list of local file paths.

    Attributes:
        None
    """

    def import_image(self, source):
        """
        Import images from a list of local file paths.

        Args:
            source: A list of file paths to the images.

        Returns:
            A list of images in RGB format.
        """
        images = []
        for path in source:
            image = cv2.imread(path)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            images.append(image)
        return images