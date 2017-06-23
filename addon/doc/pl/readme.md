# Znaczniki miejsc / placeMarkers #

* Autorzy: Noelia, Chris.
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
*	control+shift+NVDA+k: Saves the current position as a bookmark. If you
  want to provide a name for this bookmark, select some text from this
  position before saving it.
*	control+shift+NVDA+delete: Usuwa zakładkę, odnoszącą się do konkretnej
  pozycji.
*	NVDA+k: Przemieszcza się do następującej zakładki.
*	shift+NVDA+k: Przemieszcza się do poprzedniej zakładki.
*	control+shift+k: Copies the file name where the place markers data will be
  saved to the clipboard, without an extension.
*	alt+NVDA+k: Opens a dialog with the bookmarks saved for this document. You
  can write a note for each bookmark; press Save note to save
  changes. Pressing OK you can move to the selected position.


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


## Zmiany dla wersji 8.0 ##
*	Usunięto identyfikatory fragmentów z nazw plików zakładek, co może
  spowodować uniknięcie problemów  VitalSource ePUBREADER.
*	Added a Notes dialog, to associate comments for saved bookmarks and move
  to the selected position.

## Zmiany dla wersji 7.0 ##
*	The dialog to save a string of text for specific search has been
  removed. This functionality is now included in the Specific search dialog,
  which has been redesigned to allow different actions when pressing the OK
  button.
*	Wizualna prezentacja dialogów została ulepszona, aby była zgodna z
  wyświetlanymi dialogami w NVDA.
*	Performing a Find Next or Find Previous command in Browse Mode will now
  correctly do a case sensitive search if the original Find was case
  sensitive.
*	Wymagane NVDA 2016.4 lub nowsze.
*	Now you can assign gestures to open the Copy and Restore place markers
  dialogs.
*	NVDA will present a message to notify when place markers have been copied
  or restored with the corresponding dialogs.

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

[1]: http://addons.nvda-project.org/files/get.php?file=pm

[2]: http://addons.nvda-project.org/files/get.php?file=pm-dev
