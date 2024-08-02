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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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
        for _ in range(self.__y):
            print()

        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """
        Return a string representation of the Rectangle.
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - " \
            f"{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """
        Update the attributes of the Rectangle with new values.

        Args:
            *args: New values for id, width, height, x, and y in that order.
            **kwargs: New values for attributes specified by keyword arguments.
        """
        if args:
            attributes = ('id', 'width', 'height', 'x', 'y')
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                if key in ('width', 'height', 'x', 'y'):
                    setattr(self, key, value)
                elif key == 'id':
                    self.id = value

    def to_dictionary(self):
        """
        Return the dictionary representation of the Rectangle.
        """
        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
        }
