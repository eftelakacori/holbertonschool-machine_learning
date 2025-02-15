#!/usr/bin/env python3
"""Expectation-Maximization Step (Maximization) for Gaussian Mixture Model (GMM)"""
import numpy as np

def maximization(X, g):
    """
    Performs the maximization step in the EM algorithm for a Gaussian Mixture Model (GMM).

    Parameters:
    X : numpy.ndarray of shape (n, d) - The dataset of n samples, each with d features
    g : numpy.ndarray of shape (k, n) - Posterior probabilities of each sample belonging to each of k clusters

    Returns:
    pi : numpy.ndarray of shape (k,) - The updated priors for each cluster
    m : numpy.ndarray of shape (k, d) - The updated means (centroids) of each cluster
    S : numpy.ndarray of shape (k, d, d) - The updated covariance matrices for each cluster
    """

    # Validate inputs: Ensure X and g are numpy arrays and have the correct dimensions
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        return None, None, None
    if not isinstance(g, np.ndarray) or len(g.shape) != 2:
        return None, None, None
    if X.shape[0] != g.shape[1]:
        return None, None, None

    # Validate that the posterior probabilities (g) are between 0 and 1
    if not np.all((g >= 0) & (g <= 1)):
        return None, None, None

    # Number of samples (n) and number of features (d) in the dataset
    n, d = X.shape
    # Number of clusters (k)
    k = g.shape[0]

    # Compute the effective sample size for each cluster (Nk)
    Nk = np.sum(g, axis=1)

    # If any cluster has zero samples assigned to it, return None (invalid case)
    if np.any(Nk == 0):
        return None, None, None

    # Compute the updated priors (pi) for each cluster
    pi = Nk / n

    # Compute the updated means (m) for each cluster
    m = np.dot(g, X) / Nk[:, np.newaxis]

    # Compute the updated covariance matrices (S) for each cluster
    X_expanded = X[:, np.newaxis, :] - m  # Shape (n, k, d)
    S = np.einsum('kn, nkd, nkc -> kdc', g, X_expanded, X_expanded) / Nk[:, np.newaxis, np.newaxis]

    return pi, m, S
