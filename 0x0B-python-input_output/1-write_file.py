#!/usr/bin/python3
"""
This module contains a function that writes a string to a text file (UTF8) and
returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    This is a function that writes a string to a text file (UTF8) and returns
    the number of characters written.
    """

    with open(filename, mode='w+') as text_file:
        return text_file.write(text)
