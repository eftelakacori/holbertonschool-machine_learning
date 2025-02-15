#!/usr/bin/env python3
"""Expectation-Maximization Step (Maximization) for Gaussian Mixture Model (GMM)"""
import numpy as np

def maximization(X, g):
    # Check if X is valid
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        return None, None, None
    if not isinstance(g, np.ndarray) or len(g.shape) != 2:
        return None, None, None
    if X.shape[0] != g.shape[1]:
        return None, None, None

    n, d = X.shape  # number of data points, number of features
    k = g.shape[0]  # number of clusters

    # 1. Update priors (pi)
    pi = g.sum(axis=1) / n

    # 2. Update means (m)
    m = np.dot(g, X) / g.sum(axis=1)[:, np.newaxis]

    # 3. Update covariances (S)
    S = np.zeros((k, d, d))
    for i in range(k):
        X_centered = X - m[i]
        S[i] = np.dot(g[i] * X_centered.T, X_centered) / g[i].sum()

    return pi, m, S

# Example usage:
if __name__ == '__main__':
    # Generating example data and posterior probabilities g
    np.random.seed(11)
    a = np.random.multivariate_normal([30, 40], [[75, 5], [5, 75]], size=10000)
    b = np.random.multivariate_normal([5, 25], [[16, 10], [10, 16]], size=750)
    c = np.random.multivariate_normal([60, 30], [[16, 0], [0, 16]], size=750)
    d = np.random.multivariate_normal([20, 70], [[35, 10], [10, 35]], size=1000)
    X = np.concatenate((a, b, c, d), axis=0)
    np.random.shuffle(X)

    # Initialize g (posterior probabilities) as an example
    g = np.random.rand(4, X.shape[0])  # 4 clusters, X.shape[0] data points
    g = g / g.sum(axis=0)  # Normalize to make it a valid probability distribution

    # Call the maximization function
    pi, m, S = maximization(X, g)

    # Output results
    print("Updated priors (pi):", pi)
    print("Updated means (m):", m)
    print("Updated covariance matrices (S):", S)
