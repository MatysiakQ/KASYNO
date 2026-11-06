# Baza wiedzy projektu KASYNO

Dokument zbiera ustalenia i pomysły zapisane w notatniku podczas rozmowy projektowej. Elementy oznaczone jako „do ustalenia” wymagają dalszej decyzji zespołu.

## 1. Zakres gier

### Ruletka

- Ruletka.
- Wynik rozstrzygany przez serwer.
- Wynik pojawia się od razu, z animacją.
- Można obstawiać kilka zakładów.
- Przy nieprawidłowym zakładzie zakład zostaje anulowany i pojawia się błąd, zależnie od sytuacji.
- Mnożnik dla zera: `x14`.
- Do ustalenia:
  - dokładne rodzaje zakładów,
  - wypłaty,
  - zasady anulowania zakładu.

### Automat do gry

- Wstępnie układ `3 x 3`.
- W przyszłości może być możliwość wyboru układu.
- Stawka podstawowa: `0,20 gr`.
- Stawka maksymalna: `100 000 zł`.
- Symbole: do ustalenia.
- Tabela wypłat: do ustalenia.
- Automat będzie posiadał animację.
- Planowany jest tryb turbo.
- Wynik będzie generowany przez własny algorytm.

### Dodatkowe gry

- Blackjack — pomysł do rozważenia w późniejszym etapie.

## 2. Użytkownik i konta

### Konto użytkownika

- Użytkownik zakłada konto.
- Logowanie odbywa się za pomocą adresu poczty elektronicznej i hasła.
- Użytkownik może się wylogować.
- Użytkownik może mieć ustawienia konta.
- Konto ma status aktywności, na przykład `is_active`.
- Jeżeli użytkownik przez określony czas się nie loguje, jego konto przechodzi w stan nieaktywny.
- Nieaktywne konto trzeba odnowić.
- Do ustalenia:
  - po jakim czasie konto staje się nieaktywne,
  - jak wygląda odnowienie konta,
  - po jakim czasie usuwane są dane nieaktywnego konta.

### Profil użytkownika

W profilu mogą znajdować się:

- adres poczty elektronicznej,
- numer telefonu,
- narodowość,
- płeć,
- dane powiązane z płatnościami,
- status konta,
- historia gier,
- historia płatności,
- historia zmian salda.

Za pełne uzupełnienie profilu, w tym narodowości i numeru telefonu, użytkownik otrzymuje dodatkowe `5%` do depozytu.

### Konto administratora

Administrator ma posiadać pełny panel administracyjny z możliwością:

- przeglądania użytkowników,
- sprawdzania, kto, kiedy i jak zagrał,
- przeglądania pełnych historii użytkowników,
- przeglądania historii płatności,
- przeglądania logów,
- wyświetlania statystyk,
- edytowania użytkowników,
- edytowania logów.

## 3. Saldo i waluta

### Waluta

- W projekcie używany będzie polski złoty.
- Stawki, saldo i płatności są prowadzone w polskich złotych.
- Do pokazywania łącznych wygranych w profilu gracza używane będą pesos, aby suma wyglądała na większą i robiła większe wrażenie.
- Saldo użytkownika jest przechowywane w bazie.
- System sprawdza między innymi pole `is_boosted`.

### Zasady salda

- Użytkownik posiada saldo.
- Saldo jest aktualizowane po zakończeniu sesji.
- Po zejściu salda do zera pojawia się okno zachęcające do wpłaty.
- W oknie może znajdować się również możliwość pożyczki na bardzo wysoki procent.
- Do ustalenia:
  - dokładne zasady pożyczki,
  - wysokość oprocentowania,
  - kwota krytyczna,
  - sposób aktualizacji salda.

### Prezentowanie salda i wygranych

- Wygrane mają być mocno wyróżnione wizualnie, zielonym i złotym kolorem.
- Suma wygranych w profilu gracza jest prezentowana w pesos.
- Do sumy wygranych wlicza się również wkład.
- Baza przechowuje dane potrzebne do wyliczenia sumy.
- Sesja pilnuje salda oraz tego, aby użytkownik nie przekroczył kwoty krytycznej.
- Z logów pobierane są informacje o wygranych i przegranych, aby nie zapychać bazy.

## 4. Płatności

### Planowane rozwiązania

- Płatności.
- Podpięcie pełnej karty.
- Możliwość wpłaty pieniędzy.
- Bonusy do wpłat.
- Okno płatności pojawiające się po wyzerowaniu salda.

### Powiązanie użytkownika z płatnością

- Użytkownik jest przechowywany osobno.
- Użytkownik może mieć podpięte konto płatnicze.
- Dane płatności są powiązane z kontem użytkownika.

## 5. Bonusy i konta promowane

### Darmowy obrót za numer telefonu

- Po podaniu numeru telefonu użytkownik otrzymuje codzienny darmowy obrót.
- Numer telefonu musi zostać potwierdzony.

### Bonus do wpłat

- Użytkownik może otrzymać bonus do wpłaty.
- Bonus może być przyznawany czasami.
- Szczegółowe zasady bonusu są do ustalenia.

### Link afiliacyjny

- Gracze mogą posiadać link afiliacyjny.
- Nowy gracz otrzymuje `10%` do depozytu.
- Konto może być oznaczone jako `is_boosted`.
- Wzmocnienie działa jako mnożnik szansy na wygraną.
- Wzmocnienie po prostu zwiększa szansę konta na wygraną.
- Baza sprawdza, czy konto ma ustawione `is_boosted`.
- Wzmocnienie może działać na przykład przez pięć gier.

## 6. Statystyki i panel administracyjny

Panel administracyjny ma pokazywać:

