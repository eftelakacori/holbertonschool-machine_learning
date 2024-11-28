#!/usr/bin/env python3
"""defines function that performs """

import numpy as np


def np_elementwise(mat1, mat2):
    """
    Performs element-wise addition, subtraction, multiplication, and division
    on two matrices or a matrix and a scalar.

    Parameters:
        mat1 (numpy.ndarray): The first matrix.
        mat2 (numpy.ndarray or scalar): The second matrix or a scalar.

    Returns:
        tuple: A tuple containing:
            - The result of element-wise addition.
            - The result of element-wise subtraction.
            - The result of element-wise multiplication.
            - The result of element-wise division.
    """
    # Element-wise addition
    add = mat1 + mat2

    # Element-wise subtraction
    sub = mat1 - mat2

    # Element-wise multiplication
    mul = mat1 * mat2

    # Element-wise division
    div = mat1 / mat2

    # Return the results as a tuple
    return add, sub, mul, div


# Test the function
if __name__ == "__main__":
    mat1 = np.array([[11, 22, 33], [44, 55, 66]])
    mat2 = np.array([[1, 2, 3], [4, 5, 6]])

    # Display the matrices
    print("Matrix 1:")
    print(mat1)
    print("Matrix 2:")
    print(mat2)

    # Perform element-wise operations with two matrices
    add, sub, mul, div = np_elementwise(mat1, mat2)
    print("Add:\n", add, "\nSub:\n", sub, "\nMul:\n", mul, "\nDiv:\n", div)

    # Perform element-wise operations with a matrix and a scalar
    add, sub, mul, div = np_elementwise(mat1, 2)
    print("Add:\n", add, "\nSub:\n", sub, "\nMul:\n", mul, "\nDiv:\n", div)
