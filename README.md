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
  -v                        Increase verbosity (max -vvvv)
  -u, --username TEXT       Your Plex username (env PLEXDL_USER)
  -p, --password TEXT       Your Plex password (env PLEXDL_PASS)
  -r, --relay / --no-relay  Output relay servers along with direct servers
  --help                    Show this message and exit.
$ export PLEXDL_USER='foo'
$ export PELXDL_PASS='bar'
===============================================================================
Server: "demo-server"
Plex version: 1.16.1.1246-1d09ac057
"OS: Linux 3.16.0-4-amd64
-------------------------------------------------------------------------------
Show: Planet Earth II
Summary: David Attenborough presents a documentary series exploring how animals meet the challenges of surviving in the most iconic habitats on earth.


        curl -o "Islands.mkv" "https://127-0-0-1.0123456789abcd...
        curl -o "Mountains.mkv" "https://127-0-0-1.0123456789abcd...
        curl -o "Jungles.mkv" "https://127-0-0-1.0123456789abcd...
        curl -o "Deserts.mkv" "https://127-0-0-1.0123456789abcd...
        curl -o "Grasslands.mkv" "https://127-0-0-1.0123456789abcd...
        curl -o "Cities.mkv" "https://127-0-0-1.0123456789abcd...
-------------------------------------------------------------------------------
Movie: The Man from Earth
Summary: An impromptu goodbye party for Professor John Oldman becomes a mysterious interrogation after the retiring scholar reveals to his colleagues he never ages and has walked the earth for 14,000 years.
        curl -o "The Man from Earth.avi" "https://127-0-0-1.0123456789abcd...
-------------------------------------------------------------------------------
Movie: Journey to the Center of the Earth
Summary: An Edinburgh professor and assorted colleagues follow an explorer's trail down an extinct Icelandic volcano to the earth's center.
        curl -o "Journey to the Center of the Earth.mp4" "https://127-0-0-1.0123456789abcd...
```

# TODO

- cleanup
- tests
- add option to search for specific types of content
- don't try to name files with characters that would be invalid
