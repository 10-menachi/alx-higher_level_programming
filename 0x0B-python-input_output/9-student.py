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

    def to_json(self) -> dict:
        """
        This is a function that retrieves a dictionary representation
        of a Student instance
        """

        return self.__dict__
