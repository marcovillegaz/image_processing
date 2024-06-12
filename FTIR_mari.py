"""This script is a little help to my labmate to make a better plot"""

import pandas as pd
import matplotlib.pyplot as plt

# Replace 'file1.csv', 'file2.csv', 'file3.csv' with the paths to your CSV files
file1 = "file1.csv"
file2 = "file2.csv"
file3 = "file3.csv"

# Read the CSV files
data1 = pd.read_csv(file1)
data2 = pd.read_csv(file2)
data3 = pd.read_csv(file3)

# Assuming the first column is the x-axis (wavenumber) and the second column is the y-axis (absorbance)
x1, y1 = data1.iloc[:, 0], data1.iloc[:, 1]
x2, y2 = data2.iloc[:, 0], data2.iloc[:, 1]
x3, y3 = data3.iloc[:, 0], data3.iloc[:, 1]

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x1, y1, label="Sample 1")
plt.plot(x2, y2, label="Sample 2")
plt.plot(x3, y3, label="Sample 3")

# Add labels and title
plt.xlabel("Wavenumber (cm⁻¹)")
plt.ylabel("Absorbance")
plt.title("FTIR Analysis")
plt.legend()

# Show the plot
plt.show()
