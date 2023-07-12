import pytest


@pytest.mark.smoke
def test_firstProgram():
    meg = "Hello"
    assert meg =="Hello", "Test failed becase string is not matched"
    print(meg)
