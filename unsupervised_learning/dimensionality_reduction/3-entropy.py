#!/usr/bin/env python3
"""That calculates the Shannon entropy and P affinities relative """
import numpy as np


def HP(Di, beta):
    """
    Calculates the Shannon entropy (base 2) and the P affinities
    for one data point.

    Parameters:
      Di : numpy.ndarray of shape (n-1,)
           The squared distances from one data point to all others.
      beta : numpy.ndarray of shape (1,) or scalar
           The beta value for the Gaussian distribution
           (beta = 1/(2*sigma^2)).

    Returns:
      Hi : float
           The Shannon entropy (base 2) of the points.
      Pi : numpy.ndarray of shape (n-1,)
           The P affinities for the points.
    """
    P = np.exp(-beta * Di)
    sumP = np.sum(P)
    H = np.log(sumP) + beta * np.sum(Di * P) / sumP
    H = H / np.log(2)
    P = P / sumP
    return H, P
