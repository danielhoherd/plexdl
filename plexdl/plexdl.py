"""plexdl client class."""
import locale
import logging
from typing import List

import humanfriendly
import requests
from plexapi.myplex import MyPlexAccount
from plexapi.server import PlexServer

log = logging.getLogger("plexdl")
locale.setlocale(locale.LC_ALL, "")


class Client:
    """A client interface to plex for finding direct download URLs."""

    def __init__(self, **kwargs):
        """plexdl.Client __init__ method."""
        self.debug = kwargs["debug"]
        self.item_prefix = kwargs["item_prefix"]
        self.metadata = kwargs["metadata"]
        self.password = kwargs["password"]
        self.ratings = kwargs["ratings"]
        self.relay = kwargs["relay"]
        self.summary = kwargs["summary"]
        self.title = kwargs["title"]
        self.username = kwargs["username"]
        self.account = MyPlexAccount(self.username, self.password)

    available_servers: List[PlexServer] = list()

    @staticmethod
    def print_item_info(self, item, access_token):
        """Print info about a given media item."""
        log.debug(f"Filesystem locations: {item.locations}")
        if not hasattr(item, "iterParts"):
            return
        locations = [i for i in item.iterParts() if i]
        for location in locations:
            media_info = []
            download_url = item._server.url(f"{location.key}?X-Plex-Token={access_token}")
            download_filename = ""
            if hasattr(item, "seasonEpisode"):
                download_filename += f"{item.seasonEpisode} "
            download_filename += f"{item.title}.{location.container}"
            if self.metadata is True:
                if item.media[0].width is not None:
                    media_info.append(f"{item.media[0].width}x{item.media[0].height}")
                if item.media[0].videoCodec is not None:
                    media_info.append(item.media[0].videoCodec)
                if item.media[0].audioCodec is not None:
                    media_info.append(item.media[0].audioCodec)
                if item.media[0].bitrate is not None:
                    media_info.append(f"{item.media[0].bitrate}kbps")
                try:
                    length = humanfriendly.format_size(int(requests.head(download_url).headers["Content-Length"]))
                    media_info.append(f"{length}")
                except ValueError:
                    pass
            if media_info:
                print(f'({", ".join(media_info)})')
            print(f'  {self.item_prefix} "{download_filename}" "{download_url}"')

    @staticmethod
    def print_all_items_for_server(self, item, access_token):
        """Print info about all media items discovered on a given Plex server."""
        if item.TYPE in ["movie", "track"]:
            print("-" * 79)
            print(f"{item.TYPE.capitalize()}: {item.title}")
            if self.summary is True and len(item.summary) > 1:
                print(f"Year: {item.year}")
                print(f"Studio: {item.studio}")
                print(f"Summary: {item.summary}")
            if self.ratings is True:
                if item.contentRating:
                    print(f"Content rating: {item.contentRating}")
                if item.audienceRating:
                    print(f"Audience rating: {item.audienceRating}")
                if item.rating:
                    print(f"Critic rating: {item.rating}")
            self.print_item_info(self, item, access_token)
        elif item.TYPE in ["show"]:
            print("-" * 79)
            if self.summary is True and len(item.summary) > 1:
                print(f"{item.TYPE.capitalize()}: {item.title}\nSummary: {item.summary}")
            if self.ratings is True:
                print(f"Audience rating: {item.audienceRating}\nCritic rating: {item.rating}\nRated: {item.contentRating}")
            for episode in item.episodes():
                self.print_item_info(self, episode, access_token)

    # TODO: break this up into just search, with print being handled elsewhere
    def main(self):
        """Perform all search and print logic."""
        for r in self.account.resources():
            if r.product == "Plex Media Server":
                self.available_servers.append(r)

        for this_server in self.available_servers:
            if not this_server.presence:
                continue
            try:
                for connection in this_server.connections:
                    if connection.local:
                        continue
                    this_server_connection = PlexServer(connection.uri, this_server.accessToken)
                    relay_status = ""
                    if connection.relay:
                        if self.relay is False:
                            log.debug(f"Skipping {this_server_connection.friendlyName} relay")
                            continue
                        else:
                            relay_status = " (relay)"
                    print("\n")
                    print("=" * 79)
                    print(f'Server: "{this_server_connection.friendlyName}"{relay_status}')

                    # TODO: add flags for each media type to help sort down what is displayed (since /hub/seach?mediatype="foo" doesn't work)
                    # TODO: write handlers for each type
                    # TODO: save results to a native data structure and have different output methods (eg: json, download links, csv)
                    for item in this_server_connection.search(self.title):
                        self.print_all_items_for_server(self, item, this_server.accessToken)

            except (requests.exceptions.ConnectionError, requests.exceptions.ReadTimeout) as e:
                print(f'ERROR: connection to "{this_server.name}" failed.')
                log.debug(e)
                continue
