#!/usr/bin/env python3
"""
A function that saves a model’s configuration in JSON format
"""
import tensorflow.keras as K


def save_config(network, filename):
    """A function that saves a model's configuration
    in JSON format"""
    json = network.to_json()
    with open(filename, 'w+') as f:
        f.write(json)
    return None


def load_config(filename):
    """A function that loads the configuration"""
    with open(filename, 'r') as f:
        json_string = f.read()
    model = K.models.model_from_json(json_string)
    return model
