from cpd_demo import encode_sequence

def test_encoding():
    vec = encode_sequence("ACD")
    assert len(vec) == 20
