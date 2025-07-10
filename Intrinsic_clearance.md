# 🧪 What Is CLint and Why Is It Called That?

**CLint** stands for **Intrinsic Clearance** — a key pharmacokinetic parameter used to describe the liver’s inherent ability to metabolize a compound.

---

## 📖 What Does "Intrinsic" Mean?

"Intrinsic" means **independent of physiological constraints** such as:

- Liver **blood flow** (Q)
- **Plasma protein binding** (fu)
- Membrane transport or distribution

So, **CLint reflects only the enzymatic capacity** of liver cells (hepatocytes or microsomes) to metabolize a drug.

---

## 🧬 Where Is CLint Measured?

CLint is typically measured **in vitro** using:
- Human hepatocytes
- Liver microsomes
- Liver S9 fractions

**Units:**  
- `µL/min/10⁶ cells` (for hepatocytes)  
- `µL/min/mg protein` (for microsomes)

It describes the **volume of solution from which the drug is completely removed per unit time** by metabolic enzymes.

---

## 📐 Relationship to Hepatic Clearance

CLint feeds into models to estimate in vivo **hepatic clearance (CLh)**. One commonly used model is the **well-stirred liver model**:

\[
CL_{h} = \frac{Q \cdot fu \cdot CL_{int}}{Q + fu \cdot CL_{int}}
\]

Where:
- `CLh`: Hepatic clearance
- `Q`: Liver blood flow (~20 mL/min/kg in humans)
- `fu`: Fraction unbound in plasma
- `CLint`: Intrinsic clearance

### 🔁 Interpretation:
- When **CLint is high**, hepatic clearance approaches the liver blood flow (flow-limited).
- When **CLint is low**, hepatic clearance is **enzyme-limited**.

---

## ✅ Summary Table

| Term      | Meaning                                                                 |
|-----------|-------------------------------------------------------------------------|
| **CLint** | Intrinsic clearance – enzymatic capacity to metabolize drug in vitro    |
| **Why "intrinsic"?** | It excludes effects of blood flow, protein binding, transport |
| **Units** | µL/min/10⁶ cells (hepatocytes) or µL/min/mg (microsomes)                |
| **Used in** | In vitro metabolism assays, PBPK models, drug clearance prediction     |

---

CLint is an essential metric for prioritizing compounds in early drug discovery and predicting **in vivo clearance, oral bioavailability, and metabolic stability**.
