import time
import random

def simulate_design(n_sequences: int):
    results = []
    for _ in range(n_sequences):
        time.sleep(0.01)  # dummy compute
        results.append(random.random())
    return results

if __name__ == "__main__":
    for n in [10, 100]:
        start = time.time()
        simulate_design(n)
        elapsed = time.time() - start
        print(f"Sequences: {n} | Runtime: {elapsed:.3f} seconds")
