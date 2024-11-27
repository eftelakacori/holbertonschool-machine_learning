#!/usr/bin/env python3
"""defines function that calculates the shape of a matrix"""


def cat_matrices2D(mat1, mat2, axis=0):  
    """ Afunction that calculates the shape of a matrix"""
    if axis == 0:
        return mat1.copy() + mat2.copy()
    elif axis == 1:
        #
    else:
        return None
