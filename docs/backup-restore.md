# Kopie i odtwarzanie

`DEPLOY_ENV_FILE=/pełna/ścieżka/server.env bash infra/scripts/backup.sh` zapisuje dump PostgreSQL w formacie custom. Domyślny katalog backups jest ignorowany przez Git. Nieudana kopia nie jest oznaczana jako gotowa.

Skrypt nie ustawia harmonogramu, retencji, szyfrowania ani transferu poza serwer: skonfiguruj je przed użyciem produkcyjnym.

Test odtworzenia: utwórz oddzielną, pustą bazę PostgreSQL, ustaw RESTORE_DATABASE_URL, uruchom `bash infra/scripts/restore.sh /ścieżka/kopia.dump`. Narzędzie pg_restore musi być w PATH. Skrypt nie kasuje bazy i zatrzymuje się przy błędzie. Po odtworzeniu sprawdź migracje, liczbę użytkowników i działanie aplikacji w izolowanym środowisku. Nigdy nie testuj odtwarzania na produkcyjnej bazie.
