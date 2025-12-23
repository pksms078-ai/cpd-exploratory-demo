from setuptools import setup, find_packages

setup(
    name="cpd-demo",
    version="0.1.0",
    description="Exploratory Computational Protein Design Demo Framework",
    author="Prabin Kumar",
    author_email="prabincheslind@gmail.com",
    packages=find_packages(),
    install_requires=[
        "numpy"
    ],
    python_requires=">=3.8",
)
