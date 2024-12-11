#!/usr/bin/env python3
""" a script that calculates the sum of squares"""

import numpy as np


def array(df):
     """Selects the last 10 rows of the 'High' and 'Close' columns, converts them to numpy.ndarray."""
    # Select the last 10 rows of 'High' and 'Close' columns
    last_10_rows = df[['High', 'Close']].tail(10)

    # Convert the selected rows to a numpy.ndarray
    return last_10_rows.to_numpy()

def count_occurrences(df, column, value):
    """Counts the number of occurrences of a specific value in a column."""
    return (df[column] == value).sum()

# Example usage
if __name__ == "__main__":
    # Suppose df is your pandas DataFrame
    # df = from_file('your_file.csv', ',')  # Loading the data here
    
    value_to_count = 4000.0
    occurrences = count_occurrences(df, 'Close', value_to_count)
    print(f"The value {value_to_count} appears {occurrences} times in the 'Close' column.")
