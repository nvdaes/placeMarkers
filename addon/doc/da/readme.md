# placeMarkers (Stedmærker) #

* Forfattere: Noelia, Chris.
* Download [stabil version][1]
* download [testversion][2]

Dette tilføjelsesprogram bruges til at gemme og søge efter bestemte
tekststrenge på websider eller i dokumenter, som understøtter NVDAs
gennemsynstilstand. Det kan også bruges til at gemme eller søge efter
tekststrenge i felter med flere linjer. I dette tilfælde, hvis det ikke er
muligt at flytte markøren, vil den relevante tekst blive kopieret til
udklipsholderen, så man kan søge med andre værktøjer. Tilføjelsesprogrammet
gemmer de valgte strenge og bogmærker til filer der har lignende navne
svarende til de gemte strenge og bogmærker. Denne tilføjelsespakke er
baseret på Specific Search og Bookmark Search, der er udviklet af samme
forfatter. Disse tilføjelser deler tastetryk og funktionalitet, så det
anbefales at du afinstallerer dem, før du bruger denne tilføjelse.

## Tastaturkommandoer ##

*	CTRL+Skift+NVDA+F: Åbner en dialog der viser den seneste søgning. I denne
  dialog kan du vælge tidligere udførte søgninger fra en comboboks, eller
  fjerne dem fra historikken ved hjælp af en checkboks. Du kan vælge om
  teksten i boksen skal tilføjes til historikken af gemte tekster. Endelig
  skal du vælge en handling fra gruppen af radioknapper (herunder søg
  fremad, søg bagud eller søg ikke), og dernæst beslutte om NVDA skal gøre
  forskel på store og små bogstaver under søgningen. Når du trykker på "ok",
  vil NVDA udføre din søgning.
*	CTRL+skift+NVDA+k: Gemmer den aktuelle position som et bogmærke. Hvis du
  vil angive et navn til dette bogmærke, skal du vælge en tekst fra denne
  position, før du gemmer den.
*	CTRL+skift+NVDA+delete: Sletter bogmærket, der svarer til den aktuelle
  position.
*	NVDA+K: Flytter til det næste bogmærke.
*	Skift+NVDA+K: Flytter til det forrige bogmærke.
*	CTRL+Skift+K: Kopierer filnavnet på filen hvor data på stedmærker bliver
  gemt til Udklipsholderen uden filtypenavn.
*	alt+NVDA+k: Opens a dialog with the bookmarks saved for this document. You
  can write a note for each bookmark; press Save note to save
  changes. Pressing Delete you can remove the selected bookmark. Pressing OK
  you can move to the selected position.
*	Not assigned: Saves a position as a temporary bookmark.
*	Not assigned: Moves to the temporary bookmark for the current document.


## Undermenu for stedmærker (NVDA+n) ##

Ved hjælp af undermenuen for stedmærker (place markers) kan du komme til:

*	Mappe med specifikke søgninger: Åbner en mappe med tidligere gemte
  specifikke søgninger.
*	Mappe med bogmærker: Åbner en mappe med de tidligere gemte bogmærker.
*	Kopier mappe med stedmærker: Du kan gemme en kopi af mappen med bogmærker.
*	Gendan stedmærker: Du kan gendanne dine bogmærker fra en tidligere gemt
  mappe med stedmærker.

Bemærk: Positionen for et bogmærke er baseret på antallet af tegn. På
dynamiske sider er det derfor bedre at bruge specifikke søgninger og ikke
bogmærker, som gemmer en præcis position.


## Changes for 9.0
*	When moving to a bookmark from the Notes dialog, the review cursor follows
  the system cursor.
*	The command to select the previous bookmark works properly again.
*	Bookmarks can be deleted from the Notes dialog.
*	Now you can assign gestures to save and move to a temporary bookmark for
  each document.

## Ændringer i 8.0 ##
*	Fjernet fragmenter af identificeringsstrenge fra filnavne på
  bogmærker. Dette kan forhindre problemer i VitalSource Bookshelf ePUB
  reader.
*	Tilføjet en dialogboks, noter, for at knytte kommentarer til gemte
  bogmærker og flytte til den valgte placering.

## Ændringer i 7,0 ##
*	Dialogen til at gemme en tekststreng til specifikke søgninger er blevet
  fjernet. Denne funktionalitet er nu inkluderet i dialogen specifik
  søgning, som er blevet redesignet til at tillade forskellige handlinger,
  når du trykker på knappen OK.
*	Dialogens visuelle præsentation er blevet forbedret og overholder
  udseendet af de dialoger, der vises i NVDA.
*	Udføring af en Find næste eller Find forrige kommando i gennemsynstilstand
  vil nu korrekt udføre en bogstavsøgning der gør forskel på store og små
  bogstaver, hvis den oprindelige søgning gjorde forskel på store og små
  bogstaver.
*	Kræver NVDA 2016.4 eller nyere.
*	Nu kan du tildele bevægelser til at åbne dialogerne kopier og gendan
  stedmærker.
*	NVDA vil informere når stedmærker er blevet kopieret eller gendannet med
  de tilsvarende dialoger.

## Ændringer i 6.0 ##
* Når funktionerne i tilføjelsesprogrammet ikke kan bruges, bliver
  kommandoer sendt til det relevante program.

## Ændringer i 5.0 ##
* Tilføjet Forskel på små og store bogstaver under søgning.
* Fjernet mulighed for at åbne dokumentationen fra menuen Stedmærker.
* Mere intuitive tastaturkommandoer.

## Ændringer i4.0  ##
* Fjernet fragmenter af identiceringsstrenge fra filnavne på
  bogmærker. Dette kan forhindre problemer i tilføjelsesprogrammet
  ePUBREADER til Firefox.
* Hjælp til tilføjelsesprogrammet er til rådighed fra styring af
  tilføjelsesprogrammer.

## Ændringer i 3.1 ##
* Opdateringer til oversættelse og nye sprog.
* Positioner for bogmærker bliver ikke annonceret under skimlæsning.

## Ændringer i 3.0 ##
* Tilføjet understøttelse for skimlæsning.

## Ændringer i 2.0 ##
* Tilføjet mulighed for at gemme og slette forskellige søgninger for hver
  fil.
* Rettet fejl, som kom til udtryk når stier indeholdt ikke-latinske tegn.
* Genvejstaster kan nu ændres i NVDAs dialog til inputbevægelser.

## Ændringer i 1.0 ##
* Første version.
* Oversat til: Brasiliansk portugisisk, farsi, finsk, fransk, galicisk,
  tysk, italiensk, japansk, koreansk, nepalesisk, portugisisk, spansk,
  slovakisk, slovensk og tamilsk.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=pm

[2]: http://addons.nvda-project.org/files/get.php?file=pm-dev
