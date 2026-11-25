# Wstępna dokumentacja projektu

## Nazwa projektu

**KASYNO** — robocza nazwa aplikacji.

## Pomysł i krótki opis aplikacji

Projekt zakłada stworzenie internetowej aplikacji kasynowej obejmującej ruletkę i automat do gry. Użytkownicy będą mogli założyć konto, logować się, korzystać z salda i historii rozgrywek. Aplikacja ma również uwzględniać płatności oraz panel administracyjny ze statystykami i historią aktywności użytkowników.

Saldo i stawki będą prowadzone w złotych polskich, natomiast łączna suma wygranych prezentowana w profilu gracza będzie pokazywana w pesos. Wyniki gier i rozliczanie salda będą obsługiwane przez serwer.

## Uczestnicy projektu i podział funkcji

| Osoba | Funkcja | Zakres odpowiedzialności |
|---|---|---|
| Adam | Frontend, animacje, kierownik projektu (PM/TM) | Interfejs użytkownika, animacje, koordynacja projektu, dokumentacja i prezentacja |
| Łukasz | Backend, DevOps | Backend w FastAPI, sesje, logowanie, płatności, Docker, konfiguracja serwera i wdrażanie na prywatnym serwerze |
| Dzeju | Backend | Ruletka, automat i logika gier |
| Kacper | Baza danych | Model i obsługa bazy danych, historia, logi i statystyki |
| Wspólne | Prezentacja | Przygotowanie i przeprowadzenie prezentacji przez zespół |

### Pozostałe czynności

Testowanie funkcji oraz weryfikacja wdrożenia po większych zmianach będą realizowane przez każdego członka zespołu.

**Kontakt do kierownika projektu:** Adam — ajastrzebski2104@gmail.com

## Narzędzia do współpracy

- **Komunikacja:** Discord i Messenger.
- **Zadania i śledzenie postępu:** GitHub Issues oraz gotowa tablica GitHub Projects.
- **Kod i przegląd zmian:** GitHub, gałęzie i pull requesty.

## Miejsce uruchomienia aplikacji

Aplikacja będzie uruchamiana na prywatnym serwerze zespołu, w kontenerach Docker wraz z bazą PostgreSQL. Backend jest rozwijany w FastAPI. Łukasz odpowiada za konfigurację serwera i wdrażanie aplikacji. Członkowie zespołu mogą uruchamiać projekt lokalnie lub korzystać ze wspólnej wersji na serwerze.
