import matplotlib.pyplot as plt
import numpy as np

# Generate x values between 0 and 10 (inclusive)
x = np.linspace(0, 10, 100)

# Generate y values for a cubic function y = x^3
y = x**3

# Plot the graph
plt.plot(x, y, color='red')  # Ensure the line is red
plt.xlim(0, 10)  # Set the x-axis to go from 0 to 10
plt.title("Cubic Function Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# Display the plot
plt.show()
