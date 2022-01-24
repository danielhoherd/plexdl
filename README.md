# plexdl

The purpose of this tool is to allow you to download non-transcoded media from Plex Media Server shares.

- <https://github.com/danielhoherd/plexdl>
- <https://quay.io/repository/danielhoherd/plexdl>

## Run via Docker

```sh
export PLEXDL_USERNAME=whoever
export PLEXDL_PASSWORD=hunter2
alias plexdl="docker run --rm -e PLEXDL_USERNAME -e PLEXDL_PASSWORD quay.io/danielhoherd/plexdl plexdl --show-ratings"
plexdl "some movie title"
```

## Local Installation

```sh
git clone https://github.com/danielhoherd/plexdl.git
pip3 install ./plexdl
```

## Usage

```
$ plexdl --help
Usage: plexdl [OPTIONS] COMMAND [ARGS]...

  plexdl CLI.

Options:
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.

Commands:
  get-server-info  Show info about servers available to your account.
  search           Search for media in servers that are available to your...

$ plexdl get-server-info --help
Usage: plexdl get-server-info [OPTIONS] [USERNAME] [PASSWORD] [DEBUG]

  Show info about servers available to your account.

Arguments:
  [USERNAME]  [env var: PLEXDL_USERNAME]
  [PASSWORD]  [env var: PLEXDL_PASSWORD]
  [DEBUG]     [env var: PLEXDL_DEBUG;default: False]

Options:
  --help  Show this message and exit.

$ plexdl search --help
Usage: plexdl search [OPTIONS] TITLE

  Search for media in servers that are available to your account.

Arguments:
  TITLE  [env var: PLEXDL_TITLE;required]

Options:
  -u, --username TEXT  [env var: PLEXDL_USERNAME; required]
  -p, --password TEXT  [env var: PLEXDL_PASSWORD; required]
  --item-prefix TEXT   String to prefix to each item (eg: curl -o)
  --show-summary       Show media summary for each result
  --show-ratings       Show ratings for each result
  --show-metadata      Show file and codec metadata for each file in each result
  --include-relays     Output relay servers along with direct servers
  -v, --verbose
  --debug
  --help               Show this message and exit.
```

```
$ plexdl search living
===============================================================================
Server: "demo-server-1"
-------------------------------------------------------------------------------
Movie: Night of the Living Dead
   "Night of the Living Dead.mkv" "https://...some_url..."
```

```
$ plexdl search --show-ratings --show-metadata --show-summary living
===============================================================================
Server: "demo-server-2"
-------------------------------------------------------------------------------
Movie: Night of the Living Dead
Year: 1968
Studio: Image Ten
Summary: A ragtag group of Pennsylvanians barricade themselves in an old farmhouse to remain safe from a bloodthirsty, flesh-eating breed of monsters who are ravaging the East Coast of the United States.
Content rating: NR
Audience rating: 7.7
Critic rating: 5.5
(1280x672, h264, ac3, 4208kbps)
   "Night of the Living Dead.mkv" "https://...some_url..."
```

## TODO

- cleanup
- tests
- add option to search only for specific types of content
- add option to search only specific serveres
- don't try to name files with characters that would be invalid
