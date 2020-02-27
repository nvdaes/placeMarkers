# placeMarkers #
* Autorzy: Noelia, Chris.
* NVDA compatibility: 2019.3 or later.
* Pobierz [wersja stabilna][1]
* Pobierz [wersja rozwojowa][2]

Ten dodatek jest używany do zapisywania i wyszukiwania określonych ciągów
tekstowych lub zakładek, na stronach internetowych lub dokumentach trybu
czytania NVDA.  Może również być użyta do zapisania lub wyszukania ciągów
tekstowych w kontrolkach wieloliniowych; w takim przypadku, jeśli nie jest
możliwe przemieszczenie kursora, odpowiadający łańcuch zostanie skopiowany
do schowka, dzięki czemu może zostać wyszukany przy użyciu innych narzędzi.
Wtyczka zapisuje określone ciągi tekstowe i zakładki w plikach tekstowych i
.pickle. Nazwa tych plików oparta jest na tytule i adresie bieżącego
dokumentu.

## Skróty klawiszowe: ##

*	control+shift+NVDA+f: Otwiera dialog z polem edycyjnym wyświetlające
  ostatnie wyszukiwanie; W tym oknie można także zaznaczyć wczesne
  wyszukiwania z pola kombi, albo usunąć łańcuch tekstu z historii używając
  pole wyboru. Można wybierać, czy podany tekst ma być zachowany w historii
  wyszukiwań,. Nareście można wybrać akcje z następujących przycisków opcji
  (pomiędzy wyszukaj następny, wyszukaj poprzedni albo nie wyszukuj), i
  określić, czy NVDA ma zrwacać uwagę na wielkość liter. When you press
  okay, NVDA will search for this string.
*	control+shift+NVDA+k: Zapisuje terażniejszą pozycję jako zakładkę. Jeżeli
  chcesz nadać nazwę tej zakładce, zaznacz jakiś tekst z tej pozycji przed
  zapisywaniem zakładki.
*	control+shift+NVDA+delete: Usuwa zakładkę, odnoszącą się do konkretnej
  pozycji.
*	NVDA+k: Przemieszcza się do następującej zakładki.
*	shift+NVDA+k: Przemieszcza się do poprzedniej zakładki.
*	Not assigned: Shows the file name where the place markers data will be
  saved in browse mode, without an extension.
*	alt+NVDA+k: Opens a dialog with the bookmarks saved for this document. You
  can write a note for each bookmark; press Save note to save
  changes. Pressing Delete you can remove the selected bookmark. Pressing OK
  you can move to the selected position.
*	Not assigned: Saves a position as a temporary bookmark.
*	Not assigned: Moves to the temporary bookmark for the current document.
*	Not assigned: Finds the next occurrence of the last text searched for any
  specific document.
*	Not assigned: Finds the previous occurrence of the last text searched for
  any specific document.


## Podmenu Znaczniki miejsc (NVDA+N) ##

Używając podmenu znaczniki miejsc, w menu NVDA Ustawienia, możesz uzyskać
dostęp do:

*	Folder wyszukiwania: otwiera poprzednio zapisany folder specyficznych
  wyszukiwań.
*	Folder zakładek; otwiera folder zapisanych zakładek.
*	Kopiuj folder znaczników miejsc; możesz zapisać kopię folderu z
  zakładkami.
*	Przywróć zakładki; możesz przywrócić zakładki z poprzednio zapisanego
  folderu znaczników miejsc.

Uwaga: pozycja zakładki opiera się na ilości znaków; na stronach z
dynamiczną treścią lepiej używać wyszukiwania , by precyzyjnie zapamiętać
określone miejsce.

## Changes for 14.0 ##
*	The command to copy the name of the file where place markers data will be
  saved has been replaced by a command which shows this file name in browse
  mode. This is not assigned to a gesture.
*	The "Text to search" field does not overlap the "Saved text" field
  anymore. (Thanks to Cyrille Bougot).
*	Requires NVDA 2019.3 or later.

## Zmiany dla wersji 13.0 ##
*	Added not assigned commands to find the next and previous occurrences of
  the last text searched for any specific document.
*	The specific search feature works when the NVDA's About dialog is open.
*	In the Specific search dialog, the case sensitive checkbox will be checked
  if this option was selected for the last search.
*	When the add-on is updated, bookmarks and strings for specific search
  saved in the previous version of the add-on will be automatically copied
  to the new version, unless you prefer to import place markers saved in the
  main configuration folder of NVDA.
*	When using the dialog to copy place markers, if the chosen folder is not
  named placeMarkersBackup, a subfolder with this name will be created to
  prevent the deletion of directories containing important data, such as
  Documents or Downloads.

## Zmiany dla wersji 12.0 ##
*	Fixed a critical bug which caused NVDA to crash when trying to open the
  Notes dialog, if chinese characters were selected before saving bookmarks.

## Zmiany dla wersji 11.0 ##
*	Zgodny z NVDA 2018.3 i nowszymi (wymagane).
*	Jeżeli jest to konieczne, możesz pobrać [ostatnią wersję zgodną z NVDA
  2017.3][3].

## Zmiany dla wersji 10.0 ##
*	In Edge, gestures associated with bookmarks selection, such as NVDA+k,
  NVDA+shift+k or NVDA+alt+k, will be sent to the application instead of
  trying to move the cursor to bookmarks, to avoid errors, especially in
  long documents.
*	Now specific search is supported in Edge.

## Zmiany dla wersji 8.0
*	When moving to a bookmark from the Notes dialog, the review cursor follows
  the system cursor.
*	The command to select the previous bookmark works properly again.
*	Bookmarks can be deleted from the Notes dialog.
*	Now you can assign gestures to save and move to a temporary bookmark for
  each document.

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

[1]: https://addons.nvda-project.org/files/get.php?file=pm

[2]: https://addons.nvda-project.org/files/get.php?file=pm-dev

[3]: https://addons.nvda-project.org/files/get.php?file=pm-o
