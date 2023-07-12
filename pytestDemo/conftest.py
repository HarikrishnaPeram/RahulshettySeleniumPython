# fixtures
import pytest


@pytest.fixture(scope = "class")
def setup():
    print("i want to execute first")
    yield
    print("i will execute last")



@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Hari", "krishna", "Peram@gmail.com"]


@pytest.fixture(params=["Chrome", "Firefox", "IE"])
def crossBrowser(request):
    return request.param