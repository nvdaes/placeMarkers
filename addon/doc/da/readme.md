# placeMarkers (Stedmærker) #

* Forfattere: Noelia, Chris.

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

## Tastaturkommandoer: ##

*	CTRL+Skift+NVDA+F: Åbner en dialog der viser den seneste søgning. I denne
  dialog kan du vælge tidligere udførte søgninger fra en comboboks, eller
  fjerne dem fra historikken ved hjælp af en checkboks. Du kan vælge om
  teksten i boksen skal tilføjes til historikken af gemte tekster. Endelig
  skal du vælge en handling fra gruppen af radioknapper (herunder søg
  fremad, søg bagud eller søg ikke), og dernæst beslutte om NVDA skal gøre
  forskel på store og små bogstaver under søgningen. Når du trykker på "ok",
  vil NVDA udføre din søgning.
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
*	Ikke tildelt: Søger efter næste forekomst af den angivne søgestreng i et
  dokument
*	Ikke tildelt: Søger efter forrige forekomst af den angivne søgestreng i et
  dokument


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

## Ændringer for 23.0
* Tilføjelsen fungerer igen med Microsoft Word.

## Ændringer for 22.0
* Vi kan flytte til bogmærker og slette dem med UIA aktiveret, takket være
  Abdel.

## Ændringer for 21.0
* Bogmærker kan gemmes med UIA aktiveret i browsere baseret på Chromium,
  takket være Abdel.

## Ændringer for 20.0
* Kræver NVDA 2022.1 eller nyere.

## Ændringer for 19.0 ##
* Tilføjelsen kan ikke køres på sikre skærme.

## Ændringer for 18.0 ##
* Kommandoen til at se stien til stedsmarkører viser, om der er permanente
  bogmærker, tekst til specifik søgning eller et midlertidigt bogmærke for
  det aktuelle dokument.

## Ændringer for 17.0 ##
* Rettede en fejl, som ikke tillod at gemme stedsmarkører i nogle
  dokumenter.
* Rettede oversatte strenge, der fik oversættelser til at fungere korrekt.

## Ændringer for 16.0 ##
* Compatible with NVDA 2021.1 or later (required).
* Skimlæsning understøttes, når du flytter til midlertidige bogmærker.
* If needed, you can download [other
  versions](https://github.com/nvdaes/placeMarkers/releases).

## Ændringer for 15.0 ##
* Når du læser med sig alt i gennemsynstilstand, stopper kommandoerne til
  "find forrige" og "find næste" ikke længere med at læse, hvis
  indstillingen "Tillad skimlæsning" er aktiveret.
* Når dialogboksen Specifik søgning åbnes efter at have kørt kommandoen
  Specifik find forrige, vil indstillingen Søg forrige blive valgt.

## Ændringer for 14.0 ##
*	Kommandoen til at kopiere navnet på filen, hvor stedmarkeringsdataene
  gemmes, er blevet erstattet af en kommando, der viser dette filnavn i
  gennemsynstilstanden. Kommandoen er ikke tildelt et tastetryk som
  standard.
*	Feltet "Tekst til søgning" overlapper ikke længere feltet "Gemt
  tekst". (Tak til Cyrille Bougot).
*	Kræver NVDA 2019.3 eller nyere.

## Ændringer i 13,0 ##
*	Tilføjede kommandoer, så du nemt kan søge efter forrige og næste forekomst
  af den sidst angivne tekststreng. Disse kommandoer har ingen tildelte
  tastetryk.
*	Funktionen til specifikke søgninger virker kun, når NVDAs søgedialog er
  åbnet.
*	I dialogen til specifike søgninger, vil boksen til at skelne mellem store
  og små bogstaver forblive markeret, hvis dette var tilfældet under den
  sidste søgning.
*	Når tilføjelsesprogrammet er opdateret, kopieres bogmærker og strenge til
  specifik søgning der er gemt i den tidligere version af tilføjelsen
  automatisk til den nye version, medmindre du foretrækker at importere
  stedmærker, der er gemt i den primære konfigurations mappe i NVDA.
*	Når du bruger dialogen til at kopiere stedmærker, og hvis den valge mappe
  ikke hedder "placeMarkersBackup", vil en undermappe med dette navn blive
  oprettet for at forhindre sletning af mapper, der indeholder vigtige data,
  såsom dokumenter eller overførsler.

## Ændringer for 12.0 ##
*	Rettede en kritisk fejl, der forårsagede at NVDA gik ned, når man forsøgte
  at åbne dialogboksen Noter, hvis kinesiske tegn blev valgt, før bogmærker
  blev gemt.

## Ændringer for 11.0 ##
*	Kompatibel med NVDA 2018.3 eller nyere (påkrævet).
*	Hvis nødvendigt, kan du hente [den sidste version kompatibel med NVDA
  2017.3][3].

## Ændringer for 10.0 ##
*	I Edge vil kommandoer i forbindelse med bogmærkevalg, såsom NVDA+k,
  NVDA+shift+k eller NVDA+alt+k, blive sendt til applikationen i stedet for
  at forsøge at flytte markøren til bogmærker for at undgå fejl, især i
  lange dokumenter.
*	Nu understøttes specifik søgning i Edge.

## Ændringer for 9.0
*	Når du flytter til et bogmærke i dialogboksen Noter, følger
  korrekturmarkøren systemmarkøren.
*	Kommandoen til at vælge det forrige bogmærke fungerer korrekt igen.
*	Bogmærker kan slettes fra dialogen Noter.
*	Nu kan du tildele bevægelser, så du lettere kan gemme og flytte til
  midlertidige bogmærker for hvert dokument.

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

[3]: https://www.nvaccess.org/addonStore/legacy?file=pm-o
