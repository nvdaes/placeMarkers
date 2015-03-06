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

Ten dodatek jest oparty na SpecificSearch i Bookmark&Search, stworzonych
przez tego samego autora. Powinieneś je odinstalować, aby używać tego
dodatku, ponieważ mają wspólne skróty klawiszowe i funkcje.

## Skróty klawiszowe: ##

*	control+shift+NVDA+s; Opens a dialog that allows you to save a text string   you want to find in the current document. By default, the text previously saved for this file is shown. Delete this text and press Ok button if you wish to remove the text file corresponding to the saved search, or type new text to add another search.
*	control+shift+NVDA+f; opens a dialog with a edit box that shows the last saved search; in this dialog you can also select the previously saved searches from a combo box and choose an action from the next combo box. If there is no available files for specific search in the current document, NVDA will warn you that it is not found any file for specific search.
*	control+shift+NVDA+k; Saves the current position as a bookmark
*	control+shift+NVDA+delete; Deletes the bookmark corresponding to this position.
*	NVDA+k; Moves to the next bookmark.
*	shift+NVDA+k; Moves to the previous bookmark.
*	control+shift+k; Copies to clipboard the file name, without extension, where the place markers data will be saved.

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
*	Plik dokumentacji w twoim wybranym języku jeśli dostępny, albo domyślnie
  po angielsku.

Uwaga: pozycja zakładki opiera się na ilości znaków; na stronach z
dynamiczną treścią lepiej używać wyszukiwania , by precyzyjnie zapamiętać
określone miejsce.


## Changes for 5.0 ##
* Added case sensitive search.
* Removed option to open documentation from Place markers menu.
* More intuitive key commands.

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
