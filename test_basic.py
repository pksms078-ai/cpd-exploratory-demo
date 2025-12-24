import pytest
from cpd_exploratory.model import dummy_model


class TestDummyModel:
    def test_square_positive(self):
        assert dummy_model(4) == 16

    def test_square_zero(self):
        assert dummy_model(0) == 0

    def test_square_negative(self):
        assert dummy_model(-3) == 9
