#!/usr/bin/env python3
"""defines function  that transposes matrix"""


def np_transpose(matrix):
    # Use the built-in NumPy transpose functionality
    return matrix.T


# Test matrices
mat1 = np.array([1, 2, 3, 4, 5, 6])
mat2 = np.array([])
mat3 = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]],
                 [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]])

# Outputting the results
print(np_transpose(mat1))  # Expected output: matrix transpose of mat1
print(mat1)                # Original matrix, should remain the same
print(np_transpose(mat2))  # Expected output: []
print(mat2)                # Original matrix, should remain the same
print(np_transpose(mat3))  # Expected output: Transpose of mat3
print(mat3)                # Original matrix, should remain the same
