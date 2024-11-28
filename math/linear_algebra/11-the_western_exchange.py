#!/usr/bin/env python3
"""Write a function that transposes a matrix"""


def np_transpose(matrix):
    """
    Transposes the given numpy.ndarray.

    Args:
        matrix (numpy.ndarray): The matrix to be transposed.

    Returns:
        numpy.ndarray: A new matrix that is the transpose of the input matrix.
    """
    # Use the .T attribute of numpy arrays to perform the transpose operation
    return matrix.T
