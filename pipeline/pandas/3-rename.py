#!/usr/bin/env python3
""" a script that calculates the sum of squares"""

import pandas as pd


def rename(df):
    """Converts it to datetime, and displays the Datetime and Close columns."""

    # Rename the 'Timestamp' column to 'Datetime'
    df = df.rename(columns={"Timestamp": "Datetime"})

    # Convert 'Datetime' column to datetime in Unix timestamp format
    df["Datetime"] = pd.to_datetime(df["Datetime"], unit='s')

    # Select and return only the 'Datetime' and 'Close' columns
    return df[["Datetime", "Close"]]
