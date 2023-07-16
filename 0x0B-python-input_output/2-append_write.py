#!/usr/bin/python3
"""
This module contains a function that appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """
    This is a function that appends a string at the end of a text file
    """

    with open(filename, mode='a+') as text_file:
        return text_file.write(text)
