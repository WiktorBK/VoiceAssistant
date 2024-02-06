import spotipy
from spotipy.oauth2 import SpotifyOAuth

from credentials import *

class SpotifyHandler:

    def __init__(self):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope="app-remote-control user-read-playback-state user-modify-playback-state"))

    # Włącz/wznów odtwarzanie
    def play_music(self):
        try:
            self.sp.start_playback()
            return "Wznawiam odtwarzanie"
        except spotipy.SpotifyException as e:
            return "Brak dostępnych urządzeń, włącz aplikację Spotify i spróbuj ponownie"

    # zatrzymaj odtwarzanie
    def stop_music(self):
        try:
            self.sp.pause_playback()
            return "Zatrzymuje piosenkę."
        except spotipy.SpotifyException as e:
            return "Brak dostępnych urządzeń, włącz aplikację Spotify i spróbuj ponownie"

    # pomiń piosenkę
    def skip_track(self):
        try:
            self.sp.next_track()
            return "Pomijam piosenkę"
        except spotipy.SpotifyException as e:
            return "Brak dostępnych urządzeń, włącz aplikację Spotify i spróbuj ponownie"
        
    # przejdź do poprzedniej piosenki
    def skip_to_previous_track(self):
        try:
            self.sp.previous_track()
            return "Cofam do poprzedniej piosenki"
        except spotipy.SpotifyException as e:
             return "Brak dostępnych urządzeń, włącz aplikację Spotify i spróbuj ponownie"

    # zwraca id dostępnych urządzeń
    def get_devices_ids(self):
        try:
            devices = self.get_devices()
            return [devices['devices'][i]['id'] for i in range(len(devices))]
        except IndexError as e:
            return "No devices"

    # zwraca informajce o dostępnych urządzeniach
    def get_devices(self):
        return self.sp.devices()

    # zmienia głośność odtwarzania
    def change_volume(self, volume):
        try:   
            self.sp.volume(int(volume))
        except ValueError as e:
            pass

    # zwraca informacje o aktualnie odtwarzanym utworze
    def get_current_song(self):
        current_track=self.sp.current_playback()
        if current_track  and 'item' in current_track:
            return current_track['item']['name'], current_track['item']['artists'][0]['name']
        else:
            return "Nie mogę zidentyfikować utworu"

    # zwraca obecną głośność
    def get_current_volume(self):    
        current_playback = self.sp.current_playback()
        if current_playback:
            volume_percent = current_playback['device']['volume_percent']
            return volume_percent

    # zmniejsza głośność o jakąś wartość
    def turn_volume_down(self, value):
        try:
            value=int(value)
            current_volume=self.get_current_volume()
            new_volume=current_volume-value
            if new_volume < 0: new_volume=0
            if current_volume: self.change_volume(new_volume)
        except ValueError as e:
            pass

    # zwiększa głoścność o jakąś wartość
    def turn_volume_up(self, value):
        try:
            value=int(value)
            current_volume=self.get_current_volume()
            new_volume=current_volume-value
            if new_volume>100: new_volume=110
            if current_volume: self.change_volume(100)
        except ValueError as e:
            pass

    


    