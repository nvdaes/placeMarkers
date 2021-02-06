# Záložky #
* Autori): Noelia, Chris.
* Funguje s NVDA od verzie 2019.3.
* Stiahnuť [Stabilnú verzia][1]
* Stiahnuť [Vývojovú verzia][2]

Doplnok dokáže uložiť reťazec pre vyhľadávanie, alebo konkrétne miesto v
dokumente ako záložku. Funguje na webových stránkach a dokumentoch v režime
prehliadania. Funguje tiež vo viacriadkových editačných poliach. Ak sa nedá
aktualizovať systémový kurzor, reťazec je skopírovaný do schránky pre
hľadanie cez iné nástroje. Záložky a reťazce hľadania sú uložené v
súboroch. Názvy súborov sú odvodené od cesty, názvu a URL dokumentu.

## Klávesové skratky: ##

*	ctrl+shift+NVDA+f: Otvorí dialóg hľadania a zobrazí naposledy hľadané
  reťazce. Zo zoznamu môžete vybrať reťazce, ktoré ste už hľadali. Takisto
  môžete vybraté reťazce odstrániťz histórie začiarknutím príslušného
  políčka. Takisto môžete určiť, či aktuálny reťazec hľadania chcete uložiť
  na neskoršie použitie. V tomto okne môžete tiež určiť smer hľadania
  (hľadať predchádzajúce, hľadať nasledujúce), prípadne nehľadať
  vôbec. Takisto môžete začiarknuť rozlišovanie malých a veľkých
  písmen. Hľadanie spustíte tlačidlom OK.
*	ctrl+shift+NVDA+k: Uloží aktuálne miesto ako záložku. Ak chcete záložku
  pomenovať, vyberte pred stlačením skratky nejaký text, ktorý sa použije
  ako názov.
*	ctrl+shift+NVDA+delete: Odstráni záložku pod kurzorom.
*	Nvda+k: Presunie kurzor na nasledujúcu záložku.
*	NVDA+shift+k: Presunie kurzor na predchádzajúcu záložku.
*	Nedefinované: zobrazí v režime prehliadania názov súboru so záložkami pre
  aktuálny dokument.
*	alt+NVDA+k: Otvorí dialóg s uloženými záložkami pre aktuálny dokument. Tu
  môžete k záložkám priradiť poznámky. Tlačidlom vymazať záložku odstránite
  vybratú záložku. Tlačidlom OK presuniete kurzor na vybratú záložku.
*	Nedefinované: Uloží pozíciu kurzora ako dočasnú záložku.
*	Nedefinované: Presunie kurzor na dočasnú záložku.
*	Nedefinované: Nájde nasledujúci výskyt posledného hľadaného reťazca v
  dokumente.
*	Nedefinované: Nájde predchádzajúci výskyt posledného hľadaného reťazca v
  dokumente.


## Podmenu záložky (nvda+n) ##

Podmenu záložky nájdete v menu možnosti NVDA a obsahuje tieto položky:

*	Priečinok s reťazcami hľadania: Otvorí priečinok so súbormi, v ktorých sú
  uložené reťazce pre hľadanie.
*	priečinok so záložkami: otvorí priečinok v ktorom sú uložené súbory so
  záložkami.
*	Zálohovať záložky: skopíruje priečinok so záložkami na určené miesto.
*	Obnoviť záložky: Obnoví záložky z uloženého priečinka.

Poznámka: záložky fungujú na základe počtu znakov. Na dinamických stránkach
je lepšie použiť reťazce hľadania.

## Zmeny vo verzii 14.0 ##
*	Namiesto kopírovania názvu súboru do schránky sa teraz názov zobrazí v
  režime prehliadania. Funkcia nemá priradenú klávesovú skratku.
*	Políčka hľadanie a história sa viac neprekrývajú (opravil Cyrille Bougot).
*	Vyžaduje NVDA od verzie 2019.3.

## Zmeny vo verzii 13.0 ##
*	Pridané funkcie na vyhľadanie predchádzajúceho a nasledujúceho výskytu
  hľadaného reťazca. Skratky je potrebné nastaviť ručne.
*	Vyhľadávanie funguje aj vtedy, ak je otvorený dialóg O NVDA.
*	Políčko rozlišovať malé a veľké písmená sa začiarkne, ak bolo začiarknuté
  pri poslednom hľadaní.
