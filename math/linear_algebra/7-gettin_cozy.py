#!/usr/bin/env python3
"""defines function that concatenates two matrices along a specific axis:"""


def cat_matrices2D(mat1, mat2, axis=0):
    if axis == 0:  # Concatenate along rows
        # Check if both matrices have the same number of columns
        if len(mat1[0]) != len(mat2[0]):
            return None
        # Return a new matrix with the rows concatenated
        return [row[:] for row in mat1] + [row[:] for row in mat2]
    elif axis == 1:  # Concatenate along columns
        # Check if both matrices have the same number of rows
        if len(mat1) != len(mat2):
            return None
        # Return a new matrix with the columns concatenated
        return [mat1[i] + mat2[i] for i in range(len(mat1))]
    # Return None for invalid axis
    return None
