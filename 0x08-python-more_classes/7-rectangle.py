#!/usr/bin/python3
"""This module contains a Rectangle Class"""


class Rectangle:
    """
    Rectangle Class with Private instance attributes height and width,
    getter functions and setter functions
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0) -> None:
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Width property for the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        "width setter"
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """height property for the rectangle"""
        return self.__height

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
        if self.__height == 0 or self.__width == 0:
            return 0
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self) -> str:
        """Prints the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.__width] * self.__height)

    def __repr__(self) -> str:
        """Returns a string representation of the rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Deletes the rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
