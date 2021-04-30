import pytest

@pytest.mark.one
def test1():

    assert 2 == 5

@pytest.mark.two
def test2():

    assert 5 == 5
