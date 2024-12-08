#!/usr/bin/env python3
""" a script that calculates the sum of squares"""


def poly_derivative(poly):
    """
    Calculates the derivative of a polynomial.

    Args:
        poly (list): Coefficients of the polynomial.

    Returns:
        list: Coefficients of the derivative, or None if invalid.
    """
    # Verifikimi nëse poly është një listë e vlefshme
    if not isinstance(poly, list) or len(poly) == 0 or not all(isinstance(c, (int, float)) for c in poly):
        return None

    # Nëse polinomi është konstant (përmban vetëm një element)
    if len(poly) == 1:
        return [0]

    # Përllogarit derivatin: cdo koeficient shumëzohet me fuqinë përkatëse të x
    derivative = [i * poly[i] for i in range(1, len(poly))]

    return derivative
