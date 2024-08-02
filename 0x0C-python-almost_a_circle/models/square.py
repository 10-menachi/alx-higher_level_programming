#!/usr/bin/python3

"""
This module contains the Square class which inherits from Rectangle.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square instance with validation.
        """
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):
        """
        Getter for size.
        """
        return self.__width

    @size.setter
    def size(self, value):
        """
        Setter for size. Sets both width and height with validation.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """Defines a format for the string representation of the class"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
            {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """
        Update the attributes of the Square with new values.

        Args:
            *args: New values for id, size, x, and y in that order.
            **kwargs: New values for attributes specified by keyword arguments.
        """
        if args:
            attributes = ('id', 'size', 'x', 'y')
            for attr, value in zip(attributes, args):
                if attr == 'size':
                    self.size = value
                else:
                    setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    self.size = value
                else:
                    setattr(self, key, value)
