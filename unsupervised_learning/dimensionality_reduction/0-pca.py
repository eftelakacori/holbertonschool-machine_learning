#!/usr/bin/env python3
"""That performs PCA on a dataset"""
import numpy as np


def pca(X, var=0.95):
    """
    Performs PCA on a dataset to reduce dimensionality
     while preserving variance.

    Parameters:
    X (numpy.ndarray): Dataset of shape (n, d) where
     n is the number of samples and d is the number of features.
    var (float): Fraction of variance to preserve (default is 0.95).

    Returns:
    numpy.ndarray: Weight matrix W of shape (d, nd), where
     nd is the new dimensionality.
    """
    # 1. Calculate the covariance matrix
    """ This matrix represents the relationship between 
    the different features (dimensions)"""
    cov_matrix = np.cov(X, rowvar=False)

    """2. Compute the eigenvalues and
     eigenvectors of the covariance matrix"""
    # Eigenvalues indicate the importance of each principal component, 
    # and eigenvectors represent the direction of these components.
    eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)

     """3. Sort the eigenvalues and corresponding
     eigenvectors in descending order
     The higher the eigenvalue, the more variance it
      captures, so we sort by importance."""
    sorted_indices = np.argsort(eigenvalues)[::-1]  # Sorting indices in descending order
    sorted_eigenvalues = eigenvalues[sorted_indices]
    sorted_eigenvectors = eigenvectors[:, sorted_indices]

    """4. Find the number of components that preserve
     the required fraction of variance
     We calculate the cumulative variance
      and select the number of components (nd) 
    that together maintain at least `var` (e.g., 95%)
     of the total variance."""
    cumulative_variance = np.cumsum(sorted_eigenvalues) / np.sum(sorted_eigenvalues)
    nd = np.searchsorted(cumulative_variance, var) + 1  

    """5. Select the first `nd` eigenvectors to form the weight matrix W
      These eigenvectors correspond to the principal components
       we use for dimensionality reduction."""
    W = sorted_eigenvectors[:, :nd]

    """Return the weight matrix, which will be used
     to transform the dataset to a lower dimension"""
    return W
