# Voice Assistant for Spotify Control

This voice assistant application is designed to interact with Spotify, allowing users to control playback through voice commands. It leverages Python's `speech_recognition` and `pyttsx3` libraries for speech recognition and text-to-speech capabilities, respectively, alongside a custom `SpotifyHandler` class to manage Spotify API interactions.

## Features

The application supports a variety of voice commands to manage Spotify playback, including:

- **Activation**: The assistant listens continuously for the activation word "spotify" before it starts processing further commands.

- **Playback Control**:
  - **Resume Playback**: Say "wznów" or "włącz piosenkę" to resume or start playing music.
  - **Stop Playback**: Say "stop", "zatrzymaj", or "wyłącz" to stop the music.
  - **Skip Track**: Say "skip", "przewiń", or "pomiń" to skip to the next track.

- **Volume Control**:
  - To change the volume, include "ustaw głośność" followed by the desired volume level (0-100).

- **Current Track Information**:
  - Ask "podaj nazwę", "jaka to piosenka", or "jak się nazywa" to have the assistant announce the current track's name and artist.

- **Privacy Mode**:
  - Say "nie podsłuchuj mnie" to turn off the assistant.

## Usage

1. Ensure the microphone is connected and configured correctly.
2. Start the application. It will continuously listen for the activation word "spotify".
3. Once activated, speak your command clearly. The assistant will confirm the action verbally using text-to-speech.

## Technical Details

- **Speech Recognition**: Uses the `speech_recognition` library to convert spoken words into text.
- **Text-to-Speech**: Utilizes `pyttsx3` for verbal feedback to the user.
- **Spotify Integration**: The `SpotifyHandler` class handles all interactions with the Spotify API, including playback control, volume adjustments, and retrieving current track information.

## Requirements

- Python 3.x
- `speech_recognition`, `pyttsx3`, `pyaudio` libraries
- A valid Spotify Developer account and API credentials for the `SpotifyHandler`.

## Setup

1. Install the required Python libraries using pip.
2. Configure `SpotifyHandler` with your Spotify API credentials.
3. Ensure your device's microphone is properly set up and recognized by your system.

## Contributions

Contributions to the voice assistant are welcome. Feel free to fork the repository, make improvements, and submit pull requests.

## License

[Specify the license here]

---
