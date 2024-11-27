#!/usr/bin/env python3
"""defines function 2D matrices containing ints/floats"""


def cat_matrices2D(mat1, mat2, axis=0):
    if axis == 0:
        # Kontrollojmë që numri i kolonave të jetë i njëjtë
        if len(mat1[0]) != len(mat2[0]):
            return None
        return [row[:] for row in mat1] + [row[:] for row in mat2]
    elif axis == 1:
        # Kontrollojmë që numri i rreshtave të jetë i njëjtë
        if len(mat1) != len(mat2):
            return None
        return [mat1[i] + mat2[i] for i in range(len(mat1))]
    else:
        return None
