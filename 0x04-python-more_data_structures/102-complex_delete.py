#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    to_delete = ""
    for key in a_dictionary:
        if a_dictionary[key] == value:
            to_delete = key
    del a_dictionary[to_delete]
    return a_dictionary
