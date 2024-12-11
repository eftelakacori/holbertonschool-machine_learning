#!/usr/bin/env python3

from_file = __import__('2-from_file').from_file  # Import from_file to read the CSV
slice = __import__('5-slice').slice  # Import the slice function

# Load the DataFrame from the CSV file
df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')

# Call the slice function to get the sliced DataFrame
df = slice(df)

# Print the last few rows of the sliced DataFrame
print(df.tail())
