# 📦 Interpreting Lipinski's Rule of 5 (Ro5) Violations

Lipinski’s Rule of 5 (Ro5) provides a heuristic to evaluate the oral drug-likeness of compounds. It is widely used in medicinal chemistry to flag compounds that might have **poor bioavailability** due to unfavorable physicochemical properties.

Each compound is evaluated against four key criteria:

| Rule | Description |
|------|-------------|
| 1.   | Hydrogen bond donors (HBD) ≤ 5 |
| 2.   | Hydrogen bond acceptors (HBA) ≤ 10 |
| 3.   | Molecular weight (MW) ≤ 500 g/mol |
| 4.   | logP ≤ 5 (or clogP) |

The **`Ro5 Violations` column** counts how many of these four rules are broken by a given compound. This count gives a compact view of oral drug-likeness and can be used for prioritizing compounds.

---

## ✅ How to Interpret Ro5 Violations

| Ro5 Violations | Interpretation |
|----------------|----------------|
| **0** | **Ideal profile** for oral bioavailability. Likely to have good permeability and solubility. Strong candidate for oral dosing. |
| **1** | **Generally acceptable**. Many drugs have one violation, typically MW or logP. Should be investigated with in vitro ADME data. |
| **2** | **Moderate concern**. Suggests permeability or solubility issues. Consider alternate formulation or dosing route. |
| **≥3** | **High risk** for oral bioavailability failure. Often deprioritized unless biological or strategic rationale exists (e.g., peptide, transporter substrate). |

---

## 💡 Triage Strategy Using Ro5 Violations

You can use `Ro5 Violations` to triage a screening set:

- **0–1 violations**: High-priority candidates for oral drug development.
- **2 violations**: Medium-priority; suitable with ADME support or alternate routes.
- **3+ violations**: Low-priority unless exceptional rationale.

Combine Ro5 violations with other filters such as:

- **Veber Rules**
- **Waring Rule (MW vs logD)**
- **TPSA**
- **Caco-2 Permeability / Efflux Ratio**
- **Log S or Solubility Class**

---

## 🔬 Example Table

| Compound | MW | logP | HBD | HBA | Ro5 Violations | Notes |
|----------|----|------|-----|-----|----------------|-------|
| CMPD001  | 450 | 3.8  | 2   | 8   | 0              | Drug-like |
| CMPD002  | 520 | 4.9  | 1   | 12  | 2              | Watch for solubility |
| CMPD003  | 600 | 6.0  | 6   | 14  | 4              | Unlikely oral drug |

---

## 🧠 Final Notes

- The "rule of 5" is a **guideline**, not a strict cutoff.
- Some approved drugs (e.g., antibiotics, antifungals, natural products) **violate multiple rules**.
- Use Ro5 as a **first-pass filter** — not a final decision-maker.
- Always consider biological context, administration route, and target tissue exposure.


