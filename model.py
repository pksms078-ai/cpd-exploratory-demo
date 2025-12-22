import numpy as np
from sklearn.ensemble import RandomForestRegressor
from .utils import encode_sequence

class ProteinSequenceModel:
    """
    Lightweight ML model for exploratory
    protein sequence scoring.

    This model is NOT a biological oracle.
    It reduces search space for experiments.
    """

    def __init__(self):
        self.model = RandomForestRegressor(
            n_estimators=50,
            random_state=42
        )
        self.trained = False

    def fit(self, sequences, scores):
        """
        Train model on sequence-score pairs.
        """
        X = np.array([encode_sequence(s) for s in sequences])
        y = np.array(scores)

        self.model.fit(X, y)
        self.trained = True

    def predict(self, sequences):
        """
        Predict relative scores for new sequences.
        """
        if not self.trained:
            raise RuntimeError("Model not trained")

        X = np.array([encode_sequence(s) for s in sequences])
        return self.model.predict(X)
import numpy as np
from sklearn.ensemble import RandomForestRegressor

class SequenceScoringModel:
    """
    Lightweight ML model to score protein sequences.
    This does NOT claim biological accuracy.
    It demonstrates computational prioritization.
    """

    def __init__(self):
        self.model = RandomForestRegressor(
            n_estimators=50,
            random_state=42
        )

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

