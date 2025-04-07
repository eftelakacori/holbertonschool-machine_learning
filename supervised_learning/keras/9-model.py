#!/usr/bin/env python3
"""A function that saves an entire model"""
import tensorflow.keras as K


def save_model(network, filename):
    """A function that saves an entire model"""
    network.save(filename)
    return None


def load_model(filename):
    """A function that loads the model"""
    model = K.models.load_model(filename)
    return model
