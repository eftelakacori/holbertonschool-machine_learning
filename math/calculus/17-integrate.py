#!/usr/bin/env python3
""" a script that calculates the integral of a polynomial:"""


def poly_integral(poly, C=0):
    """
    Calculates the integral of a polynomial.

    Args:
        poly (list): List of coefficients representing the polynomial.
        C (int): Integration constant.

    Returns:
        list: Coefficients of the integral of the polynomial, or None if input is invalid.
    """
    # Validate that poly is a list and each element is either an integer or a float
    if not isinstance(poly, list) or not all(isinstance(x, (int, float)) for x in poly):
        return None
    # Validate that C is either an integer or a float
    if not isinstance(C, (int, float)):
        return None

    # Handle the edge case where the polynomial is [0]
    if poly == [0]:
        return [C]

    # Calculate the integral
    integral = [C]  # Start with the integration constant
    for i, coeff in enumerate(poly):
        integral.append(coeff / (i + 1))

    # Convert whole number coefficients to integers
    integral = [int(c) if c == int(c) else c for c in integral]

    return integral
