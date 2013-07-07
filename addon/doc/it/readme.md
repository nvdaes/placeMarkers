# placeMarkers #

Consente di cercare e salvare testo specifico o Segnaposti in pagine web o in documenti in Modalità Navigazione di NVDA. Il componente aggiuntivo salva la ricerca in file di testo e con estenzione pickle.

Il nome di questi file è dato dalla pagina dove eseguiamo la ricerca. all'eseguire il comando di ricerca specifica si apre una finestra di dialogo dove viene visualizzata la ricerca corrispondente alla pagina, se si è salvato del testo in precedenza per il documento.

placeMarkers proviene da SpecificSearch and Bookmark&Search, sviluppato dalla stessa autrice. E' preferibile disinstallare questi ultimi prima di installare PlaceMarkers, poiché hanno comandi e caratteristiche comuni.

## Comandi da tastiera: ##

*	control+shift+NVDA+s; Apre una finestra di dialogo per salvare del testo di ricerca associato al documento attuale. Di default verrà mostrato la ricerca corrispondente al documento, se si elimina il testo dalla finestra di dialogo verrà eliminato anche il file corrispondente.
*	control+shift+NVDA+f; se esiste un file di ricerca per il documento attuale, apre una finestra di dialogo con il testo precedentemente salvato. Premendo invio NVDA cerca il testo indicato nel campo di editazione. In caso non esiste nessun file di ricerca per il documento NVDA avvisa con un messaggio senza prire la finestra per la ricerca specifica.
*	control+shift+NVDA+k; Salva la posizione attuale del cursore come segnaposto.
*	control+shift+NVDA+delete; Cancella il Segnaposto corrispondente alla posizione attuale.
*	control+shift+k; Sposta il cursore al segnaposto seguente.
*	shift+NVDA+k; Sposta il cursore al segnaposto precedente.
*	NVDA+k; Riporta il nome del file, senza estensione, dove è stato salvato un segnaposto (posizione o testo della ricerca).

## Place markers Sottomenu (NVDA+N) ##

Dal menù Place markers , integrato al sottomenù Preferenze, si può accedere a: 

*	Cartella ricerche specifiche; visualizza una cartella con le ricerche specifiche salvate.
*	Cartella Segnaposti; visualizza la cartella dei Segnaposti salvati in precedenza.
*	Copia la cartella Segnaposti; consente di salvare una copia della cartella Segnaposti.
*	Ripristina Segnaposti; è possibile ripristinare la cartella Segnaposti da una copia salvata in precedenza.
*	Guida all'uso, se disponibile nella lingua selezionata, in alternativa di default si aprirà la guida in inglese.

Nota: la posizione del segnaposto è basata sul numero del carattere che occupa; in pagine con contenuto dinamico è preferibile utilizzare la ricerca specifica e non i segnaposti per salvare una posizione precisa.
