# Oznake pozicija (placeMarkers) #

* Autori: Noelia, Chris.

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

## Tipkovnički prečaci: ##

*	kontrol+šift+NVDA+f: Otvara dijaloški okvir s uređivačkim poljem, koje
  prikazuje posljednju spremljenu pretragu. Moguće je odabrati prethodno
  spremljene pretrage iz odabirnog okvira ili ukloniti odabrani niz iz
  povijesti, pomoću potvrdnog okvira. Moguće je odabrati, hoće li se tekst u
  uređivačkom polju dodati u povijest spremljenih tekstova. Kao zadnje,
  odaberi radnju iz sljedeće grupe izbornih gumba (Traži sljedeću, Traži
  prethodnu ili Ne traži), te odredi osjetljivost na velika i mala slova
  tijekom pretrage. Pritiskom gumba „U redu”, NVDA će tražiti taj niz.
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
*	Nije dodijeljeno: Nalazi sljedeći slučaj zadnje pretrage teksta za svaki
  određeni dokument.
*	Nije dodijeljeno: Nalazi prethodni slučaj zadnje pretrage teksta za svaki
  određeni dokument.


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

## Promjene u verziji 24.0
* Y is used instead of k in gestures such as NVDA+k, NVDA+shift+k,
  NVDA+alt+k and NVDA+control+shift+k.
* Kompatibilno s NVDA 2023.1.

## Promjene u verziji 23.0
* Dodatak ponovo radi s Microsoft Wordom.

## Promjene u verziji 22.0
* Oznake se mogu premjestiti i izbrisati s UIA-om, zahvaljujući Abdelu.

## Promjene u verziji 21.0
* Oznake se mogu spremati s uključenim UIA-om u preglednicima koji se
  temelje na Chromiumu, zahvaljujući Abdelu.

## Promjene u verziji 20.0
* Zahtijeva NVDA 2022.1 ili noviju verziju.

## Promjene u verziji 19.0 ##
* Ovaj se dodatak ne može pokretati u sigurnim ekranima.

## Promjene u verziji 18.0 ##
* The command to see the path for placeMarkers shows if there are permanent
  bookmarks, text for specific search or a temporary bookmark for the
  current document.

## Promjene u verziji 17.0 ##
* Fixed a bug which didn't allow to save place markers in some documents.
* Fixed translated strings making translations to work properly.

