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

    @property
    def width(self):
        """Width property for the rectangle"""
        return self.__width

    @property
    def height(self):
        """height property for the rectangle"""
        return self.__height

    @width.setter
    def width(self, value):
        "width setter"
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        "height setter"
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        if self.__height and self.__width == 0:
            return 0
        return self.__height * self.__width

    def perimeter(self):
        if self.__height and self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self) -> str:
        """Prints the rectangle"""
        if self.__height and self.__width == 0:
            return ""
        return "\n".join(["#" * self.__width] * self.__height)

    def __repr__(self) -> str:
        """Returns a string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)
