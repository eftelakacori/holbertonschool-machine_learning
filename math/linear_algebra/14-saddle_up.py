#!/usr/bin/env python3
"""defines function that performs matrix multiplication"""


iimport numpy as np

def np_matmul(mat1, mat2):
    """
    Krijon një matrice të re duke shumëzuar dy matrica të dhëna.
    
    Parametrat:
    mat1 -- Matricha e parë (numpy.ndarray)
    mat2 -- Matricha e dytë (numpy.ndarray)
    
    Kthen:
    numpy.ndarray -- Matricha rezultuese nga shumëzimi i mat1 dhe mat2
    """
    return np.matmul(mat1, mat2)
