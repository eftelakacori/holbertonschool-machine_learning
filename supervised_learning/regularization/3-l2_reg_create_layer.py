#!/usr/bin/env python3
import numpy as np
import tensorflow as tf
import os
import random

SEED = 0

# Sigurohuni që të gjitha variablat e nevojshme janë të setuar për riprodhueshmëri
os.environ['PYTHONHASHSEED'] = str(SEED)
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
random.seed(SEED)
np.random.seed(SEED)
tf.random.set_seed(SEED)

# Funksioni që konverton etiketat në formë one-hot
def one_hot(Y, classes):
    """Konverton një array në një matriks one-hot"""
    m = Y.shape[0]
    one_hot = np.zeros((m, classes))
    one_hot[np.arange(m), Y] = 1
    return one_hot

# Funksioni që krijon një layer me L2 regularizim
def l2_reg_create_layer(prev, n, activation, lambtha):
    """
    Krijon një TensorFlow layer me L2 regularizim
    """
    regularizer = tf.keras.regularizers.L2(lambtha)
    layer = tf.keras.layers.Dense(units=n,
                                  activation=activation,
                                  kernel_regularizer=regularizer)
    return layer(prev)

# Funksioni që llogarit kostot totale me L2 regularizimin
def l2_reg_cost(cost, model):
    """
    Llogarit kostot totale duke përfshirë regularizimin L2
    """
    l2_losses = tf.add_n(model.losses)
    return cost + l2_losses

# Ngarko të dhënat e MNIST
try:
    lib = np.load('MNIST.npz')
    X_train_3D = lib['X_train']
    Y_train = lib['Y_train']
except FileNotFoundError:
    print("Gabim: Skedari 'MNIST.npz' nuk është gjetur.")
    exit(1)

# Sigurohu që të dhënat janë të formatuara si duhet
X_train = X_train_3D.reshape((X_train_3D.shape[0], -1))
Y_train_oh = one_hot(Y_train, 10)

# Shihim dimensionet e të dhënave
print(f"Forma e X_train: {X_train.shape}")
print(f"Forma e Y_train_oh: {Y_train_oh.shape}")

input_shape = X_train.shape[1]

# Krijo modelin me katër shtresa
x = tf.keras.Input(shape=input_shape)
h1 = l2_reg_create_layer(x, 256, tf.nn.tanh, 0.05)  
y_pred = l2_reg_create_layer(h1, 10, tf.nn.softmax, 0.)   
model = tf.keras.Model(inputs=x, outputs=y_pred)

# Kompajlo modelin për të përdorur humbjen dhe optimizuesin
model.compile(optimizer='adam',
              loss=tf.keras.losses.CategoricalCrossentropy(),
              metrics=['accuracy'])

# Predikto dhe llogarit kostot
try:
    Predictions = model(X_train, training=False)
    cost = tf.keras.losses.CategoricalCrossentropy()(Y_train_oh, Predictions)
except Exception as e:
    print(f"Gabim gjatë predikimit: {e}")
    exit(1)

# Llogarit kostot totale përfshirë L2 regularizimin
l2_cost = l2_reg_cost(cost, model)

# Printo rezultatet
print("Base cost (Categorical Crossentropy):", cost.numpy())
print("Model losses (L2 regularization terms):", model.losses)
print("Total cost (with L2 regularization):", l2_cost.numpy())
