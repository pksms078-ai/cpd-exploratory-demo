from cpd_exploratory.model import dummy_model

def test_dummy_model_basic():
    assert dummy_model(5) == 25
