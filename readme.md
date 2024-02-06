# Asystent Głosowy do Sterowania Spotify

Aplikacja asystenta głosowego umożliwia interakcję ze Spotify, pozwalając użytkownikom na kontrolę odtwarzania za pomocą poleceń głosowych. Wykorzystuje biblioteki `speech_recognition` i `pyttsx3` dla rozpoznawania mowy i syntezę mowy, oraz klasę `SpotifyHandler` do zarządzania interakcjami z API Spotify.

## Funkcjonalności

Aplikacja obsługuje różnorodne polecenia głosowe do zarządzania odtwarzaniem w Spotify, w tym:

- **Aktywacja**: Asystent nasłuchuje ciągle słowa aktywacyjnego "spotify", zanim zacznie przetwarzać dalsze polecenia.

- **Kontrola Odtwarzania**:
  - **Wznów Odtwarzanie**: Powiedz "wznów" lub "włącz piosenkę", aby wznowić lub rozpocząć odtwarzanie muzyki.
  - **Zatrzymaj Odtwarzanie**: Powiedz "stop", "zatrzymaj" lub "wyłącz", aby zatrzymać muzykę.
  - **Pomiń Utwór**: Powiedz "skip", "przewiń" lub "pomiń", aby przejść do następnego utworu.

- **Kontrola Głośności**:
  - Aby zmienić głośność, powiedz "ustaw głośność" i podaj pożądany poziom głośności (0-100).

- **Informacje o Aktualnym Utworze**:
  - Zapytaj "podaj nazwę", "jaka to piosenka" lub "jak się nazywa", aby asystent ogłosił nazwę aktualnego utworu i wykonawcę.

- **Tryb Prywatności**:
  - Powiedz "nie podsłuchuj mnie", aby wyłączyć asystenta.

## Jak Zacząć

1. Upewnij się, że mikrofon jest podłączony i prawidłowo skonfigurowany.
2. Uruchom aplikację. Będzie ona ciągle nasłuchiwać słowa aktywacyjnego "spotify".
3. Po aktywacji, wyraźnie wypowiedz swoje polecenie. Asystent potwierdzi akcję werbalnie za pomocą syntezatora mowy.

## Szczegóły Techniczne

- **Rozpoznawanie Mowy**: Wykorzystuje bibliotekę `speech_recognition` do konwersji wypowiedzianych słów na tekst.
- **Synteza Mowy**: Używa `pyttsx3` do werbalnego informowania użytkownika o akcjach.
- **Integracja ze Spotify**: Klasa `SpotifyHandler` zarządza wszystkimi interakcjami z API Spotify, w tym kontrolą odtwarzania, regulacją głośności i pobieraniem informacji o aktualnym utworze.

## Wymagania

- Python 3.x
- Biblioteki `speech_recognition`, `pyttsx3`, `pyaudio`
- Ważne konto deweloperskie Spotify i poświadczenia API dla `SpotifyHandler`.

## Instalacja i Konfiguracja

1. Zainstaluj wymagane biblioteki Pythona za pomocą pip.
2. Skonfiguruj `SpotifyHandler` z poświadczeniami API Spotify.
3. Upewnij się, że mikrofon jest prawidłowo ustawiony i rozpoznawany przez system.