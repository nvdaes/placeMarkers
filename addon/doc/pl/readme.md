# placeMarkers #

* Autorzy: Noelia, Chris.

This add-on is used for saving and searching specific text strings or
placemarkers. It can be used on web pages or documents in NVDA's browse
mode. It can also be used for saving or searching strings of text in
multi-line controls; in this case, if it's not possible to update the caret,
the corresponding string will be copied to the clipboard, so that it can be
searched using other tools.  The plugin saves the specified strings and
placemarkers to files whose name is based on the title and URL of the
current document.  This add-on is based on SpecificSearch and
Bookmark&Search, developed by the same author. You should uninstall them to
use this one, since they have common keystrokes and features.

## Skróty klawiszowe: ##

*	control+shift+NVDA+f: Otwiera dialog z polem edycyjnym wyświetlające
  ostatnie wyszukiwanie; W tym oknie można także zaznaczyć wczesne
  wyszukiwania z pola kombi, albo usunąć łańcuch tekstu z historii używając
  pole wyboru. Można wybierać, czy podany tekst ma być zachowany w historii
  wyszukiwań,. Nareście można wybrać akcje z następujących przycisków opcji
  (pomiędzy wyszukaj następny, wyszukaj poprzedni albo nie wyszukuj), i
  określić, czy NVDA ma zrwacać uwagę na wielkość liter. When you press
  okay, NVDA will search for this string.
*	control+shift+NVDA+y: Saves the current position as a placemarker. If you
  want to provide a name for this placemarker, select some text from this
  position before saving it.
*	control+shift+NVDA+delete: Deletes the placemarker corresponding to this
  position.
*	NVDA+y: Moves to the next placemarker.
*	shift+NVDA+y: Moves to the previous placemarker.
*	Not assigned: Shows the file name where the placemarkers data will be
  saved in browse mode, without an extension.
*	alt+NVDA+y: Opens a dialog with the placemarkers saved for this
  document. You can write a note for each placemarker; press Save note to
  save changes. Pressing Delete you can remove the selected
  placemarker. Pressing OK you can move to the selected position.
*	Not assigned: Saves a position as a temporary placemarker.
*	Not assigned: Moves to the temporary placemarker for the current document.
*	Nieprzypisane: Wyszukuje następne wystąpienie ostatnio wyszukiwanego
  tekstu dla określonego dokumentu.
*	Nieprzypisane: Wyszukuje poprzednie wystąpienie ostatnio wyszukiwanego
  tekstu dla określonego dokumentu.


## PlaceMarkers Submenu (NVDA+N) ##

Using the PlaceMarkers submenu under NVDA's Preferences menu, you can
access:

*	Specific search folder: Opens a folder of specific searches previously
  saved.
*	Bookmarks folder: Opens a folder of the saved placemarkers.
*	Copy placeMarkers folder: You can save a copy of the placeMarkers folder.
*	Restore placeMarkers: You can restore your placeMarkers from a previously
  saved placeMarkers folder.

Note: The placemarker position is based on the number of characters; and
therefore in dynamic pages it is better to use the specific search, not
placemarkers.

## Changes for 24.0
* Y is used instead of k in gestures such as NVDA+k, NVDA+shift+k,
  NVDA+alt+k and NVDA+control+shift+k.
* Compatible with NVDA 2023.1.

## Zmiany w wersji 23.0
* Dodatek działa ponownie z programem Microsoft Word.

## Zmiany w wersji 22.0
* Możemy przejść do zakładek i usunąć je z włączonym UIA, dzięki Abdelowi.

## Zmiany w wersji 21.0
* Zakładki można zapisywać z włączonym UIA w przeglądarkach opartych na
  Chromium, dzięki Abdelowi.

## Zmiany w wersji 20.0
* Wymaga NVDA 2022.1 lub nowszego.

## Zmiany w wersji 19.0 ##
* Dodatku nie można uruchomić na bezpiecznych ekranach.

