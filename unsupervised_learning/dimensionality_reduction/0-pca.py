#!/usr/bin/env python3
"""That performs PCA on a dataset"""
import numpy as np

def pca(X, var=0.95):
    """
    Perform Principal Component Analysis (PCA) on the dataset X
    to retain a fraction of the total variance specified by var.
    
    Parameters:
    - X: numpy.ndarray of shape (n, d) where n is the number of data points 
         and d is the number of dimensions of each data point.
    - var: Fraction of variance to retain (default is 0.95).

    Returns:
    - W: numpy.ndarray of shape (d, nd) where nd is the number of dimensions 
         after reduction (which keeps the specified variance).
    """
    # Compute the covariance matrix of the centered data
    X_centered = X - np.mean(X, axis=0)
    cov_matrix = np.cov(X_centered, rowvar=False)

    # Eigenvalue decomposition
    eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)

    # Sort the eigenvalues in descending order and get the corresponding eigenvectors
    sorted_indices = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[sorted_indices]
    eigenvectors = eigenvectors[:, sorted_indices]

    # Calculate the cumulative variance explained
    explained_variance = eigenvalues / np.sum(eigenvalues)
    cumulative_variance = np.cumsum(explained_variance)

    # Print out the cumulative variance to debug
    print(f"Cumulative Variance Explained: {cumulative_variance}")

    # Find the number of components to retain the desired variance
    num_components = np.argmax(cumulative_variance >= var) + 1

    # Select the eigenvectors corresponding to the largest eigenvalues
    W = eigenvectors[:, :num_components]

    return W
