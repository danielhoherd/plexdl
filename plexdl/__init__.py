"""Shim for package execution (python3 -m plexdl ...)."""
from .cli import main

if __name__ == "__main__":  # pragma: no cover
    main()
