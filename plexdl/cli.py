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


app = typer.Typer(help=__doc__, context_settings=dict(max_content_width=9999))


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
    username: str = typer.Option(..., "-u", "--username", envvar="PLEXDL_USERNAME"),
    password: str = typer.Option(..., "-p", "--password", envvar="PLEXDL_PASSWORD"),
    title: str = typer.Argument(..., envvar="PLEXDL_TITLE"),
    item_prefix: str = typer.Option("", "--item-prefix", help="String to prefix to each item (eg: curl -o)"),
    show_summary: bool = typer.Option(False, "--show-summary", help="Show media summary for each result"),
    show_ratings: bool = typer.Option(False, "--show-ratings", help="Show ratings for each result"),
    show_metadata: bool = typer.Option(False, "--show-metadata", help="Show file and codec metadata for each file in each result"),
    include_relays: bool = typer.Option(False, "--include-relays", help="Output relay servers along with direct servers"),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
    debug: bool = typer.Option(False, "--debug"),
):
    """Search for media in servers that are available to your account."""
    p = Client(
        username=username,
        password=password,
        title=title,
        relay=include_relays,
        debug=debug,
        item_prefix=item_prefix,
        summary=show_summary,
        ratings=show_ratings,
        metadata=show_metadata,
    )
    p.main()


if __name__ == "__main__":
    try:
        app()
    except KeyboardInterrupt:
        sys.exit(1)
    except plexapi.exceptions.BadRequest:
        sys.exit(2)


# https://typer.tiangolo.com/tutorial/subcommands/add-typer/
