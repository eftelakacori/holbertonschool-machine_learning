#!/usr/bin/env python3
""" a script that calculates the sum of squares"""

class Poisson:
    def __init__(self, data=None, lambtha=1.):
        # Nëse lambtha është jo pozitiv, hidhet gabim
        if lambtha <= 0:
            raise ValueError("lambtha must be a positive value")
        
        # Nëse janë dhënë të dhëna, llogarit lambtha
        if data is not None:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = sum(data) / len(data)  # Mesatarja
        else:
            # Nëse të dhënat nuk janë dhënë, përdor lambtha e dhënë
            self.lambtha = float(lambtha)

