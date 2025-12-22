import numpy as np

AMINO_ACIDS = "ACDEFGHIKLMNPQRSTVWY"

def encode_sequence(sequence: str) -> np.ndarray:
    """
    Encode protein sequence into numerical vector.

    This is a simple frequency-based encoding.
    (Replaceable with embeddings / transformers later.)

    Parameters
    ----------
    sequence : str
        Protein amino acid sequence

    Returns
    -------
    np.ndarray
        Normalized feature vector
    """
    sequence = sequence.upper()
    counts = np.zeros(len(AMINO_ACIDS))

    for aa in sequence:
        if aa in AMINO_ACIDS:
            counts[AMINO_ACIDS.index(aa)] += 1

    if len(sequence) > 0:
        counts /= len(sequence)

    return counts

