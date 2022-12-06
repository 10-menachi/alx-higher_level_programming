#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    list2 = my_list.reverse()
    for item in list2:
        print("{:d}".format(item))
