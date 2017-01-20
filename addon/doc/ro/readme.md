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

Folosind submeniul Place markers din meniul Preferințe, puteți accesa:

*	Dosarul Căutări specificate: Deschide un director al căutărilor
  specificate salvate înainte.
*	Dosarul semnelor de carte; deschide un folder al semnelor de carte
  salvate.
*	Copiere folder placeMarkers; puteți salva o copie a a folderului cu semne
  de carte.
*	Restaurare placeMarkers; puteți restaura semnele dumneavoastră de carte
  dintr-un folder placeMarkers salvat înainte.

Notă: Poziția semn de carte se bazează pe numărul de caractere; și, prin
urmare, în pagini cu un conținut dinamic este mai bine să utilizați căutarea
specifică, și nu marcajele care economisesc o poziție precisă.

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

[1]: http://addons.nvda-project.org/files/get.php?file=pm

[2]: http://addons.nvda-project.org/files/get.php?file=pm-dev
