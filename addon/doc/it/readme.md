# placeMarkers #

* Autori: Noelia, Chris.
* download [stable version][1]
* download [development version][2]

Questo componente aggiuntivo è utilizzato per salvare segnaposti e cercare
stringhe di testo specifiche, sia nelle pagine web che in documenti,
utilizzando la modalità navigazione di NVDA. Consente la ricerca di stringhe
in campi di testo editabile; in questo caso, se non è possibile aggiornare
il cursore, la stringa corrispondente verrà copiata negli appunti, in modo
che possa essere cercata utilizzando altri strumenti. Il componente
aggiuntivo salva  i segnaposti e le ricerche specifiche in file che vengono
nominati secondo il titolo e l'indirizzo  del documento attuale. Place
Markers deriva da SpecificSearch e Bookmark&Search, sviluppato dalla stessa
autrice. È preferibile disinstallare i vecchi componenti aggiuntivi, dal
momento che usano gli stessi comandi ed hanno le stesse funzioni di Place
Markers. 

## Comandi rapidi: ##

*	Control+shift+NVDA+f: apre una finestra con un campo di editazione che
  mostra l'ultima ricerca salvata; tramite una casella combinata è anche
  possibile selezionare una ricerca specifica salvata in precedenza  o
  rimuovere la stringa selezionata dallo storico utilizzando una casella di
  controllo. È possibile scegliere se il testo contenuto nel campo
  editazione verrà aggiunto allo storico del testo salvato. Infine, è
  possibile selezionare tramite radio pulsanti tra le azioni Cerca
  successiva, Cerca Precedente o Non Cercare, e specificare se considerare
  le maiuscole o minuscole nella ricerca. Premendo Ok NVDA cercherà la
  stringa digitata.
*	control+shift+NVDA+k: Saves the current position as a bookmark. If you
  want to provide a name for this bookmark, select some text from this
  position before saving it.
*	Control+Shift+NVDA+Delete: Elimina il segnaposto corrispondente a questa
  posizione.
*	NVDA+k: vai al segnaposto successivo.
*	Shift+NVDA+k: vai al segnaposto precedente.
*	Control+Shift+K: copia negli appunti il nome del file per il quale
  verranno salvati i segnaposti e le ricerche. (Il nome non contiene
  l'estenzione).
*	alt+NVDA+k: Opens a dialog with the bookmarks saved for this document. You
  can write a note for each bookmark; press Save note to save
  changes. Pressing Delete you can remove the selected bookmark. Pressing OK
  you can move to the selected position.
*	Not assigned: Saves a position as a temporary bookmark.
*	Not assigned: Moves to the temporary bookmark for the current document.


## Sottomenu Segnaposto (NVDA+N) ##

Utilizzando il menu Placemarkes, dal menu Preferenze di NVDA, si può
accedere a:

*	Cartella ricerche specifiche; Apre una cartella delle ricerche specifiche
  precedentemente salvate.
*	Cartella segnaposto; Apre una cartella dei segnaposti precedentemente
  salvati.
*	Copia cartella segnaposti; è possibile salvare una copia della cartella
  segnaposti.
*	Ripristinare segnaposti; è possibile ripristinare i segnaposti da una
  cartella  segnaposti precedentemente salvata.

Nota: La posizione del segnalibro è basata sul numero di caratteri; in
pagine con un contenuto dinamico è meglio utilizzare la ricerca specifica, e
non i segnaposti per salvare una posizione precisa.


## Changes for 11.0 ##
*	Compatible with NVDA 2018.3 or later (required).
*	If needed, you can download the [last version compatible with NVDA
  2017.3][3].

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

## Changes for 8.0 ##
*	Removed fragment identifiers from bookmark filenames, which can avoid
  issues in the VitalSource Bookshelf ePUB reader.
*	Added a Notes dialog, to associate comments for saved bookmarks and move
  to the selected position.

## Novità nella versione 7.0 ##
*	La finestra di dialogo per salvare una stringa di testo per la ricerca
  specifica è stata rimossa. Questa funzionalità è ora inserita nella
  finestra di ricerca Specifica , la quale è stata modificata per eseguire
  diverse azioni quando si preme il pulsante Ok.
*	Migliorata la rappresentazione grafica della interfaccia per la finestra
  di dialogo, conforme alle finestre di dialogo usate in NVDA.
*	Performing a Find Next or Find Previous command in Browse Mode will now
  correctly do a case sensitive search if the original Find was case
  sensitive.
*	Placemarkers richiede NVDA 2016.4 o versioni successive.
*	Ora è possibile assegnare comandi da tastiera per aprire le finestre di
  dialogo per copiare o ripristinare. 
*	NVDA avviserà con un messaggio di notifica quando Placemarkers copia o
  ripristina le cartelle usando le relative finestre.

## Changes for 6.0 ##
* When the add-on features are not usable, gestures are sent to the
  corresponding application.

## Changes for 5.0 ##
* Added case sensitive search.
* Removed option to open documentation from Place markers menu.
* More intuitive key commands.

## Changes for 4.0 ##
* Removed fragment identifiers from bookmark filenames, which can avoid
  issues in ePUBREADER Firefox add-on.
* Add-on help is available from the Add-ons Manager.

## Changes for 3.1 ##
* Translation updates and new language.
* Bookmark position is not announced in skim reading.

## Changes for 3.0 ##
* Added support for skim reading.

## Changes for 2.0 ##
* Added options to save and delete different searches for each file.
* Fixed bug which broke when paths contained non latin characters.
* Shortcuts can now be reassigned using the NVDA gesture input dialog.

## Cambiamenti nella 1.0 ##
* Versione Iniziale.
* Tradotto in: portoghese brasiliano, farsi, finlandese, francese,
  galiziano, tedesco, italiano, giapponese, coreano, nepalese, portoghese,
  spagnolo, slovacco, sloveno, tamil.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=pm

[2]: https://addons.nvda-project.org/files/get.php?file=pm-dev [3]:
https://github.com/nvdaes/placeMarkers/releases/download/10.2/placeMarkers-10.2.nvda-addon
