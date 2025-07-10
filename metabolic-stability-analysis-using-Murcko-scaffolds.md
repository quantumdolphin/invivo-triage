# 🧪 Metabolic Stability Analysis Using Murcko Scaffolds

## 📘 Objective

To explore how **molecular structure** relates to **metabolic stability**, using a dataset containing:

- **SMILES** (molecular structure)
- **Intrinsic Clearance (CLint)** in µL/min/10⁶ cells
- **Half-life (t½)** in minutes (from human hepatocyte assay)

Our goal is to identify **scaffold-specific trends** in metabolism and uncover **outliers** that reveal the structural impact of functional group modifications on stability.

---

## ⚙️ Step 1: Binarize Metabolic Stability

We categorized each compound based on commonly accepted DMPK thresholds:

### 🧪 Intrinsic Clearance Categories
| CLint (µL/min/10⁶ cells) | Category |
|--------------------------|----------|
| ≤ 10                     | **Low Clearance** (desirable) |
| > 10                     | **High Clearance** (metabolically labile) |

### ⏱️ Half-Life Categories
| t½ (min) | Category |
|----------|----------|
| ≥ 60     | **Long Half-Life** (stable) |
| < 60     | **Short Half-Life** (unstable) |

These categories help quickly triage compounds for further optimization or deprioritization.

---

## 🧱 Step 2: Generate Murcko Scaffolds

We used **RDKit's Murcko scaffold extraction** to capture the **core chemotype** of each molecule:

> A Murcko scaffold is defined as the **union of all ring systems and the linkers that connect them**, with all side chains removed.

This helps reduce chemical noise and group molecules by shared structural backbones.

Each compound was assigned:
- A canonical **Murcko scaffold SMILES**
- A **scaffold cluster ID** for grouping

---

## 🔍 Step 3: Scaffold-Based Clustering

We clustered all compounds by their Murcko scaffold. This effectively groups analogs that share the same core structure, regardless of substitutions.

This strategy is especially powerful for:
- Visualizing **structure–metabolism relationships (SMRs)**
- Spotting **privileged scaffolds** with desirable metabolic profiles
- Focusing medicinal chemistry design efforts on **core-driven liabilities**

---

## 🚨 Step 4: Outlier Detection Within Scaffold Clusters

To understand **how substitutions affect metabolic behavior**, we computed **intra-cluster z-scores** for each compound's:

- CLint
- Half-life

We flagged outliers using a **z-score threshold of ±2**, indicating compounds that behave unusually within their scaffold group.

> 🔎 These outliers are of special interest because:
> - They may reveal **metabolic soft spots** (e.g., benzylic oxidation, exposed nitrogen)
> - They highlight **functional groups** that either protect or expose the molecule to metabolism
> - They help explain **structure–stability disconnects**

---

## 🧠 Why This Matters for Drug Discovery

| Insight | Benefit |
|--------|---------|
| Scaffold-based trends | Pinpoints **stable vs labile chemotypes** |
| Functional group impact | Helps guide **R-group optimization** |
| Outlier detection | Flags **context-sensitive liabilities** missed by global models |
| SAR meets SMR | Enables a unified approach to potency + metabolism tuning |

This approach is a practical application of cheminformatics and DMPK principles to derive **actionable insights** for lead optimization.

---

## ✅ Next Steps

- Visualize scaffold clusters and highlight outliers
- Overlay physicochemical properties (e.g., logP, TPSA) to explain differences
- Correlate with in vivo PK data if available
- Integrate matched molecular pair (MMP) analysis for precise SAR/SMR attribution

---
