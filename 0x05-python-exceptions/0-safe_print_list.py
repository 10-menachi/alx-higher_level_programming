#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for index in range(x):
        try:
            print("{:d}".format(my_list[index]))
        except IndexError:
            pass
    return x
