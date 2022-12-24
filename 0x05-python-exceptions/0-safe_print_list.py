#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print('{:d}'.format(my_list[i]), end='')
        print()
        return x
    except IndexError:
        print('Index out of range')
listt = [1, 2, 3, 4, 5]
safe_print_list(listt, x=3)
