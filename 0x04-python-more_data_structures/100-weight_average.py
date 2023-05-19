#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    total_sum = 0
    mul = 0
    avg = 0

    for tup in my_list:
        total_sum += tup[1]
        mul += tup[0] * tup[1]
    avg = mul / total_sum
    return avg
