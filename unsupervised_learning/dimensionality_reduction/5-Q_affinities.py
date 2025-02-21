#!/usr/bin/env python3
"""
Module for calculating Q affinities in t-SNE dimensionality reduction.

This module contains the function `Q_affinities`, which computes
the Q affinities and their numerators based on the low-dimensional
representation of data.
"""

import numpy as np

def Q_affinities(Y):
    """
    Calculates the Q affinities for the low-dimensional representation of X.

    Parameters:
      Y (numpy.ndarray): Shape (n, ndim), the low-dimensional representation of X.

    Returns:
      Q (numpy.ndarray): Shape (n, n), the Q affinities matrix.
      num (numpy.ndarray): Shape (n, n), the numerator of the Q affinities.
    """
    sum_Y = np.sum(np.square(Y), axis=1)
    distances = np.add(np.add(-2 * np.dot(Y, Y.T), sum_Y).T, sum_Y)
    
    num = 1 / (1 + distances)
    np.fill_diagonal(num, 0)

    denom = np.sum(num)
    Q = num / denom

    return Q, num
