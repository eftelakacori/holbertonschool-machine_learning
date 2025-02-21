#!/usr/bin/env python3
"""That calculates the gradients of Y"""
import numpy as np


def grads(Y, P):
    """
    Calculates the gradients of Y and computes the Q affinities.

    Parameters:
      Y: numpy.ndarray of shape (n, ndim)
         The low-dimensional representation.
      P: numpy.ndarray of shape (n, n)
         The P affinities computed in t-SNE.

    Returns:
      dY: numpy.ndarray of shape (n, ndim)
          The gradient of Y (do not multiply by 4).
      Q: numpy.ndarray of shape (n, n)
          The Q affinities computed from Y.
    """
    # Import the Q affinities function
    Q_affinities = __import__('5-Q_affinities').Q_affinities
    n = Y.shape[0]

    # Compute Q affinities for Y
    Q = Q_affinities(Y)  # Q has shape (n, n)

    # Compute pairwise squared Euclidean distances in Y
    sum_Y = np.sum(Y**2, axis=1)
    # D[i,j] = ||Y[i]-Y[j]||^2
    distances = np.add(np.add(-2 * np.dot(Y, Y.T), sum_Y).T, sum_Y)

    # Compute the factor: 1 / (1 + ||y_i - y_j||^2)
    factor = 1 / (1 + distances)

    # Compute differences between all pairs: shape (n, n, ndim)
    diff = Y[:, np.newaxis, :] - Y[np.newaxis, :, :]

    # Expand (P - Q) to match diff's shape: (n, n, 1)
    PQ_diff = (P - Q)[:, :, np.newaxis]

    # Expand factor to shape (n, n, 1)
    factor_exp = factor[:, :, np.newaxis]

    # Compute gradients:
    # dY[i] = sum_j (P_ij - Q_ij) * factor[i,j] * (Y[i] - Y[j])
    dY = np.sum(PQ_diff * factor_exp * diff, axis=1)

    return dY, Q
