import pytest


def test_basic():
    x = 1 + 1
    assert x == 2


def test_raises():
    with pytest.raises(ZeroDivisionError):
        1 / 0
