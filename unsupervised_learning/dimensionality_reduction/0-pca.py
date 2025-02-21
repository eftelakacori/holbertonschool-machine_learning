#!/usr/bin/env python3
"""That performs PCA on a dataset"""


import numpy as np


def pca(X, var=0.95):
    """
    Kryen PCA mbi datasetin X.
    X: numpy.ndarray me formën (n, d) ku n është numri i
       pikave dhe d numri i dimensioneve. Të gjitha kanë mesatare 0.
    var: fraksioni i variancës që duhet ruajtur.
    Kthen matricën W me formën (d, nd) ku nd është dimensionaliteti
    i ri që ruan var-fraksionin e variancës.
    """
    # Llogarit matricën e kovariancës
    cov = np.cov(X, rowvar=False)
    # Merr vlerat dhe vektorët eigen
    eigvals, eigvecs = np.linalg.eigh(cov)
    # Rendit në rend zbritës sipas vlerave eigen
    idx = np.argsort(eigvals)[::-1]
    eigvals = eigvals[idx]
    eigvecs = eigvecs[:, idx]
    # Llogarit variancën kumulative
    cum_var = np.cumsum(eigvals) / np.sum(eigvals)
    nd = np.argmax(cum_var >= var) + 1
    # Kthen matricën e peshave për komponentët e zgjedhur
    return eigvecs[:, :nd]
