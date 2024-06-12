import matplotlib.pyplot as plt

# Data
data = {
    "1:1": {"mean": 11270829, "std": 303729},
    "2:1": {"mean": 9368772, "std": 675339},
    "1:2": {"mean": 11597131, "std": 2205076},
}

# Extract data for plotting
groups = list(data.keys())
means = [data[group]["mean"] for group in groups]
stds = [data[group]["std"] for group in groups]

edge_color = "black"
line_width = 1

# Create bar plot
fig, ax = plt.subplots(figsize=(6, 6))

bars = ax.bar(
    groups,
    means,
    color=["mediumblue", "cornflowerblue", "mediumspringgreen"],
    width=0.5,
    edgecolor=edge_color,
    linewidth=line_width,
    zorder=3,
)

# Add error bars with the same line width
ax.errorbar(
    groups,
    means,
    yerr=stds,
    fmt="none",
    ecolor=edge_color,
    elinewidth=line_width,
    capsize=5,
    zorder=4,
)

# Remove top and right spines
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Add grid

plt.xlabel("Molar ratio Thy-Lid")
plt.ylabel("Signal response")

# Render the plot before saving
plt.draw()
# Save the image with desired DPI
plt.savefig(r"BarPlot_Carla\bar_plot_with_error_bars.jpeg", dpi=700)
