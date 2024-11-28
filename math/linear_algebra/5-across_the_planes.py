#!/usr/bin/env python3
"""defines function adds two matrices element-wise"""


def add_matrices2D(mat1, mat2):
    # Check if the matrices have the same number of rows and columns
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None
    
    # Create a new matrix to store the result of the addition
    result = []
    
    # Iterate through the rows of the matrices
    for i in range(len(mat1)):
        # Add corresponding elements in each row
        row = []
        for j in range(len(mat1[i])):
            row.append(mat1[i][j] + mat2[i][j])
        result.append(row)
    
    return result
