import time
import random
import string

def random_sequence(length=50):
    amino_acids = "ACDEFGHIKLMNPQRSTVWY"
    return "".join(random.choice(amino_acids) for _ in range(length))

def simulate_pipeline(seq):
    time.sleep(0.01)   # ML stage
    time.sleep(0.02)   # Structural stage

def benchmark(n_sequences):
    sequences = [random_sequence() for _ in range(n_sequences)]
    start = time.time()
    for seq in sequences:
        simulate_pipeline(seq)
    end = time.time()
    return end - start

if __name__ == "__main__":
    for n in [10, 50, 100]:
        t = benchmark(n)
        print(f"{n} sequences → {t:.2f} seconds")

