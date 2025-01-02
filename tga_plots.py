import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def tga_plot(df_dic):
    """This is a function to plot TGA result in automatic way"""


folder = r"TGA_data"

files = os.listdir(folder)

# Data procesing
PEBA_df = pd.read_csv(os.path.join(folder, files[0]), delimiter=";", decimal=",")
POMS_df = pd.read_csv(os.path.join(folder, files[2]), delimiter=";", decimal=",")

# Create a figure and axes object
fig, (ax1, ax2) = plt.subplots(2, figsize=(8, 8), sharex=True)

# Plot TGA data
ax1.plot(PEBA_df["Ts"], (PEBA_df["mass"] / PEBA_df["mass"][0]) * 100, label="PEBA")
ax1.plot(POMS_df["Ts"], (POMS_df["mass"] / POMS_df["mass"][0]) * 100, label="POMS")
# Plot derivative
ax2.plot(PEBA_df["Ts"], PEBA_df["dxdy"], linestyle="--", label="PEBA")
ax2.plot(POMS_df["Ts"], POMS_df["dxdy"], linestyle="--", label="POMS")


plt.xlabel("Temperature [°C]")  # X-axis label

ax1.set_ylabel("Mass [mg]")  # Y-axis label
ax1.tick_params(axis="y")
ax1.set_xlim([0, 800])

ax2.set_ylabel("Derivative [mg/°C]")
ax2.tick_params(axis="y")
ax2.set_xlim([0, 800])

ax1.legend(loc="center left")
ax2.legend(loc="center left")

plt.show()
