# Könyvjelzők #

* Készítők: Noelia, Chris.
* NVDA compatibility: 2018.3 to 2019.1
* [stabil verzió][1] letöltése
* [fejlesztői verzió][2] letöltése

This addon is used for saving and searching specific text strings or
bookmarks. It can be used  on web pages or documents in NVDA's browse
mode. It can also be used for saving or searching strings of text in
multi-line controls; in this case, if it's not possible to update the caret,
the corresponding string will be copied to the clipboard, so that it can be
searched using other tools.  The plugin saves the specified strings and
bookmarks to files whose name is based on the title and URL of the current
document.  This addon is based on SpecificSearch and Bookmark&Search,
developed by the same author. You should uninstall them to use this one,
since they have common keystrokes and features.

## Billentyűparancsok: ##

*	control+shift+NVDA+f: Opens a dialog with an edit box that shows the last
  saved search; in this dialog you can also select the previously saved
  searches from a combo box or remove the selected string from the history
  using a checkbox. You can choose if the text contained in the edit box
  will be added to the history of your saved texts. Finally, choose an
  action from the next group of radio buttons (between Search next, Search
  previous or Don't search), and specify if NVDA will make a case sensitive
  search. When you press okay, NVDA will search for this string.
*	control+shift+NVDA+k: Saves the current position as a bookmark. If you
  want to provide a name for this bookmark, select some text from this
  position before saving it.
*	control+shift+NVDA+delete: Deletes the bookmark corresponding to this
  position.
*	NVDA+k: Moves to the next bookmark.
*	shift+NVDA+k: Moves to the previous bookmark.
*	control+shift+k: Copies the file name where the place markers data will be
  saved to the clipboard, without an extension.
*	alt+NVDA+k: Opens a dialog with the bookmarks saved for this document. You
  can write a note for each bookmark; press Save note to save
  changes. Pressing Delete you can remove the selected bookmark. Pressing OK
  you can move to the selected position.
*	Not assigned: Saves a position as a temporary bookmark.
*	Not assigned: Moves to the temporary bookmark for the current document.


## Helyjelzők almenü (az NVDA menüben) ##

Using the Place markers submenu under NVDA's Preferences menu, you can
access:

*	Speciális keresési mappa: Megnyitja az elmentett speciális keresések
  mappáját.
*	Bookmarks folder: Opens a folder of the saved bookmarks.
*	Copy placeMarkers folder: You can save a copy of the bookmarks folder.
*	Restore placeMarkers: You can restore your bookmarks from a previously
  saved placeMarkers folder.

Note: The bookmark position is based on the number of characters; and
therefore in dynamic pages it is better to use the specific search, not
bookmarks.

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
*	When moving to a bookmark from the Notes dialog, the review cursor follows
  the system cursor.
*	The command to select the previous bookmark works properly again.
*	Bookmarks can be deleted from the Notes dialog.
*	Now you can assign gestures to save and move to a temporary bookmark for
  each document.

## Changes for 8.0 ##
*	Removed fragment identifiers from bookmark filenames, which can avoid
  issues in the VitalSource Bookshelf ePUB reader.
*	Added a Notes dialog, to associate comments for saved bookmarks and move
  to the selected position.

## Changes for 7.0 ##
*	The dialog to save a string of text for specific search has been
  removed. This functionality is now included in the Specific search dialog,
  which has been redesigned to allow different actions when pressing the OK
  button.
*	The visual presentation of the dialogs has been enhanced, adhering to the
  appearance of the dialogs shown in NVDA.
*	Performing a Find Next or Find Previous command in Browse Mode will now
  correctly do a case sensitive search if the original Find was case
  sensitive.
*	Requires NVDA 2016.4 or later.
*	Now you can assign gestures to open the Copy and Restore place markers
  dialogs.
*	NVDA will present a message to notify when place markers have been copied
  or restored with the corresponding dialogs.

## A 6.0 verzió változásai ##
* Amikor a kiegészítő szolgáltatásai nem használhatók, akkor a program
  átadja a billentyűparancsait az aktuális alkalmazásnak.

## Az 5.0 verzió változásai ##
* Kis- és nagybetűket megkülönböztető keresési lehetőség hozzáadva.
* Eltávolítva a dokumentáció megnyitásának lehetősége a kiegészítő
  menüjéből.
* Sokkal logikusabb billentyűparancsok.

## A 4.0 verzió változásai ##
* Eltávolításra került a fragment azonosító a könyvjelzők fájlneveiből, így
  elkerülhető az ePUBREADER Firefox bővítmény használatakor jelentkező hiba.
* A kiegészítő súgója elérhető a bővítmények kezelése párbeszédablakról is.

## A 3.1 verzió változásai ##
* Fordítások frissítése, és egy új nyelv hozzáadása
* Átfutó olvasás közben nem hangzik el a könyvjelző aktuális pozíciója

## A 3.0 verzió változásai ##
* Az átfutó olvasás támogatásának hozzáadása

## A 2.0 verzió változásai ##
* A különböző keresések elmenthetők és törölhetők minden fájlnál.
* A program már jól működik hogyha az elérésiút tartalmaz nem latin
  karaktereket.
* A billentyűparancsok megváltoztathatóak az NVDA Beviteli parancsok
  beállítás ablakában.

## Az 1.0 verzió változásai ##
* Első kiadás
* Lefordítva az alábbi nyelvekre: brazíliai portugál, perzsa, finn, francia,
  galíciai, magyar, német, olasz, japán, kóreai, nepáli, portugál, spanyol,
  szlovák, szlovén, tamil.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=pm

[2]: https://addons.nvda-project.org/files/get.php?file=pm-dev

[3]: https://addons.nvda-project.org/files/get.php?file=pm-o
