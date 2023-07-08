#!/usr/bin/python3
"""Empty Rectangle Class"""


class Rectangle:
    """
    Rectangle Class with Private instance attributes height and width,
    getter functions and setter functions
    """

    def __init__(self, width=0, height=0) -> None:
        self.__width = width
        self.__height = height

    def width(self, width):
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    def width(self):
        return self.__width

    def height(self, height):
        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    def height(self):
        return self.__height
