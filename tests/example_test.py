"""plexdl boilerplate tests."""
from plexdl.plexdl import Client


def test_hello():
    """Hello world test."""
    assert Client.available_servers == []
