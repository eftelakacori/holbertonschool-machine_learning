#!/usr/bin/env python3
"""Expectation Module"""
import numpy as np

def maximization(X, g):
    """
    Performs the maximization step in the EM algorithm for a GMM.

    Parameters:
    X : numpy.ndarray of shape (n, d) - dataset
    g : numpy.ndarray of shape (k, n) - posterior probabilities for each data point in each cluster

    Returns:
    pi : numpy.ndarray of shape (k,) - updated priors for each cluster
    m : numpy.ndarray of shape (k, d) - updated centroid means for each cluster
    S : numpy.ndarray of shape (k, d, d) - updated covariance matrices for each cluster
    or
    "invalid g" if g is not a valid posterior probability distribution.
    """
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        return "invalid g"
    if not isinstance(g, np.ndarray) or len(g.shape) != 2:
        return "invalid g"
    if X.shape[0] != g.shape[1]:  # Ensure number of samples match
        return "invalid g"

    # Sum of posterior probabilities per sample must be 1 (i.e., sum along axis 0)
    if not np.allclose(np.sum(g, axis=0), 1):
        return "invalid g"

    n, d = X.shape
    k = g.shape[0]

    # Compute Nk (sum of probabilities for each cluster)
    Nk = np.sum(g, axis=1)

    # Ensure no cluster has zero probability sum
    if np.any(Nk == 0):
        return "invalid g"

    # Compute priors
    pi = Nk / n

    # Compute means
    m = np.dot(g, X) / Nk[:, np.newaxis]

    # Compute covariance matrices
    S = np.zeros((k, d, d))
    for i in range(k):
        X_centered = X - m[i]  # Centered data points
        S[i] = np.dot(g[i] * X_centered.T, X_centered) / Nk[i]

    return pi, m, S
