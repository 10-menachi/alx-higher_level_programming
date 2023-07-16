#!/usr/bin/python3
"""
This module contains a class MyInt that inherits from int
"""


class MyInt(int):
    """
    This is a class MyInt that inherits from int
    """

    def __eq__(self, other):
        """Returns the opposite of the equality"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Returns the opposite of the inequality"""
        return super().__eq__(other)
