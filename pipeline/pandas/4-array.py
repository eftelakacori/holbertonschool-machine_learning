#!/usr/bin/env python3
""" a script that calculates the sum of squares"""

import numpy as np

def array(df):
    """Selects the last 10 rows of the High and Close columns, 
    converts them to numpy.ndarray."""

    # Select the last 10 rows of 'High' and 'Close' columns
    last_10_rows = df[['High', 'Close']].tail(10)

    # Convert the selected rows to a numpy.ndarray
    return last_10_rows.to_numpy()
