cat > src/cpd_exploratory/model.py << 'EOF'
def dummy_model(x: int) -> int:
    """
    Dummy_model for benchmarking and pipeline validation.
    """
    return x * x
if __name__ == "__main__":
    print(dummy_model(5))
EOF

cat > src/cpd_exploratory/model.py << 'EOF'
def dummy_model(x: int) -> int:
    """
    Dummy model for benchmarking and pipeline validation.
    """
    return x * x
if __name__ == "__main__":
    print(dummy_model(5))
EOF
def dummy_model(x):
    return x * 2
