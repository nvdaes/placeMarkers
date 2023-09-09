# placeMarkers #

* Autori: Noelia, Chris.

This add-on is used for saving and searching specific text strings or
placemarkers. It can be used on web pages or documents in NVDA's browse
mode. It can also be used for saving or searching strings of text in
multi-line controls; in this case, if it's not possible to update the caret,
the corresponding string will be copied to the clipboard, so that it can be
searched using other tools.  The plugin saves the specified strings and
placemarkers to files whose name is based on the title and URL of the
current document.  This add-on is based on SpecificSearch and
Bookmark&Search, developed by the same author. You should uninstall them to
use this one, since they have common keystrokes and features.

## Comandi rapidi: ##

*	control+shift+NVDA+f: apre una finestra con un campo editazione che mostra
  l'ultima ricerca salvata; tramite una casella combinata è anche possibile
  selezionare una ricerca specifica salvata in precedenza  o rimuovere la
  stringa selezionata dalle ricerche recenti utilizzando una casella di
  controllo. Nella stessa finestra, è possibile scegliere se il testo
  contenuto nel campo editazione verrà aggiunto alle ricerche
  recenti. Infine è possibile scegliere, tramite pulsanti radio, tra le
  azioni Cerca successiva, Cerca Precedente o Non Cercare, e specificare se
  distinguere tra le lettere maiuscole e minuscole nella ricerca. Premendo
  Ok NVDA cercherà la stringa digitata.
*	control+shift+NVDA+y: Saves the current position as a placemarker. If you
  want to provide a name for this placemarker, select some text from this
  position before saving it.
*	control+shift+NVDA+delete: Deletes the placemarker corresponding to this
  position.
*	NVDA+y: Moves to the next placemarker.
*	shift+NVDA+y: Moves to the previous placemarker.
*	Not assigned: Shows the file name where the placemarkers data will be
  saved in browse mode, without an extension.
*	alt+NVDA+y: Opens a dialog with the placemarkers saved for this
  document. You can write a note for each placemarker; press Save note to
  save changes. Pressing Delete you can remove the selected
  placemarker. Pressing OK you can move to the selected position.
*	Not assigned: Saves a position as a temporary placemarker.
*	Not assigned: Moves to the temporary placemarker for the current document.
*	Tasto non assegnato: trova l'occorrenza successiva dell'ultimo testo
  cercato in uno specifico documento.
*	Tasto non assegnato: trova l'occorrenza precedente dell'ultimo testo
  cercato in uno specifico documento.


## PlaceMarkers Submenu (NVDA+N) ##

Using the PlaceMarkers submenu under NVDA's Preferences menu, you can
access:

*	Specific search folder: Opens a folder of specific searches previously
  saved.
*	Bookmarks folder: Opens a folder of the saved placemarkers.
*	Copy placeMarkers folder: You can save a copy of the placeMarkers folder.
*	Restore placeMarkers: You can restore your placeMarkers from a previously
  saved placeMarkers folder.

Note: The placemarker position is based on the number of characters; and
therefore in dynamic pages it is better to use the specific search, not
placemarkers.

## Changes for 24.0
* Y is used instead of k in gestures such as NVDA+k, NVDA+shift+k,
  NVDA+alt+k and NVDA+control+shift+k.
* Compatible with NVDA 2023.1.

## Changes for 23.0
* The add-on works again with Microsoft Word.

## Changes for 22.0
* We can move to bookmarks and delete them with UIA enabled, thanks to
  Abdel.

## Novità nella versione 21.0
* I segnalibri possono essere salvati con UIA abilitato nei browser basati
  su Chromium, grazie al contributo di Abdel.

## Novità nella versione 20.0
* Richiede NVDA 2022.1 o versioni successive.

## Novità nella versione 19.0 ##
* Il componente aggiuntivo non può essere eseguito in modalità protetta.

## Changes per la 18.0 ##
* Il comando per vedere il percorso per placeMarkers avvisa se ci sono
  segnaposto permanenti, testo per una ricerca specifica o un segnalibro
  temporaneo per il documento corrente.

## Changes per la 17.0 ##
* Risolto un bug che non permetteva di salvare i segnaposto in alcuni
  documenti.
* Risolto il problema con le stringhe per tradurre correttamente.

## Changes per la  16.0 ##
* Compatible with NVDA 2021.1 or later (required).
* supporto alla lettura rapida nella navigazione con i  segnaposto
  temporanei.
