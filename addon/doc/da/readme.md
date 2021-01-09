# placeMarkers (Stedmærker) #
* Forfattere: Noelia, Chris.
* NVDA-kompatibilitet: 2019.3 eller nyere
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

## Tastaturkommandoer: ##

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
*	Ikke tildelt: Viser filnavnet, hvor stedmarkørens data gemmes i
  gennemsynstilstand uden en filtypenavn.
*	Alt+NVDA+K: Åbner en dialog med de bogmærker, der er gemt for det aktuelle
  dokument. Du kan skrive en note til hvert bogmærke. Tryk på "Gem note" for
  at gemme ændringer. Ved at trykke på OK kan du flytte til den valgte
  position.
*	Ikke tildelt: Gemmer en position som et midlertidigt bogmærke.
*	Ikke tildelt: Flytter til det midlertidige bogmærke for det aktuelle
  dokument.
*	Ikke tildelt: Søger efter næste forekomst af den angivne søgestreng i et
  dokument
*	Ikke tildelt: Søger efter forrige forekomst af den angivne søgestreng i et
  dokument


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

[1]: https://addons.nvda-project.org/files/get.php?file=pm

[2]: https://addons.nvda-project.org/files/get.php?file=pm-dev

[3]: https://addons.nvda-project.org/files/get.php?file=pm-o
