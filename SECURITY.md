# Bezpieczeństwo

KASYNO jest projektem z wirtualną walutą. Nie umieszczaj w repozytorium haseł, tokenów, kluczy API ani danych użytkowników.

## Zgłaszanie problemów

Nie publikuj szczegółów exploita w otwartym issue. Skontaktuj się prywatnie z właścicielem repozytorium i podaj opis, sposób odtworzenia oraz potencjalny wpływ.

## Minimalne wymagania

- walidacja danych wejściowych po stronie backendu,
- brak ujemnego salda,
- transakcje i blokady przy rozliczaniu rund,
- idempotencja żądań rozliczających,
- bezpieczne przechowywanie sekretów poza repozytorium,
- logowanie bez haseł i tokenów.
