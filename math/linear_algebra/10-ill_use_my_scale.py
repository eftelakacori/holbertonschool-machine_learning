#!/usr/bin/env python3
"""defines function that returns the transpose of a 2D matrix"""


def np_shape(matrix):
    # Return the shape of the matrix as a tuple of integers
    return matrix.shape

# Test matrices
mat1 = np.array([1, 2, 3, 4, 5, 6])  # 1D array with 6 elements
mat2 = np.array([])  # Empty array
mat3 = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], 
                 [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]])  # 3D array

# Outputting the results
print(np_shape(mat1))  # Expected output: (6,)
print(np_shape(mat2))  # Expected output: (0,)
print(np_shape(mat3))  # Expected output: (2, 2, 5)
