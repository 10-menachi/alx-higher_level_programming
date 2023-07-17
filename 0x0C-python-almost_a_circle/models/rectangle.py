#!/usr/bin/python3
"""
This module contains a class called Rectangle
that inherits from the Base class
"""

from base import Base


class Rectangle(Base):
    """
    This is a rectangle class that inherits
    from the Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        This is the constructor for the Rectangle class
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        This is the getter method for the width attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        This is the setter method for the width attribute
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        This is the getter method for the height attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        This is the setter method for the height attribute
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """
        This is the getter method for the x attribute
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        This is the setter method for the x attribute
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """
        This is the getter method for the y attribute
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        This is the setter method for the y attribute
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """
        This method returns the area of the Rectangle instance
        """
        return self.__width * self.__height
