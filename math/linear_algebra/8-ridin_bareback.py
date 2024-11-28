#!/usr/bin/env python3
"""Write a function that performs matrix multiplication"""


def mat_mul(mat1, mat2):
    """
    Performs matrix multiplication of two 2D matrices.

    Args:
        mat1: List of lists (2D matrix) containing ints/floats.
        mat2: List of lists (2D matrix) containing ints/floats.

    Returns:
        A new 2D matrix that is the result of multiplying mat1 and mat2.
        Returns None if the matrices cannot be multiplied.
    """
    # Validate if matrix multiplication is possible
    # Number of columns in mat1 must equal number of rows in mat2
    if len(mat1[0]) != len(mat2):
        return None

    # Perform matrix multiplication
    # Result matrix dimensions will be len(mat1) x len(mat2[0])
    result = [
        [sum(a * b for a, b in zip(row, col)) for col in zip(*mat2)]
        for row in mat1
    ]

    return result
