#!/usr/bin/env python3
"""Expectation Module"""
import numpy as np

def maximization(X, g):
    """
    Maximization step of the EM algorithm for Gaussian Mixture Models (GMM).

    X: numpy.ndarray of shape (n, d) containing the data set.
    g: numpy.ndarray of shape (k, n) containing the posterior probabilities for each data point in each cluster.

    Returns:
    pi: numpy.ndarray of shape (k,) containing the updated priors for each cluster.
    m: numpy.ndarray of shape (k, d) containing the updated centroid means for each cluster.
    S: numpy.ndarray of shape (k, d, d) containing the updated covariance matrices for each cluster.
    """

    # Check if the inputs are valid
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        return None, None, None
    if not isinstance(g, np.ndarray) or len(g.shape) != 2:
        return None, None, None
    n, d = X.shape
    k, n_g = g.shape
    
    # Ensure g has the correct shape (k, n) and the same number of data points
    if n != n_g:
        return None, None, None

    # Check if g contains any NaN or Inf values
    if np.isnan(g).any() or np.isinf(g).any():
        return None, None, None

    # Calculate updated priors (pi)
    pi = g.sum(axis=1) / n

    # Calculate updated means (m)
    m = np.dot(g, X) / g.sum(axis=1)[:, np.newaxis]

    # Calculate updated covariance matrices (S)
    S = np.zeros((k, d, d))
    for i in range(k):
        # Center the data by subtracting the mean for each cluster
        X_centered = X - m[i]
        # Compute covariance for each cluster
        S[i] = np.dot(g[i] * X_centered.T, X_centered) / g[i].sum()

    return pi, m, S
