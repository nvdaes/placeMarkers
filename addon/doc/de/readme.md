# Lesezeichen #

* Autoren: Noelia, Chris.
* [stabile version:][1] herunterladen
* [Testversion][2] herunterladen

Mit dieser Erweiterung können Sie innerhalb des Lesemodus von NVDA
Suchanfragen oder Lesezeichen speichern Bzw. Suchläufe durchführen. Die
Erweiterung kann auch dazu verwendet werden, Suchanfragen in mehrzeiligen
Elementen zu starten und zu speichern. Wenn der Cursor nicht an die
Fundposition gezogen werden kann, wird die Stelle in die Zwischenablage
kopiert, sodass Sie den Text mittels anderer Tools suchen können. Die
Lesezeichen und Suchanfragen werden dabei in Text- und «pickle»-Dateien
gespeichert. Die Namen der Dateien richten sich dabei nach den Titeln der
angezeigten Dokumente.

Diese Erweiterung basiert auf SpecificSearch und Bookmark&Search. Aufgrund
gemeinsam genutzter Tastenkombinationen und Funktionen sollten Sie diese
beiden Erweiterungen deinstallieren

## Tastenkombinationen: ##

*	control+shift+NVDA+s; Opens a dialog that allows you to save a text string   you want to find in the current document. By default, the text previously saved for this file is shown. Delete this text and press Ok button if you wish to remove the text file corresponding to the saved search, or type new text to add another search.
*	control+shift+NVDA+f; opens a dialog with a edit box that shows the last saved search; in this dialog you can also select the previously saved searches from a combo box and choose an action from the next combo box. If there is no available files for specific search in the current document, NVDA will warn you that it is not found any file for specific search.
*	control+shift+NVDA+k; Saves the current position as a bookmark
*	control+shift+NVDA+delete; Deletes the bookmark corresponding to this position.
*	NVDA+k; Moves to the next bookmark.
*	shift+NVDA+k; Moves to the previous bookmark.
*	control+shift+k; Copies to clipboard the file name, without extension, where the place markers data will be saved.

## Untermenü Sprungmarken (nvda+n) ##


Über das Untermenü Sprungmarken (innerhalb der Einstellungen) können Sie auf
folgende Elemente zugreifen:

*	Suchanfragen: Öffnet einen Ordner, in dem zuvor gespeicherte Suchanfragen
  abgelegt sind.
*	Lesezeichen-Ordner; öffnet einen Ordner mit gespeicherten Lesezeichen
*	Lesezeichen-Ordner kopieren; Speichert eine Kopie des Lesezeichen-Ordners
*	Lesezeichen wiederherstellen: Stellt die Lesezeichen aus einer zuvor
  erstellten sicherung wieder her.
*	Dokumentation: Zeigt die Dokumentation in der eingestellten Sprache an

Anmerkung: Die Lesezeichen basieren auf der Position im Dokument (gezählt in
Zeichen vom Dokumentanfang). Bei dynamischen Webseiten empfielt sich daher,
stattdessen Suchanfragen zu verwenden.


## Changes for 5.0 ##
* Added case sensitive search.
* Removed option to open documentation from Place markers menu.
* More intuitive key commands.

## Änderungen für 4.0 ##
* Removed fragment identifiers from bookmark filenames, which can avoid
  issues in ePUBREADER Firefox add-on.
* Die Hilfe zur Erweiterung ist nun über den Erweiterungs-Manager verfügbar.

## Änderungen für 3.1 ##
* aktualisierte Übersetzungen und neue Sprache.
* Bookmark position is not announced in skim reading.

## Änderungen für 3.0 ##
* Unterstützung für "Navigation während alles lesen" hinzugefügt.

## Änderungen für 2.0 ##
* Option hinzugefügt, verschiedene Suchbegriffe für jede Datei zu speichern
  und zu löschen.
* Fehler behoben, wenn Pfad-Angaben nichtlateinische Zeichen enthalten.
* Tastenkombinationen können nun mittels des Eingaben-Dialogs von NVDA
  geändert werden.


## Änderungen für 1.0 ##
* Erstveröffentlichung.
* übersetzt in: brasilianisches Portugiesisch, Farsi, Finnisch, französisch,
  Galizisch, deutsch, italienisch, japanisch, Koreanisch, Nepalesisch,
  Portugiesisch, Spanisch, Slovakisch, Slovenisch, Tamil.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=pm

[2]: http://addons.nvda-project.org/files/get.php?file=pm-dev
