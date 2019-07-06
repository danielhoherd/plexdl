import logging

import requests
from plexapi.myplex import MyPlexAccount
from plexapi.server import PlexServer

log = logging.getLogger("plexdl")


class Client(object):
    """A client interface to plex for finding direct download URLs"""

    def __init__(self, **kwargs):
        self.username = kwargs["username"]
        self.password = kwargs["password"]
        self.title = kwargs["title"]
        self.relay = kwargs["relay"]
        self.debug = kwargs["debug"]
        self.account = MyPlexAccount(self.username, self.password)

    available_servers = []

    @staticmethod
    def print_item_info(self, item, access_token):
        if hasattr(item, "iterParts"):
            locations = [i for i in item.iterParts() if i]
            for location in locations:
                media_info = []
                if self.debug > 0:
                    if item.media[0].width is not None:
                        media_info.append(f"{item.media[0].width}x{item.media[0].height}")
                    if item.media[0].videoCodec is not None:
                        media_info.append(item.media[0].videoCodec)
                    if item.media[0].audioCodec is not None:
                        media_info.append(item.media[0].audioCodec)
                    if item.media[0].bitrate is not None:
                        media_info.append(f"{item.media[0].bitrate}kbps")
                if len(media_info) > 0:
                    print(f'({", ".join(media_info)})')
                download_url = item._server.url(f"{location.key}?download=1&X-Plex-Token={access_token}")
                print(f'        curl -o "{item.title}.{location.container}" "{download_url}"')

    @staticmethod
    def print_all_items_for_server(self, item, access_token):
        if item.TYPE in ["movie", "track"]:
            print("-" * 79)
            print(f"{item.TYPE.capitalize()}: {item.title}")
            if len(item.summary) > 1:
                print(f"Summary: {item.summary}")
            self.print_item_info(self, item, access_token)
        if item.TYPE in ["show"]:
            print("-" * 79)
            print(f"{item.TYPE.capitalize()}: {item.title}\nSummary: {item.summary}")
            for item in item.episodes():
                self.print_item_info(self, item, access_token)

    def main(self):
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
                    print(
                        f'Server: "{this_server_connection.friendlyName}"{relay_status}\n'
                        f'Plex version: {this_server_connection.version}\n"'
                        f"OS: {this_server_connection.platform} {this_server_connection.platformVersion}"
                    )

                    # TODO: add flags for each media type to help sort down what is displayed (since /hub/seach?mediatype="foo" doesn't work)
                    # TODO: write handlers for each type
                    # TODO: save results to a native data structure and have different output methods (eg: json, download links, csv)
                    for item in this_server_connection.search(self.title):
                        self.print_all_items_for_server(self, item, this_server.accessToken)

            except (requests.exceptions.ConnectionError, requests.exceptions.ReadTimeout) as e:
                print(f'ERROR: connection to "{this_server.name}" failed.')
                log.debug(e)
                continue
