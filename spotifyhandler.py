import spotipy
from spotipy.oauth2 import SpotifyOAuth
from credentials import *

class SpotifyHandler:

    def __init__(self):

        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope="app-remote-control user-read-playback-state user-modify-playback-state"))


    def play_music(self):
        self.sp.start_playback()


    def stop_music(self):
        self.sp.pause_playback()


    def skip_track(self):
        self.sp.next_track()

