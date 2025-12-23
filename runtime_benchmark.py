import time
import numpy as np

def dummy_run(n):
    data = np.random.rand(n, 100)
    return np.mean(data)

sizes = [10, 100, 1000]

for s in sizes:
    start = time.time()
    dummy_run(s)
    print(f"Size {s}: {time.time() - start:.6f} seconds")
