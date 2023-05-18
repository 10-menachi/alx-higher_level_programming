#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set()
    for item in my_list:
        my_set.add(item)
    sum = 0
    for elem in my_set:
        sum += elem
    return sum
