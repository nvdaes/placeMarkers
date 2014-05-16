# place Markers #

* Auteur: Noelia, Chris.
* Download [stabiele versie][1]
* Download [ontwikkelversie][2]

Deze addon dient om specifieke tekstdelen of bookmarks op te slaan en te
zoeken, op webpagina's of documenten met de bladermodus van NVDA. De add-on
kan ook gebruikt worden voor het opzoeken van tekst in meervoudige
invoervelden; wanneer het in dit geval niet mogelijk is om de cursor te
updaten wordt de tekst naar het klembord gekopieerd zodat deze gezocht kan
worden met behulp van andere hulpmiddelen. De plugin slaat de tekstdelen en
bookmarks op in text- en pickle-bestanden. De bestandsnaam is gebaseerd op
de titel en URL van het huidige document.

Deze addon is gebaseerd op SpecificSearch en Bookmark&Search, ontwikkeld
door dezelfde auteur. U moet ze verwijderen om deze addon te kunnen
gebruiken omdat ze gemeenschappelijke sneltoetsen en features hebben.

## Belangrijke commando's: ##

*	control+shift+NVDA+s; Opent een dialoogvenster dat u toelaat een tekststring op te slaan die u in het huidige document wilt vinden. Standaard wordt de voor dit bestand eerder opgeslagen tekst getoond. Verwijder deze tekst en druk op de Ok-knop als u het tekstbestand wilt verwijderen dat overeenkomt met de opgeslagen zoekopdracht, of type nieuwe tekst om een andere zoekopdracht toe te voegen.
*	control+shift+NVDA+f; opent een dialoogvenster met een invoerveld dat de laatst opgeslagen zoekopdracht toont; in dit dialoogvenster kunt u ook de eerder opgeslagen zoekopdrachten selecteren uit een keuzelijst en een actie kiezen uit de volgende keuzelijst. Als er geen beschikbare bestanden zijn voor specifieke zoekopdrachten in het huidige document, zal NVDA u waarschuwen dat geen bestand is gevonden voor specifieke zoekopdrachten.
*	control+shift+NVDA+k; Slaat de huidige positie op als een bookmark
*	control+shift+NVDA+delete; Verwijdert de bookmark die overeenkomt met deze positie.
*	control+shift+k; Gaat naar de volgende bookmark.
*	shift+NVDA+k; Gaat naar de vorige bookmark.
*	NVDA+k; Kopieert de bestandsnaam, zonder extensie, waar degegevens van de place markers zullen worden opgeslagen naar het klembord.

## Place markers Submenu (NVDA+N) ##


Via het Place markers submenu, onder het Instellingen menu, heeft u toegang
tot:

*	Specific search folder: opent een map met eerder opgeslagen specific
  searches.
*	Bookmarks folder; opent een map met de opgeslagen bookmarks.
*	Copy placeMarkers folder; u kan een kopie maken van de map met bookmarks.
*	Restore placeMarkers; u kan uw bookmarks herstellen vanuit een map met
  eerder opgeslagen placeMarkers.
*	Documentation file, in uw gekozen taal indien beschikbaar, of standaard in
  het Engels.

Noot: de bookmark positie is gebaseerd op het aantal tekens; in pagina's met
dynamische inhoud kunt u beter de specific search gebruiken in plaats van de
bookmarks die een specifieke positie opslaan.

## Veranderingen voor 3.1 ##
* Vertalingen bijgewerkt en een nieuwe taal toegevoegd.

## Veranderingen voor 3.0 ##
* Ondersteuning toegevoegd voor doorbladeren.

## Veranderingen voor 2.0 ##
* Opties toegevoegd die het mogelijk maken om verschillende zoekopdrachten
  voor ieder bestand op te slaan en te verwijderen.
* Een probleem opgelost met paden die vreemde tekens bevatten
* Sneltoetsen kunnen nu opnieuw toegewezen worden met behulp van het NVDA
  dialoogvenster voor invoergebaren.


## Veranderingen voor 1.0 ##
* Eerste versie.
* Vertaald in: Braziliaans Portuguees, Farsi, Fins, Frans, Galicisch, Duits,
  Italiaans, Japans, Koreaans, Nepalees, Portuguees, Spaans, Slovaaks,
  Sloveens, Tamil.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=pm

[2]: http://addons.nvda-project.org/files/get.php?file=pm-dev