- pełne historie użytkowników,
- kto, kiedy i jak zagrał,
- najczęściej graną grę,
- statystyki gier,
- wysokość zarobku lub straty,
- procent zwrotu,
- historię płatności,
- historię zmian salda,
- logi użytkowników.

Planowane sekcje panelu:

- automat,
- ruletka,
- portfel,
- logowanie,
- strona główna,
- regulamin i informacje prawne,
- ustawienia.

## 7. Interfejs i animacje

- Ruletka posiada animację.
- Automat posiada animację.
- Duże wygrane są mocno widoczne na ekranie.
- Wyniki są prowadzone w polskich złotych, a łączna suma wygranych w profilu gracza jest prezentowana w pesos.
- Przy opuszczaniu strony może pojawić się okno z pytaniem, czy użytkownik na pewno chce odejść.
- Jeżeli użytkownik zdecyduje się pozostać, może otrzymać wygraną zgodnie z ustalonym algorytmem.
- Wygrana przy opuszczaniu strony może obowiązywać maksymalnie dla zakładu do `10 zł`.
- Dla zakładu wyższego niż `10 zł` obowiązują normalne zasady.
- Planowany jest tryb turbo na automatach.

### Elementy dodatkowe

- Animowana postać kobieca przy ruletce.
- Postać w prawym dolnym rogu ekranu, na przykład z piwem, przy logowaniu.
- Easter egg z Magistrem Kotyrą: przy dokładnym saldzie `2 zł` pojawia się zdjęcie.
- Dla mężczyzn planowany jest dodatkowy element wizualny związany z większą ilością dekoltu.

## 8. Technologie i infrastruktura

- Backend: FastAPI — zapisane w dokumentacji projektu; wymaga ostatecznego potwierdzenia.
- Frontend: React i TypeScript.
- Baza danych: PostgreSQL.
- Konteneryzacja: Docker.
- Projekt działa na prywatnym serwerze.
- Każdy członek zespołu powinien mieć możliwość uruchomienia projektu.
- Projekt musi być uruchamiany w kontenerach.
- Po większych aktualizacjach kontenery powinny być zweryfikowane.
- Weryfikacja środowiska jest planowana kwartalnie.
- Do ustalenia:
  - sposób wykonywania migracji,
  - sposób przechowywania sekretów,
  - sposób wykonywania kopii zapasowych,
  - sposób wdrażania aktualizacji.

## 9. Podział odpowiedzialności

### Backend

- Łukasz:
  - sesje,
  - logowanie,
  - płatności.
- Dzeju:
  - gry,
  - ruletka,
  - automat,
  - pozostałe elementy logiki gier.

### Frontend

- Adam:
  - frontend,
  - interfejs,
  - prezentowanie salda,
  - animacje.

### Bazy danych

- Kacper:
  - baza danych,
  - model danych,
  - historia,
  - logi,
  - statystyki.

### DevOps

- Łukasz:
  - Docker,
  - prywatny serwer,
  - wdrażanie.

### Koordynacja i dokumentacja

- Adam:
  - kierownik projektu,
  - dokumentacja,
  - prezentacja.

### Testy i prezentacja

- Wszyscy:
  - testowanie,
  - sprawdzanie funkcji,
  - przygotowanie prezentacji.

## 10. Terminy

- Dokumentacja: styczeń.
- Projekt: marzec/kwiecień.
- Testy: przed ukończeniem projektu, zgodnie z harmonogramem prac.
- Prezentacja: styczeń.
- Ukończenie projektu: marzec/kwiecień.
- W przypadku braku realizacji projektu: śmierć.

## 11. Testowanie

Do ustalenia:

- sposób testowania ruletki,
- sposób testowania automatu,
- testowanie sesji,
- testowanie salda,
- testowanie płatności,
- testowanie panelu administracyjnego,
- testowanie interfejsu,
- testowanie serwera,
- obsługa błędnych danych.

Zachowanie przy wielokrotnym klikaniu jest ustalone:

- najpierw pojawia się okno z ostrzeżeniem, że użytkownik nie powinien wielokrotnie klikać,
- po wyświetleniu ostrzeżenia dalsze klikanie może powodować pobieranie pieniędzy,
- użytkownik może tracić saldo, nawet jeżeli gra nie będzie się obracała.

Funkcja jest gotowa, gdy:

- działa zgodnie z ustalonym zakresem,
- ma obsługę błędów,
- nie pozwala na nieprawidłowe saldo,
- została przetestowana,
- działa lokalnie i na prywatnym serwerze,
- jest opisana w dokumentacji.

## 12. Prezentacja

- Prezentacja ma obejmować normalne uruchomienie i grę.
- Podczas prezentacji pokazujemy aplikację, interfejs oraz działanie funkcji.
- Kod, baza danych i architektura mogą zostać pokazane.
- Należy przygotować konta oraz dane demonstracyjne.
- Podział osób prezentujących pozostaje do ustalenia.
- Kopia zapasowa prezentacji pozostaje do ustalenia.

## 13. Pomysły dodatkowe

- Blackjack.
- Tryb turbo na automatach.
- Linki afiliacyjne.
- Konta promowane.
- Bonus za pełny profil.
- Bonus za potwierdzony numer telefonu.
- Easter egg przy saldzie `2 zł`.
- Animowana postać przy ruletce.
- Postać w oknie logowania.

## 14. Elementy wymagające dalszego ustalenia

- Dokładne zasady ruletki.
- Dokładne zasady automatu.
- Symbole i tabela wypłat automatu.
- Zasady płatności.
- Zasady podpięcia karty.
- Czas dezaktywacji konta.
- Zasady odnawiania konta.
- Czas przechowywania danych.
- Zasady pożyczki.
- Kwota krytyczna.
- Obsługa błędnych danych.
- Dokładny termin oddania.
- Zakres prezentacji.
- Podział osób prezentujących.
