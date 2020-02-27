# placeMarkers #
* Autori: Noelia, Chris.
* NVDA compatibility: 2019.3 or later.
* Scarica la  [versione stabile][1]
* Scarica la [versione in sviluppo][2]

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
*	control+shift+NVDA+k: Salva la posizione corrente come segnalibro. Se si
  desidera dare un nome per il segnalibro, selezionare un testo da questa
  posizione prima di salvarlo.
*	Control+Shift+NVDA+Delete: Elimina il segnaposto corrispondente a questa
  posizione.
*	NVDA+k: vai al segnaposto successivo.
*	Shift+NVDA+k: vai al segnaposto precedente.
*	Not assigned: Shows the file name where the place markers data will be
  saved in browse mode, without an extension.
*	alt+NVDA+k: apre una finestra di dialogo con i segnalibri salvati per il
  documento corrente. È possibile scrivere una nota per ogni segnalibro;
  premere Salva nota per salvare le modifiche. Premendo il tasto Canc è
  possibile rimuovere il segnalibro selezionato. Premendo OK si sposta il
  cursore nella posizione selezionata.
*	Tasto non assegnato: Salva la posizione attuale come segnalibro
  temporaneo.
*	Tasto non assegnato: sposta il cursore nel segnalibro temporaneo nel
  documento corrente. 
*	Not assigned: Finds the next occurrence of the last text searched for any
  specific document.
*	Not assigned: Finds the previous occurrence of the last text searched for
  any specific document.


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

## Changes for 12.0 ##
*	Risolto un errore che causava un crash in NVDA quando si tentava di aprire
  la finestra di dialogo Note, se i caratteri cinesi venivano selezionati
  prima di salvare i segnalibri.

## Changes for 11.0 ##
*	Compatibile con NVDA 2018.3 superiori(required).
*	Se è necessario, è possibile scaricare la  [versione compatibile  con NVDA
  2017.3][3].

## Changes for 10.0 ##
*	In Edge, i comandi associati ai segnaposti, come NVDA+k, NVDA+shift+k o
  NVDA+alt+k, saranno inviati all'applicazione, invece di tentare di
  spostare il cursore al segnaposto, per evitare errori, particolarmente in
  documenti lunghi.
*	La ricerca specifica è supportata anche in Edge.

## Changes for 9.0
*	Quando ci si sposta ad un segnalibro dalla finestra  Note, il cursore di
  controllo segue il cursore di sistema. 
*	The command to select the previous bookmark works properly again.
*	I segnalibri possono essere eliminati dalla finestra  Note.
*	Ora  è possibile assegnare comandi da tastiera per spostarsi sui
  segnalibri temporanei.

## Changes for 8.0 ##
*	Removed fragment identifiers from bookmark filenames, which can avoid
  issues in the VitalSource Bookshelf ePUB reader.
*	Added a Notes dialog, to associate comments for saved bookmarks and move
  to the selected position.

## Changes for 7.0 ##
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

[2]: https://addons.nvda-project.org/files/get.php?file=pm-dev

[3]: https://addons.nvda-project.org/files/get.php?file=pm-o
