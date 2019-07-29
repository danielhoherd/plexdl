The purpose of this tool is to allow you to download non-transcoded media from Plex Media Server shares.

- <https://github.com/danielhoherd/plexdl>
- <https://hub.docker.com/r/danielhoherd/plexdl>

# Run via Docker

```
export PLEXDL_USER=whoever
export PLEXDL_PASS=hunter2
alias plexdl='docker run --rm -e PLEXDL_USER -e PLEXDL_PASS danielhoherd/plexdl plexdl'
plexdl <movie_name>
```

# Local Installation

```
git clone https://github.com/danielhoherd/plexdl.git
pip3 install ./plexdl
```

# Usage

```
$ plexdl --help
Usage: plexdl [OPTIONS] TITLE

  Searches your plex account for media matching the given string, then
  prints out download commands.

Options:
  -v                              Increase verbosity (max -vvvv)
  -u, --username TEXT             Your Plex username (env PLEXDL_USER)
  -p, --password TEXT             Your Plex password (env PLEXDL_PASS)
  -r, --relay / --no-relay        Output relay servers along with direct
                                  servers
  --item-prefix TEXT              String to prefix to each item (eg: curl -o)
  --server-info / --no-server-info
                                  Output summary about each server
  --summary / --no-summary        Output summary about each result
  --ratings / --no-ratings        Output rating information for each result
  --metadata / --no-metadata      Output media metadata about each file for
                                  each result
  --help                          Show this message and exit.$ export PLEXDL_USER='foo'
```
```
$ plexdl automobile
===============================================================================
Server: "demo-server-1"
-------------------------------------------------------------------------------
Movie: Planes, Trains and Automobiles
   "Planes, Trains and Automobiles.mkv" "https://...some_url..."
```
```
$ plexdl --ratings --metadata --summary flower
===============================================================================
Server: "demo-server-2"
-------------------------------------------------------------------------------
Movie: Back to the Future: Part II
Summary: After visiting 2015, Marty McFly must repeat his visit to 1955 to prevent disastrous changes to 1985... without interfering with his first trip.
Audience rating: 8.5
Critic rating: 6.3
Rated: PG
(1280x688, h264, ac3, 4005kbps)
   "Back to the Future: Part II.mp4" "https://...some_url..."
-------------------------------------------------------------------------------
Movie: Back to the Future
Summary: A teenager is accidentally sent 30 years into the past in a time-traveling DeLorean invented by his friend, Dr. Emmett Brown, and must make sure his high-school-age parents unite in order to save his own existence.
Audience rating: 9.4
Critic rating: 9.6
Rated: PG
(1280x688, h264, ac3, 5043kbps)
   "Back to the Future.mp4" "https://...some_url..."
```

# TODO

- cleanup
- tests
- add option to search for specific types of content
- don't try to name files with characters that would be invalid
