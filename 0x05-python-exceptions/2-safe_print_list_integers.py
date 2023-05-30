#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for index in range(0, x):
        try:
            print("{:d}".format(my_list[index]), end="")
            if my_list[index]:
                count += 1
        except (ValueError, TypeError, IndexError):
            pass
    print()
    return count
