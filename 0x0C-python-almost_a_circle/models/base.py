#!/usr/bin/python3

"""
This module contains the class Base
"""


class Base:
    """
    This is the base class of all other classes
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        This is the constructor for the Base class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
