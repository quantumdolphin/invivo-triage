# 📘 Quick Refresher on Caco-2 Permeability Assays

The **Caco-2 assay** is a widely used in vitro model to predict the **intestinal permeability** of drug candidates. It uses human epithelial colorectal adenocarcinoma cells that differentiate into a monolayer resembling intestinal epithelium, with tight junctions and relevant transporter activity.

This assay is critical for evaluating:
- **Passive diffusion**
- **Drug absorption potential**
- **Efflux risk**
- **Early oral bioavailability predictions**

---

## 📊 Key Outputs and Interpretation

### 🔹 Papp (Apparent Permeability)
- Units: typically **cm/s** or **nm/s**
- Measures the **rate of compound transport** across the monolayer

| Papp Range (nm/s) | Interpretation         |
|------------------|------------------------|
| < 10             | Low permeability       |
| 10–100           | Moderate permeability  |
| > 100            | High permeability      |

> Note: Papp thresholds can vary by lab, but this is a commonly used scale.

---

### 🔹 Directionality: A→B vs B→A
- **A→B (Apical to Basolateral):** Mimics intestinal drug absorption
- **B→A (Basolateral to Apical):** Highlights potential **efflux transporter** activity
- **Efflux Ratio = Papp (B→A) / Papp (A→B)**
  - Ratio > 2: suggests **efflux**
  - Ratio ≈ 1: passive diffusion likely

---

### 🔹 Recovery (%)
- Reflects how much of the dosed compound is accounted for after the experiment
- **80–120%**: acceptable range (good assay quality)
- Low recovery can indicate:
  - Compound degradation
  - Adsorption to plastic
  - Intracellular trapping

---

## 🧾 Typical Caco-2 Dataset Columns

| Column Name                    | Meaning / Use                                 |
|-------------------------------|-----------------------------------------------|
| `Molecule Name`               | Identifier of the compound                    |
| `Molecular weight (g/mol)`    | Used for permeability stratification          |
| `log D`                       | Lipophilicity at pH 7.4 (vs. log P)            |
| `Caco-2 Papp A→B (nm/s)`      | Permeability in absorption direction          |
| `Caco-2 Papp B→A (nm/s)`      | Permeability in efflux direction              |
| `Efflux Ratio`                | B→A / A→B; >2 may indicate active efflux       |
| `Recovery (%)`                | Assay mass balance; <80% suggests instability |
| `log P`, `log S`, `TPSA`      | Additional predictors for permeability, solubility, and polarity |

---

## 🧪 Best Practices for Use

- Use **Efflux Ratio** to flag compounds likely affected by P-gp or BCRP
- **Recovery (%)** is a critical QC metric — always check it!
- Combine Papp data with structural rules (e.g., Veber, Lipinski) to guide optimization
- Consider **permeability**, **solubility**, and **efflux** together when ranking compounds for further studies

---

## 📚 References

- Hidalgo IJ, et al. (1989). *Characterization of the human colon carcinoma cell line (Caco-2) as a model for intestinal epithelial permeability*. Gastroenterology.
- Waring MJ. (2009). *Defining optimum lipophilicity and molecular weight ranges for drug candidates*. **Bioorg. Med. Chem. Lett.**, 19(10), 2844–2851.
- SwissADME: https://www.swissadme.ch/
