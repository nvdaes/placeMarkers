# mjesne oznake / placemarkerss #
* Autori: Noelia, Chris.
* NVDA compatibility: 2018.3 to 2019.2
* preuzmi [stabilnu inačicu][1]
* preuzmi [razvojnu inačicu][2]

Ovaj dodatak se koristi za pretraživanje i čuvanje zabilješki na web
stranicama i dokumentima u NVDA modu pretraživanja. Možete pretraživati i
višelinijski, dodatak će se prilagoditi. Naziv zabilješke koju sačuvate
zasnovan je na naslovu i adresi stranice/dokumenta. 

## Tipkovne prečice:  ##

*	control+shift+NVDA+f: Otvara dijaloški okvir s uređivačkim poljem koje
  prikazuje posljednju spremljenu pretragu; u tom dijaloškom okviru također
  možete odabrati prethodno spremljene pretrage ili ukloniti odabrani
  niz. Možete odabrati hoće li se tekst sadržan u uređivačkom polju dodati
  među sačuvane tekstove. Konačno, odaberite akciju iz sljedeće grupe radio
  gumbića (između Traži sljedeće, Traži prethodno ili Ne traži), te
  definirajte hoće li NVDA biti osjetljiv na velika i mala slova tijekom
  pretrage. Kada pritisnete u redu, NVDA će tražiti taj niz.
*	control+shift+NVDA+k: Sprema trenutnu poziciju kao zabilješku. Ako želite
  dodijeliti ime toj zabilješki, odaberite neki tekst prije spremanja. 
*	control+shift+NVDA+delete: briše zabilješku u skladu s njenom pozicijom.
*	NVDA+k: pomiče na sljedeću zabilješku.
*	shift+NVDA+k: pomiče na prethodnu zabilješku.
*	control+shift+A: Kopira ime datoteke u kojoj će se čuvati podaci mjesne
  oznake u međuspremnik, bez ekstenzije.
*	alt+NVDA+k: Opens a dialog with the bookmarks saved for this document. You
  can write a note for each bookmark; press Save note to save
  changes. Pressing Delete you can remove the selected bookmark. Pressing OK
  you can move to the selected position.
*	Nije dodijeljeno: Sprema poziciju kao privremenu zabilješku.
*	Nije dodijeljeno: Pomiče se na privremenu zabilješku za trenutni dokument.
*	Not assigned: Finds the next occurrence of the last text searched for any
  specific document.
*	Not assigned: Finds the previous occurrence of the last text searched for
  any specific document.


## Podizbornik Mjesne oznake (NVDA+N)  ##

Korištenjem podizbornika Mjesne oznake u izborniku postavki NVDA, možete
pristupiti: 

*	Mapi posebnih pretraga: otvara mapu prethodno spremljenih posebnih
  pretraživanja.
*	Mapi zabilješki: otvara mapu spremljenih zabilješki.
*	Kopiraj mapu mjesnih oznaka: Možete sačuvati kopiju mape zabilješki.
*	Vrati mjesne oznake: Možete vratiti zabilješke iz mape prethodno
  spremljenih zabilješki.

Napomena: Pozicija zabilješke bazirana je na broju znakova; nadalje, u
dinamičkim stranicama, bolje je koristiti posebnu pretragu, ne zabilješke.

## Changes for 13.0 ##
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

## Changes for 12.0 ##
*	Fixed a critical bug which caused NVDA to crash when trying to open the
  Notes dialog, if chinese characters were selected before saving bookmarks.

## Changes for 11.0 ##
*	Compatible with NVDA 2018.3 or later (required).
*	If needed, you can download the [last version compatible with NVDA
  2017.3][3].

## Changes for 10.0 ##
*	In Edge, gestures associated with bookmarks selection, such as NVDA+k,
  NVDA+shift+k or NVDA+alt+k, will be sent to the application instead of
  trying to move the cursor to bookmarks, to avoid errors, especially in
  long documents.
*	Now specific search is supported in Edge.

## Changes for 9.0
*	Dok se pomičete na zabilješku iz dijaloškog okvira Napomene, pregledni
  kursor slijedi kursor sustava.
*	Naredba za odabir prethodne zabilješke opet radi ispravno.
*	Zabilješke se mogu brisati u dijaloškom okviru Napomene.
*	Now you can assign gestures to save and move to a temporary bookmark for
  each document.

## Promjene u inačici 8.0 ##
*	Izmijenjen način odabira naslova zabilješki, što rješava problem sa nekim
  aplikacijama kao što je ePUB reader.
*	Dodan dijaloški okvir Napomene za dodavanje komentara spremljenim
  zabilješkama i pomak na odabranu poziciju.

## Promjene u inačici 7.0 ##
*	Dijaloški okvir za spremanje niza teksta za posebnu pretragu je
  uklonjen. Ta funkcija sada je uključena u dijaloški okvir Posebno
  pretraživanje, koji je ponovno dizajniran kako bi omogućio različite
  akcije dok pritisnete gumb U redu.
*	Vizualni prikaz dijaloških okvira je poboljšan, pridržavajući se izgleda
  dijaloških okvira u NVDA. 
*	Naredbe Traži sljedeće i Traži prethodno sada će ispravno izvršavati
  pretragu s osjetljivošću na velika i mala slova.
*	Zahtijeva NVDA inačicu 2016.4 ili noviju.
*	Sada možete dodati geste za otvaranje dijaloških okvira Kopiraj i Vrati
  mjesne oznake.
*	NVDA će prikazati poruku kako bi obavijestio da su mjesne oznake kopirane
  ili premještene.

## Promjene u 6.0 ##
* Kada značajke dodatka nisu upotrebljive, geste su poslane u odgovarajuću
  aplikaciju.

## Promjene u 5.0 ##
* Dodana pretraga s osjetljivošću na velika i mala slova.
* Uklonjena opcija za otvaranje dokumentacije iz izbornika Mjesne oznake.
* Prečice koje se lakše pamte.

## Promjene u inačici 4.0 ##
* Promijenjen način definiranja naslova zabilješki, što rješava problem u
  dodatku EPUBREADER za Firefox.
* Pomoć za ovaj dodatak dostupna je u Upravitelju dodacima.

## Promjene u inačici 3.1 ##
* Ažurirani prijevodi i novi jezik.
* Pozicija zabilješke više se ne izgovara u čitanju dokumenta.

## Promjene u inačici 3.0 ##
* Dodana podrška za čitanje dokumenta.

## Promjene u inačici 2.0 ##
* Dodane opcije za spremanje i brisanje različitih pretraga za svaku
  datoteku.
* Omogućen rad s nelatiničnim znakovima.
* Omogućena promjena prečica korištenjem dijaloškog okvira za ulazne geste.

## Promjene u inačici 1.0 ##
* Prva verzija.
* Prevedeno na: brazilski portugalski, farsi, finski, francuski, galicijski,
  njemački, talijanski, japanski, korejski, nepalski, portugalski,
  španjolski, slovački, slovenski, tamilski.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=pm

[2]: https://addons.nvda-project.org/files/get.php?file=pm-dev

[3]: https://addons.nvda-project.org/files/get.php?file=pm-o
