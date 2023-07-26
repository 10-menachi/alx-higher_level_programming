#!/usr/bin/python3

"""
This module contains a function that prints a text with 2 new lines after each
"""


def text_indentation(text):
    """
    This function prints a text
    with 2 new lines after each of these characters:
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for char in ".?:":
        text = (char + "\n\n").join([line.strip(" ")
                                     for line in text.split(char)])
        print(text, end="")
