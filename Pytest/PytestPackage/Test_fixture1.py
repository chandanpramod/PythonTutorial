import pytest
@pytest.fixture()
def setup():
    print("Lounch Browser")
    print("Login")
    print("Select items")
    yield
    print("logout")
    print("Close browser")

def test_additems(setup):
    print("Iteams added")
def test_removeitems(setup):
    print("Items removed")
