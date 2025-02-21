#!/usr/bin/env python3
import numpy as np


def pca(X, var=0.95):
    """
    Performs PCA on a dataset to reduce dimensionality while
    preserving variance.

    Parameters:
    X (numpy.ndarray): Dataset of shape (n, d) where n is the
    number of samples and d is the number of features.
    var (float): Fraction of variance to preserve (default is
    0.95).

    Returns:
    numpy.ndarray: Weight matrix W of shape (d, nd), where nd
    is the new dimensionality.
    """
    # 1. Calculate the covariance matrix
    cov_matrix = np.cov(X, rowvar=False)

    # 2. Compute the eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)

    # 3. Sort the eigenvalues and corresponding eigenvectors
    sorted_indices = np.argsort(eigenvalues)[::-1] 
    sorted_eigenvalues = eigenvalues[sorted_indices]
    sorted_eigenvectors = eigenvectors[:, sorted_indices]

    # 4. Check the cumulative variance to understand
    # how much variance is captured
    cumulative_variance = np.cumsum(sorted_eigenvalues) / np.sum(
        sorted_eigenvalues)
    print(f'Cumulative variance: {cumulative_variance}')  

    # 5. Find the number of components that preserve
    # the required fraction of variance
    nd = np.searchsorted(cumulative_variance, var) + 1 

    # 6. Select the first `nd` eigenvectors to form
    # the weight matrix W
    W = sorted_eigenvectors[:, :nd]

    # Return the weight matrix
    return W
