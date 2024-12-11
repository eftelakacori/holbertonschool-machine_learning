#!/usr/bin/env python3
""" a script that calculates the sum of squares"""

import pandas as pd


def rename(df):
    """Renames the Timestamp column to Datetime, converts it to datetime, 
    and displays only the Datetime and Close columns."""

    # Rename the 'Timestamp' column to 'Datetime'
    df = df.rename(columns={"Timestamp": "Datetime"})

    # Convert 'Datetime' column to datetime
    df["Datetime"] = pd.to_datetime(df["Datetime"])

    # Select and return only the 'Datetime' and 'Close' columns
    return df[["Datetime", "Close"]]
