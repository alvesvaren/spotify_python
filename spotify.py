import dbus





class Spotify:
    """
    A spotify dbus client object to control spotify from python.
    """

    class Track:
        """
        An object representing a spotify track
        """
        def __init__(self, *args, title, artist, art_uri=None):
            self.title = str(title)
            self.artist = str(artist)
            self.art_uri = str(art_uri) if art_uri else art_uri
        
        def __str__(self):
            return f"{self.title} - {self.artist}"
        
        def __repr__(self):
            return f'Spotify.Track(title={repr(self.title)},artist={repr(self.artist)},art_uri={repr(self.art_uri)})'

    def __init__(self):
        self._bus = dbus.SessionBus()
        self._obj = self._bus.get_object(
            "org.mpris.MediaPlayer2.spotify", "/org/mpris/MediaPlayer2")
        self._spotify_iface = dbus.Interface(
            self._obj, dbus_interface="org.mpris.MediaPlayer2.Player")
        self._props_iface = dbus.Interface(
            self._obj, dbus_interface="org.freedesktop.DBus.Properties")
    
    def __repr__(self):
        return f"Spotify(track={repr(self.track)})"

    def get_metadata(self) -> dbus.Dictionary:
        """
        Returns the raw dbus metadata.
        """
        return self._props_iface.GetAll("org.mpris.MediaPlayer2.Player")["Metadata"]

    def play(self):
        """
        Tells spotify to start playing.
        """
        self._spotify_iface.Play()

    def play_pause(self):
        """
        Tells spotify to toggle playing.
        """
        self._spotify_iface.PlayPause()

    def pause(self):
        """
        Tells spotify to pause.
        """
        self._spotify_iface.Pause()

    def stop(self):
        """
        Tells spotify to stop playing.
        """
        self._spotify_iface.Stop()

    @property
    def track(self) -> Track:
        """
        Returns a track object containing current track data.
        """
        metadata = self.get_metadata()
        return self.Track(title=metadata["xesam:title"], artist=metadata["xesam:artist"][0])


if __name__ == "__main__":
    spotify = Spotify()
    print("Currently playing:", spotify.track)
