## Veber Rule for Predicting Oral Bioavailability

The **Veber Rule** was derived from a dataset of 1,100 drug candidates with measured oral bioavailability (F) in rats. The threshold for acceptable bioavailability was set at 20%.

This rule set is specifically focused on compounds that are **intended for oral delivery and intestinal absorption**. Unlike Lipinski’s rules, which consider general developability, the Veber Rule is more narrowly aimed at bioavailability prediction after oral dosing.

### ✴️ Background

The Veber Rule found that compounds with:

- Lower **molecular flexibility** (fewer rotatable bonds)
- Lower **polar surface area (PSA)**
- Fewer **hydrogen bonding groups**

… were more likely to exhibit oral bioavailability >20% in rats.

> For example, 65% of compounds with ≤7 rotatable bonds had good F, while only 20% of compounds with >10 rotatable bonds met the criteria.

### 📊 Rule Criteria

A compound is more likely to have good oral bioavailability if it satisfies:

- **Rotatable bonds ≤ 10**
- AND one of the following:
  - **Polar Surface Area (PSA) ≤ 140 Å²**
  - **Total H-bond donors + acceptors ≤ 12**

These properties relate to molecular flexibility and polarity — key factors that affect permeability and absorption through the intestinal wall.

### ✅ Implementation

The project applies this rule by creating a new column in the compound descriptor table:

- `"Y"` = Passes Veber Rule (likely to be orally bioavailable)
- `"N"` = Fails Veber Rule (less likely to be orally bioavailable)

This annotation supports **early-stage triaging** of compounds for oral dosing feasibility.
