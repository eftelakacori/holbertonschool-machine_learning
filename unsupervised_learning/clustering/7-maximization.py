#!/usr/bin/env python3
"""Expectation Module"""
import numpy as np

def maximization(X, g):
    """
    Performs the maximization step in the EM algorithm for a Gaussian Mixture Model.
    
    Parameters:
    - X: numpy.ndarray of shape (n, d) containing the dataset
    - g: numpy.ndarray of shape (k, n) containing the posterior probabilities
         for each data point in each cluster
    
    Returns:
    - pi: numpy.ndarray of shape (k,) containing the updated priors for each cluster
    - m: numpy.ndarray of shape (k, d) containing the updated centroid means for each cluster
    - S: numpy.ndarray of shape (k, d, d) containing the updated covariance matrices for each cluster
    - None, None, None on failure
    """
    if not isinstance(X, np.ndarray) or not isinstance(g, np.ndarray):
        return None, None, None
    if len(X.shape) != 2 or len(g.shape) != 2:
        return None, None, None
    
    n, d = X.shape
    k, n_g = g.shape
    
    if n != n_g:
        return None, None, None
    
    # Sum of posterior probabilities for each cluster (Nk)
    Nk = np.sum(g, axis=1)
    if np.any(Nk == 0):  # Avoid division by zero
        return None, None, None
    
    # Compute updated priors
    pi = Nk / n
    
    # Compute updated means
    m = (g @ X) / Nk[:, np.newaxis]
    
    # Compute updated covariance matrices
    S = np.zeros((k, d, d))
    for i in range(k):
        diff = X - m[i]  # (n, d)
        S[i] = (g[i, :, np.newaxis] * diff).T @ diff / Nk[i]
    
    return pi, m, S
