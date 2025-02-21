#!/usr/bin/env python3
import numpy as np

def grads(Y, P):
    """
    Calculates the gradients of Y and the Q affinities in the t-SNE algorithm.

    Parameters:
      Y: numpy.ndarray of shape (n, ndim)
         The low-dimensional representation of X.
      P: numpy.ndarray of shape (n, n)
         The P affinities of X.

    Returns:
      dY: numpy.ndarray of shape (n, ndim)
          The gradients of Y.
      Q: numpy.ndarray of shape (n, n)
          The Q affinities of Y.
    """
    # Import the Q_affinities function
    Q_affinities = __import__('5-Q_affinities').Q_affinities
    
    # Compute Q affinities for Y
    Q, num = Q_affinities(Y)  # Q has shape (n, n)
    
    # Ensure no division by zero (clip minimum value to avoid instability)
    PQ_diff = P - Q
    
    # Compute pairwise squared Euclidean distances in Y
    sum_Y = np.sum(np.square(Y), axis=1)
    distances = np.add(np.add(-2 * np.dot(Y, Y.T), sum_Y).T, sum_Y)

    # Compute 1 / (1 + ||y_i - y_j||^2)
    inv_distances = 1 / (1 + distances)

    # Compute the differences (Y[i] - Y[j])
    diff = Y[:, np.newaxis, :] - Y[np.newaxis, :, :]

    # Compute gradients
    dY = np.sum((PQ_diff * inv_distances)[:, :, np.newaxis] * diff, axis=1)

    return dY, Q
