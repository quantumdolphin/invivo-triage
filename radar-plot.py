# radar_plot.py
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# --- Parameters ---
descriptor_cols = {
    'LIPO': 'log P',
    'SIZE': 'Molecular weight (g/mol)',
    'POLAR': 'Topological polar surface area (Å²)',
    'INSOLU': 'log S',
    'FLEX': 'Rotatable bonds',
    'INSATU': 'Fsp3'
}

relaxed_bounds = {
    'LIPO': (-2.0, 5.5),
    'SIZE': (150, 650),
    'POLAR': (20, 180),
    'INSOLU': (-6.5, 0.0),
    'FLEX': (0, 12),
    'INSATU': (0.15, 1.0)
}

def normalize_feature(series, min_val, max_val, clamp=True):
    norm = (series - min_val) / (max_val - min_val)
    if clamp:
        norm = norm.clip(0, 1.5)
    return norm

# --- Load and filter data ---
df = pd.read_csv("cpds.csv")
df_filtered = df[df['FCharge'] <= 1].copy()

# Normalize for radar plot
df_norm = pd.DataFrame()
df_norm['Molecule Name'] = df_filtered['Molecule Name']
for axis, col in descriptor_cols.items():
    min_val, max_val = relaxed_bounds[axis]
    df_norm[axis] = normalize_feature(df_filtered[col], min_val, max_val)

# --- Radar Plot ---
def plot_radar_all(df_norm, color='grey'):
    labels = list(descriptor_cols.keys())
    num_vars = len(labels)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]  # complete the circle

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

    for i, row in df_norm.iterrows():
        values = row[labels].tolist()
        values += values[:1]
        ax.plot(angles, values, color=color, linewidth=0.8, alpha=0.5)
        ax.fill(angles, values, color=color, alpha=0.1)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    ax.set_yticks([0.25, 0.5, 0.75, 1.0])
    ax.set_yticklabels(["0.25", "0.5", "0.75", "1.0"])
    ax.set_ylim(0, 1.5)
    plt.title("Radar Plot: Bioavailability Parameters", y=1.08)
    plt.tight_layout()
    plt.show()

# Run
plot_radar_all(df_norm)
