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
    """
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        return None, None, None
    if not isinstance(g, np.ndarray) or len(g.shape) != 2:
        return None, None, None
    if X.shape[0] != g.shape[1]:
        return None, None, None
    
    n, d = X.shape
    k = g.shape[0]

    # Compute the new priors
    Nk = np.sum(g, axis=1)
    pi = Nk / n

    # Compute the new means
    m = np.dot(g, X) / Nk[:, np.newaxis]

    # Compute the new covariance matrices using a single loop
    S = np.zeros((k, d, d))
    for i in range(k):
        X_centered = X - m[i]  # Centered data points
        S[i] = np.dot(g[i] * X_centered.T, X_centered) / Nk[i]

    return pi, m, S
