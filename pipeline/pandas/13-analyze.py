#!/usr/bin/env python3
""" a script that calculates the sum of squares"""

def analyze(df):
    # Step 1: Exclude the 'Timestamp' column if it exists
    columns = list(df.keys())
    if 'Timestamp' in columns:
        columns.remove('Timestamp')

    # Step 2: Initialize the statistics dictionary
    stats = {}

    # Step 3: Calculate descriptive statistics for each column
    for column in columns:
        values = df[column]

        # Calculate the count (number of non-null values)
        count = len(values)

        # Calculate the mean
        mean = sum(values) / count if count > 0 else 0

        # Calculate the standard deviation (using a sample variance formula)
        variance = sum((x - mean) ** 2 for x in values) / (count - 1) if count > 1 else 0
        std_dev = variance ** 0.5

        # Calculate the min and max
        min_val = min(values)
        max_val = max(values)

        # Calculate the 25th, 50th (median), and 75th percentiles
        sorted_values = sorted(values)
        q1 = sorted_values[int(count * 0.25)] if count > 0 else 0
        q2 = sorted_values[int(count * 0.5)] if count > 0 else 0
        q3 = sorted_values[int(count * 0.75)] if count > 0 else 0

        # Store the statistics for this column
        stats[column] = {
            'count': count,
            'mean': mean,
            'std': std_dev,
            'min': min_val,
            '25%': q1,
            '50%': q2,
            '75%': q3,
            'max': max_val,
        }

    # Step 4: Calculate the sum of squares for each numerical column
    sum_of_squares = {col: sum(x ** 2 for x in df[col]) for col in columns}

    # Step 5: Add sum of squares to the statistics
    stats['sum_of_squares'] = sum_of_squares

    # Return the statistics dictionary
    return stats
