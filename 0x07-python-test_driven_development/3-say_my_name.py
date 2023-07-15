#!/usr/bin/python3

"""
This module contains a function that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    This function prints My name is <first name> <last name>
    """
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError(
            "first_name must be a string or last_name must be a string")
    if last_name:
        print(f"My name is {first_name} {last_name}")
    else:
        print(f"My name is {first_name}")
