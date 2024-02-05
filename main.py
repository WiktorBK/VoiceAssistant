import speech_recognition as sr
import pyttsx3 as tts
import pyaudio
from spotifyhandler import SpotifyHandler
import time

recognizer = sr.Recognizer()
mic = sr.Microphone()
engine=tts.init()
engine.setProperty('rate', 150)

spoti=SpotifyHandler()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    print("Czekam na komendę...")
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio, language="pl-PL").lower()
        print("Powiedziałeś/aś: " + command)
        return command
    except sr.UnknownValueError:
        print("Nie mogłem zrozumieć :(")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    return ""

def main_loop():
    activation_word = "spotify"
    while True:
        time.sleep(0.3)
        command = listen()
        if activation_word in command:
            if 'wznów' in command or 'włącz piosenkę' in command:
                speak("Wznawiam odtwarzanie utworu")
                spoti.play_music()
            elif 'stop' in command or 'zatrzymaj' in command:
                speak("Zatrzymuje utwór")
                spoti.stop_music()
            elif 'skip' in command or 'przewiń' in command or 'pomiń' in command:
                speak("Pomijam utwór")
                spoti.skip_track()
            elif "nie podsłuchuj mnie" in command:
                speak("Rozumiem, wyłączam się.")
                break
        else:
            print("Czekam na komendę...")

if __name__ == "__main__":
    main_loop()

