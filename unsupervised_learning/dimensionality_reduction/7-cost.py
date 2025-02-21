#!/usr/bin/env python3
"""That that calculates the cost of the t-SNE transformation"""
import numpy as np


def cost(P, Q):
    """
    Calculates the t-SNE cost (KL divergence between P and Q).
    
    Parameters:
      P: numpy.ndarray of shape (n, n)
         The P affinities.
      Q: numpy.ndarray of shape (n, n)
         The Q affinities.
    
    Returns:
      C: float
         The cost of the t-SNE transformation.
         Computed as: C = sum(P * log(P / Q))
         
         Small values (e.g., 1e-12) are used to avoid division by zero.
    """
    eps = 1e-12
    # Avoid division by zero by capping the minimum values in P and Q
    P_safe = np.maximum(P, eps)
    Q_safe = np.maximum(Q, eps)
    C = np.sum(P_safe * np.log(P_safe / Q_safe))
    return C
