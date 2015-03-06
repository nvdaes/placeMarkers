# Záložky #

* Autori): Noelia, Chris.
* Stiahnuť [Stabilná verzia][1]
* Stiahnuť [Vývojová verzia][2]

Doplnok dokáže uložiť reťazec pre vyhľadávanie, alebo konkrétne miesto v
dokumente ako záložku. Funguje na webových stránkach a dokumentoch v režime
prehliadania. Funguje tiež vo viacriadkových editačných poliach. Ak sa nedá
aktualizovať systémový kurzor, reťazec je skopírovaný do schránky pre
hľadanie cez iné nástroje. Záložky a reťazce hľadania sú uložené v textových
a pickle súboroch. Názvy súborov sú odvodené od cesty a názvu dokumentu.

Doplnok využíva funkcie predošlých doplnkov známych ako SpecificSearch a
Bookmark&Search, ktoré vytvoril ten istý autor. Tieto staré doplnky
odinštalujte, lebo majú spoločné funkcie a klávesové skratky.

## Klávesové skratky: ##

*	control+shift+NVDA+s; Opens a dialog that allows you to save a text string   you want to find in the current document. By default, the text previously saved for this file is shown. Delete this text and press Ok button if you wish to remove the text file corresponding to the saved search, or type new text to add another search.
*	control+shift+NVDA+f; opens a dialog with a edit box that shows the last saved search; in this dialog you can also select the previously saved searches from a combo box and choose an action from the next combo box. If there is no available files for specific search in the current document, NVDA will warn you that it is not found any file for specific search.
*	control+shift+NVDA+k; Saves the current position as a bookmark
*	control+shift+NVDA+delete; Deletes the bookmark corresponding to this position.
*	NVDA+k; Moves to the next bookmark.
*	shift+NVDA+k; Moves to the previous bookmark.
*	control+shift+k; Copies to clipboard the file name, without extension, where the place markers data will be saved.

## Podmenu záložky (nvda+n) ##


Podmenu záložky nájdete v menu možnosti NVDA a obsahuje tieto položky:

*	Priečinok s reťazcami hľadania: Otvorí priečinok so súbormi, v ktorých sú
  uložené reťazce pre hľadanie.
*	priečinok so záložkami: otvorí priečinok v ktorom sú uložené súbory so
  záložkami.
*	Zálohovať záložky: skopíruje priečinok so záložkami na určené miesto.
*	Obnoviť záložky; Obnoví záložky z uloženého priečinka.
*	Dokumentácia: zobrazí návod v Slovenčine.

Poznámka: záložky fungujú na základe počtu znakov. Na dinamických stránka je
lepšie použiť reťazce hľadania.


## Changes for 5.0 ##
* Added case sensitive search.
* Removed option to open documentation from Place markers menu.
* More intuitive key commands.

## Zmeny vo verzii 4.0 ##
* odstránená identifikácia fragmentov z názvov súborov pre záložky, keďže
  toto spôsobovalo problémy v doplnku ePUBREADER pre Firefox.
* Návod k doplnku nájdete v správcovi doplnkov.

## Zmeny vo verzii 3.3 ##
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

[1]: http://addons.nvda-project.org/files/get.php?file=pm

[2]: http://addons.nvda-project.org/files/get.php?file=pm-dev
