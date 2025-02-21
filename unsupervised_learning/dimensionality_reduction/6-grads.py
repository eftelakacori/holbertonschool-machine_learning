#!/usr/bin/env python3
import numpy as np
Q_affinities = __import__('5-Q_affinities').Q_affinities


def grads(Y, P):
    """
    Calculate the gradients of Y.

    Parameters:
    Y (numpy.ndarray): Low-dimensional transformation of X, of shape (n, ndim).
    P (numpy.ndarray): P affinities of X, of shape (n, n).

    Returns:
    dY (numpy.ndarray): Gradients of Y, of shape (n, ndim).
    Q (numpy.ndarray): Q affinities of Y, of shape (n, n).
    """
    # Step 1: Compute Q affinities
    Q = Q_affinities(Y)

    # Step 2: Compute gradients
    n, ndim = Y.shape
    dY = np.zeros_like(Y)

    for i in range(n):
        diff = Y[i] - Y  # Shape: (n, ndim)
        pq_diff = (P[i] - Q[i])[:, np.newaxis]  # Shape: (n, 1)
        dY[i] = np.sum(pq_diff * diff, axis=0)  # Sum over j

    return dY, Q


# Example usage (as provided in the main script)
if __name__ == "__main__":
    np.random.seed(0)
    X = np.loadtxt("mnist2500_X.txt")
    X = pca(X, 50)
    P = P_affinities(X)
    Y = np.random.randn(X.shape[0], 2)
    dY, Q = grads(Y, P)
    print('dY:', dY.shape)
    print(dY)
    print('Q:', Q.shape)
    print(Q)
    print(np.sum(Q))
