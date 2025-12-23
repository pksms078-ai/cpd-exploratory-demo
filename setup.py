from setuptools import setup, find_packages

setup(
    name="cpd-exploratory-demo",
    version="0.3.0",
    description="Computational Protein Design – Exploratory Demo",
    author="Prabin Kumar",
    author_email="",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.9",
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
    ],
)
