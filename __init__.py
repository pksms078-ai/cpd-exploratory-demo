"""
Computational Protein Design Demo Package
=========================================

A minimal, reproducible demonstration package for
ML-assisted protein sequence exploration and
in-silico structural validation.

Author: Prabin Kumar
License: MIT
"""

from .model import ProteinSequenceModel
from .simulation import MolecularSimulation
from .utils import encode_sequence

__all__ = [
    "ProteinSequenceModel",
    "MolecularSimulation",
    "encode_sequence",
]

