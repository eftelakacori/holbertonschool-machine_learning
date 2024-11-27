#!/usr/bin/env python3
"""defines function 2D matrices containing ints/floats"""


def add_matrices2D(mat1, mat2):
    """Adds two 2D matrices element-wise.
    Args:
        mat1 (list of lists): The first 2D matrix (list of lists of ints/floats).
        mat2 (list of lists): The second 2D matrix (list of lists of ints/floats).
    Returns:
        list of lists: A new matrix containing the element-wise sum of mat1 and mat2,
                       or None if the matrices have different shapes."""
    # Kontrollo nëse matricat kanë të njëjtën formë
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None    
    # Kthe matricën që është shuma element-për-element
    return [
        [mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))]
        for i in range(len(mat1))
    ]
