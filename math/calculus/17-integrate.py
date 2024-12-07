#!/usr/bin/env python3
""" a script that calculates the integral of a polynomial:"""


def poly_integral(poly, C=0):
    """
    Calculates the integral of a polynomial.

    Args:
        poly (list): List of coefficients representing the polynomial.
        C (int): Integration constant.

    Returns:
        list: Coefficients of the integral of the polynomial.
    """
    # Validate inputs
    if not isinstance(poly, list) or not all(isinstance(c, (int, float)) for c in poly):
        return None
    if not isinstance(C, (int, float)):
        return None

    # Calculate the integral
    integral = [C]  # Start with the integration constant
    for i, coeff in enumerate(poly):
        integral.append(coeff / (i + 1))

    # Convert whole number coefficients to integers
    integral = [int(c) if c == int(c) else c for c in integral]

    return integral
