from . import Spotify

if __name__ == "__main__":
    spotify = Spotify()
    print("Currently playing:", spotify.track)
