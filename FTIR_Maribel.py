"""This script is a little help to my labmate to make a better plot"""

import os
import pandas as pd
import matplotlib.pyplot as plt

folder = r"FTIR_data_maribel"
font_size = 15
colors = ["#5CE1E6", "#1A014B", "#A9014B"]
# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))

i = 0
for filename in os.listdir(folder):
    if filename.endswith(".csv"):  # Only process CSV files

        data = pd.read_csv(os.path.join(folder, filename), delimiter=";", decimal=",")

        # Assuming the first column is the x-axis (wavenumber) and the second column is the y-axis (absorbance)
        x1, y1 = data.iloc[:, 0], data.iloc[:, 1]
        x1 = x1.transpose()
        ax.plot(x1, y1, label=filename.split(".")[0], linewidth=2, color=colors[i])
        i = i + 1

print(x1)

# Add labels and title
ax.set_xlabel("Wavenumber (cm$^{-1}$)", fontsize=font_size)
ax.set_ylabel("Transmitance (%)", fontsize=font_size)
ax.set_xlim(left=min(x1), right=max(x1))
ax.xaxis.set_inverted(True)  # inverted axis with autoscaling

# Adjust tick parameters
# ax.tick_params(axis="both", which="major", labelsize=font_size)

# Save and show the plot
ax.legend(fontsize=font_size)
output_path = os.path.join(folder, "FTIR_Carla_Toledo_v2.jpeg")
plt.savefig(output_path, dpi=600)
plt.show()
