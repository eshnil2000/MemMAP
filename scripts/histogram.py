import re
import matplotlib.pyplot as plt
import numpy as np

# Define the input file name
input_file = '../data/output.csv'

# Read the lines from the input file
with open(input_file, 'r') as f:
    lines = f.readlines()


# Extract the last column from each line and convert to integer (base 16)
values = [int(line.split()[2], 16) for line in lines]

# Compute the differences between consecutive values
differences = [values[i + 1] - values[i] for i in range(len(values) - 1)]
# Calculate statistics
mean = np.mean(differences)
median = np.median(differences)
std_dev = np.std(differences)

print("Statistics:")
print(f"Mean: {mean:.2f}")
print(f"Median: {median:.2f}")
print(f"Standard Deviation: {std_dev:.2f}")

# Find unique values of differences
unique_differences = np.unique(differences)
print("\nNo of Unique values of differences:", len(unique_differences))

# Plot a histogram of the differences
plt.hist(differences, bins=50, alpha=0.7, color='blue')
plt.xlabel('Differences')
plt.ylabel('Frequency')
plt.yscale('log')
plt.xscale('log')
plt.title('Histogram of Differences')
#plt.xlim(0, sorted(differences)[-11])  # Limit x-axis to top 10 bins
plt.show()

