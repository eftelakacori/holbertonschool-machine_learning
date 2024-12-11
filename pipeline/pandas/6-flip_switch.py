#!/usr/bin/env python3
""" a script that Write a function def flip_switch(df) takes a pd.DataFrame"""


from_file = __import__('2-from_file').from_file
flip_switch = __import__('6-flip_switch').flip_switch

# Load data from the CSV file
df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')

# Call the flip_switch function
df = flip_switch(df)

# Print the last 8 rows of the transposed DataFrame
print(df.tail(8))
