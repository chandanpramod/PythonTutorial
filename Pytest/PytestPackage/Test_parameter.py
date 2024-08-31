import pytest
@pytest.fixture(params=["a","b","c"],autouse=True)
def demofixture(request):
    print(request.param)
def testlogin(demofixture):
    print("Login successfully")

# def cal():
    # print("Calculations are correct")
    assert 3+3==9
# def logout():
#     print("logout is working fine")