import dbus

class Spotify:
    def __init__(self):
        self._bus = dbus.SessionBus()
        self._obj = self._bus.get_object("org.mpris.MediaPlayer2.spotify","/org/mpris/MediaPlayer2")
        self._spotify_iface = dbus.Interface(self._obj, dbus_interface="org.mpris.MediaPlayer2.Player")
        self._props_iface = dbus.Interface(self._obj, dbus_interface="org.freedesktop.DBus.Properties")

    def get_metadata(self) -> dbus.Dictionary:
        return self._props_iface.GetAll("org.mpris.MediaPlayer2.Player")["Metadata"]

    def play(self):
        self._spotify_iface.Play()

    def play_pause(self):
        self._spotify_iface.PlayPause()

    def pause(self):
        self._spotify_iface.Pause()

    def stop(self):
        self._spotify_iface.Stop()

    @property
    def track(self) -> tuple:
        metadata = self.get_metadata()
        return str(metadata["xesam:title"]), str(metadata["xesam:artist"][0])
    
    @property
    def art_uri(self):
        return self.get_metadata()["mpris:artUrl"]


if __name__ == "__main__":
    spotify = Spotify()
    print("Currently playing:", spotify.track[0], "-", spotify.track[1])
