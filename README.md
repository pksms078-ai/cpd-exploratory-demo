# Computational Protein Design – Demo Package

This repository provides a **minimal, installable demo**
of an exploratory computational protein design framework.

## Purpose

This package demonstrates:
- Clean Python packaging
- ML-assisted sequence exploration
- Conceptual molecular simulation integration
- Scientific boundary clarity (no over-claiming)

This is **not a biological product**.
It is a **decision-support framework** for research teams.

## Installation (local)

```bash
pip install -e .
from cpd_demo import ProteinSequenceModel, MolecularSimulation

model = ProteinSequenceModel()

sequences = ["ACDEFGHIK", "LMNPQRSTV"]
scores = [0.7, 0.4]

model.fit(sequences, scores)
predictions = model.predict(sequences)

sim = MolecularSimulation()
result = sim.run("example.pdb")

---

# 🔹 STEP 6: `requirements.txt`

```txt
numpy
scikit-learn

