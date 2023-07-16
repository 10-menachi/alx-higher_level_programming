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
        raise ValueError(
            f"shapes {np_a.shape} and {np_b.shape} not aligned: {np_a.shape[1]} (dim 1) != {np_b.shape[0]} (dim 0)")

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
        raise ValueError(
            f"shapes ({len(matrix)}, {len(matrix[0])}) not aligned: ({len(matrix)}, 0) (dim 1) != ({len(matrix[0])},) (dim 0)")

    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError(
                f"setting an array element with a sequence.")

        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "invalid data type for einsum")
