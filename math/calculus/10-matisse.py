#!/usr/bin/env python3
""" a script that calculates the sum of squares"""


def poly_derivative(poly):
    """
    Calculates the derivative of a polynomial.

    Args:
        poly (list): List of coefficients representing the polynomial.

    Returns:
    list: Coefficients of the derivative of the polynomial.
    """
    # Validate that poly is a list
    if not isinstance(poly, list) or not all(isinstance(x, (int, float)) for x in poly):
        return None

    # Handle the edge case where the polynomial is [0]
    if poly == [0]:
        return [0]

    # Calculate the derivative
    derivative = []
    for i in range(1, len(poly)):
        derivative.append(poly[i] * i)
    if not derivative:
        return [0]

    return derivative
