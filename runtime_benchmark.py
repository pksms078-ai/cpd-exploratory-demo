import time
from cpd_exploratory.model import dummy_model

for n in [10, 100, 1000]:
    start = time.time()
    dummy_model(n)
    print(f"{n} sequences → {time.time() - start:.6f}s")
