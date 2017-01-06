# placeMarkers #

* Autori: Noelia, Chris.
* Descărcați [versiunea stabilă][1]
* Descărcați [versiunea în dezvoltare][2]

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
*	control+shift+NVDA+k: Salvează poziția curentă ca un semn de carte.
*	control+shift+NVDA+delete: Șterge semnul de carte corespunzător acestei
  poziții.
*	NVDA+k: Deplasează la semnul de carte următor.
*	shift+NVDA+k: Deplasează la semnul de carte precedent.
*	control+shift+k: Copiază pe planșetă numele fișierului unde data place
  markers va fi salvată, fără o extensie.


## Submeniul Place markers (NVDA+N) ##

Using the Place markers submenu under NVDA's Preferences menu, you can
access:

*	Dosarul Căutări specificate: Deschide un director al căutărilor
  specificate salvate înainte.
*	Bookmarks folder: Opens a folder of the saved bookmarks.
*	Copy placeMarkers folder: You can save a copy of the bookmarks folder.
*	Restore placeMarkers: You can restore your bookmarks from a previously
  saved placeMarkers folder.

Note: The bookmark position is based on the number of characters; and
therefore in dynamic pages it is better to use the specific search, not
bookmarks.

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

[1]: http://addons.nvda-project.org/files/get.php?file=pm

[2]: http://addons.nvda-project.org/files/get.php?file=pm-dev
