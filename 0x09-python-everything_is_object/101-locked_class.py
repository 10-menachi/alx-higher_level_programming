#!/usr/bin/python3

"""
This module contains a class called LockedClass
"""


class LockedClass:
    """
    This class has no class or object attribute
    """
    __slots__ = ['first_name']

    def __init__(self, first_name=""):
        self.first_name = first_name
