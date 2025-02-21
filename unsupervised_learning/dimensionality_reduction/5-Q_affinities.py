#!/usr/bin/env python3
import numpy as np


def Q_affinities(Y):
    """
    Calculates the Q affinities for the low-dimensional
     representation of X.

    Parameters:
      Y: numpy.ndarray of shape (n, ndim)
         The low-dimensional representation of X.

    Returns:
      Q: numpy.ndarray of shape (n, n)
         The Q affinities matrix.
      num: numpy.ndarray of shape (n, n)
         The numerator of the Q affinities.
    """
    # Compute pairwise squared Euclidean distances in Y
    sum_Y = np.sum(np.square(Y), axis=1)
    distances = np.add(np.add(-2 * np.dot(Y, Y.T), sum_Y).T, sum_Y)

    # Compute the numerator of Q: 1 / (1 + ||y_i - y_j||^2)
    num = 1 / (1 + distances)

    # Set diagonal elements to zero (self-affinities should be 0)
    np.fill_diagonal(num, 0)

    # Compute the denominator: sum of all numerators
    denom = np.sum(num)

    # Compute Q affinities
    Q = num / denom

    return Q, num
