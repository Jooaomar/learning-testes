from hypothesis import given, strategies as st

@given(st.integers(), st.integers())
def test_ints_are_commutative(x, b):
    assert x + b == b + x