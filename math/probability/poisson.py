#!/usr/bin/env python3
""" a script that calculates the sum of squares"""

import math

class Poisson:
    def __init__(self, data=None, lambtha=1.):
        # Validate lambtha
        if lambtha <= 0:
            raise ValueError("lambtha must be a positive value")
        
        # If data is provided, calculate lambtha based on data
        if data is not None:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = sum(data) / len(data)  # Calculate lambtha from data
        else:
            # If no data is provided, use the given lambtha
            self.lambtha = float(lambtha)
    
    def pmf(self, k):
        """
        Calculate the probability mass function for a given k.
        """
        if k < 0 or not isinstance(k, int):
            raise ValueError("k must be a non-negative integer")
        
        # Poisson PMF formula: P(X = k) = (lambda^k * e^(-lambda)) / k!
 