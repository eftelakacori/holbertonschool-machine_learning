    #!/usr/bin/env python3
"""defines function that calculates the shape of a matrix"""
def matrix_transpose(matrix):
    """
    Returns the transpose of a 2D matrix.
    
    Args:
        matrix (list of lists): The input 2D matrix to be transposed.
    
    Returns:
        list of lists: The transposed 2D matrix.
    """
    return [[matrix[row][col] for row in range(len(matrix))] for col in range(len(matrix[0]))]
    
