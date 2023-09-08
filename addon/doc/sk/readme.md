# Záložky #

* Autori): Noelia, Chris.

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

## Klávesové skratky: ##

*	ctrl+shift+NVDA+f: Otvorí dialóg hľadania a zobrazí naposledy hľadané
  reťazce. Zo zoznamu môžete vybrať reťazce, ktoré ste už hľadali. Takisto
  môžete vybraté reťazce odstrániťz histórie začiarknutím príslušného
  políčka. Takisto môžete určiť, či aktuálny reťazec hľadania chcete uložiť
  na neskoršie použitie. V tomto okne môžete tiež určiť smer hľadania
  (hľadať predchádzajúce, hľadať nasledujúce), prípadne nehľadať
  vôbec. Takisto môžete začiarknuť rozlišovanie malých a veľkých
  písmen. Hľadanie spustíte tlačidlom OK.
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
*	Nedefinované: Nájde nasledujúci výskyt posledného hľadaného reťazca v
  dokumente.
*	Nedefinované: Nájde predchádzajúci výskyt posledného hľadaného reťazca v
  dokumente.


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

## Changes for 23.0
* The add-on works again with Microsoft Word.

## Changes for 22.0
* We can move to bookmarks and delete them with UIA enabled, thanks to
  Abdel.

## Changes for 21.0
* Bookmarks can be saved with UIA enabled in browsers based on Chromium,
  thanks to Abdel.

## Changes for 20.0
* Requires NVDA 2022.1 or later.

## Changes for 19.0 ##
* The add-on cannot be run on secure screens.

## Changes for 18.0 ##
* The command to see the path for placeMarkers shows if there are permanent
  bookmarks, text for specific search or a temporary bookmark for the
  current document.

## Changes for 17.0 ##
* Fixed a bug which didn't allow to save place markers in some documents.
* Fixed translated strings making translations to work properly.

## Changes for 16.0 ##
* Compatible with NVDA 2021.1 or later (required).
* Skim reading is supported when moving to temporary bookmarks.
* If needed, you can download [other
  versions](https://github.com/nvdaes/placeMarkers/releases).

## Changes for 15.0 ##
* When reading with say all in browse mode, the specific find next and
  specific find previous commands do not stop reading anymore if Allow skim
  reading option is enabled, according to find next and find previous
  commands from NVDA 2020.4.
* When the Specific search dialog is opened after running the Specific find
  previous command, the Search previous option will be selected.

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

[3]: https://www.nvaccess.org/addonStore/legacy?file=pm-o
