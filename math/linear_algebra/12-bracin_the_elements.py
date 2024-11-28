#!/usr/bin/env python3
"""defines function that Performs element-wise"""


def np_elementwise(mat1, mat2):
    """
    Performs element-wise addition, subtraction, multiplication, and division on two matrices.

    Args:
        mat1: A numpy.ndarray.
        mat2: A numpy.ndarray or a scalar value.

    Returns:
        A tuple containing:
        - Element-wise sum (mat1 + mat2)
        - Element-wise difference (mat1 - mat2)
        - Element-wise product (mat1 * mat2)
        - Element-wise quotient (mat1 / mat2)
    """
    # Perform element-wise addition using the + operator
    return mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2
    