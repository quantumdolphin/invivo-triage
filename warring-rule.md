## Waring Rule for Permeability Prediction

The **Waring Rule** is a permeability profiling guideline derived from a large set of 8,865 compounds with measured Caco-2 permeability (Papp). It provides minimum log D thresholds that correspond to a >50% probability of high permeability, depending on the compound’s molecular weight (MW).

Unlike Lipinski’s Rule of 5 which sets upper limits, the Waring Rule defines **lower bounds for log D** across MW bands.

### 📊 Minimum log D Thresholds by MW Range

| Molecular Weight Range (Da) | Minimum log D Required |
|-----------------------------|-------------------------|
| < 300                       | > 0.5                   |
| 300–350                     | > 1.1                   |
| 350–400                     | > 1.7                   |
| 400–450                     | > 3.1                   |
| 450–500                     | > 3.4                   |
| > 500                       | > 4.5                   |

These thresholds were developed to identify compounds with a **high likelihood of Caco-2 permeability**, making them more suitable for oral administration.

In validation studies, 82% of compounds that passed these criteria showed high permeability, while 70% of those that failed had low permeability.

### 🧪 How It Works

- **log D** is used instead of log P because it reflects the compound’s distribution at physiological pH, accounting for ionization.
- **MW** defines how strict the log D requirement should be. As MW increases, higher lipophilicity is needed to maintain permeability.
- The rule is useful in **early screening** to rapidly eliminate compounds unlikely to have sufficient passive absorption.

### ✅ Implementation

A new column called `Waring Rule` was added to the compound descriptor table with values:

- `"Y"` for compounds meeting the MW-appropriate log D threshold
- `"N"` for compounds falling below the threshold

This flag supports prioritizing compounds for **oral or systemic administration** in early-stage screening.
