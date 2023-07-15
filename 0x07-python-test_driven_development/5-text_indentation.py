#!/usr/bin/python3

"""
This module contains a function that prints a text with 2 new lines after each
"""


def text_indentation(text):
    """
    This function prints a text
    with 2 new lines after each of these characters:
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.strip()
    output = ""
    for char in text:
        output += char
        if char in ('.', '?', ':'):
            output += '\n\n'
    print(output)
