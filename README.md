The purpose of this tool is to allow you to download non-transcoded media from Plex Media Server shares.

# Installation

```
git clone https://github.com/danielhoherd/plexdl.git
pipsi install --editable .  # --editable is only useful for developing
```

# Usage

```
$ plexdl --help
Usage: plexdl [OPTIONS] TITLE

  Searches your plex account for media matching the given string, then
  prints out download commands.

Options:
  --username TEXT  Your plex username  [required]
  --password TEXT  Your plex password  [required]
  --help           Show this message and exit.
$ export PLEXDL_USER='foo'
$ export PELXDL_PASS='bar'
$ plexdl farm

Searching server: "Plex Cloud"
  Plex version: 1.5.2.246-1a7319ace
  OS: Cloud 0.1

Searching server: "plata"
  Plex version: 1.9.2.4285-9f65b88ae
  OS: Linux 4.10.0-22-generic (#24~16.04.1-Ubuntu SMP Tue May 23 17:03:51 UTC 2017)
    Farmer Chords NonexNone None
        curl -o "Farmer Chords.mp3" "https://..."
    Old MacDonald Had a Farm NonexNone None
        curl -o "Old MacDonald Had a Farm.mp4" "https://..."
    Combination Squares; Farmed Shrimp; Ball Valves; String Trimmers 1280x720 h264
        curl -o "Combination Squares; Farmed Shrimp; Ball Valves; String Trimmers.mkv" "https://..."
```

# TODO

- cleanup
- tests
- make search type limited to movies, maybe add option to search for specific types
- make this only use python3 because unicode
- don't try to print resolution for non-movie files
- don't try to name files with characters that would be invalid
