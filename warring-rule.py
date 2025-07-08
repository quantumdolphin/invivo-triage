def passes_waring_rule(mw, logd):
    if pd.isna(mw) or pd.isna(logd):
        return "N/A"
    if mw < 300:
        return "Y" if logd > 0.5 else "N"
    elif 300 <= mw < 350:
        return "Y" if logd > 1.1 else "N"
    elif 350 <= mw < 400:
        return "Y" if logd > 1.7 else "N"
    elif 400 <= mw < 450:
        return "Y" if logd > 3.1 else "N"
    elif 450 <= mw < 500:
        return "Y" if logd > 3.4 else "N"
    else:  # mw >= 500
        return "Y" if logd > 4.5 else "N"

# Apply to your DataFrame
df['Waring Rule'] = df.apply(lambda row: passes_waring_rule(row['Molecular weight (g/mol)'], row['log D']), axis=1)
