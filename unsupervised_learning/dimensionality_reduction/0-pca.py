#!/usr/bin/env python3
"""That performs PCA on a dataset"""
import numpy as np


def pca(X, var=0.95):
    """
    Performs Principal Component Analysis (PCA) on the dataset X
    :param X: numpy.ndarray of shape (n, d) where n is the number of data points,
              and d is the number of dimensions in each point
    :param var: fraction of the variance that the PCA transformation should maintain
    :return: the weights matrix W that maintains var fraction of X's original variance,
             W is a numpy.ndarray of shape (d, nd) where nd is the new dimensionality
    """
    # Step 1: Compute the covariance matrix
    cov_matrix = np.cov(X, rowvar=False)

    # Step 2: Compute the eigenvalues and eigenvectors
    eigvals, eigvecs = np.linalg.eigh(cov_matrix)

    # Step 3: Sort eigenvalues and eigenvectors in descending order
    sorted_idx = np.argsort(eigvals)[::-1]  # Sort indices by eigenvalues in descending order
    eigvals = eigvals[sorted_idx]
    eigvecs = eigvecs[:, sorted_idx]

    # Step 4: Compute cumulative variance ratio
    cumulative_var = np.cumsum(eigvals) / np.sum(eigvals)

    # Step 5: Find the number of principal components to retain the desired variance
    nd = np.argmax(cumulative_var >= var) + 1  # Find minimum number of components needed

    # Step 6: Select the top nd eigenvectors (principal components)
    W = eigvecs[:, :nd]

    return W
