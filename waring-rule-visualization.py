import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Use seaborn styling for clean plot
sns.set(style="whitegrid", context="notebook")

# Set up figure size and resolution
plt.figure(figsize=(12, 7), dpi=120)

# Define the color map for true permeability classes
color_map = {
    "Low": "#e74c3c",       # red
    "Moderate": "#f39c12",  # orange
    "High": "#27ae60"       # green
}

# Define Waring rule thresholds as (MW_min, MW_max, required_logD_to_pass)
waring_thresholds = [
    (0, 300, 0.5),
    (300, 350, 1.1),
    (350, 400, 1.7),
    (400, 450, 3.1),
    (450, 500, 3.4),
    (500, 800, 4.5)  # extended to match x-axis
]

# Plot shaded regions: red = Waring fail zone, green = pass zone
for mw_min, mw_max, logd_thresh in waring_thresholds:
    # Waring FAIL zone (below the threshold line)
    plt.fill_betweenx(
        y=[-1, logd_thresh],      # y-range from bottom up to the threshold
        x1=mw_min,
        x2=mw_max,
        color='lightcoral',
        alpha=0.2
    )
    # Waring PASS zone (above the threshold line)
    plt.fill_betweenx(
        y=[logd_thresh, 6],       # y-range from threshold to top
        x1=mw_min,
        x2=mw_max,
        color='lightgreen',
        alpha=0.1
    )
    # Draw the threshold boundary line
    plt.hlines(
        y=logd_thresh,
        xmin=mw_min,
        xmax=mw_max,
        colors='blue',
        linestyles='dashed',
        linewidth=1.5
    )
    # Optional: label the line
    plt.text(
        x=mw_max + 5,         # small offset to the right
        y=logd_thresh,
        s=f"logD > {logd_thresh}",
        fontsize=9,
        verticalalignment='center',
        color='blue'
    )

# Scatterplot: MW vs logD, colored by Permeability_Class
sns.scatterplot(
    data=df,
    x='MW',
    y='logD',
    hue='Permeability_Class',
    palette=color_map,
    s=70,
    alpha=0.85,
    edgecolor='black',
    linewidth=0.5
)

# Set axis limits and labels
plt.xlim(0, 800)        # Extend MW range
plt.ylim(-1, 7)         # Reasonable logD scale for most drug-like molecules
plt.xlabel("Molecular Weight (g/mol)", fontsize=13)
plt.ylabel("logD", fontsize=13)
plt.title("MW vs logD with Waring Rule Zones and True Permeability", fontsize=15)

# Legend formatting
plt.legend(title="True Permeability", loc='upper left', frameon=True)

# Layout fix
plt.tight_layout()
plt.show()
