# src/cpd_exploratory/model.py

def dummy_model(x: int) -> int:
    """
    Dummy model for benchmarking and pipeline validation.
    """
    return x * x


if __name__ == "__main__":
    print(dummy_model(5))

