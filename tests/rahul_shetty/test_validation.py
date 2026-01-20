import pytest

#Fixtures

@pytest.fixture(scope="session")

def prework():
    print("Is setup browser instance")


def test_initialCheck(prework):
    assert 1 == 1
print("This is the first test case  ")


def test_second_Check(prework):
    assert 1 == 1
print("This is the second test case  ")