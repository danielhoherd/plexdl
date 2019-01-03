# -*- coding: utf-8 -*-
import logging

import requests
from plexapi.myplex import MyPlexAccount
from plexapi.server import PlexServer

logging.basicConfig(
        format='%(asctime)s %(levelname)s: %(message)s',
        datefmt='%FT%T%z',
        level='WARN',
        )


class Client:
    """A client interface to plex for finding direct download URLs"""

    @staticmethod
    def print_item_info(item, access_token):
        if hasattr(item, 'iterParts'):
            locations = [i for i in item.iterParts() if i]
            media_info = '    {}'.format(item.title)
            for location in locations:
                download_url = item._server.url('{}?download=1&X-Plex-Token={}'.format(location.key, access_token))
                if item.media[0].width is not None:
                    media_info += ' {}x{}'.format(item.media[0].width, item.media[0].height)
                if item.media[0].videoCodec is not None:
                    media_info += ' {}'.format(item.media[0].videoCodec)
                if item.media[0].audioCodec is not None:
                    media_info += ' {}'.format(item.media[0].audioCodec)
                if item.media[0].bitrate is not None:
                    media_info += ' {}kbps'.format(item.media[0].bitrate)
                print(media_info)
                print('        curl -o "{}.{}" "{}"'
                      .format(item.title,
                              location.container,
                              download_url))

    def main(self, username, password, title):
        account = MyPlexAccount(username, password)
        available_resources = list()

        for r in account.resources():
            if r.product == 'Plex Media Server':
                available_resources.append(r)

        for this_resource in available_resources:
            if not this_resource.presence:
                continue
            try:
                this_server = PlexServer(this_resource.connections[-1:][0].uri, this_resource.accessToken)
                print('\nSearching server: "{}"\n  Plex version: {}\n  OS: {} {}'
                      .format(this_server.friendlyName,
                              this_server.version,
                              this_server.platform,
                              this_server.platformVersion))
                for item in this_server.search(title, mediatype='movie'):
                    self.print_item_info(item, this_resource.accessToken)

            except requests.exceptions.ConnectionError as e:
                print('  ERROR: something went wrong with "{}"'.format(this_resource.name))
                print(e)
                pass