*	Pri aktualizácii sa aktualizujú a presunú aj adresáre so záložkami, pričom
  stále je možné ponechať súbory aj v hlavnom adresári NVDA.
*	Pri zálohovaní sa vytvorí priečinok placeMarkersBackup a do neho sa
  skopírujú príslušné súbory, abysa zabránilo nechcenému odstráneniu súborov
  a priečinkou s dátami. Toto sa deje len v prípade, ak už vybratý priečinok
  nemá  názov placeMarkersBackup.

## Zmeny vo verzii 12.0 ##
*	NVDA viac nepadá pri vybratí čínskych znakov a následnom pokuse napísať
  poznámku k záložke.

## Zmeny vo verzii 11.0 ##
*	Vyžaduje NVDA od verzie 2018.3.
*	Môžete si stiahnuť [Verziu pre NVDA 2017.3][3].

## Zmeny vo verzii 10.0 ##
*	V aplikácii MS edge sú skratky NVDA+k, NVDA+shift+k alebo NVDA+alt+k
  odosielané aj do aplikácie, aby nedochádzalo k chybám, hlavne pri dlhých
  dokumentoch.
*	Špecifické hľadanie funguje aj v aplikácii Edge.

## Zmeny vo verzii 9.0
*	Prezerací kurzor sleduje systémový kurzor pri aktivovaní záložky z
  dialógu.
*	Opravené fungovanie prechodu na predchádzajúcu záložku.
*	Záložky je možné odstrániť z dialógu s poznámkami.
*	Odteraz je možné nastaviť skratky pre uloženie a aktivovanie dočasnej
  záložky.

## Zmeny vo verzii 8.0 ##
*	odstránená identifikácia fragmentov z názvov súborov pre záložky, keďže
  toto spôsobovalo problémy v programe VitalSource Bookshelf ePUB reader.
*	Pridaný dialóg, v ktorom je možné k záložkám písať poznámky a tiež
  presunúť kurzor na vybratú záložku.

## Zmeny vo verzii 7.0 ##
*	Dialóg s uložením špecifického textu hľadania bol nahradený novým. Tu je
  možné určiť presné parametre hľadania.
*	Upravený vzhľad dialógov.
*	Vyhľadanie predchádzajúceho alebo nasledujúceho výskytu rešpektuje
  nastavenie rozlišovania malých a veľkých písmen.
*	Vyžaduje NVDA od verzie 2016.4.
*	Pridaná možnosť nastaviť skratky na zálohu a obnovenie záložiek.
*	NVDA upozorní po dokončení obnovi alebo zálohy záložiek.

## Zmeny vo verzii 6.0 ##
* Ak nie sú dostupné funkcie doplnku, doplnok odošle skratky do aktuálneho
  otvoreného okna príslušnej aplikácie.

## Zmeny vo verzii 5.0 ##
* pridané hľadanie s rozlišovaním malých a veľkých písmen.
* odstránená položka na otvorenie návodu z menu doplnku.
* Prepracované klávesové skratky.

## Zmeny vo verzii 4.0 ##
* odstránená identifikácia fragmentov z názvov súborov pre záložky, keďže
  toto spôsobovalo problémy v doplnku ePUBREADER pre Firefox.
* Návod k doplnku nájdete v správcovi doplnkov.

## Zmeny vo verzii 3.1 ##
* aktualizované a doplnené preklady.
* Pozícia záložky nie je oznamovaná počas rýchleho čítania.

## Zmeny vo verzii 3.0 ##
* pridaná podpora pre rýchle čítanie

## Zmeny vo verzii 2.0 ##
* pridaná možnosť uložiť rôzne reťazce hľadania pre rôzne dokumenty.
* opravená chyba, ktorá sa vyskytovala, ak cesta neobsahovala len ascii
  znaky.
* Skratky môžete zmeniť v nastaveniach klávesových skratiek NVDA.

## Zmeny vo verzii 1.0 ##
* prvé vydanie
* Pridané jazyky: Brazílska portugalčina, fínčina, francúzština,
  galícijčina, nemčina, taliančina, japončina, kórejčina, nepálčina,
  Perzština, Portugalčina, španielčina, slovenčina, slovinčina, Tamilčina.


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=pm

[2]: https://addons.nvda-project.org/files/get.php?file=pm-dev

[3]: https://addons.nvda-project.org/files/get.php?file=pm-o
