#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for index in range(0, x):
        try:
            count += 1
            print("{:d}".format(my_list[index]), end="")
        except IndexError:
            break
    print()
    return x
