import time
from cpd_exploratory.model import dummy_model

def run(n):
    start = time.time()
    for i in range(n):
        dummy_model(i)
    return time.time() - start

if __name__ == "__main__":
    t10 = run(10)
    t100 = run(100)
    print(f"Runtime 10 seq: {t10:.6f}s")
    print(f"Runtime 100 seq: {t100:.6f}s")
