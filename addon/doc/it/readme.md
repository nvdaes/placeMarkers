# placeMarkers #
* Autori: Noelia, Chris.
* Compatibilità con NVDA: versione 2019.3 e successive.
* scarica la  [versione stabile][1]
* scarica la [versione in sviluppo][2]

Questo componente aggiuntivo è utilizzato per salvare e cercare segnaposto e
stringhe di testo specifiche, sia nelle pagine web che in documenti,
utilizzando la modalità navigazione di NVDA. E' utile anche per salvare e
cercare  stringhe di testo in campi editazione multilinea; in questo caso,
se non è possibile aggiornare il cursore, la stringa corrispondente verrà
copiata negli appunti, in modo che possa essere cercata utilizzando altri
strumenti. Il componente aggiuntivo salva  i segnaposto e le ricerche
specifiche in file il cui nome si basa sul titolo e l'indirizzo  del
documento attuale. Place Markers deriva da SpecificSearch e Bookmark&Search,
sviluppati dalla stessa autrice. È preferibile disinstallare i vecchi
componenti aggiuntivi, dal momento che usano gli stessi comandi ed hanno le
stesse funzioni di Place Markers.

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
*	control+shift+NVDA+k: Salva la posizione corrente come segnaposto. Se si
  desidera dare un nome al segnaposto, selezionare del testo da questa
  posizione prima di salvarlo.
*	control+Shift+NVDA+canc: Elimina il segnaposto corrispondente a questa
  posizione.
*	NVDA+k: va al segnaposto successivo.
*	shift+NVDA+k: va al segnaposto precedente.
*	Tasto non assegnato: mostra il nome del file per il quale verranno salvati
  i segnaposto e le ricerche in modalità navigazione. (Il nome non contiene
  l'estensione).
*	alt+NVDA+k: apre una finestra di dialogo con i segnaposto salvati per il
  documento corrente. È possibile scrivere una nota per ogni segnaposto;
  premere Salva nota per salvare le modifiche. Premendo il tasto Canc è
  possibile rimuovere il segnaposto selezionato. Premendo OK si sposta il
  cursore nella posizione selezionata.
*	Tasto non assegnato: Salva la posizione attuale come segnaposto
  temporaneo.
*	Tasto non assegnato: sposta il cursore nel segnaposto temporaneo del
  documento corrente.
*	Tasto non assegnato: trova l'occorrenza successiva dell'ultimo testo
  cercato in uno specifico documento.
*	Tasto non assegnato: trova l'occorrenza precedente dell'ultimo testo
  cercato in uno specifico documento.


## Sottomenu Place Markers (NVDA+N) ##

Utilizzando il sottomenu Place markers dal menu Preferenze di NVDA, si può
accedere a:

*	Cartella ricerche specifiche: Apre una cartella delle ricerche specifiche
  precedentemente salvate.
*	Cartella segnaposto: Apre una cartella dei segnaposto precedentemente
  salvati.
*	Copia cartella segnaposto: è possibile salvare una copia della cartella
  segnaposto.
*	Ripristina segnaposto: è possibile ripristinare i segnaposto da una
  cartella  segnaposto precedentemente salvata.

Nota: La posizione del segnaposto è basata sul numero di caratteri; in
pagine con un contenuto dinamico è meglio utilizzare la ricerca specifica, e
non i segnaposto, per salvare una posizione precisa.

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

[1]: https://addons.nvda-project.org/files/get.php?file=pm

[2]: https://addons.nvda-project.org/files/get.php?file=pm-dev

[3]: https://addons.nvda-project.org/files/get.php?file=pm-o
