#!/usr/bin/python3
def max_integer(my_list=[]):
    maximum = 0
    if my_list:
        maximum = my_list[0]
        for elem in my_list:
            if elem > maximum:
                maximum = elem
    else:
        maximum = None
    return maximum
