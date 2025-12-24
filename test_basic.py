from cpd_exploratory.model import dummy_model

def test_pytest_is_working():
    assert 1 + 1 == 2

def test_dummy_model():
    assert dummy_model(3) == 6



