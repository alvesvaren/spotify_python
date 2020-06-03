# Spotify python

Control your spotify client using an easy-to-use dbus interface for python 3!

Disclaimer: This only works on DBus-enabled systems, like most linux distrubutions.

## Usage

```python
>>> from spotify import Spotify
>>> spotify = Spotify()
>>> print(spotify.track)
some song - an artist
>>> spotify.next()
```

## Installation
```bash
$ pip install git+https://github.com/alvesvaren/spotify_python
```
