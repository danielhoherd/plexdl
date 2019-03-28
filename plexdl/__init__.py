# -*- coding: utf-8 -*-
import logging

import requests
from plexapi.myplex import MyPlexAccount
from plexapi.server import PlexServer

logging.basicConfig(format="%(asctime)s %(levelname)s: %(message)s", datefmt="%FT%T%z", level="WARN")


class Client:
    """A client interface to plex for finding direct download URLs"""

    @staticmethod
    def print_item_info(item, access_token):
        if hasattr(item, "iterParts"):
            locations = [i for i in item.iterParts() if i]
            for location in locations:
                media_info = list()
                if item.media[0].width is not None:
                    media_info.append(f"{item.media[0].width}x{item.media[0].height}")
                if item.media[0].videoCodec is not None:
                    media_info.append(item.media[0].videoCodec)
                if item.media[0].audioCodec is not None:
                    media_info.append(item.media[0].audioCodec)
                if item.media[0].bitrate is not None:
                    media_info.append(f"{item.media[0].bitrate}kbps")
                print(f'    {item.title} ({", ".join(media_info)})')
                download_url = item._server.url(f"{location.key}?download=1&X-Plex-Token={access_token}")
                print(f'        curl -o "{item.title}.{location.container}" "{download_url}"')

    def main(self, username, password, title):
        account = MyPlexAccount(username, password)
        available_resources = list()

        for r in account.resources():
            if r.product == "Plex Media Server":
                available_resources.append(r)

        for this_resource in available_resources:
            if not this_resource.presence:
                continue
            try:
                for connection in this_resource.connections:
                    if connection.local:
                        continue
                    this_server = PlexServer(connection.uri, this_resource.accessToken)
                    relay_status = ""
                    if connection.relay:
                        relay_status = " (relay)"
                    print(
                        f'\nServer: "{this_server.friendlyName}"{relay_status}\n'
                        f'Plex version: {this_server.version}\n"'
                        f"OS: {this_server.platform} {this_server.platformVersion}"
                    )
                    for item in this_server.search(title, mediatype="movie"):
                        self.print_item_info(item, this_resource.accessToken)
            except (requests.exceptions.ConnectionError, requests.exceptions.ReadTimeout) as e:
                print(f'ERROR: connection to "{this_resource.name}" failed.')
                logging.debug(e)
                continue
