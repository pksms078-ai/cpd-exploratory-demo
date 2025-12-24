cat << 'EOF' > src/cpd_exploratory/model.py
def dummy_model(x: int) -> int:
    return x * x
EOF
if __name__ == "__main__":
    print("Manual run result:", dummy_model(5))

