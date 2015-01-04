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

*	control+shift+NVDA+s; otwiera okno dialogowe, pozwalające zapisać ciąg znaków, który chcesz znaleźć w bieżącym dokumencie. Domyślnie pokazywany jest tekst zapisany poprzednio dla tego pliku. Usuń ten tekst i naciśnij przycisk OK, jeśli chcesz usunąć plik tekstowy odpowiadający zapisanemu wyszukiwaniu lub wpisz nowy tekst aby dodać inne wyszukiwanie.
*	control+shift+NVDA+f; otwiera okno dialogowe z polem edycji zawierającym ostatnio zapisane wyszukiwanie; w oknie tym możesz również wybrać z listy rozwijanej, poprzednio zapisane wyszukiwania a następnie wybrać akcję z następnej listy rozwijanej. Jeśli nie ma dostępnych plików dla aktualnego dokumentu NVDA  poinformuje, że nie znalazł żadnego pliku dla określonego wyszukiwania.
*	control+shift+NVDA+k; zapisuje aktualną pozycję jako zakładkę
*	control+shift+NVDA+delete; usuwa zakładkę powiązaną z tym miejscem.
*	control+shift+k; przechodzi do następnej zakładki.
*	shift+NVDA+k; przechodzi do poprzedniej zakładki.
*	NVDA+k; kopiuje do schowka nazwę pliku bez rozszerzenia, w którym zapisane zostaną dane dodatku.

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

## Changes for 4.0 ##
* Removed fragment identifiers from bookmark filenames, which can avoid
  issues in ePUBREADER Firefox add-on.
* Add-on help is available from the Add-ons Manager.

## Zmiany dla wersji 3.1 ##
* Aktualizacje tłumaczenia i nowy język.
* Bookmark position is not announced in skim reading.

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
