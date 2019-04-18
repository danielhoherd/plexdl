import argparse
import os
import sys

import plexdl


def parse_args():
    parser = argparse.ArgumentParser(description="Search your Plex libraries and show download URLs")
    parser.add_argument("--debug", action="store_true", help="Enable debug output")
    parser.add_argument("--username", default=os.environ.get("PLEXDL_USER", None), help="Your plex username (env PLEXDL_USER)")
    parser.add_argument("--password", default=os.environ.get("PLEXDL_PASS", None), help="Your plex password (env PLEXDL_PASS)")
    parser.add_argument("title", help="Title to search for")
    arg_parser = parser.parse_args()
    arg_parser.print_help = parser.print_help
    return arg_parser


def main():
    """Searches your plex account for media matching the given string, then prints out download commands."""
    args = parse_args()
    if args.password is None or args.username is None:
        print("Error: must provide username and password\n")
        args.print_help()
        sys.exit(1)
    p = plexdl.Client()
    try:
        p.main(args.username, args.password, args.title)
    except KeyboardInterrupt:
        sys.exit(1)


if __name__ == "__main__":
    main()
