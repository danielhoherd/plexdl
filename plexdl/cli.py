# -*- coding: utf-8 -*-
import argparse

import plexdl


def parse_args():
    parser = argparse.ArgumentParser(description='Search your Plex libraries and show download URLs')
    parser.add_argument('--debug', action='store_true', help='Enable debug output')
    parser.add_argument('--username', required=True, help='Your plex username')
    parser.add_argument('--password', required=True, help='Your plex password')
    parser.add_argument('title', help='Title to search for')
    return parser.parse_args()


def main():
    """Searches your plex account for media matching the given string, then prints out download commands."""
    args = parse_args()
    p = plexdl.Client()
    p.main(args.username, args.password, args.title)


if __name__ == '__main__':
    main()
