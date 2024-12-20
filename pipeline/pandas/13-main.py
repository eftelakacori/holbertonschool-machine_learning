#!/usr/bin/env python3
""" a script that calculates the sum of squares"""
import pandas as pd

def analyze(df):
    # Exclude the 'Timestamp' column if it exists
    df = df.drop(columns=['Timestamp'], errors='ignore')
    
    # Compute descriptive statistics
    stats = df.describe()
    
    # Compute sum of squares for each numerical column
    sum_of_squares = df.apply(lambda x: (x ** 2).sum())
    
    # Add the sum of squares as a new row to the stats DataFrame
    stats.loc['sum_of_squares'] = sum_of_squares
    
    return stats
