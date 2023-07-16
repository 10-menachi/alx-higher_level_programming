#!/usr/bin/python3
"""
This module contains a function  that inserts a
line of text to a file, after each line containing
a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    This function inserts a
    line of text to a file, after each line containing
    a specific string:
    """

    temp_filename = filename + ".tmp"

    with open(filename, 'r') as file_in, open(temp_filename, 'w') as file_out:
        for line in file_in:
            file_out.write(line)
            if search_string in line:
                file_out.write(new_string)

    with open(temp_filename, 'r') as temp_file, open(filename, 'w') as original_file:
        for line in temp_file:
            original_file.write(line)

    with open(temp_filename, 'w') as temp_file:
        temp_file.write("")
