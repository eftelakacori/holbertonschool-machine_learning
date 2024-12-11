#!/usr/bin/env python3
""" A script that sets the Timestamp column as the index. """

import pandas as pd

def index(df):
    """Set the Timestamp column as the index of the DataFrame."""
    # Set the 'Timestamp' column as the index
    df.set_index('Timestamp', inplace=True)
    
    # Return the modified DataFrame
    return df
