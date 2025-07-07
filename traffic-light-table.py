# traffic_table.py
import pandas as pd

# Load data
df = pd.read_csv("cpds.csv")
df_filtered = df[df['FCharge'] <= 1].copy()

# Define properties and relaxed cutoffs
properties = {
    'LIPO': {'col': 'log P', 'low': -2.0, 'high': 5.5},
    'SIZE': {'col': 'Molecular weight (g/mol)', 'low': 150, 'high': 650},
    'POLAR': {'col': 'Topological polar surface area (Å²)', 'low': 20, 'high': 180},
    'INSOLU': {'col': 'log S', 'low': -6.5, 'high': 0.0},
    'FLEX': {'col': 'Rotatable bonds', 'low': 0, 'high': 12},
    'INSATU': {'col': 'Fsp3', 'low': 0.15, 'high': 1.0}
}

# Create DataFrame for styling
traffic_df = df_filtered[['Molecule Name']].copy()
for key, meta in properties.items():
    traffic_df[key] = df_filtered[meta['col']].round(1)

def color_cell(val, param):
    low = properties[param]['low']
    high = properties[param]['high']
    margin = 0.1 * (high - low)
    if val < low - margin or val > high + margin:
        return 'background-color: red'
    elif val < low or val > high:
        return 'background-color: yellow'
    else:
        return 'background-color: lightgreen'

# Apply styling
styled_table = traffic_df.style
for param in properties.keys():
    styled_table = styled_table.map(lambda v: color_cell(v, param), subset=[param])

# Save to Excel
styled_table.to_excel("traffic_signal_table.xlsx", engine='openpyxl', index=False)
print("Traffic signal table saved as Excel file.")
