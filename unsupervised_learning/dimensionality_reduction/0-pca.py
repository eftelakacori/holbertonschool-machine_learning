#!/usr/bin/env python3
"""That performs PCA on a dataset"""


import numpy as np

def pca(X, var=0.95):
    # Kryej SVD-në në X (të dhënat prapë të centruar)
    U, S, Vt = np.linalg.svd(X, full_matrices=False)
    # Llogarit përqindjen e variancës së shpjeguar nga secili komponent
    var_exp = S**2 / np.sum(S**2)
    cum_var = np.cumsum(var_exp)
    # Zgjidh numrin minimal të komponentëve që mbajnë të paktën 'var' të variancës
    nd = np.argmax(cum_var >= var) + 1
    # Kthe matricën e peshave: kolona jone janë komponentët kryesorë
    W = Vt[:nd].T
    return W
