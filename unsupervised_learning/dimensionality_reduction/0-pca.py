#!/usr/bin/env python3
"""That performs PCA on a dataset"""
import numpy as np

def pca(X, var=0.95):
    # Step 1: Compute the covariance matrix
    cov_matrix = np.cov(X, rowvar=False)

    # Step 2: Perform eigen decomposition
    eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)

    # Step 3: Sort eigenvalues and eigenvectors in descending order
    sorted_indices = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[sorted_indices]
    eigenvectors = eigenvectors[:, sorted_indices]

    # Step 4: Calculate the cumulative variance
    total_variance = np.sum(eigenvalues)
    cumulative_variance = np.cumsum(eigenvalues) / total_variance

    # Step 5: Find the number of components needed to maintain the specified variance
    num_components = np.argmax(cumulative_variance >= var) + 1

    # Step 6: Select the first 'num_components' eigenvectors
    W = eigenvectors[:, :num_components]

    return W
