#!/usr/bin/env python3



import numpy as np
Poisson = __import__('poisson').Poisson

# Gjenerimi i të dhënave me shpërndarje Poisson (lambda=5)
np.random.seed(0)
data = np.random.poisson(5., 100).tolist()

# Krijo objektin Poisson duke përdorur të dhënat
p1 = Poisson(data)
print('Lambtha:', p1.lambtha)  # Pritet 4.84

# Krijo objektin Poisson me lambtha të dhënë
p2 = Poisson(lambtha=5)
print('Lambtha:', p2.lambtha)  # Pritet 5.0
