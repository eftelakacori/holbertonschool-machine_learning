#!/usr/bin/env python3
"""That performs PCA on a dataset"""


import numpy as np
from 0-pca import pca

# Të dhënat tuaja për PCA
X = np.array([...])  # Vendosni këtu të dhënat tuaja

# Qendërzoni të dhënat dhe thirrni PCA
X_centered = X - np.mean(X, axis=0)
W = pca(X_centered)

# Printoni rezultatin
print("PCA Weights Matrix:")
print(W)
