#!/usr/bin/python3

"""
This module contains a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix.
    """
    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    divided_matrix = [
        [round(element / div, 2) if isinstance(element,
                                               (
                                                   int, float
                                               )
                                               )
         else element for element in row
         ]
        for row in matrix]
    return divided_matrix