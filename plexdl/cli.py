import logging
import os
import sys

import plexapi
from click import argument
from click import command
from click import option

import plexdl

# def main():
#     """Searches your plex account for media matching the given string, then prints out download commands."""
#     args = parse_args()
#     if args.password is None or args.username is None:
#         sys.exit("Error: must provide username and password")
#     p = plexdl.Client()
#     try:
#         p.main(**args.__dict__)
#     except KeyboardInterrupt:
#         sys.exit(1)
# if __name__ == "__main__":
#     main()


def get_logger(ctx, param, value):
    logging.basicConfig(format="%(asctime)s %(levelname)s: %(message)s", datefmt="%FT%T%z")
    log = logging.getLogger("plexdl")
    log.setLevel(50 - (value * 10))  # https://docs.python.org/3.7/library/logging.html#logging-levels


@command()
@option("-v", count=True, help="Increase verbosity (max -vvvv)", callback=get_logger)
@option("-u", "--username", help="Your Plex username (env PLEXDL_USER)", envvar="PLEXDL_USER")
@option("-p", "--password", help="Your Plex password (env PLEXDL_PASS)", envvar="PLEXDL_PASS")
@option("-r", "--relay/--no-relay", default=False, help="Output relay servers along with direct servers")
@argument("title", default="robot")
def main(v, relay, username, password, title):
    """Searches your plex account for media matching the given string, then prints out download commands."""
    p = plexdl.Client()
    try:
        p.main(username=username, password=password, title=title, relay=relay)
    except KeyboardInterrupt:
        sys.exit(1)
    except plexapi.exceptions.BadRequest:
        sys.exit(2)


if __name__ == "__main__":
    main()
