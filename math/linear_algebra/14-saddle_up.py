#!/usr/bin/env python3
"""defines function that performs matrix multiplication"""


import numpy as np


def np_matmul(mat1, mat2):
    """
    Performs matrix multiplication between two given matrices.
    Parameters:
    mat1 -- The first matrix (numpy.ndarray)
    mat2 -- The second matrix (numpy.ndarray)
    Returns: numpy.ndarray --The resulting matrix from the
    multiplication of mat1 and mat2
    """
    return np.matmul(mat1, mat2)
