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

*	control+shift+NVDA+s; Opens a dialog that allows you to save a text string   you want to find in the current document. By default, the text previously saved for this file is shown. Delete this text and press Ok button if you wish to remove the text file corresponding to the saved search, or type new text to add another search.
*	control+shift+NVDA+f; opens a dialog with a edit box that shows the last saved search; in this dialog you can also select the previously saved searches from a combo box and choose an action from the next combo box. If there is no available files for specific search in the current document, NVDA will warn you that it is not found any file for specific search.
*	control+shift+NVDA+k; Saves the current position as a bookmark
*	control+shift+NVDA+delete; Deletes the bookmark corresponding to this position.
*	NVDA+k; Moves to the next bookmark.
*	shift+NVDA+k; Moves to the previous bookmark.
*	control+shift+k; Copies to clipboard the file name, without extension, where the place markers data will be saved.

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

## Changes for 6.0 ##
* When the add-on features are not usable, gestures are sent to the
  corresponding application.

## Changes for 5.0 ##
* Added case sensitive search.
* Removed option to open documentation from Place markers menu.
* More intuitive key commands.

## Veranderingen in 4.0 ##
* Fragment identifiers verwijderd uit bestandsnamen zodat problemen met de
  ePUBREADER Firefox add-on vermeden kunnen worden.
* Add-on help is beschikbaar vanuit Add-ons beheren

## Veranderingen in 3.1 ##
* Vertalingen bijgewerkt en een nieuwe taal toegevoegd.
* Bookmarkpositie wordt niet gemeld bij doorbladeren tijdens automatisch
  lezen.

## Veranderingen in 3.0 ##
* Ondersteuning toegevoegd voor doorbladeren.

## Veranderingen in 2.0 ##
* Opties toegevoegd die het mogelijk maken om verschillende zoekopdrachten
  voor ieder bestand op te slaan en te verwijderen.
* Een probleem opgelost met paden die vreemde tekens bevatten
* Sneltoetsen kunnen nu opnieuw toegewezen worden met behulp van het NVDA
  dialoogvenster voor invoergebaren.

## Veranderingen in 1.0 ##
* Eerste versie.
* Vertaald in: Braziliaans Portuguees, Farsi, Fins, Frans, Galicisch, Duits,
  Italiaans, Japans, Koreaans, Nepalees, Portuguees, Spaans, Slovaaks,
  Sloveens, Tamil.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=pm

[2]: http://addons.nvda-project.org/files/get.php?file=pm-dev
