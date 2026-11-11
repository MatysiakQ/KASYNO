# KASYNO — backend strony

Branch `backend/site-foundation` obejmuje backend Łukasza i infrastrukturę. Nie zawiera zasad ruletki, automatu, losowania wyników ani kodu frontendu.

## Start lokalny

Wymagane Docker i Docker Compose v2:

```bash
cp .env.example .env
docker compose up --build -d --wait
```

API: http://localhost:8000/docs. Schemat: http://localhost:8000/openapi.json.
Migracje wykonuje osobny kontener przed startem API. Lokalne dane demonstracyjne połączenia nie nadają się na serwer publiczny.

## Działające funkcje

- `POST /api/v1/auth/register` — JSON email, password (12–128 znaków).
- `POST /api/v1/auth/login` — ten sam JSON; zwraca losowy token Bearer ważny domyślnie godzinę.
- `POST /api/v1/auth/logout` — unieważnia bieżący token.
- `GET /api/v1/users/me` — dane zalogowanego użytkownika.
- `GET /health/live` i `/health/ready` — stan procesu i połączenia z bazą.

Do chronionych endpointów przekazuj `Authorization: Bearer <access_token>`. Token przechowuj w pamięci frontendu; odświeżenie strony wymaga ponownego logowania. Brak refresh tokenów i cookies. Baza zawiera tylko SHA-256 tokena i hasło haszowane Argon2. Sesje mają stały czas ważności i sprawdzają aktywność konta.

## Zakres i ograniczenia

To fundament do pracy zespołu, nie gotowy system produkcyjny. Płatności, portfel i panel admina mają tylko katalogi z opisem planowanej integracji. Nie wykonują transakcji i nie przyjmują pieniędzy.

Przed publicznym uruchomieniem trzeba dodać rozproszony limit prób logowania/rejestracji, weryfikację emaila, odzyskiwanie konta, role administratorów, czyszczenie wygasłych sesji i audyt działań. Brak automatycznej dezaktywacji kont. Nie wdrażać publicznie bez tych prac. Plik produkcyjny jest szablonem środowiska do skonfigurowania.

## Podział kodu

- Łukasz: `backend/app/modules/auth`, `users`, przyszłe `payments`, `infra`, CI.
- Kacper: uzgadnianie modeli i wspólnej historii `backend/migrations`.
- Dzeju: późniejszy moduł gier; korzysta ze wspólnego `get_current_user`, bez osobnego uwierzytelniania.
- Adam: `frontend` i dokumentacja projektu.
- Właściciel implementacji portfela oraz kontrakt rozliczeń: do wspólnego ustalenia.

Instrukcje: [praca lokalna](docs/local-development.md), [wdrażanie](docs/deployment.md), [backup](docs/backup-restore.md).
