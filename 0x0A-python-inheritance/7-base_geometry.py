#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
This module contains a BaseGeometry class
"""


class BaseGeometry:
    """class with public instance method area() and integer_validator()"""

    def area(self):
        """raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(value))
