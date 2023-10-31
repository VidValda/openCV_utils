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
        

    def display_image(self,image = None, text=None, figsize=None):
        """
        Display an image using the current display strategy.

        Args:
            text (str, optional): Text to display alongside the image. Defaults to None.
        """
        imagen = self.image
        if text is not None:
            self.text = text
        if image is not None:
            imagen = image


        if isinstance(imagen,list):
            numbers = [(i) for i in range(len(imagen))]
            self.displayStrategy.display(imagen, numbers, figsize)
        else:
            self.displayStrategy.display(imagen, self.text, figsize)

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
            strategy (str): The extraction strategy to set ("path", "url", "numpy", "random", "pathlist", or "urllist").
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
        elif strategy == "pathlist":
            self.extractStrategy = PathListStrategy()
        elif strategy == "urllist":
            self.extractStrategy = URLListStrategy()
        else:
            raise ValueError("Invalid extract strategy")
