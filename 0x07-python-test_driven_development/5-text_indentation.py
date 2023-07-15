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
    result = ""
    for char in text:
        result += char
        if char in ('.', '?', ':', ' ', '\t'):
            result += '\n' * 2
    print(result)
