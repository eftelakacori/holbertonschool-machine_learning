#!/usr/bin/env python3
"""defines function that that transposes matrix"""


import numpy as np


def np_transpose(matrix):
    """
    Transposes the given numpy.ndarray matrix.

    Parameters:
        matrix (numpy.ndarray): The matrix to transpose.

    Returns:
        numpy.ndarray: The transposed matrix.
    """
    # Use NumPy's .transpose() method to transpose the matrix
    return matrix.transpose()


# Testing the function
if __name__ == "__main__":
    mat1 = np.array([1, 2, 3, 4, 5, 6])  # A 1D array
    mat2 = np.array([])  # An empty array
    mat3 = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]],
                     [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]])

    # Test with mat1
    print(np_transpose(mat1))
    print(mat1)

    # Test with mat2
    print(np_transpose(mat2))
    print(mat2)

    # Test with mat3
    print(np_transpose(mat3))
    print(mat3)
