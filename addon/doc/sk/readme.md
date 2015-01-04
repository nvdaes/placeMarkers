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

*	control+shift+NVDA+s; otvorí dialóg, v ktorom môžete nastaviť textový reťazec , ktorý chcete hľadať v aktuálnom dokumente.Predvolene sa zobrazí text, ktorý ste uložili pred tým. Ak chcete text odstrániť, vymažte ho a stlačte OK. Ak chcete zadať nový reťazec, napíšte ho a stlačte OK.
*	control+shift+NVDA+f; zobrazí posledne hľadané reťazce. V zozname môžete vybrať požadovanú akciu. Ak neexistujú žiadne reťazce, NVDA na to upozorní.
*	control+shift+NVDA+k; uloží aktuálnu pozíciu kurzora ako záložku.
*	control+shift+NVDA+delete; odstráni záložku z pozície kurzora.
*	control+shift+k; presunie kurzor na nasledujúcu záložku.
*	shift+NVDA+k; presunie kurzor na predchádzajúcu záložku.
*	NVDA+k; Skopíruje do schránky názov súboru bez prípony, v ktorom sú uložené dáta doplnku.

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
