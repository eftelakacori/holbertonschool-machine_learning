#!/usr/bin/env python3
"""A function that saves a model's weights"""
import tensorflow.keras as K


def save_weights(network, filename, save_format='h5'):
    """A function that saves a model's weights"""
    network.save_weights(filename, save_format=save_format)
    return None


def load_weights(network, filename):
    """A function that loads the weights"""
    network.load_weights(filename)
    return None
