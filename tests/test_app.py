from src.app import get_message


def test_get_message():
    assert len(get_message()) == 63
