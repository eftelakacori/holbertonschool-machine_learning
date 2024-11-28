#!/usr/bin/env python3
"""defines function that concatenates two matrices along a specific axis"""


import numpy as np


def np_cat(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specified axis.
    Parameters:
    mat1 --The first matrix (numpy.ndarray)
    mat2 --The second matrix (numpy.ndarray)
    axis --The axis along which to concatenate
    the matrices (default is 0, for vertical concatenation)
    Returns:
    numpy.ndarray -- The concatenated matrix
    """
    # Use np.concatenate to join mat1 and mat2 along the specified axis
    return np.concatenate((mat1, mat2), axis=axis)
