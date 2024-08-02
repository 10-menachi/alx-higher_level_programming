#!/usr/bin/python3

"""
This module contains a class that defines a rectangle.
"""


class Rectangle:
    """
    This class defines a rectangle.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0) -> None:
        """
        Initializes the rectangle with the given width and height.
        Increments the number_of_instances class attribute.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Returns the value of the width property.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width property to the value provided.
        Validates that the value is a non-negative integer.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Returns the value of the height property.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height property to the value provided.
        Validates that the value is a non-negative integer.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle.
        If either width or height is 0, the perimeter is 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Returns a string representation of the rectangle
        using the '#' character.
        If width or height is 0, returns an empty string.
        """
        if self.width == 0 or self.height == 0:
            return ""
        rect_str = []
        for i in range(self.height):
            rect_str.append("#" * self.width)
        return "\n".join(rect_str)

    def __repr__(self):
        """
        Returns a string representation of the rectangle
        that can be used to recreate a new instance using eval().
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Prints a message when the instance is deleted.
        Decrements the number_of_instances class attribute.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
