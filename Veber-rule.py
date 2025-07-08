def passes_veber_rule(rot_bonds, tpsa, hbd, hba):
    total_hbonds = hbd + hba
    if pd.isna(rot_bonds) or pd.isna(tpsa) or pd.isna(hbd) or pd.isna(hba):
        return "N/A"
    if rot_bonds <= 10 and (tpsa <= 140 or total_hbonds <= 12):
        return "Y"
    else:
        return "N"

# Apply the rule to your DataFrame
df['Veber Rule'] = df.apply(
    lambda row: passes_veber_rule(
        row['Rotatable bonds'],
        row['Topological polar surface area (Å²)'],  # or 'TPSA'
        row['H-bond donors'],
        row['H-bond acceptors']
    ),
    axis=1
)
