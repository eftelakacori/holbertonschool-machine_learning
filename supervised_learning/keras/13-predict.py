#!/usr/bin/env python3
"""
A function that makes a prediction using a neural network
"""
import tensorflow.keras as K


def predict(network, data, verbose=False):
    """A function that makes a prediction usinf a
    neural network"""
    prediction = network.predict(x=data,
                                 verbose=verbose)
    return prediction
