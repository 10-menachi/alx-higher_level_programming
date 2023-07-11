#!/usr/bin/python3
"""
This module contains a class that inherits from list
"""


class MyList(list):
    """Class that inherits from list"""

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        new = self[:]
        print("{}".format(new.sort()))
