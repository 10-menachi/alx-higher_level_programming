#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list2 = my_list.copy()
    if idx > len(list2) - 1 or idx < 0:
        return list2
    list2[idx] = element
    return list2
