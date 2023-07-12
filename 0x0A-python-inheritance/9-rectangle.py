#!/usr/bin/python3
"""
This module contains a class Rectangle that inherits from BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This is a Rectangle that inherits from the BaseGeometry class.
    It contains private instance attributes width and height, and public function area
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        return self.__width * self.__height
