from plexdl import Client


def test_hello():
    assert Client.hello() == "world"
