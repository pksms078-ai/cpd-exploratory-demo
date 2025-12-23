# Computational Protein Design – Demo

This repository provides a **minimal, installable demo package**
illustrating an exploratory computational protein design workflow.

## Purpose
- Reduce experimental search space
- Explore sequence-level patterns
- Provide reproducible, transparent structure

## Install
```bash
pip install -e .
from cpd_demo import encode_sequence, ProteinMLModel, run_md_simulation

seq = "ACDEFGHIK"
encoded = encode_sequence(seq)

model = ProteinMLModel()
score = model.predict_score(encoded)

result = run_md_simulation(seq)
print(score, result)

---

## 5️⃣ STEP 1 COMMIT MESSAGE (IMPORTANT)

When pushing to GitHub, use:
Fix GitHub Actions workflow syntax
git checkout SRC
nano .github/workflows/python-app.yml   # or VS Code
# paste content
git add .github/workflows/python-app.yml
git commit -m "Fix GitHub Actions workflow"
git push origin SRC


