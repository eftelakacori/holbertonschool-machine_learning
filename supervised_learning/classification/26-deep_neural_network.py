#!/usr/bin/env python3
"""Deep neural network"""
import numpy as np


class DeepNeuralNetwork:
    """Klasë që përfaqëson një rrjet të thellë nervor për klasifikimin binar"""
    
    def __init__(self, nx, layers):
        """Konstruktori i klasës për inicializimin e rrjetit nervor"""
        
        # Kontrollo nëse nx është një integer
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        
        # Kontrollo nëse nx është më i vogël se 1
        if nx <= 0:
            raise ValueError("nx must be a positive integer")
        
        # Kontrollo nëse layers është një listë dhe nuk është e zbrazët
        if type(layers) is not list or len(layers) == 0:
            raise TypeError("layers must be a list of positive integers")
        
        # Kontrollo nëse të gjitha elementet në layers janë numra pozitivë
        for nodes in layers:
            if type(nodes) is not int or nodes <= 0:
                raise TypeError("layers must be a list of positive integers")
        
        # Atributet
        self.__L = len(layers)  # Numri i niveleve (layer)
        self.__cache = {}  # Diccionario për mbajtjen e vlerave ndërmjetës
        self.__weights = {}  # Diccionario për peshat dhe biaset
        
        # Inicializimi i peshave dhe bias
        # Pesha e parë (W1)
        self.__weights["W1"] = np.random.randn(layers[0], nx) * np.sqrt(2 / nx)
        self.__weights["b1"] = np.zeros([layers[0], 1], dtype=float)
        
        # Pesha dhe bias për nivelet e tjera
        for i in range(1, self.__L):
            self.__weights["W{}".format(i + 1)] = np.random.randn(layers[i], layers[i - 1]) * np.sqrt(2 / layers[i - 1])
            self.__weights["b{}".format(i + 1)] = np.zeros([layers[i], 1], dtype=float)

    @property
    def L(self):
        """Kthen numrin e niveleve (L)"""
        return self.__L

    @property
    def cache(self):
        """Kthen cache-n me vlerat ndërmjetëse"""
        return self.__cache

    @property
    def weights(self):
        """Kthen peshat dhe biaset e rrjetit"""
        return self.__weights
