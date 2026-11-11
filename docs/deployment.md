# Wdrożenie — szablon do skonfigurowania

Nie uruchomiono wdrożenia ani nie skonfigurowano prywatnego serwera. Najpierw uzupełnij zabezpieczenia wymienione w README i uzyskaj zielone CI. Workflow deploy.yml tylko publikuje obraz po ręcznym uruchomieniu; nie wdraża na serwer.

Na serwerze przygotuj Docker Compose v2 i plik środowiska poza repozytorium z uprawnieniami 600. Ustaw POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB, DATABASE_URL (host postgres), CORS_ORIGINS (JSON z dokładnym adresem frontendu HTTPS), DOMAIN oraz BACKEND_IMAGE (obraz z tagiem SHA commita). Znaki specjalne hasła w DATABASE_URL wymagają kodowania URL. Nie używaj lokalnych haseł z przykładu.

DNS domeny musi wskazywać serwer; otwórz porty 80/443. Caddy obsługuje HTTPS. PostgreSQL i API nie mają publicznie mapowanych portów. Obrazy bazowe mają tagi wersji; przed produkcją przypnij również digesty i zaplanuj aktualizacje bezpieczeństwa.

Uruchom `DEPLOY_ENV_FILE=/pełna/ścieżka/server.env bash infra/scripts/deploy.sh` z katalogu repozytorium. Skrypt pobiera obrazy, uruchamia bazę, wykonuje migrację jednorazowo i sprawdza healthcheck backendu. Następnie ręcznie sprawdź HTTPS i logowanie. Aktualizację istniejącej bazy poprzedź backupem.

Rollback aplikacji: ustaw BACKEND_IMAGE na poprzedni SHA tylko jeśli pozostaje zgodny ze schematem, ponownie uruchom backend. Nie uruchamiaj automatycznego downgrade bazy przy błędzie. Migracje destrukcyjne wymagają osobnego planu; stosuj zmiany zgodne ze starą i nową wersją aplikacji.

Monitorowanie, harmonogram backupów, przechowywanie kopii poza serwerem, alerty, rotacja sekretów i zdalne wdrożenia pozostają do skonfigurowania. Wygasłe sesje wymagają okresowego usuwania, bez zmieniania historii finansowej.
