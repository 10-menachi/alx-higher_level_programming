#!/usr/bin/python3

"""
This module contains a function that multiplies 2 matrices.
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.
    """
    validate_matrix(m_a, "m_a")
    validate_matrix(m_b, "m_b")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            element = 0
            for k in range(len(m_b)):
                element += m_a[i][k] * m_b[k][j]
            row.append(element)
        result.append(row)

    return result


def validate_matrix(matrix, name_of_matrix):
    """
    Validates the matrix for the required conditions.
    """
    if not isinstance(matrix, list):
        raise TypeError(f"{name_of_matrix} must be a list")

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(f"{name_of_matrix} must be a list of lists")

    if len(matrix) == 0 or any(len(row) == 0 for row in matrix):
        raise ValueError(f"{name_of_matrix} can't be empty")

    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    f"{name_of_matrix} should contain only integers or floats")

    row_sizes = set(len(row) for row in matrix)
    if len(row_sizes) > 1:
        raise TypeError(
            f"each row of {name_of_matrix} must be of the same size")
