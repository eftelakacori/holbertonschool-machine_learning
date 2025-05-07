#!/usr/bin/env python3
"""
Creates a layer with L2 regularization
"""

import tensorflow as tf


def l2_reg_create_layer(prev, n, activation, lambtha):
    """
    Creates a TensorFlow layer that includes L2 regularization

    Parameters:
    - prev: tensor containing the output of the previous layer
    - n: number of nodes in the new layer
    - activation: activation function for the layer
    - lambtha: L2 regularization parameter

    Returns:
    - The output tensor of the created layer
    """
    regularizer = tf.keras.regularizers.L2(lambtha)
    layer = tf.keras.layers.Dense(units=n,
                                  activation=activation,
                                  kernel_regularizer=regularizer)
    return layer(prev)
