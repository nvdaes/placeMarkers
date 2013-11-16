# Könyvjelzők #
* Készítők: Noelia, Chris.
* download [stable version][1]
* download [development version][2]

Ez a kiegészítő különböző karakterláncok, vagy könyvjelzők mentésére, és
keresésére használható dokumentumokban és internetes oldalakon, az nvda
böngésző módjában. A bővítmény a meghatározott karakterláncokat és
könyvjelzőket szöveges file-okba menti. A mentett file-ok neve mindig az
aktuális dokumentum címe, vagy url-je lesz.

Ez a kiegészítő a "SpecificSearch" és a "Bookmark&Search" bővítményekre
épül, amiket ugyanezen bővítmény készítője fejlesztett. Ezeket ajánlott
eltávolítani, amikor a "placemarkers"-t használjuk, hiszen ugyanolyan
szolgáltatásokkal, és billentyűparancsokkal rendelkezik.

## Billentyűparancsok: ##

*	control+shift+NVDA+s; Opens a dialog that allows you to save a text string   you want to find in the current document. By default, the text previously saved for this file is shown. Delete this text and press Ok button if you wish to remove the text file corresponding to the saved search, or type new text to add another search.
*	control+shift+NVDA+f; opens a dialog with a edit box that shows the last saved search; in this dialog you can also select the previously saved searches from a combo box and choose an action from the next combo box. If there is no available files for specific search in the current document, NVDA will warn you that it is not found any file for specific search.
*	control+shift+NVDA+k; Saves the current position as a bookmark
*	control+shift+NVDA+delete; Deletes the bookmark corresponding to this position.
*	control+shift+k; Moves to the next bookmark.
*	shift+NVDA+k; Moves to the previous bookmark.
*	NVDA+k; Copies to clipboard the file name, without extension, where the place markers data will be saved.

## Helyjelzők almenü (az NVDA menüben) ##


A könyvjelzők almenü elérhető A Beállítások almenüből. Itt a következőkhöz
fér hozzá:

*	Speciális keresési mappa: Megnyitja az elmentett speciális keresések
  mappáját.
*	Könyvjelzők mappa; Megnyitja az elmentett könyvjelzők mappáját
*	A helyjelzők mappájának másolása
*	Könyvjelzők visszaállítása; visszaállíthatja előzőleg elmentett
  helyjelzőit egy mappából.
*	Dokumentáció, a jelenleg használt nyelven (ha elérhető), vagy angolul.

Megjegyzés: A könyvjelzők karakterszámot használnak. Dinamikus oldalak
esetén eredményesebb a Speciális Keresés funkció használata.


## Changes for 3.0 ##
* Added support for skim reading.

## A 2.0 verzió változásai ##
* Added options to save and delete different searches for each file.
* Fixed bug which broke when paths contained non latin characters.
* Shortcuts can now be reassigned using the NVDA gesture input dialog.


## Az 1.0 verzió változásai ##
* Első kiadás
* Lefordítva az alábbi nyelvekre: brazíliai portugál, perzsa, finn, francia,
  galíciai, magyar, német, olasz, japán, kóreai, nepáli, portugál, spanyol,
  szlovák, szlovén, tamil.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=pm[1]:
http://addons.nvda-project.org/files/get.php?file=pm

[2]: http://addons.nvda-project.org/files/get.php?file=pm-dev
