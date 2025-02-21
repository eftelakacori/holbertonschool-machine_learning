#!/usr/bin/env python3
import numpy as np


def pca(X, var=0.95):
    """
    Performs Principal Component Analysis (PCA) on a dataset,
    keeping a specified amount of variance.

    Parameters:
    - X: numpy.ndarray of shape (n, d), where:
        * n is the number of data points
        * d is the number of dimensions in each point
    - var: float, the fraction of variance to preserve.

    Returns:
    - W: numpy.ndarray of shape (d, nd), the transformation matrix 
         used for dimensionality reduction.
    """

    # Compute the covariance matrix of the dataset
    covariance_matrix = np.cov(X, rowvar=False)

    # Compute eigenvalues and eigenvectors of the covariance matrix
    eigenvalues, eigenvectors = np.linalg.eigh(covariance_matrix)

    # Sort eigenvalues and corresponding eigenvectors in descending order
    sorted_indices = np.argsort(eigenvalues)[::-1]
    sorted_eigenvalues = eigenvalues[sorted_indices]
    sorted_eigenvectors = eigenvectors[:, sorted_indices]

    # Compute cumulative variance
    cumulative_variance = np.cumsum(sorted_eigenvalues) / np.sum(sorted_eigenvalues)

    # Find the number of components that retain the required variance
    nd = np.searchsorted(cumulative_variance, var) + 1

    # Select the first 'nd' eigenvectors (principal components)
    W = sorted_eigenvectors[:, :nd]

    # DEBUG: Print relevant information to verify the output
    print("Eigenvalues:", sorted_eigenvalues)
    print("Cumulative Variance:", cumulative_variance)
    print("Number of selected components (nd):", nd)
    print("Shape of transformation matrix W:", W.shape)

    return W
