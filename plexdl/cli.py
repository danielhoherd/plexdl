"""plexdl CLI."""
import logging
import os
import sys

import plexapi
from click import argument
from click import command
from click import echo
from click import option
from click import version_option
from importlib_metadata import version

__version__ = version(__package__)

from plexdl.plexdl import Client


def get_logger(ctx, param, value):
    """Get logger and return verbosity value."""
    logging.basicConfig(format="%(message)s")
    log = logging.getLogger("plexdl")
    if value > 0:
        log.setLevel("DEBUG")  # https://docs.python.org/3.7/library/logging.html#logging-levels
    return value


@command()
@option("-v", count=True, help="Be verbose", callback=get_logger)
@option("-u", "--username", help="Your Plex username (env PLEXDL_USER)", envvar="PLEXDL_USER")
@option("-p", "--password", help="Your Plex password (env PLEXDL_PASS)", envvar="PLEXDL_PASS")
@option("-r", "--relay/--no-relay", default=False, help="Output relay servers along with direct servers")
@option("--item-prefix", default=str(""), help="String to prefix to each item (eg: curl -o)", envvar="PLEXDL_ITEM_PREFIX")
@option("--server-info/--no-server-info", default=False, help="Output summary about each server")
@option("--summary/--no-summary", default=False, help="Output summary about each result")
@option("--ratings/--no-ratings", default=False, help="Output rating information for each result")
@option("--metadata/--no-metadata", default=False, help="Output media metadata about each file for each result")
@version_option(version=__version__)
@argument("title", envvar="PLEXDL_TITLE")
def main(username, password, title, relay, server_info, item_prefix, summary, ratings, metadata, v):
    """Search your plex account for media matching the given string, then prints out download commands."""
    try:
        p = Client(
            username=username,
            password=password,
            title=title,
            relay=relay,
            debug=v,
            item_prefix=item_prefix,
            server_info=server_info,
            summary=summary,
            ratings=ratings,
            metadata=metadata,
        )

        p.main()
    except KeyboardInterrupt:
        sys.exit(1)
    except plexapi.exceptions.BadRequest:
        sys.exit(2)
