#!/usr/bin/env python3
"""defines function that returns the transpose of a 2D matrix"""
# Import the add_matrices2D function from 5-across_the_planes.py
add_matrices2D = __import__('5-across_the_planes').add_matrices2D

# Test case 1
mat1 = [[1, 2], [3, 4]]
mat2 = [[5, 6], [7, 8]]
print("Result of adding mat1 and mat2:")
print(add_matrices2D(mat1, mat2))  # Expected output: [[6, 8], [10, 12]]

# Ensure mat1 and mat2 are not modified
print("mat1:", mat1)  # Expected output: [[1, 2], [3, 4]]
print("mat2:", mat2)  # Expected output: [[5, 6], [7, 8]]

# Test case 2 (matrices with different dimensions)
print("Result of adding mat1 and a matrix with different dimensions:")
print(add_matrices2D(mat1, [[1, 2, 3], [4, 5, 6]]))  # Expected output: None

