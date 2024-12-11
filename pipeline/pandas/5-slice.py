#!/usr/bin/env python3
""" a script that calculates the sum of squares"""

import pandas as pd

def slice(df):
    """Extracts 'High', 'Low', 'Close', and 'Volume_BTC' columns and selects every 60th row."""
    # Extract relevant columns
    selected_columns = df[['High', 'Low', 'Close', 'Volume_BTC']]
    
    # Select every 60th row from these columns
    sliced_df = selected_columns.iloc[::60]
    
    return sliced_df
