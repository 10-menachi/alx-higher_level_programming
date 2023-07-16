#!/usr/bin/python3

"""
This module contains a function that multiplies 2 matrices.
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices.
    """
    validate_matrix(m_a, "matrix_a")
    validate_matrix(m_b, "matrix_b")

    np_a = np.array(m_a)
    np_b = np.array(m_b)

    if np_a.shape[1] != np_b.shape[0]:
        raise ValueError("m_a and m_b can't be multiplied")

    result = np.matmul(np_a, np_b)

    return result


def validate_matrix(matrix, name_of_matrix):
    """
    Validates the matrix.
    """
    if not isinstance(matrix, list):
        raise ValueError("Scalar operands are not allowed, use '*' instead")

    if not all(isinstance(row, list) for row in matrix):
        raise ValueError("Scalar operands are not allowed, use '*' instead")

    if len(matrix) == 0 or any(len(row) == 0 for row in matrix):
        raise ValueError(f"{name_of_matrix} can't be empty")

    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError(
                f"each row of {name_of_matrix} must be of the same size")

        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    f"{name_of_matrix} should contain only integers or floats")
