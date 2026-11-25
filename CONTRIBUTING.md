# Współpraca przy projekcie

## Zanim zaczniesz

1. Wybierz issue ze statusu `Ready` na tablicy.
2. Sprawdź kryteria akceptacji i zależności.
3. Przypisz issue sobie i utwórz krótką gałąź, np. `feat/roulette-bets` albo `fix/wallet-race-condition`.
4. Jeśli zakres jest niejasny, dopisz komentarz do issue zamiast zgadywać.

## Pull Request

- PR powinien realizować jedno spójne issue.
- Opis musi zawierać sposób testowania i ewentualne migracje.
- Nie zatwierdzamy własnego PR bez review drugiej osoby.
- `Done` oznacza merge do `main`, nie samo zakończenie pracy lokalnej.

## Zasady domenowe

- Wynik gry zawsze rozstrzyga backend.
- Frontend nie jest źródłem prawdy dla salda, zakładu ani wypłaty.
- Każda zmiana portfela musi być atomowa i audytowalna.
- Nie dodajemy prawdziwych płatności bez osobnej decyzji zakresowej i analizy prawnej.
