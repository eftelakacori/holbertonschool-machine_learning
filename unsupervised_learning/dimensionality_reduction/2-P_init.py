#!/usr/bin/env python3
"""That initializes all variables required to calculate """

import numpy as np


def P_init(X, perplexity):
    """
    Initializes variables for computing P affinities in t-SNE.

    Parameters:
      X : numpy.ndarray of shape (n, d)
          Dataset to be transformed. Each of the n points is in d dimensions.
          All dimensions have mean 0.
      perplexity : float
          The perplexity that all Gaussian distributions should have.

    Returns:
      D : numpy.ndarray of shape (n, n)
          Squared pairwise distance matrix between data points.
          The diagonal elements are 0.
      P : numpy.ndarray of shape (n, n)
          Initialized to all zeros, will store the P affinities.
      betas : numpy.ndarray of shape (n, 1)
          Initialized to all ones. Each beta_i = 1/(2 * sigma_i^2).
      H : float
          The Shannon entropy corresponding to the given perplexity,
          i.e. H = log2(perplexity).
    """
    n, d = X.shape
    # Compute squared pairwise distances:
    sum_X = np.sum(X**2, axis=1)
    D = sum_X.reshape(-1, 1) + sum_X.reshape(1, -1) - 2 * np.dot(X, X.T)
    np.fill_diagonal(D, 0)  # Ensure diagonal is 0

    # Initialize P as zeros and betas as ones:
    P = np.zeros((n, n))
    betas = np.ones((n, 1))

    # Compute Shannon entropy for the perplexity with base 2:
    H = np.log2(perplexity)

    return D, P, betas, H
