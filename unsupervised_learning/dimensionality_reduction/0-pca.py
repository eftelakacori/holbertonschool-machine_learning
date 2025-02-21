#!/usr/bin/env python3
"""That performs PCA on a dataset"""
import numpy as np


def pca(X, var=0.95):
    """
    Perform PCA on the dataset X to retain a specified
    fraction of the variance.

    Parameters:
    X (numpy.ndarray): Input data of shape (n, d), where n is the number of
                       data points and d is the number of dimensions.
    var (float): Fraction of the variance to retain (default is 0.95).

    Returns:
    W (numpy.ndarray): Weights matrix of shape (d, nd), where nd is the new
                       dimensionality.
    """
    # Step 1: Compute the covariance matrix
    cov_matrix = np.cov(X, rowvar=False)

    # Step 2: Perform eigenvalue decomposition
    eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)

    # Step 3: Sort eigenvalues and eigenvectors in descending order
    sorted_indices = np.argsort(eigenvalues)[::-1]
    sorted_eigenvalues = eigenvalues[sorted_indices]
    sorted_eigenvectors = eigenvectors[:, sorted_indices]

    # Step 4: Determine the number of components to retain the variance
    total_variance = np.sum(sorted_eigenvalues)
    explained_variance_ratio = np.cumsum(sorted_eigenvalues) / total_variance
    num_components = np.argmax(explained_variance_ratio >= var) + 1

    # Step 5: Construct the weights matrix W
    W = sorted_eigenvectors[:, :num_components]

    return W


# Example usage (as provided in the main script)
if __name__ == "__main__":
    np.random.seed(0)
    a = np.random.normal(size=50)
    b = np.random.normal(size=50)
    c = np.random.normal(size=50)
    d = 2 * a
    e = -5 * b
    f = 10 * c

    X = np.array([a, b, c, d, e, f]).T
    m = X.shape[0]
    X_m = X - np.mean(X, axis=0)
    W = pca(X_m)
    T = np.matmul(X_m, W)
    print(T)
    X_t = np.matmul(T, W.T)
    print(np.sum(np.square(X_m - X_t)) / m
