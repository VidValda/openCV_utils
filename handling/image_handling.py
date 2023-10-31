from .handling_strategies.display_strategies import *
from .handling_strategies.extract_strategies import *

class ImageHandling:
    def __init__(self):
        """
        Initialize an ImageHandling instance with default extract and display strategies.

        The extract strategy is set to UrlImportStrategy, and the display strategy
        is set to SingleDisplayStrategy. The image and text attributes are initialized as None.
        """
        self.extractStrategy = UrlImportStrategy()
        self.displayStrategy = SingleDisplayStrategy()
        self.image = None
        self.text = "Image"

    def extract_image(self, source):
        """
        Extract an image using the current extract strategy.

        Args:
            source (str): The source of the image to extract, depending on the chosen strategy.
        """
        self.image = self.extractStrategy.import_image(source)
        return self.image
        

    def display_image(self,text=None):
        """
        Display an image using the current display strategy.

        Args:
            image: The image to display.
            text (str, optional): Text to display alongside the image. Defaults to None.
        """
        if text:
            self.text = text
        self.displayStrategy.display(self.image, self.text)

    def set_display_strategy(self, strategy, rows=None, cols=None):
        """
        Set the display strategy for rendering images.

        Args:
            strategy (str): The display strategy to set ("single", "multiple", or "grid").
            rows (int, optional): Number of rows for the grid display strategy. Defaults to None.
            cols (int, optional): Number of columns for the grid display strategy. Defaults to None.

        Raises:
            ValueError: If an invalid display strategy is provided.
        """
        if strategy == "single":
            self.displayStrategy = SingleDisplayStrategy()
        elif strategy == "multiple":
            self.displayStrategy = MultipleDisplayStrategy()
        elif strategy == "grid":
            self.displayStrategy = GridDisplayStrategy(rows, cols)
        else:
            raise ValueError("Invalid display strategy")

    def set_extract_strategy(self, strategy, width=None, height=None):
        """
        Set the image extraction strategy.

        Args:
            strategy (str): The extraction strategy to set ("path", "url", "numpy", or "random").
            width (int, optional): Width parameter for the extraction strategy. Defaults to None.
            height (int, optional): Height parameter for the extraction strategy. Defaults to None.

        Raises:
            ValueError: If an invalid extraction strategy is provided.
        """
        if strategy == "path":
            self.extractStrategy = FilePathImportStrategy()
        elif strategy == "url":
            self.extractStrategy = UrlImportStrategy()
        elif strategy == "numpy":
            self.extractStrategy = NumpyImportStrategy()
        elif strategy == "random":
            self.extractStrategy = RandomImportStrategy()
        else:
            raise ValueError("Invalid extract strategy")
