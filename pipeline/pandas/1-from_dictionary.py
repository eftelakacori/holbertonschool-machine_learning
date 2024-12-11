#!/usr/bin/env python3
""" a script that calculates the sum of squares"""

import pandas as pd

# Create a dictionary with the data for the DataFrame
data = {
    "First": [0.0, 0.5, 1.0, 1.5],
    "Second": ["one", "two", "three", "four"]
}

# Create the DataFrame from the dictionary
df = pd.DataFrame(data, index=["A", "B", "C", "D"])
