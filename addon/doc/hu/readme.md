# Könyvjelzők #

* Készítők: Noelia, Chris.
* letöltés [stabil verzió][1]  letöltése
* letöltés [fejlesztői verzió][2]  letöltése

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

*	control+shift+NVDA+s: Megnyit egy párbeszédablakot, amely lehetővé teszi egy szövegrészlet elmentését, amit szeretne megtalálni a későbbiekben ebben a dokumentumban. Alapértelmezetten a mező az előzőleg elmentett szöveget tartalmazza. Törölje ki és nyomja meg az ok gombot ha el szeretné távolítani az elmentett keresések közül ezt a fájlt, vagy gépeljen be egy másik szöveget új keresés hozzáadásához.
*	control+shift+NVDA+f: Megnyit egy párbeszédablakot egy szerkesztőmezővel, ami a legutóbb elmentett keresést mutatja. Ezen a párbeszédablakon egy kombinált listamezőben kiválaszthatja a legutóbb elmentett kereséseket, a következő kombinált listamezőben kiválaszthatja mit szeretne velük tenni. Ha nincs elérhető fájl az aktuális dokumentumban a speciális kereséshez, akkor az NVDA figyelmeztet, hogy nem található fájl a speciális kereséshez.
*	control+shift+NVDA+k: Az aktuális pozíciót elmenti könyvjelzőként.
*	control+shift+NVDA+delete: Törli az aktuális pozícióhoz tartozó könyvjelzőt.
*	NVDA+k: A következő könyvjelzőhöz lép.
*	shift+NVDA+k: Az előző könyvjelzőhöz lép.
*	Control+shift+k: A vágólapra másolja annak a fájlnak a nevét, kiterjesztés nélkül, ahová a helyjelző adatok rögzítésre kerülnek.

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

[1]: http://addons.nvda-project.org/files/get.php?file=pm[1]:
http://addons.nvda-project.org/files/get.php?file=pm

[2]: http://addons.nvda-project.org/files/get.php?file=pm-dev
