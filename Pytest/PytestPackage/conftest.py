import pytest
@pytest.fixture(scope='session',autouse=True)
def tc_setup():
    print("Lounch Browser")
    print("Login")
    print("Select items")
    yield
    print("logout")
    print("Close browser")
