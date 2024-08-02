#!/usr/bin/python3

"""
This module contains the Rectangle class which inherits from Base.
"""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a Rectangle instance with validation.
        """
        super().__init__(id)
        self.width = width  # Calls the setter for validation
        self.height = height  # Calls the setter for validation
        self.x = x  # Calls the setter for validation
        self.y = y  # Calls the setter for validation

    @property
    def width(self):
        """
        Getter for width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width with validation.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height with validation.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter for x.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for x with validation.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter for y.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for y with validation.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculate the area of the Rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        Print the Rectangle instance with the
        character #, taking into account x and y.
        """
        # Print `y` lines of empty space
        for _ in range(self.__y):
            print()

        # Print the rectangle with `x` spaces before each line
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """
        Return a string representation of the Rectangle.
        """

        return f"[Rectangle] ({self.id}) {self.__x}
        /{self.__y} - {self.__width}/{self.__height}"

