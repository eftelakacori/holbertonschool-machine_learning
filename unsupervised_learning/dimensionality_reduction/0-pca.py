#!/usr/bin/env python3
"""That performs PCA on a dataset"""


import numpy as np


def pca(X, var=0.95):
    """
    Performs PCA on dataset X.

    X is a numpy.ndarray of shape (n, d) where:
      - n: number of data points
      - d: number of dimensions in each point
    All dimensions have mean 0.

    var is the fraction of variance to maintain.
    Returns:
      W, a numpy.ndarray of shape (d, nd) where
      nd is the new dimensionality that maintains
      var fraction of X's variance.
    """
    # Compute covariance matrix of X
    cov_matrix = np.cov(X, rowvar=False)

    # Compute eigenvalues and eigenvectors
    eigvals, eigvecs = np.linalg.eigh(cov_matrix)

    # Sort eigenvalues and eigenvectors in descending order
    sorted_idx = np.argsort(eigvals)[::-1]
    eigvals = eigvals[sorted_idx]
    eigvecs = eigvecs[:, sorted_idx]

    # Compute cumulative variance ratio
    cumulative_var = np.cumsum(eigvals) / np.sum(eigvals)

    """Find minimum number of components to
    reach desired variance"""
    nd = np.argmax(cumulative_var >= var) + 1

    # Return top nd eigenvectors as the weights matrix
    return eigvecs[:, :nd]
