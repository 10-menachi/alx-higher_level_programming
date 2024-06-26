#!/usr/bin/python3

"""
This is the Base Class
"""


class Base:
    """
    This is the Base Class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        This is the __init__ method
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
