# Lesezeichen #
* Autoren: Noelia, Chris.
* NVDA-Kompatibilität: 2019.3 oder höher.
* [Stabile Version herunterladen][1]
* [Entwicklerversion herunterladen][2]

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
*	NVDA+K: Wechselt zum nächsten Lesezeichen.
*	Umschalt+NVDA+K: Wechselt zum vorherigen Lesezeichen.
*	Nicht zugewiesen: Zeigt die Datei, in welcher die Lesezeichen gespeichert
  werden im Lesemodus, ohne deren Erweiterung an.
*	Alt+NVDA+K: Öffnet einen Dialog mit den für dieses Dokument gespeicherten
  Lesezeichen. Sie können für jedes Lesezeichen eine Notiz schreiben. Mit
  Klicken auf "Notiz speichern" können Sie die Änderungen speichern. Mit
  "Entfernen" können Sie das ausgewählte Lesezeichen löschen und mit dem
  Schalter OK können Sie zur gewählten Position springen.
*	Nicht zugewiesen: speichert die Position als temporäres Lesezeichen.
*	Nicht zugewiesen: springt zum temporären Lesezeichen für das aktuelle
  Dokument.
*	Nicht zugeordnet: Findet das nächste Vorkommen des zuletzt gesuchten
  Textes in einem bestimmten Dokument.
*	Nicht zugeordnet: Findet das vorherige Vorkommen des zuletzt gesuchten
  Textes in einem bestimmten Dokument.


## Lesezeichen Untermenü (nvda+n) ##

Über das Untermenü Lesezeichen in NVDA-Einstellungen können Sie auf folgende
Elemente zugreifen:

*	Suchanfragen: Öffnet einen Ordner, in dem zuvor gespeicherte Suchanfragen
  abgelegt sind.
*	Lesezeichen-Ordner: öffnet einen Ordner mit gespeicherten Lesezeichen.
*	Lesezeichen-Ordner kopieren: Speichert eine Kopie des Lesezeichen-Ordners.
*	Lesezeichen wiederherstellen: Stellt die Lesezeichen aus einem zuvor
  gespeicherten Lesezeichen-Ordner wieder her.

Anmerkung: Die Lesezeichen basieren auf der Position im Dokument (welche in
Zeichen vom Dokumentanfang gemessen wird). Bei dynamischen Webseiten
empfielt sich daher stattdessen Suchanfragen zu verwenden.

## Änderungen für 14.0 ##
*	Der Befehl zum Kopieren des Namens der Datei, in der Lesezeichen
  gespeichert werden, wurde durch einen Befehl ersetzt, der diesen
  Dateinamen im Lesemodus anzeigt. Dies ist keiner Geste zugewiesen.
*	Das Feld "suchen" überlappt nun nicht mehr das Feld "gespeicherter
  Text". (Danke an Cyrille Bougot).
*	Erfordert NVDA 2019.3 oder höher.

## Änderungen in 13.0 ##
*	Es wurden nicht zugewiesene Befehle hinzugefügt, um das nächste und
  vorherige Auftreten des zuletzt gesuchten Textes in einem bestimmten
  Dokument zu finden.
*	Die spezifische Suche funktioniert auch, wenn das Dialogfeld "Info" von
  NVDA geöffnet ist.
*	Im Dialogfeld Spezifische Suche wird das Kontrollkästchen für die
  Berücksichtigung der Groß-/Kleinschreibung aktiviert, wenn diese Option
  für die letzte Suche ausgewählt wurde.
*	Bei der Aktualisierung dieser Erweiterung werden die in der vorherigen
  Version gespeicherten Lesezeichen und Zeichenketten aus der spezifischen
  Suche automatisch in die neue Version kopiert, es sei denn, Sie möchten
  ausdrücklich, dass diese aus dem Hauptkonfigurationsordner von NVDA
  importiert werden.
*	Wenn Sie den Dialog zum Kopieren von Lesezeichen verwenden und der
  ausgewählte Ordner nicht "placeMarkersBackup" heißt, wird ein Unterordner
  mit diesem Namen erstellt, um das Löschen von Verzeichnissen mit wichtigen
  Daten wie Dokumente oder Downloads zu verhindern.

## Änderungen für 12.0 ##
*	Es wurde ein kritischer Fehler behoben, der dazu führte, dass NVDA beim
  Versuch, den Notizen-Dialog zu öffnen, abstürzte, wenn chinesische Zeichen
  ausgewählt wurden bevor Lesezeichen gespeichert wurden.

## Änderungen in 11.0 ##
*	Kompatibel mit NVDA 2018.3 oder neuer (erforderlich).
*	Bei Bedarf können Sie die [letzte Version][3], die mit NVDA 2017.3
  kompatibel ist herunterladen.

## Änderungen in 10.0 ##
*	In Microsoft Edge, vor allem in langen Dokumenten, werden bestimmte
  Tastenkombinationen zur Anwendung weitergereicht ohne den Cursor zu einem
  Lesezeichen zu bewegen, um Fehlermeldungen zu vermeiden. Dies gilt für
  Tastenkombinationen, die für das Auswählen von Lesezeichen zugewiesen
  wurden (z.B. NVDA+k, NVDA+Umschalt+k oder NVDA+Alt+k).
*	Die gezielte Suche nach Lesezeichen funktioniert jetzt auch in Microsoft
  Edge.

## Änderungen in 9.0
*	Der NVDA-Cursor folgt dem System-Cursor, wenn Sie aus dem Dialog für
  Notizen zu einem Lesezeichen springen.
*	Der Befehl zum Auswählen des vorherigen Lesezeichens funktioniert wieder
  ordnungsgemäß.
*	Lesezeichen können aus dem Dialog für Notizen gelöscht werden.
*	Nun können dokumentspezifische Tastenkombinationen im NVDA Eingabendialog
  zugewiesen werden, um temporäre Lesezeichen in einem bestimmten Dokument
  anzusteuern und zu speichern.

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
* Tastenkürzel sind nun intuitiver.

## Änderungen in 4.0 ##
* Fragment-Identifikatoren aus den Dateinamen der Lesezeichen
  entfernt. Dadurch werden Fehler in der Erweiterung ePUBREADER für Firefox
  vermieden.
* Die Hilfe zur Erweiterung ist nun über den Erweiterungs-Manager verfügbar.

## Änderungen in 3.1 ##
* Aktualisierte Übersetzungen und neue Sprache.
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
* Übersetzt in: brasilianisches Portugiesisch, Farsi, Finnisch, französisch,
  Galizisch, deutsch, italienisch, japanisch, Koreanisch, Nepalesisch,
  Portugiesisch, Spanisch, Slovakisch, Slovenisch, Tamil.


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=pm

[2]: https://addons.nvda-project.org/files/get.php?file=pm-dev

[3]: https://addons.nvda-project.org/files/get.php?file=pm-o
