# eMule #

*	Autorzy: Noelia, Chris, Alberto.
*	NVDA compatibility: 2019.3 or later.
*	Pobierz [wersja stabilna][1]
*	Pobierz [wersja rozwojowa][3]
*	download [version compatible with NVDA 2017.3][4]

This add-on helps to improve accessibility of eMule with nVDA.  It also
provides additional keyboard commands for moving in different windows and
gives Useful information about eMule.

It's based on the eMuleNVDASupport add-on, developed by the same author. You
should uninstall that old add-on to use this one, since both have common
keystrokes and features.

Przetestowany na [eMule][2] 0.50a.

## Skróty klawiszowe: ##

*	control+shift+h: przenosi mysz i punkt uwagi do głównego paska narzędzi.
*	control+shift+t: odczytuje bieżące okno.
*	control+shift+n: przenosi punkt uwagi do pola nazwy w oknie znajdowania.
*	control+shift+p: w oknie wyszukiwania, przenosi mysz i punkt uwagi do
  listy parametrów, albo opcji pola edycji.
*	control+shift+b: przenosi punkt uwagi do listy w aktualnym
  oknie. Przydatne do listy wyników w oknie wyszukiwania, listy pobierań w
  oknie transfer itd.
*	control+shift+o: przenosi punkt uwagi do pól edycji tylko do odczytu,
  znajdujących się w aktualnym oknie, np. otrzymane wiadomości IRC, dostępne
  serwery itd.
*	control+NVDA+f: jeśli kursor systemowy znajduje się w polu edycji tylko do
  odczytu, otwiera okno Znajdź, aby móc użyć komend do wyszukiwania tekstu w
  NVDA. 
*	control+shift+l: przenosi obiekt nawigatora i wskaźnik myszy do nagłówków
  aktualnej listy.
*	control+shift+q: odczytuje pierwszy obiekt na pasku stanu; dostarcza
  informację o ostatniej aktywności.
*	control+shift+w: odczytuje drugi obiekt na pasku stanu; zawiera informacje
  o plikach i użytkownikach na aktualnym serwerze.
*	control+shift+e: odczytuje trzeci obiekt na pasku stanu; użyteczne aby
  poznać prędkość pobierania i wysyłania.
*	control+shift+r: odczytuje czwarty obiekt na pasku stanu; raport z
  połączenia z siecią eD2K i Kad.

## Zarządzanie kolumnami. ##

Kiedy znajdujesz się na liście, możesz przemieszczać kursor pomiędzy liniami
i kolumnami używając klawisza alt+control+ Strzałki.  Dostępne są również
następujące polecenia klawiszowe w tym dodatku:

*	nvda+control+1-0: czyta pierwsze 10 kolumn.
*	nvda+shift+1-0: czyta kolumny do 20.
*	nvda+shift+C: kopiuje do schowka treść ostatnio przeczytanej kolumny.

## Changes for 4.0 ##
*	Requires NVDA 2019.3 or later.

## Zmiany dla 3.0 ##
*	 To search text in the readonly edit boxes,  the find dialog  can be used,
   such as nvda+control+f to activate the find dialog.

## Zmiany dla 2.0 ##
*	 Pomoc dodatku dostępna w oknie zarządzania dodatkami.

## Zmiany dla 1.2 ##
*	 Po przejściu do wiadomości IRC, zaznaczony tekst jest prawidłowo
   odczytywany.
*	 Komenda przechodzenia do wyników wyszukiwania została uogólniona i
   przenosi punkt uwagi do jakiejkolwiek pierwszej dostępnej listy w
   aktualnym oknie.
*	 Komenda przechodzenia do wiadomości IRC została uogólniona i  teraz
   umożliwia przejście do jakiegokolwiek pola tylko do odczytu  dzięki czemu
   można przeglądać informacje o połączeniach w oknie serwera.
*	 Po przemieszczeniu myszy lub punktu uwagi do paska narzędzi, w niektórych
   sytuacjach był oznajmiany podwójnie. Zostało to naprawione.

## Zmiany dla 1.1 ##
*	 Poprawiony błąd polecenia Emule w menu Pomoc NVDA, gdy nazwa folderu
   konfiguracyjnego użytkownika zawierała znaki z poza alfabetu łacińskiego.
*	 Skróty klawiszowe mogą być modyfikowane przy użyciu okna Zdarzeń wejścia
   w menu NVDA.

## Zmiany dla 1.0 ##
*	 Pierwsza wersja.


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=em

[2]: https://www.emule-project.net

[3]: https://addons.nvda-project.org/files/get.php?file=em-dev
