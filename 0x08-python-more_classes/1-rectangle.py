class Rectangle:
    """
    This class defines a rectangle.
    """

    def __init__(self, width=0, height=0) -> None:
        """
        This method initializes a rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        This method returns the value of the width property
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        This method sets the width property to the value variable
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        This method returns the value of the height property
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        This method sets the height property to the value variable
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
