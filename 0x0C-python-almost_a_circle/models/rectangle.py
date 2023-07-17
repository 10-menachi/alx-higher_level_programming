#!/usr/bin/python3
"""
This module contains a class called Rectangle
that inherits from the Base class
"""

from models.base import Base


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

    def display(self):
        """
        This method prints in stdout the Rectangle instance
        with the character #
        """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self) -> str:
        """
        This method returns the string representation of the Rectangle
        instance
        """

        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x,
            self.__y, self.__width,
            self.__height
        )

    def update(self, *args):
        """
        This method assigns an argument to each attribute
        """

        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.__width = args[i]
                elif i == 2:
                    self.__height = args[i]
                elif i == 3:
                    self.__x = args[i]
                elif i == 4:
                    self.__y = args[i]
