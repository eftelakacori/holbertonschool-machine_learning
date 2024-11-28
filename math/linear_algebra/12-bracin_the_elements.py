#!/usr/bin/env python3
"""defines function that Performs element-wise"""


def np_elementwise(mat1, mat2):
    # Perform element-wise operations directly using numpy
    return mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2
