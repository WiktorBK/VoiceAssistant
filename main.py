import speech_recognition as sr
import pyttsx3 as tts
import time

from spotifyhandler import SpotifyHandler
from config import *

class VoiceAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.mic = sr.Microphone()
        self.engine = tts.init()
        self.engine.setProperty('rate', 150)
        self.spoti = SpotifyHandler()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        with self.mic as source:
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
        try:
            command = self.recognizer.recognize_google(audio, language="pl-PL").lower()
            print(f"Powiedziałeś/aś: {command}")
            return command
        except sr.UnknownValueError:
            pass
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        return ""

    def announce_current_track(self):
        current_volume = self.spoti.get_current_volume()
        self.spoti.turn_volume_down(int(current_volume * 0.5))
        track_info = self.spoti.get_current_song()
        with open("piosenki.txt", "a") as f: 
            f.write(f"{track_info[0]}, {track_info[1]}")
        self.speak(f"{track_info[0]}, {track_info[1]}")
        self.spoti.change_volume(current_volume)

    def execute_command(self, command):
        action_map = {
            'play': (self.spoti.play_music, play_prompts),
            'stop': (self.spoti.stop_music, stop_prompts),
            'skip': (self.spoti.skip_track, skip_prompts),
            'change_volume': (lambda value: self.spoti.change_volume(value), volume_prompts),
            'track_info': (self.announce_current_track, current_track_prompts),
            'volume_down': (lambda value: self.spoti.turn_volume_down(value), volume_down_prompts),
            'volume_up': (lambda value: self.spoti.turn_volume_up(value), volume_up_prompts),
        }

        for action, (func, prompts) in action_map.items():
            if any(prompt in command for prompt in prompts):
                if 'volume' in action:
                    volume_value = command.split()[-1]
                    func(volume_value)
                else:
                    result = func()
                    if result: self.speak(result)
                return True

        if "nie podsłuchuj mnie" in command:
            self.speak("Rozumiem, wyłączam się.")
            return False

        return True

    def start(self):
        while True:
            time.sleep(0.5)
            command = self.listen()
            if activation_word in command and not self.execute_command(command):
                break

if __name__ == "__main__":
    assistant = VoiceAssistant()
    assistant.start()
