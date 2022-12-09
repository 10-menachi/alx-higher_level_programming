#!/usr/bin/python3
def roman_to_int(roman_string):
    if not str(roman_string):
        return None

    roman_to_int_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    prev = 0
    for c in reversed(roman_string):
        curr = roman_to_int_map[c]
        if curr >= prev:
            result += curr
        else:
            result -= curr
        prev = curr
    return result
