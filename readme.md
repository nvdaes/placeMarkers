# placeMarkers #

* Authors: Noelia, Chris.
* download [stable version: 1.0][1]
* download [development version: 2.0-dev][2]

This addon is used for saving and searching specific text strings or bookmarks, on web pages or documents in NVDA's browse mode, or multi-line controls
The plugin saves the specified strings and bookmarks to text and pickle files. The name of these files is based on the title and URL of the current document.

This addon is based on SpecificSearch and Bookmark&Search, developed by the same author. You should uninstall them to use this one, since they have common keystrokes and features.

## Key Commands: ##

*	control+shift+NVDA+s; Opens a dialog that allows you to save a text string   you want to find in the current document. By default is shown the text previously saved for this file. Delete this text and press Ok button if you wish to remove the text file corresponding to the saved search, or type a new text  to add another search.
*	control+shift+NVDA+f; opens a dialog with a edit box that shows the last saved search; in this dialog you can also select the previously saved searches with a combo box and choose an action with another next  combo box . If there is no available files for specific search in the current document, NVDA will warn you that it is not found any file for specific search.
*	control+shift+NVDA+k; Saves the current position as a bookmark
*	control+shift+NVDA+delete; Deletes the bookmark corresponding to this position.
*	control+shift+k; Moves to the next bookmark.
*	shift+NVDA+k; Moves to the previous bookmark.
*	NVDA+k; Copies to clipboard the file name, without extension, where could be saved place markers (positions or a string to search).

## Place markers Submenu (NVDA+N) ##

Using Place markers submenu, under Preferences menu, you can access to 

*	Specific search folder: opens a folder of specific searches previously saved.
*	Bookmarks folder; opens a folder of the bookmarks saved.
*	Copy placeMarkers folder; you can save a copy of the bookmarks folder.
*	Restore placeMarkers; you can restore your bookmarks from a placeMarkers folder previously saved.
*	Documentation file, in your selected language if available, or English by default.

Note: The bookmark position is based on the number of characters; in pages with a dynamic content is better to use the specific search, and not the bookmarks to save a precise position.

## Changes for 2.0 ##
* Added options to save and delete different searches for each file.
* Fixed reported bug: now mbcs is used to decode the path for place markers.

## Changes for 1.0 ##
* Initial version.
* Translated into: Brazilian Portuguese, Farsi, Finnish, French, Galician, German, Italian, Japanese, Korean, Nepali, Portuguese, Spanish, Slovak, Slovenian, Tamil.

[1]: http://addons.nvda-project.org/files/get.php?file=pm
[2]: http://addons.nvda-project.org/files/get.php?file=pm-dev
