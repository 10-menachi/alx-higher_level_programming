#!/usr/bin/python3
""" Defines a class called Rectangle with height and width properties"""


class Rectangle:
    """ A class Rectangle that defines a rectangle with height and width properties """

    def __init__(self, width=0, height=0) -> None:
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.width = width
        self.height = height

    def width(self):
        return self.width

    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.width = value

    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.height = value
