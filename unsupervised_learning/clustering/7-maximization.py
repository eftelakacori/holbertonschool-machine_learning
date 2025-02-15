#!/usr/bin/env python3
"""Expectation Module"""
import numpy as np

def maximization(X, g):
    # Sigurohuni që X të jetë një array 2D (n, d)
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        return None, None, None
    
    n, d = X.shape  # Nxjerrim numrin e pikave të të dhënave (n) dhe karakteristikave (d)
    
    # Sigurohuni që g të jetë një array 2D (k, n)
    if not isinstance(g, np.ndarray) or len(g.shape) != 2:
        return None, None, None
    
    # Sigurohuni që numri i pikave të të dhënave në X të përputhet me numrin e pikave të të dhënave në g
    if X.shape[0] != g.shape[1]:
        return None, None, None

    # Normalizoni g për t'u siguruar që është një shpërndarje probabiliteti valide
    g_sum = g.sum(axis=0)
    if np.any(g_sum == 0):  # Nëse ndonjë kolonë ka shumën zero, është e pavlefshme
        return None, None, None
    g = g / g_sum  # Normalizo

    k = g.shape[0]  # numri i grupeve (k)

    # 1. Përditësojmë priors (pi)
    pi = g.sum(axis=1) / n

    # 2. Përditësojmë mesataren (m)
    m = np.dot(g, X) / g.sum(axis=1)[:, np.newaxis]

    # 3. Përditësojmë kovariancat (S)
    S = np.zeros((k, d, d))
    for i in range(k):
        X_centered = X - m[i]
        S[i] = np.dot(g[i] * X_centered.T, X_centered) / g[i].sum()
        # Rounding për të shmangur gabimet e vogla të saktësisë
        S[i] = np.round(S[i], decimals=8)  # rrethimi në 8 vendosje pas presjes

    return pi, m, S

# Përdorimi:
if __name__ == '__main__':
    # Krijimi i të dhënave shembull dhe probabiliteteve posterior g
    np.random.seed(11)
    a = np.random.multivariate_normal([30, 40], [[75, 5], [5, 75]], size=10000)
    b = np.random.multivariate_normal([5, 25], [[16, 10], [10, 16]], size=750)
    c = np.random.multivariate_normal([60, 30], [[16, 0], [0, 16]], size=750)
    d = np.random.multivariate_normal([20, 70], [[35, 10], [10, 35]], size=1000)
    X = np.concatenate((a, b, c, d), axis=0)
    np.random.shuffle(X)

    # Inicializimi i g (probabilitetet posterior) si shembull
    g = np.random.rand(4, X.shape[0])  # 4 grupe, X.shape[0] pika të të dhënave
    g = g / g.sum(axis=0)  # Normalizo për ta bërë një shpërndarje probabiliteti të vlefshme

    # Thirrja e funksionit të maksimizimit
    pi, m, S = maximization(X, g)

    # Printimi i rezultateve
    print("Priors të përditësuar (pi):", pi)
    print("Mesataret e përditësuara (m):", m)
    print("Matrica të kovariancave të përditësuara (S):", S)
