#!/usr/bin/env python3
"""That performs PCA on a dataset"""
import numpy as np

def pca(X, var=0.95):
    """
    Perform PCA on the dataset X and return the weights matrix W.
    Parameters:
    X (numpy.ndarray): Input data of shape (n, d).
    var (float): Fraction of the variance to maintain (default is 0.95).
    Returns:
    W (numpy.ndarray): Weights matrix of shape (d, nd).
    """
    # Step 1: Compute the covariance matrix
    cov_matrix = np.cov(X, rowvar=False)

    # Step 2: Perform eigenvalue decomposition
    eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

    # Step 3: Sort eigenvalues and corresponding eigenvectors
    sorted_indices = np.argsort(eigenvalues)[::-1]
    sorted_eigenvalues = eigenvalues[sorted_indices]
    sorted_eigenvectors = eigenvectors[:, sorted_indices]

    # Step 4: Select the top eigenvectors that capture the desired variance
    total_variance = np.sum(sorted_eigenvalues)
    cumulative_variance = np.cumsum(sorted_eigenvalues) / total_variance
    num_components = np.argmax(cumulative_variance >= var) + 1

    # Ensure at least 3 dimensions are retained
    num_components = max(num_components, 3)

    # Step 5: Return the weights matrix W
    W = sorted_eigenvectors[:, :num_components]
    
    return W

# Example usage
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
    print(T.shape)
    W = pca(X_m, var=0.99)  # Test with a higher variance threshold
    T = np.matmul(X_m, W)
    print(T)
    print(T.shape)
