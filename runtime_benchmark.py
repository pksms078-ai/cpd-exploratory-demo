import time
import numpy as np
import matplotlib.pyplot as plt

def run_test(n):
    start = time.time()
    _ = np.random.rand(n, 20)
    time.sleep(0.01)
    return time.time() - start

sizes = [10, 100]
times = [run_test(n) for n in sizes]

plt.plot(sizes, times, marker='o')
plt.xlabel("Number of sequences")
plt.ylabel("Runtime (seconds)")
plt.title("Runtime Benchmark (Exploratory)")
plt.savefig("benchmark.png")

print("Benchmark completed:", dict(zip(sizes, times)))
