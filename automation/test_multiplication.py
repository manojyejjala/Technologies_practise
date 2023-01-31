import pytest

@pytest.mark.parametrize("num, output", [(1,11), (2,20), (3,33), (4,44)])
def test_mutiplicaion_11(num, output):
    assert 11*num == output