* If needed, you can download [other
  versions](https://github.com/nvdaes/placeMarkers/releases).

## Novità nella versione 15.0 ##
* Quando si usa il comando "dire tutto" (NVDA+freccia giù) in modalità
  navigazione e l'opzione Lettura continua è attivata, i comandi "trova
  precedente" e "trova successivo" relativi alla ricerca specifica non
  interrompono più la lettura, in analogia con i comandi "trova precedente"
  (NVDA+f3) e "trova successivo" (NVDA+shift+f3) di NVDA 2020.4.
* Quando, dopo l'esecuzione del comando "Trova precedente" relativo alla
  ricerca specifica, si apre la finestra Ricerca specifica, viene
  selezionata l'opzione Cerca precedente.

## Novità nella versione 14.0 ##
*	Il comando per copiare il nome del file in cui vengono salvati i dati di
  placeMarkers è stato sostituito da un comando che mostra questo nome file
  in modalità navigazione. Questo comando non è assegnato ad alcun tasto.
*	Il campo "Testo da cercare" non si sovrappone più al campo "Testo
  salvato". (Grazie a Cyrille Bougot).
*	Richiede NVDA 2019.3 o versioni successive.

## Novità nella versione 13.0 ##
*	Aggiunto un comando, non assegnato ad alcun tasto, per trovare
  l'occorrenza precedente o successiva dell'ultimo testo cercato in uno
  specifico documento.
*	La funzione Ricerca specifica funziona anche quando è aperta la finestra
  INformazioni su NVDA.
*	Nella finestra Ricerca specifica, la casella di controllo per distinguere
  tra lettere maiuscole e minuscole sarà attivata se era già attiva
  nell'ultima ricerca.
*	Quando il componente aggiuntivo viene aggiornato, i segnaposto e le
  stringhe per le ricerche specifiche salvati nella precedente versione
  saranno automaticamente copiati nella nuova, a meno che non si preferisca
  importare i segnaposto salvati nella cartella di configurazione principale
  di NVDA.
*	Quando si usa la finestra per copiare i segnaposto, se la cartella scelta
  non si chiama placeMarkersBackup, verrà creata una sottocartella con
  questo nome, per evitare la cancellazione di cartelle contenenti dati
  importanti, quali Documenti o Downloads.

## Novità nella versione 12.0 ##
*	Risolto un errore che causava un crash in NVDA quando si tentava di aprire
  la finestra di dialogo Note, se venivano selezionati i caratteri cinesi
  prima di salvare i segnaposto.

## Novità nella versione 11.0 ##
*	Compatibile con NVDA 2018.3 o superiore (richiesto).
*	Se è necessario, è possibile scaricare la  [versione compatibile  con NVDA
  2017.3][3].

## Novità nella versione 10.0 ##
*	In Edge, i comandi associati ai segnaposto, come NVDA+k, NVDA+shift+k o
  NVDA+alt+k, saranno inviati all'applicazione, invece di tentare di
  spostare il cursore al segnaposto, per evitare errori, specie in documenti
  lunghi.
*	Ora la ricerca specifica è supportata anche in Edge.

## Novità nella versione 9.0
*	Quando ci si sposta ad un segnaposto dalla finestra  Note, il cursore di
  controllo segue il cursore di sistema.
*	Il comando per selezionare il segnaposto precedente funziona di nuovo
  correttamente.
*	I segnaposto possono essere eliminati dalla finestra  Note.
*	Ora  è possibile assegnare comandi da tastiera per creare e spostarsi sui
  segnaposto temporanei.

## Novità nella versione 8.0 ##
*	Rimossi gli identificatori di frammento dai nomi dei file segnaposto, per
  evitare problemi nell'ePUB reader VitalSource Bookshelf.
*	Aggiunta una finestra Note, per associare commenti ai segnaposto salvati e
  spostarsi alla posizione selezionata.

## Novità nella versione 7.0 ##
*	La finestra di dialogo per salvare una stringa di testo per la ricerca
  specifica è stata rimossa. Questa funzionalità è ora inserita nella
  finestra di ricerca Specifica , la quale è stata modificata per eseguire
  diverse azioni quando si preme il pulsante Ok.
*	La rappresentazione grafica dell'interfaccia per le finestre di dialogo è
  stata migliorata, in conformità con il layout delle finestre di dialogo di
  NVDA.
*	L'esecuzione dei comandi Trova Successivo o Trova Precedente in Modalità
  Navigazione  ora darà luogo a una ricerca distinguendo tra lettere
  maiuscole e minuscole se così era stata impostata la ricerca originale.
*	Richiede NVDA 2016.4 o superiore.
*	Ora è possibile assegnare comandi da tastiera per aprire le finestre di
  dialogo per copiare o ripristinare i segnaposto.
*	NVDA mostrerà un messaggio di notifica quando i segnaposto saranno copiati
  o ripristinati mediante le relative finestre.

## Novità nella versione 6.0 ##
* Quando le funzioni dell'add-on non sono utilizzabili, i comandi sono
  inviati all'applicazione corrispondente.

## Novità nella versione 5.0 ##
* Aggiunta la ricerca con distinzione tra lettere maiuscole e minuscole.
* Rimossa l'opzione per aprire la documentazione dal menu di PlaceMarkers .
* Comandi rapidi più intuitivi.

## Novità nella versione 4.0 ##
* Rimossi gli identificatori di frammento dai nomi dei file segnaposto, per
  evitare problemi nel componente aggiuntivo di Firefox ePUBREADER.
* La guida dell'add-on è disponibile dal gestore componenti aggiuntivi.

## Novità nella versione 3.1 ##
* Traduzioni aggiornate e nuove lingue.
* La posizione dei segnaposto non viene vocalizzata durante la lettura
  continua.

## Novità nella versione 3.0 ##
* Aggiunto il supporto per la lettura continua.

## Novità nella versione 2.0 ##
* Aggiunte opzioni per salvare e cancellare ricerche diverse per ogni file.
* Risolto un problema che si verificava quando i percorsi contenevano
  caratteri non latini.
* I tasti possono ora essere riassegnati usando la finestra Gesti e Tasti di
  Immissione di NVDA.

## Novità nella versione 1.0 ##
* Versione Iniziale.
* Tradotto in: portoghese brasiliano, farsi, finlandese, francese,
  galiziano, tedesco, italiano, giapponese, coreano, nepalese, portoghese,
  spagnolo, slovacco, sloveno, tamil.

[[!tag dev stable]]

[3]: https://www.nvaccess.org/addonStore/legacy?file=pm-o
