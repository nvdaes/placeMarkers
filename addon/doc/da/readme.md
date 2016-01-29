# placeMarkers (stedmærker) #

* Forfattere: Noelia, Chris.
* Download [stabil version][1]
* download [testversion][2]

Dette tilføjelsesprogram bruges til at gemme og søge efter bestemte
tekststrenge på websider eller i dokumenter, som understøtter NVDAs
gennemsynstilstand. Det kan også bruges til at gemme eller søge efter
tekststrenge i felter med flere linjer. I dette tilfælde, hvis det ikke er
muligt at flytte markøren, vil den relevante tekst blive kopieret til
udklipsholderen, så man kan søge med andre værktøjer. Tilføjelsesprogrammet
gemmer de valgte tekststrenge og bogmærker i tekst- og pickle-filer. Navnet
på disse filer bliver baseret på titel og URL-adresse på det aktuelle
dokument.

Dette tilføjelsesprogram er baseret på SpecificSearch og Bookmark&Search,
som er udviklet af samme forfatter. Du skal afinstallere dem for at kunne
bruge dette program, eftersom de har fælles tastaturkommandoer og
funktioner.

## Tastaturkommandoer ##

*	control+shift+NVDA+s: Åbner en dialog, hvor du kan gemme en tekststreng, som du vil finde i det aktuelle dokument. Som standard bliver den forrige tekst, som blev gemt for denne fil, vist. Slet denne tekst, og tryk på OK-knappen, hvis du vil fjerne tekstfilen, som svarer til den gemte søgning, eller skriv en ny tekst for at tilføje endnu en søgning.
*	control+shift+NVDA+f: Åbner en dialog med et editfelt, der viser den sidst gemte søgning. I denne dialog kan du også vælge tidligere gemte søgninger i en comboboks og vælge en handling fra den næste comboboks. Hvis der ikke er nogen filer til rådighed med specifikke søgninger i dette dokument, vil NVDA advare dig om, at der ikke blev fundet nogen filer med specifikke søgninger.
*	control+shift+NVDA+k: Gemmer den aktuelle position som et bogmærke.
*	control+shift+NVDA+delete: Sletter bogmærket, som svarer til denne position.
*	NVDA+k: Går til næste bogmærke.
*	shift+NVDA+k: Går til forrige bogmærke.
*	control+shift+k: Kopierer navnet på filen (uden filtypenavn), hvor data for stedmærker bliver gemt, til udklipsholderen.

## Undermenu for stedmærker (NVDA+n) ##


Ved hjælp af undermenuen for stedmærker (place markers) kan du komme til:

*	Mappe med specifikke søgninger: Åbner en mappe med tidligere gemte
  specifikke søgninger.
*	Mappe med bogmærker: Åbner en mappe med de tidligere gemte bogmærker.
*	Kopier mappe med stedmærker: Du kan gemme en kopi af mappen med bogmærker.
*	Gendan stedmærker: Du kan gendanne dine bogmærker fra en tidligere gemt
  mappe med stedmærker.
*	Fil med dokumentation, på det valgte sprog, hvis tilgængeligt, eller som
  standard på engelsk.

Bemærk: Positionen for et bogmærke er baseret på antallet af tegn. På
dynamiske sider er det derfor bedre at bruge specifikke søgninger og ikke
bogmærker, som gemmer en præcis position.

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
