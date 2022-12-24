#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(0, x + 1):
            print('{:d}'.format(my_list[i]), end='')
            return x
    except IndexError:
        print('Index out of range')
