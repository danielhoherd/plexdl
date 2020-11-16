# plexdl

The purpose of this tool is to allow you to download non-transcoded media from Plex Media Server shares.

- <https://github.com/danielhoherd/plexdl>
- <https://quay.io/user/danielhoherd/plexdl>

## Run via Docker

```
export PLEXDL_USER=whoever
export PLEXDL_PASS=hunter2
alias plexdl='docker run --rm -e PLEXDL_USER -e PLEXDL_PASS quay.io/danielhoherd/plexdl plexdl'
plexdl $movie_title
```

## Local Installation

```
git clone https://github.com/danielhoherd/plexdl.git
pip3 install ./plexdl
```

## Usage

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
$ plexdl living
===============================================================================
Server: "demo-server-1"
-------------------------------------------------------------------------------
Movie: Night of the Living Dead
   "Night of the Living Dead.mkv" "https://...some_url..."
```

```
$ plexdl --ratings --metadata --summary living
===============================================================================
Server: "demo-server-2"
-------------------------------------------------------------------------------
Movie: Night of the Living Dead
Summary: A ragtag group of Pennsylvanians barricade themselves in an old farmhouse to remain safe from a bloodthirsty, flesh-eating breed of monsters who are ravaging the East Coast of the United States.
Audience rating: 7.7
Critic rating: 5.5
Rated: NR
(1280x672, h264, ac3, 4208kbps)
   "Night of the Living Dead.mkv" "https://...some_url..."
```

## TODO

- cleanup
- tests
- add option to search for specific types of content
- don't try to name files with characters that would be invalid
