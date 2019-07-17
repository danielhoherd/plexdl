import logging
import os
import sys

import plexapi
from click import argument
from click import command
from click import option

import plexdl


def get_logger(ctx, param, value):
    logging.basicConfig(format="%(asctime)s %(levelname)s: %(message)s", datefmt="%FT%T%z")
    log = logging.getLogger("plexdl")
    log.setLevel(50 - (value * 10))  # https://docs.python.org/3.7/library/logging.html#logging-levels
    return value


@command()
@option("-v", count=True, help="Increase verbosity (max -vvvv)", callback=get_logger)
@option("-u", "--username", help="Your Plex username (env PLEXDL_USER)", envvar="PLEXDL_USER")
@option("-p", "--password", help="Your Plex password (env PLEXDL_PASS)", envvar="PLEXDL_PASS")
@option("-r", "--relay/--no-relay", default=False, help="Output relay servers along with direct servers")
@option("--summary/--no-summary", default=False, help="Output summary about each movie, show, etc..")
@option("--server-info/--no-server-info", default=False, help="Output summary about each server. (OS, Plex Server version, etc..)")
@argument("title", envvar="PLEXDL_TITLE")
def main(username, password, title, relay, summary, server_info, v):
    """Searches your plex account for media matching the given string, then prints out download commands."""

    p = plexdl.Client(
        username=username, password=password, title=title, relay=relay, debug=v, summary=summary, server_info=server_info
    )
    try:
        p.main()
    except KeyboardInterrupt:
        sys.exit(1)
    except plexapi.exceptions.BadRequest:
        sys.exit(2)


if __name__ == "__main__":
    main()
