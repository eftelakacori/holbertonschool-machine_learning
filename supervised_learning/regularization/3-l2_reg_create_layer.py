# 3-l2_reg_create_layer.py

import tensorflow as tf
from tensorflow.keras import regularizers

def l2_reg_create_layer(prev, n, activation, lambtha):
    """
    Creates a neural network layer with L2 regularization.

    Arguments:
    prev -- tensor containing the output of the previous layer
    n -- the number of nodes the new layer should contain
    activation -- activation function to use for the new layer
    lambtha -- the L2 regularization parameter

    Returns:
    The output tensor of the new layer with L2 regularization applied
    """
    return tf.keras.layers.Dense(
        units=n,
        activation=activation,
        kernel_regularizer=regularizers.l2(lambtha)
    )(prev)
