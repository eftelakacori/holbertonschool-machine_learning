#!/usr/bin/env python3
"""
Module for calculating symmetric P affinities in t-SNE.

This module contains the function `P_affinities`, which computes
the probability distribution P using pairwise similarities and
perplexity constraints.
"""

import numpy as np


P_init = __import__('2-P_init').P_init
HP = __import__('3-entropy').HP


def P_affinities(X, tol=1e-5, perplexity=30.0):
    """
    Calculates the symmetric P affinities of a dataset.

    Parameters:
      X (numpy.ndarray): Shape (n, d), dataset to be transformed.
      tol (float): Tolerance for the difference in Shannon entropy.
      perplexity (float): Desired perplexity value.

    Returns:
      P (numpy.ndarray): Shape (n, n), symmetric P affinities matrix.
    """
    n, d = X.shape
    P, betas, D = P_init(X)  # Initialize P, betas, and distance matrix

    log_perp = np.log(perplexity)

    for i in range(n):
        beta_min = None
        beta_max = None
        beta = betas[i]

        # Perform binary search to find the optimal beta
        while True:
            Hi, Pi = HP(D[i], beta)
            diff = Hi - log_perp

            if np.abs(diff) <= tol:
                break

            if diff > 0:  # Entropy too high, increase beta
                beta_min = beta
                if beta_max is None:
                    beta *= 2
                else:
                    beta = (beta + beta_max) / 2
            else:  # Entropy too low, decrease beta
                beta_max = beta
                if beta_min is None:
                    beta /= 2
                else:
                    beta = (beta + beta_min) / 2

        P[i] = Pi
        betas[i] = beta

    # Compute the symmetric P matrix
    P = (P + P.T) / (2 * n)

    return P
