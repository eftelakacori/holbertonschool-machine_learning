#!/usr/bin/env python3 
"""
    Create layer with L2 regularization
"""

import tensorflow as tf

def l2_reg_create_layer(prev, n, activation, lambtha):
    """
        Function that creates a tensorflow layer with L2 regularization
    """
    # Set initialization to He et al.
    initializer = tf.keras.initializers.VarianceScaling(scale=2.0, mode='fan_avg')

    # Create the Dense layer with L2 regularization
    new_layer = tf.keras.layers.Dense(
        units=n,
        activation=activation,
        kernel_initializer=initializer,
        kernel_regularizer=tf.keras.regularizers.l2(lambtha),
        name="layer"
    )

    # Apply the layer to the input
    output = new_layer(prev)

    return output
