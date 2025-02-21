#!/usr/bin/env python3
"""That calculates the gradients of Y"""
import numpy as np

def tsne(X, ndims=2, idims=50, perplexity=30.0, iterations=1000, lr=500):
    pca = __import__('1-pca').pca
    P_affinities = __import__('4-P_affinities').P_affinities
    grads = __import__('6-grads').grads
    cost = __import__('7-cost').cost

    n, d = X.shape
    # Reduce dimensionality with PCA to idims
    X_pca = pca(X, idims)
    # Compute P affinities on the PCA-reduced data
    P = P_affinities(X_pca, perplexity)  # P has shape (n, n)
    # Initialize low-dim representation Y randomly
    Y = np.random.randn(n, ndims)
    # Initialize momentum variable
    v = np.zeros_like(Y)
    early_exag = 4

    for i in range(iterations + 1):
        # Apply early exaggeration for first 100 iterations
        if i < 100:
            P_current = P * early_exag
        else:
            P_current = P

        # Print cost every 100 iterations (excluding iteration 0)
        if i != 0 and i % 100 == 0:
            c = cost(Y, P_current)
            print("Cost at iteration {}: {}".format(i, c))

        # Compute gradient of the cost with respect to Y
        dY = grads(Y, P_current)
        # Set momentum: 0.5 for the first 20 iterations, 0.8 thereafter
        momentum = 0.5 if i < 20 else 0.8
        # Update the momentum and then Y
        v = momentum * v - lr * dY
        Y = Y + v
        # Re-center Y by subtracting its mean
        Y = Y - np.mean(Y, axis=0)
    
    return Y
