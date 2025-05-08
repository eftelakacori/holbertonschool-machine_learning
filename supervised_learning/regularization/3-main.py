#!/usr/bin/env python3

import numpy as np
import tensorflow as tf
import os
import random

SEED = 0

# Set random seeds to ensure reproducibility
os.environ['PYTHONHASHSEED'] = str(SEED)
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
random.seed(SEED)
np.random.seed(SEED)
tf.random.set_seed(SEED)

# Import the functions
l2_reg_cost = __import__('2-l2_reg_cost').l2_reg_cost
l2_reg_create_layer = __import__('3-l2_reg_create_layer').l2_reg_create_layer

def one_hot(Y, classes):
    """Convert an array to a one-hot matrix"""
    m = Y.shape[0]
    one_hot = np.zeros((m, classes))
    one_hot[np.arange(m), Y] = 1
    return one_hot

# Load the dataset
lib = np.load('MNIST.npz')
X_train_3D = lib['X_train']
Y_train = lib['Y_train']
X_train = X_train_3D.reshape((X_train_3D.shape[0], -1))
Y_train_oh = one_hot(Y_train, 10)

# Define the input shape
input_shape = X_train.shape[1]

# Create the model using the functional API
x = tf.keras.Input(shape=input_shape)
h1 = l2_reg_create_layer(x, 256, tf.nn.tanh, 0.05)  
y_pred = l2_reg_create_layer(h1, 10, tf.nn.softmax, 0.)   
model = tf.keras.Model(inputs=x, outputs=y_pred)

# Make predictions
Predictions = model(X_train)

# Compute the cost using categorical cross-entropy loss
cost = tf.keras.losses.CategoricalCrossentropy()(Y_train_oh, Predictions)

# Calculate the L2 regularization cost
l2_cost = l2_reg_cost(cost, model)
print(l2_cost)
