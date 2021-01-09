# Oznake pozicija (placeMarkers) #
* Autori: Noelia, Chris.
* NVDA kompatibilnost: 2019.3 ili novija.
* Preuzmi [stabilnu verziju][1]
* preuzmi [razvojnu verziju][2]

Ovaj se dodatak koristi za spremanje i pretraživanje određenih tekstualnih
nizova ili knjižnih oznaka. Može se koristiti za web stranice ili za
dokumente u NVDA modusu čitanja. Može se koristiti i za spremanje i
pretraživanje teksta u višerednim kontrolama. Ako nije moguće aktualizirati
tekstualni kursor, odgovarajući niz će se kopirati u međuspremnik, kako bi
se mogao pretraživati pomoću drugih alata. Dodatak sprema navedene nizove i
knjižne oznake u datoteke, čije se ime temelji na naslovu i URL-u
trenutačnog dokumenta. Ovaj se dodatak temelji na „SpecificSearch” i na
„Bookmark&Search”, koje je razvio isti autor. Da bi se ovaj dodatak mogao
koristiti, moraju se deinstalirati navedeni dodaci, jer imaju zajedničke
tipke i funkcije.

## Tipkovnički prečaci: ##

*	kontrol+šift+NVDA+f: Otvara dijaloški okvir s uređivačkim poljem, koje
  prikazuje posljednju spremljenu pretragu. Moguće je odabrati prethodno
  spremljene pretrage iz odabirnog okvira ili ukloniti odabrani niz iz
  povijesti, pomoću potvrdnog okvira. Moguće je odabrati, hoće li se tekst u
  uređivačkom polju dodati u povijest spremljenih tekstova. Kao zadnje,
  odaberi radnju iz sljedeće grupe izbornih gumba (Traži sljedeću, Traži
  prethodnu ili Ne traži), te odredi osjetljivost na velika i mala slova
  tijekom pretrage. Pritiskom gumba „U redu”, NVDA će tražiti taj niz.
*	kontrol+šift+NVDA+k: Sprema trenutačnu poziciju kao knjižnu oznaku. Ako
  toj knjižnoj oznaci želiš dodijeliti ime, odaberi neki tekst ove pozicije
  prije spremanja.
*	kontrol+šift+NVDA+delete: Briše knjižnu oznaku koja odgovara ovoj
  poziciji.
*	NVDA+k: Premješta se na sljedeću knjižnu oznaku.
*	šift+NVDA+k: Premješta se na prethodnu knjižnu oznaku.
*	Nije dodijeljeno: Pokazuje naziv datoteke u modusu čitanja, bez nastavka.
*	alt+NVDA+k: Otvara dijaloški okvir sa spremljenim knjižnim oznakama za
  ovaj dokument. Za svaku knjižnu oznaku je moguće upisati napomenu;
  pritisni „Spremi napomenu” za spremanje promjene. Pritiskom na „Odustani”
  brišeš odabranu knjižnu oznaka. Pritiskom na „U redu” premještaš se na
  odabranu poziciju.
*	Nije dodijeljeno: Sprema poziciju kao privremenu knjižnu oznaku.
*	Nije dodijeljeno: Pomiče se na privremenu knjižnu oznaku za trenutačni
  dokument.
*	Nije dodijeljeno: Nalazi sljedeći slučaj zadnje pretrage teksta za svaki
  određeni dokument.
*	Nije dodijeljeno: Nalazi prethodni slučaj zadnje pretrage teksta za svaki
  određeni dokument.


## Podizbornik „Oznake pozicija” (NVDA+N)  ##

Korištenjem podizbornika „Oznake pozicija” u izborniku NVDA postavki, možeš
pristupiti:

*	Mapi određene pretrage: otvara mapu prethodno spremljenih određenih
  pretraživanja.
*	Mapi knjižnih oznaka: otvara mapu spremljenih knjižnih oznaka.
*	Kopiraj mapu za „Oznake pozicija”: omogućuje spremanje kopije mape
  knjižnih oznaka.
*	Obnovi „Oznake pozicija”: omogućuje obnovljanje knjižnih oznaka iz mape
  prethodno spremljenih knjižnih oznaka.

Napomena: Pozicija knjižne oznake se zasniva na broju znakova. Stoga je u
dinamičkim stranicama bolje koristiti određenu pretragu, a ne knjižne
oznake.

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

[1]: https://addons.nvda-project.org/files/get.php?file=pm

[2]: https://addons.nvda-project.org/files/get.php?file=pm-dev

[3]: https://addons.nvda-project.org/files/get.php?file=pm-o
