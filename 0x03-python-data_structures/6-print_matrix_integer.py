#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for l in matrix:
        for item in l:
            print('{:d}'.format(item))
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print_matrix_integer(matrix)
