from setuptools import setup, find_packages

setup(
    name="cpd-exploratory-demo",
    version="0.1.0",
    description="Computational Protein Design – Exploratory Demo",
    author="Prabin Kumar",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=["numpy"],
)
