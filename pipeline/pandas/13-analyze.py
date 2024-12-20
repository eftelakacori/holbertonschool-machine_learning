#!/usr/bin/env python3
""" a script that calculates the sum of squares"""

import pandas as pd

def analyze(df):
    # Exclude the 'Timestamp' column if it exists
    df = df.drop(columns=['Timestamp'], errors='ignore')
    
    # Compute descriptive statistics
    stats = df.describe()
    
    return stats
