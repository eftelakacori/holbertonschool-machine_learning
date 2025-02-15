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

    n, d = X.shape  # n is the number of data points, d is the number of features
    k, n_g = g.shape  # k is the number of clusters, n_g is the number of data points (should match n)

    if n != n_g:
        return None, None, None

    # Calculate updated priors (pi)
    pi = g.sum(axis=1) / n  # sum along the rows of g and normalize by the number of data points

    # Calculate updated means (m)
    m = np.dot(g, X) / g.sum(axis=1)[:, np.newaxis]  # weighted sum of data points for each cluster

    # Calculate updated covariance matrices (S)
    S = np.zeros((k, d, d))  # Initialize covariance matrices

    for i in range(k):  # Loop over the clusters
        X_centered = X - m[i]  # Center the data points by subtracting the mean
        S[i] = np.dot((g[i] * X_centered.T), X_centered) / g[i].sum()  # Compute the covariance matrix for cluster i

    return pi, m, S
