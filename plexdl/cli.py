"""plexdl CLI."""
import logging
import os
import sys

import plexapi
import typer
from importlib_metadata import version

__version__ = version(__package__)

from plexdl.plexdl import Client


def get_logger(ctx, param, value):
    """Get logger and return verbosity value."""
    logging.basicConfig(format="%(message)s")
    log = logging.getLogger("plexdl")
    if value > 0:
        log.setLevel("DEBUG")  # https://docs.python.org/3.9/library/logging.html#logging-levels
    return value


# @command()
# @option("-v", count=True, help="Be verbose", callback=get_logger)
# @option("-u", "--username", help="Your Plex username (env PLEXDL_USER)", envvar="PLEXDL_USER")
# @option("-p", "--password", help="Your Plex password (env PLEXDL_PASS)", envvar="PLEXDL_PASS")
# @option("-r", "--relay/--no-relay", default=False, help="Output relay servers along with direct servers")
# @option("--item-prefix", default="", help="String to prefix to each item (eg: curl -o)", envvar="PLEXDL_ITEM_PREFIX")
# @option("--server-info/--no-server-info", default=False, help="Output summary about each server")
# @option("--summary/--no-summary", default=False, help="Output summary about each result")
# @option("--ratings/--no-ratings", default=False, help="Output rating information for each result")
# @option("--metadata/--no-metadata", default=False, help="Output media metadata about each file for each result")
# @version_option(version=__version__)
# @argument("title", envvar="PLEXDL_TITLE")
# def main(username, password, title, relay, server_info, item_prefix, summary, ratings, metadata, v):
#     """Search your plex account for media matching the given string, then prints out download commands."""
#     try:
#         p = Client(
#             username=username,
#             password=password,
#             title=title,
#             relay=relay,
#             debug=v,
#             item_prefix=item_prefix,
#             server_info=server_info,
#             summary=summary,
#             ratings=ratings,
#             metadata=metadata,
#         )

#         p.main()
#     except KeyboardInterrupt:
#         sys.exit(1)
#     except plexapi.exceptions.BadRequest:
#         sys.exit(2)

app = typer.Typer(help=__doc__)


@app.command()
def get_server_info():
    """Show info about available servers available to your account."""
    print("unimplemented")


@app.command()
def search():
    """Search for media in servers that are available to your account."""
    print("unimplemented")


if __name__ == "__main__":
    app()
