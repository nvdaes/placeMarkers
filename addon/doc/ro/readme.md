# placeMarkers #

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

## Combinații de taste: ##

*	control+shift+NVDA+f: Deschide un dialog cu o casetă de editare care arată
  ultima căutare salvată; în acest dialog puteți, de asemenea, să selectați
  căutările precedente salvate dintr-o casetă combinată sau să ștergeți
  fraza selectată din istoric folosind o casetă de bifat. Puteți alege dacă
  textul conținut în caseta de editare va fi adăugat la istoricul textelor
  salvate. În final, alegeți o acțiune din următorul grup al butoanelor
  rotative (între caută următorul, caută anteriorul, sau nu căuta), și
  specificați dacă NVDA va face un caz senzitiv de căutare. Când apăsați OK,
  NVDA va căuta pentru această frază.
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
*	Not assigned: Finds the next occurrence of the last text searched for any
  specific document.
*	Not assigned: Finds the previous occurrence of the last text searched for
  any specific document.


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

## Changes for 14.0 ##
*	The command to copy the name of the file where place markers data will be
  saved has been replaced by a command which shows this file name in browse
  mode. This is not assigned to a gesture.
*	The "Text to search" field does not overlap the "Saved text" field
  anymore. (Thanks to Cyrille Bougot).
*	Requires NVDA 2019.3 or later.

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

## Modificări în 12.0 ##
*	S-a rezolvat o problemă critică care făcea ca NVDA să dea crash când
  încerca să deschidă dialogul de note dacă caractere chinezești erau
  selectate înainte de salvarea semnelor de carte.

## Modificări în 11.0 ##
*	Compatibil cu NVDA 2018.3 sau mai nou (necesar).
*	Dacă e musai, puteți descărca [ultima versiune compatibilă cu NVDA
  2017.3][3].

## Modificări în 10.0 ##
*	În Edge, gesturile asociate cu selectarea semnelor de carte, cum ar fi
  NVDA+k, NVDA+shift+k sau NVDA+alt+k, vor fi trimise la aplicație în loc să
  încerce să mute cursorul la semne de carte ca să evite erori, în special
  din documentele bogate în conținut.
*	Nicio căutare specifică nu este suportată în Edge.

## Modificări în 9.0
*	Atunci când se deplasează la un semn de carte de la dialogul notelor,
  cursorul de examinare îl urmărește pe cel al sistemului.
*	Comanda pentru selectarea semnului de carte anterior funcționează din nou
  așa cum trebuie.
*	Semnele de carte pot fi șterse din dialogul notelor.
*	Acum poți atribui gesturi pentru a salva și pentru a te deplasa la un semn
  de carte temporar.

## Modificări în 8.0 ##
*	Au fost eliminate identificatori de fragment din numele fișierului semn de
  carte, care pot evita problemele în VitalSource Bookshelf ePUB reader.
*	A fost adăugat un dialog de note pentru asocierea comentariilor pentru
  semnele de carte salvate și pentru deplasarea la poziția selectată.

## Modificări în 6.0 ##
*	Dialogul pentru salvarea unui string a textului pentru căutarea
  specificată a fost șters. Această funcționalitate acum este inclusă în
  dialogul căutării specificate care a fost reproiectat pentru a permite
  acțiuni diferite la apăsarea butonului OK.
*	Prezentarea vizuală a dialogurilor a fost îmbunătățită, aderând la
  aspectul dialogurilor afișate în NVDA.
*	Efectuând comanda găsirea anterioară sau găsirea următoare în modul
  navigare acum va face în mod corect un caz de căutare sensitiv, dacă
  căutarea originală este în cazul sensitiv.
*	Necesită 2016.4 sau mai nou.
*	Acum poți atribui gesturi pentru a deschide dialogurile copiere și
  restaurare place marker.
*	NVDA va prezenta când place markerul a fost copiat sau restaurat cu
  dialogurile corespunzătoare.

## Modificări în 6.0 ##
* Când caracteristicile add-on-ului nu sunt utilizabile, gesturile sunt
  trimise la aplicația corespunzătoare.

## Modificări în 5.0 ##
* A fost adăugată căutarea sensibilă.
* A fost eliminată opțiunea pentru deschiderea documentației din meniul
  Place markers.
* Multe comenzi de taste intuitive.

## Modificări în 4.0 ##
* Au fost eliminate identificatori de fragment din numele fișierului semn de
  carte, care pot evita problemele în ePUBREADER Firefox add-on.
* Ghidul add-onului este disponibil în managerul de add-on-uri.

## Modificări în 3.1 ##
* Actualizări la traduceri și o limbă nouă adăugată.
* Poziția semnului de carte nu este anunțată în citirea skim -ului.

## Modificări în 3.0 ##
* A fost adăugat suportul pentru citirea skim -ului.

## Modificări în 2.0 ##
* Au fost adăugate opțiuni pentru a salva și a șterge căutări diferite
  pentru fiecare filă.
* A fost t reparată o eroare cu calea care conținea caractere non latine.
* Scurtăturile pot fi reatribuite utilizând dialogul gesturilor de intrare.

## Modificări în 1.0 ##
* Versiunea inițială.
* Tradusă în: Portugheză Braziliană, Persană, Finlandeză, Franceză,
  Galiciană, Germană, Italiană, Japoneză, Coreeană, Nepaleză, Portugheză,
  Spaniolă, Slovacă, Slovenă, Tamilă.

[[!tag dev stable]]

[3]: https://www.nvaccess.org/addonStore/legacy?file=pm-o
