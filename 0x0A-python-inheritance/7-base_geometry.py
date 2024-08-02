#!/usr/bin/python3

"""
This module contains a BaseGeometry class.
"""


class BaseGeometry:
    """A class with public instance methods for geometric operations."""

    def area(self):
        """Raises an Exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer.

        Args:
            name (str): The name of the variable (used for error messages).
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer or is a boolean.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
