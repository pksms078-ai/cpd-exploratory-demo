import time
import numpy as np

def dummy_design(n):
    time.sleep(0.01 * n)
    return np.random.rand(n, 10)

if __name__ == "__main__":
    for n in [10, 100]:
        start = time.time()
        dummy_design(n)
        print(f"{n} sequences runtime: {time.time() - start:.3f}s")
