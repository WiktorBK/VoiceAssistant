
# Dokumentacja Asystenta Głosowego Spotify

Asystent głosowy Spotify to aplikacja zaprojektowana do sterowania odtwarzaczem Spotify za pomocą poleceń głosowych. Umożliwia użytkownikom łatwe zarządzanie odtwarzaniem muzyki, bez konieczności korzystania z interfejsu użytkownika Spotify.

## Funkcje

Asystent oferuje następujące funkcje sterowania głosowego:

- **Odtwarzanie muzyki**: Rozpocznij odtwarzanie muzyki za pomocą poleceń takich jak "wznów", "odtwórz" czy "włącz".
- **Zatrzymywanie muzyki**: Zatrzymaj odtwarzanie za pomocą poleceń "stop", "zatrzymaj" czy "wyłącz".
- **Pomijanie utworów**: Przejdź do następnego utworu za pomocą poleceń "pomiń", "przewiń", "skip", "dalej", "następna".
- **Zmiana głośności**: Dostosuj poziom głośności odtwarzania komendami "ustaw głośność", "zmniejsz głośność" czy "zwiększ głośność".
- **Informacje o aktualnie odtwarzanym utworze**: Zapytaj o aktualnie odtwarzany utwór za pomocą "jak się nazywa", "jaka to piosenka" czy "podaj nazwę".

## Jak używać asystenta na swoim komputerze

### Wymagania

Aby korzystać z asystenta, upewnij się, że spełnione są następujące wymagania:

- Python 3.x zainstalowany na komputerze.
- Zainstalowane biblioteki `speech_recognition`, `pyttsx3`, `pyaudio`.
- Konto Spotify oraz konfiguracja aplikacji na [Dashboardzie Deweloperskim Spotify](https://developer.spotify.com/dashboard/).

### Instalacja

1. Zainstaluj potrzebne biblioteki za pomocą pip:

```bash
pip install speech_recognition pyttsx3 pyaudio
```

2. Sklonuj repozytorium projektu na swój komputer lub pobierz pliki projektu.

### Konfiguracja

1. Utwórz plik konfiguracyjny `config.py` i dodaj do niego swoje poświadczenia deweloperskie Spotify (Client ID i Client Secret).

```python
SPOTIFY_CLIENT_ID = 'twoje_client_id'
SPOTIFY_CLIENT_SECRET = 'twoje_client_secret'
```

2. Skonfiguruj urządzenie wejściowe (mikrofon) w systemie, aby upewnić się, że jest poprawnie rozpoznawane przez aplikację.

### Uruchomienie

1. Otwórz terminal lub wiersz poleceń w folderze projektu.
2. Uruchom skrypt główny aplikacji:

```bash
python main.py
```

3. Po uruchomieniu aplikacji, zaczekaj na inicjalizację i zacznij używać poleceń głosowych do sterowania Spotify.

## Licencja

Określ licencję, na jakiej udostępniasz projekt.

---

Projekt jest ciągle rozwijany, a wszelkie propozycje zmian i ulepszeń są mile widziane.
