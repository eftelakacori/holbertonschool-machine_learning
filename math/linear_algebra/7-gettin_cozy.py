#!/usr/bin/env python3
"""defines function that calculates the shape of a matrix"""


def cat_matrices2D(mat1, mat2, axis=0):
    # Concatenate along rows (axis = 0)
    if axis == 0:
        # Check if the matrices have the same number of columns
        if len(mat1[0]) == len(mat2[0]):
            return mat1 + mat2  # Concatenate the matrices vertically
    # Concatenate along columns (axis = 1)
    elif axis == 1:
        # Check if the matrices have the same number of rows
        if len(mat1) == len(mat2):
            return [mat1[i] + mat2[i] for i in range(len(mat1))]
    # Return None if the matrices can't be concatenated
    return None
