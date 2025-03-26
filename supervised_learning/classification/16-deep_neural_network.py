#!/usr/bin/env python3
"""
a class that defines a deep neural network performing
binary classification
"""
import numpy as np


class DeepNeuralNetwork:
    """
    A class that defines a deep neural network performing
    binary classification.
    """
    def __init__(self, nx, layers):
        """Class constructor."""

        # Check if nx is an integer
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")

        # Check if nx is a positive integer
        if nx < 1:
            raise ValueError("nx must be a positive integer")

        # Check if layers is a list
        if not isinstance(layers, list) or len(layers) == 0:
            raise TypeError("layers must be a list of positive integers")

        # Check if all elements in layers are positive integers
        for i, n in enumerate(layers):
            if not isinstance(n, int) or n < 1:
                raise TypeError("layers must be a list of positive integers")

            # Initialize weights and biases using He initialization
            if i == 0:
                self.weights = {"W1": np.random.randn(n, nx) * np.sqrt(2 / nx),
                                "b1": np.zeros((n, 1))}
            else:
                self.weights["W{}".format(i + 1)] = \
                    np.random.randn(n, layers[i - 1]) * np.sqrt(2 / layers[i - 1])
                self.weights["b{}".format(i + 1)] = np.zeros((n, 1))

        # Set the number of layers (L) in the network
        self.L = len(layers)

        # Initialize the cache dictionary to store intermediary results
        self.cache = {}
