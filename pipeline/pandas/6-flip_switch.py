#!/usr/bin/env python3
""" a script that Write a function def flip_switch(df) takes a pd.DataFrame"""


import pandas as pd

def flip_switch(df):
    """Sorts the data in reverse chronological order and transposes it."""
    # Sort the dataframe by the 'Timestamp' column in reverse order
    df_sorted = df.sort_values(by='Timestamp', ascending=False)
    
    # Transpose the sorted dataframe
    df_transposed = df_sorted.transpose()
    
    return df_transposed
