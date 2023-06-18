#!/usr/bin/python3
""" Defines a class called Rectangle with height and width properties"""


class Rectangle:
    """ A class Rectangle that defines a
    rectangle with height and width properties """

    def __init__(self, width=0, height=0) -> None:
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def __dict__(self):
        return {
            f"_{self.__class__.__name__}__width": self._width,
            f"_{self.__class__.__name__}__height": self._height
        }
