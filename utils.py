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
import numpy as np

AMINO_ACIDS = "ACDEFGHIKLMNPQRSTVWY"

def encode_sequence(sequence: str) -> np.ndarray:
    """
    Simple numeric encoding of amino acid sequence.
    Each amino acid mapped to an integer index.
    """
    encoding = []
    for aa in sequence:
        if aa not in AMINO_ACIDS:
            raise ValueError(f"Invalid amino acid: {aa}")
        encoding.append(AMINO_ACIDS.index(aa))
    return np.array(encoding, dtype=np.float32)

def pad_sequence(encoded_seq, max_len=50):
    """
    Pad or truncate sequence to fixed length.
    """
    if len(encoded_seq) >= max_len:
        return encoded_seq[:max_len]
    return np.pad(encoded_seq, (0, max_len - len(encoded_seq)))

