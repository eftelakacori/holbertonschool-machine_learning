#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

def line():
    # Generate y values as the cube of integers from 0 to 10
    y = np.arange(0, 11) ** 3
    
    # Set up the x values, which should match the length of y
    x = np.arange(0, 11)

    # Create the plot with a solid red line
    plt.plot(x, y, color='red', linestyle='-', linewidth=2)  # Solid red line

    # Set the x-axis range from 0 to 10
    plt.xlim(0, 10)

    # Set the title and labels
    plt.title("Cubic Function")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")

    # Display the plot
    plt.show()

# Call the function to display the plot
line()
