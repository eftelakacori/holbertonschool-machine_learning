#!/usr/bin/env python3
"""That performs PCA on a dataset"""
import numpy as np


def pca(X, var=0.95):
    cov = np.cov(X.T)
    eigvals, eigvecs = np.linalg.eigh(cov)
    idx = np.argsort(eigvals)[::-1]
    eigvals, eigvecs = eigvals[idx], eigvecs[:, idx]
    cum_var = np.cumsum(eigvals) / np.sum(eigvals)
    nd = np.argmax(cum_var >= var) + 1
    return eigvecs[:, :nd]
