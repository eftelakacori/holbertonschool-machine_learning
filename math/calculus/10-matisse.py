def poly_derivative(poly):
    """
    Calculates the derivative of a polynomial.

    Args:
        poly (list): Coefficients of the polynomial.

    Returns:
        list: Coefficients of the derivative, or None if invalid.
    """
    if not isinstance(poly, list) or len(poly) == 0 or not all(isinstance(c, (int, float)) for c in poly):
        return None
    
    if len(poly) == 1:  # Polinomi është konstant
        return [0]
    
    # Derivati
    derivative = [i * poly[i] for i in range(1, len(poly))]
    return derivative
