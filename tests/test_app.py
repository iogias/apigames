from app import __version__


def test_version() -> str:
    assert __version__ == "0.1.0"