import dbus


class Track:
    """
    An object representing a spotify track
    """

    def __init__(self, *args, title, artist, album, length, track_id, art_url):
        self.title: str = str(title)  # Track title
        self.artist: str = str(artist)  # Track artist
        self.album: str = str(album)  # Track album
        # Track length in seconds (rounded to 5 decimals)
        self.length: float = round(length*(10**-6), 5)
        self.id: str = str(track_id)  # Spotify track id (spotify uri)
        self.art_url: str = str(art_url)  # Spotify art url

    def __str__(self):
        return f"{self.title} - {self.artist}"

    def __repr__(self):
        items = []
        for key, value in (
            ("title", self.title), ("artist", self.artist),
            ("album", self.album), ("length", self.length),
                ("id", self.id), ("art_url", self.art_url)):
            items.append(f"{key}={repr(value)}")
        return f'Spotify.Track({",".join(items)})'


class Spotify:
    """
    A spotify dbus client object to control spotify from python
    """

    def __init__(self):
        self._bus = dbus.SessionBus()
        self._obj = self._bus.get_object(
            "org.mpris.MediaPlayer2.spotify", "/org/mpris/MediaPlayer2")
        self._spotify_iface = dbus.Interface(
            self._obj, dbus_interface="org.mpris.MediaPlayer2.Player")
        self._props_iface = dbus.Interface(
            self._obj, dbus_interface="org.freedesktop.DBus.Properties")

    def __repr__(self):
        return f"Spotify(track={repr(self.track)},state={self.state})"

    def _get_all_props(self) -> dbus.Dictionary:
        return self._props_iface.GetAll("org.mpris.MediaPlayer2.Player")

    def play(self):
        """
        Tells spotify to start playing
        """
        self._spotify_iface.Play()

    def open(self, uri: str):
        """
        Plays the specified `uri` in spotify
        """
        self._spotify_iface.OpenUri(uri)

    def play_pause(self):
        """
        Tells spotify to toggle playing
        """
        self._spotify_iface.PlayPause()

    def pause(self):
        """
        Tells spotify to pause
        """
        self._spotify_iface.Pause()

    def stop(self):
        """
        Tells spotify to stop playing
        """
        self._spotify_iface.Stop()

    def next(self):
        """
        Tells spotify to skip to the next song
        """
        self._spotify_iface.Next()

    def previous(self):
        """
        Tells spotify to skip back to the previous song
        """
        self._spotify_iface.Previous()

    @property
    def metadata(self) -> dbus.Dictionary:
        """
        Returns the raw dbus metadata
        """
        return self._get_all_props()["Metadata"]

    @property
    def track(self) -> Track:
        """
        Returns a track object containing current track data
        """
        metadata = self.metadata
        return Track(
            title=metadata["xesam:title"], artist=metadata["xesam:artist"][0],
            length=metadata["mpris:length"], track_id=metadata["mpris:trackid"],
            album=metadata["xesam:album"], art_url=metadata["mpris:artUrl"])

    @property
    def state(self) -> str:
        """
        Returns the current playback status as a string
        """
        return str(self._get_all_props()["PlaybackStatus"]).lower()
