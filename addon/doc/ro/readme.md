# placeMarkers #
* Autori: Noelia, Chris.
* NVDA compatibility: 2019.3 or later.
* descărcați [versiunea stabilă][1]
* descărcați [versiunea în dezvoltare][2]

Acest supliment este folosit pentru salvarea și căutarea textelor specifice
din stringuri sau semne de carte, pe paginile web sau documente în modul de
navigare al NVDA. De asemenea, poate fi utilizat pentru salvarea și căutarea
stringurilor din textele controalelor linii-multiple. În acest caz, dacă nu
este posibil să actualizați cursorul de scriere, stringul corespunzător va
fi copiat pe planșetă, deci poate fi căutat folosind alte
unelte. Suplimentul salvează stringurile specificate și semnele de carte la
text și fișiere pickle. Numele acestor fișiere este bazat pe titlul și
URL-ul documentului curent.

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
*	control+shift+NVDA+k: Salvează poziția curentă ca un semn de carte. Dacă
  vreți să furnizați un nume pentru el, selectați textul din acea poziție
  înainte de a o salva.
*	control+shift+NVDA+delete: Șterge semnul de carte corespunzător acestei
  poziții.
*	NVDA+k: Deplasează la semnul de carte următor.
*	shift+NVDA+k: Deplasează la semnul de carte precedent.
*	Not assigned: Shows the file name where the place markers data will be
  saved in browse mode, without an extension.
*	alt+NVDA+k: Deschide un dialog cu semnele de carte salvate pentru acest
  document. Puteți scrie o notă pentru fiecare semn de carte. Apăsați
  „Salvare notă” pentru a salva modificările. Prin apăsarea butonului „OK”
  vă deplasați la poziția selectată.
*	Neatribuit: Salvează poziția curentă ca un semn de carte temporar.
*	Neatribuită: Mută la semnul de carte temporar pentru documentul curent.
*	Not assigned: Finds the next occurrence of the last text searched for any
  specific document.
*	Not assigned: Finds the previous occurrence of the last text searched for
  any specific document.


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

[1]: https://addons.nvda-project.org/files/get.php?file=pm

[2]: https://addons.nvda-project.org/files/get.php?file=pm-dev

[3]: https://addons.nvda-project.org/files/get.php?file=pm-o
