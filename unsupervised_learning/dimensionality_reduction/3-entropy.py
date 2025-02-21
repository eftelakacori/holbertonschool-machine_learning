#!/usr/bin/env python3
"""That calculates the Shannon entropy and P affinities relative """
import numpy as np


def HP(Di, beta):
    """
    Calculate the Shannon entropy and P affinities relative
     to a data point.

    Parameters:
    Di (numpy.ndarray): Pairwise distances between a data
     point and all other points except itself, of shape (n - 1,).
    beta (numpy.ndarray): Beta value for the Gaussian
    distribution, of shape (1,).

    Returns:
    Hi (float): Shannon entropy of the points.
    Pi (numpy.ndarray): P affinities of the points, of shape (n - 1,).
    """
    # Step 1: Compute the P affinities using a Gaussian distribution
    Pi = np.exp(-Di * beta)
    Pi_sum = np.sum(Pi)
    Pi = Pi / Pi_sum  # Normalize to get probabilities

    # Step 2: Compute the Shannon entropy
    Hi = -np.sum(Pi * np.log2(Pi + 1e-12))

    return Hi, Pi


# Example usage (as provided in the main script)
if __name__ == "__main__":
    X = np.loadtxt("mnist2500_X.txt")
    X = pca(X, 50)
    D, P, betas, _ = P_init(X, 30.0)
    H0, P[0, 1:] = HP(D[0, 1:], betas[0])
    print(H0)
    print(P[0])
