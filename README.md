# 🧪 Early-Stage Bioavailability Profiling and Triage for In Vivo Studies

## Overview

This document outlines a strategy for evaluating early-stage drug candidates using physicochemical descriptors. The approach integrates bioavailability profiling, compound filtering, radar plots, and traffic light tables, drawing inspiration from SwissADME and medicinal chemistry literature.

## Objectives

* Identify compounds suitable for **first in vivo studies**.
* Distinguish between **oral** and **parenteral** candidates using relaxed criteria.
* Visualize key bioavailability features via **radar plots** and **color-coded traffic light tables**.
* Filter out undesirable scaffolds (e.g., dibasic compounds with high formal charge).

## Descriptor Themes and Cutoffs

Six core descriptors were selected based on the SwissADME radar plot framework:

| Theme      | Descriptor               | Relaxed Range (Parenteral-inclusive) |
| ---------- | ------------------------ | ------------------------------------ |
| **LIPO**   | log P                    | –2.0 to 5.5                          |
| **SIZE**   | Molecular weight (g/mol) | 150 to 650                           |
| **POLAR**  | TPSA                     | 20 to 180 Å²                         |
| **INSOLU** | log S                    | ≥ –6.5                               |
| **FLEX**   | Rotatable bonds          | 0 to 12                              |
| **INSATU** | Fsp³                     | ≥ 0.15                               |

These thresholds were relaxed to accommodate parenteral dosing scenarios, where oral bioavailability constraints are less stringent.

## Radar Plot Construction

Radar plots were generated using `matplotlib` and `pandas`:

* Data was normalized to \[0–1.5] using relaxed cutoffs.
* Radar plots show **all remaining compounds** as grey lines.
* Highlighted compounds (e.g., top-ranked) shown separately.

### Normalization Function

```python
def normalize_feature(series, min_val, max_val, clamp=True):
    norm = (series - min_val) / (max_val - min_val)
    if clamp:
        norm = norm.clip(0, 1.5)
    return norm
```

## Traffic Light Table

A `pandas.Styler`-based table was created to show each compound’s status on each descriptor:

* **Green**: Within ideal range
* **Yellow**: Borderline (10% outside bounds)
* **Red**: Clear outlier

| Descriptor | Description                 | Outlier Impact                                               |
| ---------- | --------------------------- | ------------------------------------------------------------ |
| log P      | Lipophilicity (direct)      | Too high: metabolism & toxicity; Too low: permeability issue |
| MW         | Molecular size (indirect)   | High MW → poor PK & synthetic complexity                     |
| TPSA       | Polar surface area (direct) | Too high → poor permeability                                 |
| log S      | Solubility (direct)         | Poor log S → formulation risk                                |
| RotB       | Flexibility (indirect)      | Too flexible → low oral absorption                           |
| Fsp³       | 3D character (indirect)     | Low Fsp³ → flat, likely promiscuous                          |

## Scientific Rationale

This method is inspired by the SwissADME radar plot and expands it to include relaxed cutoffs suitable for parenteral candidates. It incorporates insights from drug metabolism, permeability studies, and medicinal chemistry best practices:

> "Direct properties like log P and log S reflect actual behavior in vivo. Indirect ones like MW and Fsp³ are valuable design levers." — Based on medicinal chemistry literature.

## Deliverables

* 📊 Radar plots (oral and parenteral criteria)
* ✅ Traffic signal tables for:

## Future Directions

* Add composite scoring (e.g., CNS MPO or MPO+solubility index)
* Include reactivity and mutagenicity filters
* Integrate into Streamlit dashboard or KNIME workflow
