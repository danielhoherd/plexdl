# -*- coding: utf-8 -*-
import click
import plexdl


@click.command()
@click.option('--username', envvar='PLEXDL_USER',
              required=True, help='Your plex username')
@click.option('--password', envvar='PLEXDL_PASS',
              required=True, help='Your plex password')
@click.argument('movie')
def main(username, password, movie):
    """Prints out a direct download URL for the given media"""
    p = plexdl.client()
    p.main(username, password, movie)


if __name__ == '__main__':
    main()
