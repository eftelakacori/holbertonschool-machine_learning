#!/usr/bin/env python3
""" a script that calculates the sum of squares"""


import numpy as np


def array(df):
    """Select the last 10 rows of 'High' and 'Close' columns."""
    # Select the last 10 rows of 'High' and 'Close' columns
    last_10_rows = df[['High', 'Close']].tail(10)
    
    # Convert the selected values to numpy.ndarray and return
    return last_10_rows.to_numpy()
