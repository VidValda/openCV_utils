import matplotlib.pyplot as plt
from abc import ABC, abstractmethod
import math

class DisplayStrategy(ABC):
    """
    An abstract base class for defining display strategies.
    """

    @abstractmethod
    def display(self, images, texts,figsize=None):
        """
        Display images with optional associated text.

        Parameters:
            images (list): A list of images to be displayed.
            texts (list): A list of text labels for the images.
            figsize (tuple): A tuple specifying the figure size (width, height).


        This method should be implemented by subclasses to define how the images are displayed.
        """
        pass

class SingleDisplayStrategy(DisplayStrategy):
    """
    A display strategy for showing a single image with an optional title.
    """

    def display(self, images, texts,figsize=None):
        """
        Display a single image with an optional title.

        Parameters:
            images (list): A list containing a single image.
            texts (str): A title or label for the image.
            figsize (tuple): A tuple specifying the figure size (width, height).

        The image is displayed with the specified title.
        """

        if figsize is not None:
            plt.figure(figsize=figsize)
        plt.title(texts)
        plt.imshow(images)
        plt.axis("off")
        plt.show()

class MultipleDisplayStrategy(DisplayStrategy):
    """
    A display strategy for showing multiple images in a grid layout.
    """

    def display(self, images, texts,figsize=None):
        """
        Display multiple images in a grid layout with optional titles.

        Parameters:
            images (list): A list of images to be displayed.
            texts (list): A list of text labels for the images.
            figsize (tuple): A tuple specifying the figure size (width, height).

        The images are displayed in a grid with titles if provided.
        """

        num_images = len(images)
        # Calculate the number of rows and columns for the grid
        rows = int(math.ceil(num_images ** 0.5))
        cols = int(math.ceil(num_images / rows))

        # Create a new figure
        if figsize is not None:
            plt.figure(figsize=figsize)


        for i in range(num_images):
            # Create a subplot for each image
            plt.subplot(rows, cols, i + 1)
            plt.title(texts[i])
            plt.imshow(images[i])
            plt.axis("off")
        plt.show()

class GridDisplayStrategy(DisplayStrategy):
    """
    A display strategy for showing images in a custom grid layout.
    """

    def __init__(self, rows, cols):
        """
        Initialize a GridDisplayStrategy with a specified grid size.

        Parameters:
            rows (int): The number of rows in the grid.
            cols (int): The number of columns in the grid.
        """
        self.rows = rows
        self.cols = cols

    def display(self, images, texts,figsize=None):
        """
        Display images in a custom grid layout with optional titles.

        Parameters:
            images (list): A list of images to be displayed.
            texts (list): A list of text labels for the images.
            figsize (tuple): A tuple specifying the figure size (width, height).

        The images are displayed in a custom grid layout with titles if provided.
        """
        num_images = len(images)
        if num_images != self.rows * self.cols:
            raise ValueError("Number of images should match the grid size (rows x cols).")

        if figsize is not None:
            plt.figure(figsize=figsize)

        for i in range(num_images):
            # Create a subplot for each image
            plt.subplot(self.rows, self.cols, i + 1)
            plt.title(texts[i])
            plt.imshow(images[i])
            plt.axis("off")
        plt.show()
