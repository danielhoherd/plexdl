"""Shim for package execution (python3 -m plexdl ...)."""
from .cli import app

if __name__ == "__main__":  # pragma: no cover
    app()
