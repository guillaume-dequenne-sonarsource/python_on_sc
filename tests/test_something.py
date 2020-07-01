import pytest


def test_basic():
    x = 1 + 1
    assert x == 2


def test_raises():
    with pytest.raises(ZeroDivisionError):
        1 / 0


def test_fails():
    assert 1 + 1 == 4
