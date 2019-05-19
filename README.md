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
usage: plexdl [-h] [--debug] --username USERNAME --password PASSWORD title

Search your Plex libraries and show download URLs

positional arguments:
  title                Title to search for

optional arguments:
  -h, --help           show this help message and exit
  --debug              Enable debug output
  --username USERNAME  Your plex username
  --password PASSWORD  Your plex password
$ export PLEXDL_USER='foo'
$ export PELXDL_PASS='bar'
$ plexdl --username="${PLEXDL_USER}" --password="${PELXDL_PASS}" farm

Searching server: "Plex Cloud"
  Plex version: 1.5.2.246-1a7319ace
  OS: Cloud 0.1

Searching server: "plata"
  Plex version: 1.9.2.4285-9f65b88ae
  OS: Linux 4.10.0-22-generic (#24~16.04.1-Ubuntu SMP Tue May 23 17:03:51 UTC 2017)
    Farmer Chords mp3
        curl -o "Farmer Chords.mp3" "https://..."
    Old MacDonald Had a Farm aac
        curl -o "Old MacDonald Had a Farm.mp4" "https://..."
    Combination Squares; Farmed Shrimp; Ball Valves; String Trimmers 1280x720 h264 ac3
        curl -o "Combination Squares; Farmed Shrimp; Ball Valves; String Trimmers.mkv" "https://..."
```

# TODO

- Make this work with pipenv
- cleanup
- tests
- make search type limited to movies, maybe add option to search for specific types
- don't try to name files with characters that would be invalid
