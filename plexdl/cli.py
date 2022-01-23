"""plexdl CLI."""
import datetime
import logging
import os
import sys

import humanize
import plexapi
import typer
from importlib_metadata import version

__version__ = version(__package__)

from plexapi.myplex import MyPlexAccount
from plexapi.server import PlexServer

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
def get_server_info(
    username: str = typer.Argument(None, envvar="PLEXDL_USERNAME"),
    password: str = typer.Argument(None, envvar="PLEXDL_PASSWORD"),
    debug: bool = typer.Argument(False, envvar="PLEXDL_DEBUG"),
):
    """Show info about servers available to your account."""
    p = MyPlexAccount(
        username=username,
        password=password,
    )
    servers = p.resources()
    for server in servers:
        if server.product == "Plex Media Server":
            print(f"{server.name=} ", "-" * 70)
            print(f"    clientIdentifier: {server.clientIdentifier}")
            last_seen_diff = datetime.datetime.now() - server.lastSeenAt
            last_seen_time_delta = humanize.naturaldelta(last_seen_diff)
            print(f"    lastSeenAt: {server.lastSeenAt.strftime('%FT%T%z')} ({last_seen_time_delta})")
            created_diff = datetime.datetime.now() - server.createdAt
            created_time_delta = humanize.naturaldelta(created_diff)
            print(f"    createdAt: {server.createdAt.strftime('%FT%T%z')} ({created_time_delta})")
            for i, connection in enumerate(server.connections):
                preferred = connection.uri in server.preferred_connections()
                print(f"    connections[{i}]:")
                print(f"        local: {connection.local}")
                print(f"        uri: {connection.uri}")
                print(f"        httpuri: {connection.httpuri}")
                print(f"        relay: {bool(connection.relay)}")
                print(f"        preferred: {preferred}")
            print(f"    device: {server.device}")
            print(f"    home: {server.home}")
            print(f"    httpsRequired: {server.httpsRequired}")
            print(f"    name: {server.name}")
            print(f"    owned: {server.owned}")
            print(f"    ownerid: {server.ownerid}")
            print(f"    platform: {server.platform}")
            print(f"    platformVersion: {server.platformVersion}")
            print(f"    presence: {server.presence}")
            print(f"    product: {server.product}")
            print(f"    productVersion: {server.productVersion}")
            print(f"    provides: {server.provides}")
            print(f"    publicAddressMatches: {server.publicAddressMatches}")
            print(f"    sourceTitle: {server.sourceTitle}")
            print(f"    synced: {server.synced}")
            print("")


@app.command()
def search(
    username: str = typer.Argument(None, envvar="PLEXDL_USERNAME"),
    password: str = typer.Argument(None, envvar="PLEXDL_PASSWORD"),
    debug: bool = typer.Argument(False, envvar="PLEXDL_PASSWORD"),
):
    """Search for media in servers that are available to your account."""
    print("unimplemented")


if __name__ == "__main__":
    app()


# https://typer.tiangolo.com/tutorial/subcommands/add-typer/
