#!/usr/bin/env python3
""" a script that calculates the sum of squares"""

import pandas as pd


def from_file(filename, delimiter):
    """Loads data from a file and returns a pandas DataFrame."""
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(filename, delimiter=delimiter)

    return df
