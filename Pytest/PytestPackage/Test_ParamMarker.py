import pytest
@pytest.mark.parametrize("a,b,sum",[(12,12,0),(5,10,0),(20,30,0)])
def test_add(a,b,sum):
    assert a+b == sum