## Zmiany w wersji 18.0 ##
* Polecenie wyświetlania ścieżki dla placeMarkers pokazuje, czy istnieją
  stałe zakładki, tekst do określonego wyszukiwania lub tymczasowa zakładka
  dla bieżącego dokumentu.

## Zmiany w wersji 17.0 ##
* Naprawiono błąd, który nie pozwalał na zapisywanie znaczników miejsc w
  niektórych dokumentach.
* Naprawiono przetłumaczone ciągi znaków, dzięki czemu tłumaczenia działały
  poprawnie.

## Zmiany w wersji 16.0 ##
* Compatible with NVDA 2021.1 or later (required).
* Czytanie z tłuszczem jest obsługiwane podczas przechodzenia do zakładek
  tymczasowych.
* If needed, you can download [other
  versions](https://github.com/nvdaes/placeMarkers/releases).

## Zmiany w wersji 15.0 ##
* Podczas czytania z powiedzmy wszystkim w trybie przeglądania, konkretne
  polecenia znajdź następny i konkretne znajdź poprzednie nie przestają już
  czytać, jeśli włączona jest opcja Zezwalaj na czytanie odtłuszczone,
  zgodnie z znajdź następny i znajdź poprzednie polecenia z NVDA 2020.4.
* Po otwarciu okna dialogowego Określone wyszukiwanie po uruchomieniu
  polecenia Określone znajdź poprzednie zostanie wybrana opcja Wyszukaj
  poprzednie.

## Zmiany w wersji 14.0 ##
*	Polecenie skopiowania nazwy pliku, w którym zostaną zapisane dane
  znaczników miejsca, zostało zastąpione poleceniem, które pokazuje tę nazwę
  pliku w trybie przeglądania. Nie jest to przypisane do gestu.
*	Pole "Tekst do wyszukania" nie nakłada się już na pole "Zapisany
  tekst". (Podziękowania dla Cyrille Bougot).
*	Wymaga NVDA 2019.3 lub nowszej.

## Zmiany dla wersji 13.0 ##
*	Dodano nieprzypisane polecenia, aby znaleźć następne i poprzednie
  wystąpienia ostatniego wyszukiwanego tekstu dla określonego dokumentu.
*	Określona funkcja wyszukiwania działa, gdy okno dialogowe Informacje NVDA
  jest otwarte.
*	W oknie dialogowym Określone wyszukiwanie pole wyboru z uwzględnieniem
  wielkości liter zostanie zaznaczone, jeśli ta opcja została wybrana dla
  ostatniego wyszukiwania.
*	Po zaktualizowaniu dodatku zakładki i ciągi znaków do określonego
  wyszukiwania zapisane w poprzedniej wersji dodatku zostaną automatycznie
  skopiowane do nowej wersji, chyba że wolisz importować znaczniki miejsc
  zapisane w głównym folderze konfiguracyjnym NVDA.
*	Podczas korzystania z okna dialogowego do kopiowania znaczników miejsc,
  jeśli wybrany folder nie ma nazwy placeMarkersBackup, zostanie utworzony
  podfolder o tej nazwie, aby zapobiec usunięciu katalogów zawierających
  ważne dane, takie jak Dokumenty lub Pobrane.

## Zmiany dla wersji 12.0 ##
*	Naprawiono krytyczny błąd, który powodował awarię NVDA podczas próby
  otwarcia okna dialogowego Notatki, jeśli chińskie znaki zostały wybrane
  przed zapisaniem zakładek.

## Zmiany dla wersji 11.0 ##
*	Zgodny z NVDA 2018.3 i nowszymi (wymagane).
*	Jeżeli jest to konieczne, możesz pobrać [ostatnią wersję zgodną z NVDA
  2017.3][3].

## Zmiany dla wersji 10.0 ##
*	W Edge gesty związane z zaznaczaniem zakładek, takie jak NVDA+k,
  NVDA+shift+k lub NVDA+alt+k, będą wysyłane do aplikacji zamiast próbować
  przesunąć kursor do zakładek, aby uniknąć błędów, szczególnie w długich
  dokumentach.
*	Teraz określone wyszukiwanie jest obsługiwane w Edge.

## Zmiany dla wersji 8.0
*	Podczas przechodzenia do zakładki z okna dialogowego Notatki kursor
  recenzji podąża za kursorem systemowym.
*	Polecenie wyboru poprzedniej zakładki działa ponownie poprawnie.
*	Zakładki można usuwać z okna dialogowego Notatki.
*	Teraz możesz przypisywać gesty do zapisywania i przechodzenia do
  tymczasowej zakładki dla każdego dokumentu.

## Zmiany dla wersji 8.0 ##
*	Usunięto identyfikatory fragmentów z nazw plików zakładek, co może
  spowodować uniknięcie problemów  VitalSource ePUBREADER.
*	Dodano dialog notatek, aby skojarzyć komentarze zapisanych zakładek i
  przemieszczać się do danej pozycji.

## Zmiany dla wersji 7.0 ##
*	Dialog do przeszukiwania określonego łańcuchu tekstu jest usunięty. Ta
  funkcjonalność jest przeniesiona do okna dialogowego określone
  wyszukiwanie, który jest zmieniony, aby z niego użytkownicy mogli
  wypełniać różne komendy.
*	Wizualna prezentacja dialogów została ulepszona, aby była zgodna z
  wyświetlanymi dialogami w NVDA.
*	Przy wywołaniu komendy szukaj następne /poprzednie w trybie przeglądania
  teraz sprawnie zrobi wyszukiwanie uwzględniające wielkie litery, jeżeli
  wyszukiwanie oryginalne uwzględniało wielkość liter.
*	Wymagane NVDA 2016.4 lub nowsze.
*	Teraz można przydzielić zdarzenie wejścia dla okien dialogowych "kopiuj",
  i "wklej" znaczniki miejsc.
*	NVDA pokaże wiadomość przy powodzeniu kopiowania lub przywracania
  znaczników za pomocą określonych okien dialogowych.

## Zmiany dla wersji 6.0 ##
* Kiedy funkcje dodatku nie są dostępne, zdarzenia wejścia są wysyłane do
  danej aplikacji.

## Zmiany dla wersji 5.0 ##
* Dodane wyszukiwanie z uwzględnieniem wielkości liter.
* Usunięta opcja otwierania dokumentacji z menu dodatku.
* Bardziej intuicyjne skróty klawiszowe.

## Zmiany dla wersji 4.0 ##
* Usunięto identyfikatory fragmentów z nazw plików zakładek, co może
  spowodować uniknięcie problemów w dodatku do Firefox ePUBREADER.
* Pomoc dodatku dostępna w managerze dodatków.

## Zmiany dla wersji 3.1 ##
* Aktualizacje tłumaczenia i nowy język.
* Pozycja zakładki nie jest oznajmiana w czytaniu przeglądowym.

## Zmiany dla wersji 3.0 ##
* Dodano wsparcie czytania przeglądowego.

## Zmiany dla wersji 2.0 ##
* Dodane opcje zapisania i usunięcia różnych wyszukiwań dla każdego pliku.
* Usunięto błąd, który pojawiał się gdy ścieżka zawierała znaki inne niż
  alfabetu łacińskiego.
* Skróty klawiszowe mogą być modyfikowane przy użyciu polecenia NVDA
  Zdarzenia wejścia.

## Zmiany dla wersji 1.0 ##
* Wstępne wydanie.
* Przetłumaczony na: brazylijski portugalski, farsi, fiński, francuski,
  galicyjski, niemiecki, włoski, japoński, koreański, nepalski, portugalski,
  hiszpański, słowacki, słoweński, tamilski.

[[!tag dev stable]]

[3]: https://www.nvaccess.org/addonStore/legacy?file=pm-o
