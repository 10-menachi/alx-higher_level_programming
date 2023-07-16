#!/usr/bin/python3

"""
This module contains a function that prints a text with 2 new lines after each
"""


def text_indentation(text):
    """
    This function prints a text with 2 new lines after each of these characters:
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.strip()
    result = ""
    indentation = ""
    for char in text:
        result += indentation + char
        if char in ('.', '?', ':'):
            result += '\n\n'
        if char == ' ' and indentation == '':
            indentation = '    '
        elif char != ' ' and indentation != '':
            indentation = ''
    print(result, end="")
