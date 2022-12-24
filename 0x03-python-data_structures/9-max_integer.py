#!/usr/bin/python3
def max_integer(my_list=[]):
    maximum = 0
    if len(my_list) == 0:
        return None
    for number in my_list:
        if number > maximum:
            maximum = number
    return maximum
print(max_integer([1, 90, 2, 13, 34, 5, -13, 3]))
