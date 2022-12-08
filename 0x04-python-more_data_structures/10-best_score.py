#!/usr/bin/python3
def best_score(a_dictionary):
    if len(a_dictionary) == 0 or a_dictionary is dict:
        return None
    init = list(a_dictionary.keys())[0]
    maxim = a_dictionary[init]
    for key, value in a_dictionary.items():
        if value > maxim:
            maxim = value
            init = key
    return init
