#!/usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd
from_file = __import__('2-from_file').from_file

# Load the data
df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')

# Step 1: Remove the column Weighted_Price
df = df.drop(columns=['Weighted_Price'])

# Step 2: Rename the column Timestamp to Date
df = df.rename(columns={'Timestamp': 'Date'})

# Step 3: Convert the timestamp values to date values
df['Date'] = pd.to_datetime(df['Date'], unit='s')

# Step 4: Index the DataFrame on Date
df = df.set_index('Date')

# Step 5: Handle missing values
df['Close'] = df['Close'].fillna(method='ffill')
df['High'] = df['High'].fillna(df['Close'])
df['Low'] = df['Low'].fillna(df['Close'])
df['Open'] = df['Open'].fillna(df['Close'])
df['Volume_(BTC)'] = df['Volume_(BTC)'].fillna(0)
df['Volume_(Currency)'] = df['Volume_(Currency)'].fillna(0)

# Step 6: Filter data from 2017 and beyond
df = df['2017':]

# Step 7: Resample data to daily intervals and group values
df_daily = df.resample('D').agg({
    'High': 'max',
    'Low': 'min',
    'Open': 'mean',
    'Close': 'mean',
    'Volume_(BTC)': 'sum',
    'Volume_(Currency)': 'sum'
})

# Plot the data
plt.figure(figsize=(12, 6))
df_daily['Close'].plot(title='Close Prices (2017+)', ylabel='USD', xlabel='Date')
plt.grid()
plt.show()

# Return the transformed DataFrame before plotting
print(df_daily)
