# placeMarkers #

* Autori: Noelia, Chris.
* Descărcați [versiunea stabilă][1]
* Descărcați [versiunea în dezvoltare][2]

Acest add-on este folosit pentru salvarea și căutarea textelor specifice din
stringuri sau semne de carte, pe paginile web sau documente în modul de
navigare al NVDA. De asemenea, poate fi utilizat pentru salvarea și căutarea
stringurilor din textele controalelor linii-multiple. În acest caz, dacă nu
este posibil să actualizați caret-ul, stringul corespunzător va fi copiat pe
planșetă, deci poate fi căutat folosind alte unelte. Suplimentul salvează
stringurile specificate și semnele de carte la text și fișiere
pickle. Numele acestor fișiere este bazat pe titlul și URL-ul documentului
curent.

Acest add-on este bazat pe SpecificSearch și Bookmark&Search, dezvoltate de
același autor. Ar trebui să le dezinstalați pentru a-l uutiliza pe
acesta. Aceste extensii au combinații de taste și caracteristici comune.

## Combinații de taste: ##

*	control+shift+NVDA+s; Deschide un dialog care vă permite să salvați un text string pe care vreți să-l găsiți în documentul curent. În mod implicit, textul salvat înainte pentru această filă este arătat. Ștergeți acest text și apăsați butonul OK dacă doriți să ștergeți fila text corespunzătoare căutării salvate, sau scrieți un nou text pentru a adăuga altă căutare.
*	control+shift+NVDA+f; Deschide un dialog cu o casetă de editare care arată ultima căutare salvată; în acest dialog puteți, de asemenea, să selectați căutările salvate înainte dintr-o casetă combinată și să alegeți o acțiune pentru caseta combinată următoare. Dacă nu există file disponibile pentru căutarea specificată în documentul curent, NVDA vă va atenționa că nu a fost găsită nicio filă pentru căutarea specificată.
*	control+shift+NVDA+k; Salvează poziția curentă ca un semn de carte
*	control+shift+NVDA+delete; Șterge semnul de carte corespunzător acestei poziții.
*	NVDA+k; Mută la următorul semn de carte.
*	shift+NVDA+k; Mută la semnul de carte anterior.
tcontrol+shift+k; Copiază pe planșetă numele fișierului, fără extensie, unde data locului semnelor de carte va fi salvată.

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
*	Fișierul Documentație, în limba selectată dacă este disponibilă, sau
  engleză (limba implicită).

Notă: Poziția semn de carte se bazează pe numărul de caractere; și, prin
urmare, în pagini cu un conținut dinamic este mai bine să utilizați căutarea
specifică, și nu marcajele care economisesc o poziție precisă.

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
