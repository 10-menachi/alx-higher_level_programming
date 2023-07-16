#!/usr/bin/python3
"""
This module contains a class Student that defines a student
"""


class Student:
    """
    This is a class Student that defines a student
    """

    def __init__(self, first_name, last_name, age) -> None:
        """
        This is a function that defines a student
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attributes=None) -> dict:
        """
        This is a function that retrieves a dictionary representation
        of a Student instance
        """

        the_dict = {}
        if type(attributes) is list:
            for i in attributes:
                if type(i) is str:
                    if hasattr(self, i):
                        the_dict[i] = getattr(self, i)
            return the_dict
        return self.__dict__
