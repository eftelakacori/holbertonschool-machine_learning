#!/usr/bin/env python3
"""That performs PCA on a dataset"""
import numpy as np


def pca(X, var=0.95):
    """
    Perform PCA on the dataset X to retain a fraction var of the variance.
    
    Parameters:
    - X: numpy.ndarray of shape (n, d), where n is the number of data points
      and d is the number of features.
    - var: float, fraction of variance to retain.
    
    Returns:
    - W: numpy.ndarray of shape (d, nd), weight matrix that projects the data
      onto the new space with reduced dimensions.
    """

    # Step 1: Compute the covariance matrix
    cov_matrix = np.cov(X.T)

    # Step 2: Compute eigenvalues and eigenvectors of the covariance matrix
    eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)

    # Step 3: Sort eigenvalues in descending order and get the corresponding eigenvectors
    sorted_indices = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[sorted_indices]
    eigenvectors = eigenvectors[:, sorted_indices]

    # Step 4: Calculate the cumulative variance
    total_variance = np.sum(eigenvalues)
    cumulative_variance = np.cumsum(eigenvalues) / total_variance

    # Step 5: Select the number of components that preserve the required variance
    nd = np.where(cumulative_variance >= var)[0][0] + 1
 
    # Step 6: Select the corresponding eigenvectors (principal components)
    W = eigenvectors[:, :nd]

    return W
