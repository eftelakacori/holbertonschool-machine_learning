#!/usr/bin/env python3
""" a script that calculates the sum of squares"""


def poly_derivative(poly):
    """
    Calculates the derivative of a polynomial.

    Args:
        poly (list): List of coefficients representing the polynomial.

    Returns:
        list: Coefficients of the derivative of the polynomial, or None if input is invalid.
    """
    # Validate that poly is a list and each element is either an integer or a float
    if not isinstance(poly, list) or not all(isinstance(x, (int, float)) for x in poly):
        return None
    
    # Handle the edge case where the polynomial is [0]
    if poly == [0]:
        return [0]

    # Calculate the derivative
    derivative = []
    for i in range(1, len(poly)):  # Start from 1, as the derivative of a constant is 0
        derivative.append(poly[i] * i)

    # If the derivative is an empty list, meaning the original polynomial was a constant, return [0]
    if not derivative:
        return [0]

    return derivative
