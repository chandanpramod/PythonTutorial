import pytest
@pytest.mark.Sanity
def test_fail():
    a=10
    b=20
    assert a+b==100