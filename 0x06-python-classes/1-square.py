#!/usr/bin/python3

"""This module creates a class Square."""


class Square:
    """Square class with a private attribute size."""
    def __init__(self, size=0):
        """Initializes the size variable as a private instance attribute."""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
