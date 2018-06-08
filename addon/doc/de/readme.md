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
gespeichert. Die Namen der Dateien richten sich dabei nach den Titeln und
URLs der angezeigten Dokumente.

## Tastenkombinationen: ##

*	STRG+Umschalt+NVDA+f: Öffnet einen Dialog mit einem Eingabefeld, in dem
  die zuletzt gespeicherte Suche angezeigt wird. In diesem Dialog können Sie
  auch die zuvor gespeicherten Suchen aus einem Kombinationsfeld auswählen
  oder die ausgewählte Zeichenkette über ein Kontrollkästchen aus dem
  Verlauf entfernen. Sie können wählen, ob der im Eingabefeld enthaltene
  Text im Verlauf Ihrer gespeicherten Texte aufgenommen werden soll. Wählen
  Sie abschließend eine Aktion aus der nächsten Gruppe von Auswahlschaltern
  aus (weiter suchen, Rückwärtssuche oder keine Suche) und geben Sie an, ob
  NVDA die Groß- und Kleinschreibung berücksichtigen soll. Wenn Sie auf OK
  drücken, sucht NVDA nach dieser Zeichenfolge.
*	STRG+Umschalt+NVDA+k: Speichert die aktuelle Position als
  Lesezeichen. Wenn Sie einen Namen für dieses Lesezeichen vergeben möchten,
  wählen Sie einen Teil vom Text an dieser Position aus, bevor Sie das
  Lesezeichen speichern.
*	STRG+Umschalt+NVDA+Entfernen: Löscht das Lesezeichen an der aktuellen
  Position.
*	NVDA+k: Wechselt zum nächsten Lesezeichen.
*	Umschalt+NVDA+k: Wechselt zum vorherigen Lesezeichen.
*	STRG+Umschalt+k: Kopiert den Dateinamen (ohne Dateierweiterung), unter
  welchem die Daten der Lesezeichen in der Zwischenablage gespeichert
  werden.
*	alt+NVDA+k: Opens a dialog with the bookmarks saved for this document. You
  can write a note for each bookmark; press Save note to save
  changes. Pressing Delete you can remove the selected bookmark. Pressing OK
  you can move to the selected position.
*	Not assigned: Saves a position as a temporary bookmark.
*	Not assigned: Moves to the temporary bookmark for the current document.


## Lesezeichen Untermenü (nvda+n) ##

Über das Untermenü Lesezeichen in NVDA-Einstellungen können Sie auf folgende
Elemente zugreifen:

*	Suchanfragen: Öffnet einen Ordner, in dem zuvor gespeicherte Suchanfragen
  abgelegt sind.
*	Lesezeichen-Ordner: öffnet einen Ordner mit gespeicherten Lesezeichen
*	Lesezeichen-Ordner kopieren: Speichert eine Kopie des Lesezeichen-Ordners
*	Lesezeichen wiederherstellen: Stellt die Lesezeichen aus einem zuvor
  gespeicherten Lesezeichen-Ordner wieder her.

Anmerkung: Die Lesezeichen basieren auf der Position im Dokument (welche in
Zeichen vom Dokumentanfang gemessen wird). Bei dynamischen Webseiten
empfielt sich daher stattdessen Suchanfragen zu verwenden.


## Changes for 10.0 ##
*	In Edge, gestures associated with bookmarks selection, such as NVDA+k,
  NVDA+shift+k or NVDA+alt+k, will be sent to the application instead of
  trying to move the cursor to bookmarks, to avoid errors, especially in
  long documents.
*	Now specific search is supported in Edge.

## Changes for 9.0
*	When moving to a bookmark from the Notes dialog, the review cursor follows
  the system cursor.
*	The command to select the previous bookmark works properly again.
*	Bookmarks can be deleted from the Notes dialog.
*	Now you can assign gestures to save and move to a temporary bookmark for
  each document.

## Änderungen in 8.0 ##
*	Fragment-Identifikatoren aus den Dateinamen der Lesezeichen
  entfernt. Dadurch werden Fehler im  ePUBREADER VitalSource Bookshelf
  vermieden.
*	Ein Notizen-Dialog wurde hinzugefügt, um Kommentare für gespeicherte
  Lesezeichen zuzuordnen und an die ausgewählte Position zu verschieben.

## Änderungen in 7.0 ##
*	Der Dialog zum Speichern einer Zeichenkette für die spezifische Suche
  wurde entfernt. Diese Funktionalität ist nun auch im Dialog Spezifische
  Suche enthalten, der neu gestaltet wurde, um verschiedene Aktionen beim
  Drücken der Schaltfläche OK zu ermöglichen.
*	Die visuelle Darstellung der Dialoge wurde verbessert und entspricht dem
  Erscheinungsbild der Dialoge in NVDA.
*	Wenn Sie im Lesemodus den Befehl"Weiter suchen" oder"Rückwärtssuche"
  ausführen, wird nun korrekt nach Groß- und Kleinschreibung gesucht, sofern
  bei der ursprünglichen Suche die Groß- und Kleinschreibung beachtet wurde.
*	Benötigt NVDA 2016.4 oder höher.
*	Nun können Tastenkombinationen im NVDA Eingabendialog unter Einstellungen
  zugewiesen werden, um die Dialogfelder Lesezeichen Kopieren und
  Wiederherstellen aufzurufen.
*	NVDA zeigt eine Meldung an, wenn Lesezeichen kopiert oder mit den
  entsprechenden Dialogen wiederhergestellt wurden.

## Änderungen in 6.0 ##
* Wenn die Funktionen der Erweiterung nicht verfügbar sind, werden die
  Tastenkombinationen an die aktuelle Anwendung weitergereicht.

## Änderungen in 5.0 ##
* Die Groß- und Kleinschreibung kann nun bei der Suche berücksichtigt
  werden.
* Der Menüpunkt Hilfe wurde aus dem Menü entfernt.
* Tastenkürzel sind nun intuitiver

## Änderungen in 4.0 ##
* Fragment-Identifikatoren aus den Dateinamen der Lesezeichen
  entfernt. Dadurch werden Fehler in der Erweiterung ePUBREADER für Firefox
  vermieden.
* Die Hilfe zur Erweiterung ist nun über den Erweiterungs-Manager verfügbar.

## Änderungen in 3.1 ##
* aktualisierte Übersetzungen und neue Sprache.
* Die Position von Lesezeichen wird nicht während der Navigation während
  alles  lesen ausgegeben..

## Änderungen in 3.0 ##
* Unterstützung für "Navigation während alles lesen" hinzugefügt.

## Änderungen in 2.0 ##
* Option zum Speichern und Löschen verschiedener Suchbegriffe für jede Datei
  wurde hinzugefügt.
* Fehler behoben, wenn Pfad-Angaben nichtlateinische Zeichen enthalten.
* Tastenkombinationen können nun mittels des Eingaben-Dialogs von NVDA
  geändert werden.

## Änderungen in 1.0 ##
* Erstveröffentlichung.
* übersetzt in: brasilianisches Portugiesisch, Farsi, Finnisch, französisch,
  Galizisch, deutsch, italienisch, japanisch, Koreanisch, Nepalesisch,
  Portugiesisch, Spanisch, Slovakisch, Slovenisch, Tamil.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=pm

[2]: http://addons.nvda-project.org/files/get.php?file=pm-dev
