# Praca lokalna

Uruchomienie całego środowiska opisuje README. Po zmianach: `docker compose up --build -d --wait`.
Zatrzymanie: `docker compose down`. Dodanie `-v` usuwa lokalną bazę — nie używaj tego na serwerze.

Do pracy poza kontenerem zainstaluj uv i Python 3.14, następnie:

```bash
cd backend
uv sync --frozen
uv run ruff check .
uv run ruff format --check .
uv run mypy app
uv run pytest
```

Testy lokalne domyślnie używają SQLite. Pełne testy CI korzystają z osobnej bazy PostgreSQL. `TEST_DATABASE_URL` może wskazywać WYŁĄCZNIE pustą, dedykowaną bazę testową: testy tworzą i usuwają tabele. Nie podawaj produkcyjnego URL.

Do uruchomienia API poza Dockerem ustaw DATABASE_URL na lokalny port PostgreSQL, wykonaj `uv run alembic upgrade head`, potem `uv run uvicorn app.main:app --reload`.

Nowe migracje: uzgodnij model z Kacprem, zaimportuj model w migrations/env.py i wykonaj `uv run alembic revision --autogenerate -m opis`; przejrzyj wynik przed commitem. Repozytoria danych nie wykonują commitów — transakcją zarządza service.py.

Sekretów nie commitujemy. Dodając endpointy gier Dzeju importuje CurrentUser z app.modules.auth.dependencies. Logika gier nie wchodzi w zakres tego brancha.
