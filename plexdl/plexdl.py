# -*- coding: utf-8 -*-
from plexapi.myplex import MyPlexAccount
from plexapi.server import PlexServer
import requests


class client():
    """A client interface to plex for finding direct download URLs"""

    @staticmethod
    def print_item_info(item):
        if item.iterParts:
            locations = [i for i in item.iterParts() if i]
            media_info = '    {}'.format(item.title)
            for location in locations:
                download_url = item._server.url('{}?download=1'.format(location.key))
                if item.media[0].width is not None:
                    media_info += ' {}x{}'.format(item.media[0].width, item.media[0].height)
                if item.media[0].videoCodec is not None:
                    media_info += ' {}'.format(item.media[0].videoCodec)
                if item.media[0].audioCodec is not None:
                    media_info += ' {}'.format(item.media[0].audioCodec)
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
            try:
                this_server = PlexServer(this_resource.connections[-1:][0].uri, this_resource.accessToken)
                print('\nSearching server: "{}"\n  Plex version: {}\n  OS: {} {}'
                      .format(this_server.friendlyName,
                              this_server.version,
                              this_server.platform,
                              this_server.platformVersion))
                for item in this_server.search(title, mediatype='movie'):
                    self.print_item_info(item)

            except requests.exceptions.ConnectionError as e:
                print('  ERROR: something went wrong with "{}"'.format(this_server.friendlyName))
                print(e)
                pass

            except:
                raise
