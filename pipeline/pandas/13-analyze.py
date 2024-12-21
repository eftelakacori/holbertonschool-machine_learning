#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

# Function to load the CSV file
def from_file(filename, delimiter):
    try:
        # Read the CSV file
        df = pd.read_csv(filename, delimiter=delimiter)
        return df
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return None

# Function to analyze and plot the data
def analyze():
    # File path to the CSV
    filename = 'coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv'
    
    # Load the data from the file
    df = from_file(filename, ',')

    if df is not None:
        # Step 1: Remove the column Weighted_Price
        df = df.drop(columns=['Weighted_Price'])

        # Step 2: Rename the column Timestamp to Date
        df = df.rename(columns={'Timestamp': 'Date'})

        # Step 3: Convert the timestamp values to date values
        df['Date'] = pd.to_datetime(df['Date'], unit='s')

        # Step 4: Index the DataFrame on Date
        df = df.set_index('Date')

        # Step 5: Handle missing values
        df['Close'] = df['Close'].fillna(method='ffill')  # Fill Close missing values with the previous row value
        df['High'] = df['High'].fillna(df['Close'])  # Fill High with the same row's Close value
        df['Low'] = df['Low'].fillna(df['Close'])  # Fill Low with the same row's Close value
        df['Open'] = df['Open'].fillna(df['Close'])  # Fill Open with the same row's Close value
        df['Volume_(BTC)'] = df['Volume_(BTC)'].fillna(0)  # Fill Volume_(BTC) with 0
        df['Volume_(Currency)'] = df['Volume_(Currency)'].fillna(0)  # Fill Volume_(Currency) with 0

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
        df_daily['Close'].plot(title='Close Prices (2017+)', ylabel='USD', xlabel='Date', grid=True)
        plt.show()

        # Return the transformed DataFrame before plotting
        print(df_daily)