## Promjene u verziji 16.0 ##
* Kompatibilno s NVDA 2021.1 i novijim verzijama (obavezno).
* Brzo čitanje je podržano prilikom prelaska na privremene oznake.
* If needed, you can download [other
  versions](https://github.com/nvdaes/placeMarkers/releases).

## Promjene u verziji 15.0 ##
* When reading with say all in browse mode, the specific find next and
  specific find previous commands do not stop reading anymore if Allow skim
  reading option is enabled, according to find next and find previous
  commands from NVDA 2020.4.
* When the Specific search dialog is opened after running the Specific find
  previous command, the Search previous option will be selected.

## Promjene u verziji 14.0 ##
*	Prečac koji kopira ime datoteke u kojoj se spremaju oznake mjesta
  zamijenjen je prečacem koji to pokazuje u modusu čitanja. Taj prečac nije
  dodijeljen.
*	Polje "tekst pretrage" više se ne poklapa s poljem "spremljeni
  tekst". (Zahvaljujem Cyrilleu Bougotu).
*	Zahtijeva NVDA 2019.3 ili noviju verziju.

## Promjene u verziji 13.0 ##
*	Dodane se nedodijeljene naredbe za pronalaženje sljedeće i prethodne
  pojave zadnje traženog teksta za bilo koji određeni dokument.
*	Funkcija određenog pretraživanje radi, kad je otvoren dijaloški okvir „O
  programu NVDA”.
*	U dijaloškom okviru „Određena pretraga”, potvrdit će se potvrdni okvir za
  velika slova, ako je ova opcija odabrana u zadnjoj pretrazi.
*	Kad se dodatak nadogradi, knjižne oznake i nizovi za određenu pretragu
  koji su spremljeni u prethodnoj verziji dodatka, će se automatski kopirati
  u novu verziju, osim ako ne želiš uvesti oznake pozicija, spremljene u
  glavnu mapu NVDA konfiguracije.
*	Kad se koristi dijaloški okvir za kopiranje oznaka pozicija, ako odabrana
  mapa nije imenovana „placeMarkersBackup”, stvorit će se podmapa s tim
  nazivom, kako bi se spriječilo brisanje mapa koje sadrže važne podatke,
  poput „Dokumenati” ili „Preuzimanja”.

## Promjene u verziji 12.0 ##
*	Popravljena je kritična greška zbog koje se NVDA rušio prilikom otvaranja
  dijaloškog okvira „Napomene”, ako su prije spremanja knjižnih oznaka
  odabrani kineski znakovi.

## Promjene u verziji 11.0 ##
*	Kompatibilno s NVDA 2018.3 i budućim verzijama (obavezno).
*	Ako treba, moguće je preuzeti [zadnju verziju kompatibilnu s NVDA
  2017.3][3].

## Promjene u verziji 10.0 ##
*	U Edgeu, geste koje su povezane s odabirom knjižnih oznaka, kao što su
  NVDA+k, NVDA+šift+k ili NVDA+alt+k, bit će poslane aplikaciji, umjesto da
  se pokuša premjestiti pokazivača na knjižne oznake, kako bi se izbjegle
  greške, posebno u dugačkim dokumentima.
*	Sada se određena pretraga podržava u Edge.

## Promjene u verziji 9.0
*	Tijekom premještanja na knjižnu oznaku iz dijaloškog okvira Napomene,
  pregledni kursor slijedi kursor sustava.
*	Naredba za biranje prethodne knjižne oznake opet radi ispravno.
*	Zabilješke se mogu brisati u dijaloškom okviru Napomene.
*	Sada je moguće dodijeliti geste za spremanje i premještanje na privremenu
  knjižnu oznaku za svaki dokument.

## Promjene u verziji 8.0 ##
*	Izmijenjen je način odabira naslova knjižnih oznaka, što rješava problem s
  nekim aplikacijama kao što je ePUB reader.
*	Dodan je dijaloški okvir „Napomene”, za dodavanje komentara za spremljene
  knjižne oznake i premještanje na odabranu poziciju.

## Promjene u verziji 7.0 ##
*	Dijaloški okvir za spremanje niza teksta za određenu pretragu je
  uklonjen. Ta funkcija je sada uključena u dijaloški okvir „Određena
  pretraga”, koji je novo dizajniran, kako bi omogućio različite radnje kad
  se pritisne gumb „U redu”.
*	Vizualni prikaz dijaloških okvira je poboljšan, pridržavajući se izgleda
  dijaloških okvira u NVDA čitaču.
*	Naredbe „Traži sljedeće” i „Traži prethodno” sada će ispravno izvršavati
  pretragu osjetljivu na velika i mala slova, ako se početna pretraga
  zasnivala na razlikovanju velikih i malih slova.
*	Zahtijeva NVDA verziju 2016.4 ili noviju.
*	Sada je moguće dodati geste za otvaranje dijaloških okvira za kopiranje i
  obnavljanje oznaka pozicija.
*	NVDA će prikazati poruku kako bi obavijestio o kopiranju ili obnavljanju
  oznaka pozicija pomoću odgovarajućih dijaloških okvira.

## Promjene u verziji 6.0 ##
* Kad funkcije dodatka nisu upotrebljive, geste se šalju odgovarajućoj
  aplikaciji.

## Promjene u verziji 5.0 ##
* Dodana je pretraga s osjetljivošću na velika i mala slova.
* Uklonjena je opcija za otvaranje dokumentacije iz izbornika „Oznake
  pozicija”.
* Logičniji prečaci.

## Promjene u verziji 4.0 ##
* Promijenjen je način definiranja naslova zabilješki, što rješava problem u
  dodatku EPUBREADER za Firefox.
* Pomoć za ovaj dodatak je dostupna u Upravljaču dodataka.

## Promjene u verziji 3.1 ##
* Ažurirani prijevodi i novi jezik.
* Pozicija knjižne oznake se više ne najavljuje u brzom čitanju dokumenta.

## Promjene u verziji 3.0 ##
* Dodana je podrška za brzo čitanje dokumenta.

## Promjene u verziji 2.0 ##
* Dodane su opcije za spremanje i brisanje različitih pretraga za svaku
  datoteku.
* Ispravljena je greška u baratanju nelatiničnim znakovima u stazama.
* Prečace je sada moguće nanovo odrediti korištenjem dijaloškog okvira za
  ulazne geste.

## Promjene u verziji 1.0 ##
* Prva verzija.
* Prevedeno na: brazilski portugalski, farsi, finski, francuski, galicijski,
  njemački, talijanski, japanski, korejski, nepalski, portugalski,
  španjolski, slovački, slovenski, tamilski.

[[!tag dev stable]]

[3]: https://www.nvaccess.org/addonStore/legacy?file=pm-o
