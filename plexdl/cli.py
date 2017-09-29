# -*- coding: utf-8 -*-
import click
import plexdl


@click.command()
@click.option('--username', envvar='PLEXDL_USER',
              required=True, help='Your plex username')
@click.option('--password', envvar='PLEXDL_PASS',
              required=True, help='Your plex password')
@click.argument('title')
def main(username, password, title):
    """Searches your plex account for media matching the given string, then prints out download commands."""
    p = plexdl.client()
    p.main(username, password, title)


if __name__ == '__main__':
    main()
