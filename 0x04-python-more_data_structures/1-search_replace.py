#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    idx = 0
    for items in new_list:
        if items == search:
            new_list[idx] = replace
        idx += 1
    return new_list
