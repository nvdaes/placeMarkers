# placeMarkers (stedmærker) #

* Forfattere: Noelia, Chris.
* Download [stabil version][1]
* download [testversion][2]

This addon is used for saving and searching specific text strings or
bookmarks. It can be used  on web pages or documents in NVDA's browse
mode. It can also be used for saving or searching strings of text in
multi-line controls; in this case, if it's not possible to update the caret,
the corresponding string will be copied to the clipboard, so that it can be
searched using other tools.  The plugin saves the specified strings and
bookmarks to files whose name is based on the title and URL of the current
document.  This addon is based on SpecificSearch and Bookmark&Search,
developed by the same author. You should uninstall them to use this one,
since they have common keystrokes and features.

## Tastaturkommandoer ##

*	control+shift+NVDA+f: Opens a dialog with an edit box that shows the last
  saved search; in this dialog you can also select the previously saved
  searches from a combo box or remove the selected string from the history
  using a checkbox. You can choose if the text contained in the edit box
  will be added to the history of your saved texts. Finally, choose an
  action from the next group of radio buttons (between Search next, Search
  previous or Don't search), and specify if NVDA will make a case sensitive
  search. When you press okay, NVDA will search for this string.
*	control+shift+NVDA+k: Saves the current position as a bookmark.
*	control+shift+NVDA+delete: Deletes the bookmark corresponding to this
  position.
*	NVDA+k: Moves to the next bookmark.
*	shift+NVDA+k: Moves to the previous bookmark.
*	control+shift+k: Copies the file name where the place markers data will be
  saved to the clipboard, without an extension.


## Undermenu for stedmærker (NVDA+n) ##

Using the Place markers submenu under NVDA's Preferences menu, you can
access:

*	Mappe med specifikke søgninger: Åbner en mappe med tidligere gemte
  specifikke søgninger.
*	Bookmarks folder: Opens a folder of the saved bookmarks.
*	Copy placeMarkers folder: You can save a copy of the bookmarks folder.
*	Restore placeMarkers: You can restore your bookmarks from a previously
  saved placeMarkers folder.

Note: The bookmark position is based on the number of characters; and
therefore in dynamic pages it is better to use the specific search, not
bookmarks.

## Changes for 7.0 ##
*	The dialog to save a string of text for specific search has been
  removed. This functionality is now included in the Specific search dialog,
  which has been redesigned to allow different actions when pressing the OK
  button.
*	The visual presentation of the dialogs has been enhanced, adhering to the
  appearance of the dialogs shown in NVDA.
*	Performing a Find Next or Find Previous command in Browse Mode will now
  correctly do a case sensitive search if the original Find was case
  sensitive.
*	Requires NVDA 2016.4 or later.
*	Now you can assign gestures to open the Copy and Restore place markers
  dialogs.
*	NVDA will present a message to notify when place markers have been copied
  or restored with the corresponding dialogs.

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
