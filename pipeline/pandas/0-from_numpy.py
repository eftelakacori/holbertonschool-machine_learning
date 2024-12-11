#!/usr/bin/env python3
""" a script that calculates the sum of squares"""


import pandas as pd

def from_numpy(array):
    """Convert a NumPy array to a Pandas DataFrame with labeled columns."""
    # Generate column labels starting from 'A' to 'Z'
    columns = [chr(65 + i) for i in range(array.shape[1])]
    
    # Create and return the DataFrame with the appropriate column labels
    return pd.DataFrame(array, columns=columns)
