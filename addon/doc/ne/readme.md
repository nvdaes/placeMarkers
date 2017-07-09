# स्थान चिनो #

* लेखक: Noelia, Chris.
* अनुबहन[version 1.0][1]
* अनुबहन [development version][2]

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

## कुञ्जी आदेस: ##

*	control+shift+NVDA+f: Opens a dialog with an edit box that shows the last
  saved search; in this dialog you can also select the previously saved
  searches from a combo box or remove the selected string from the history
  using a checkbox. You can choose if the text contained in the edit box
  will be added to the history of your saved texts. Finally, choose an
  action from the next group of radio buttons (between Search next, Search
  previous or Don't search), and specify if NVDA will make a case sensitive
  search. When you press okay, NVDA will search for this string.
*	control+shift+NVDA+k: Saves the current position as a bookmark. If you
  want to provide a name for this bookmark, select some text from this
  position before saving it.
*	control+shift+NVDA+delete: Deletes the bookmark corresponding to this
  position.
*	NVDA+k: Moves to the next bookmark.
*	shift+NVDA+k: Moves to the previous bookmark.
*	control+shift+k: Copies the file name where the place markers data will be
  saved to the clipboard, without an extension.
*	alt+NVDA+k: Opens a dialog with the bookmarks saved for this document. You
  can write a note for each bookmark; press Save note to save
  changes. Pressing OK you can move to the selected position.


## स्थान आदेस उप मेनु(नेत्रवानी+N) ##

Using the Place markers submenu under NVDA's Preferences menu, you can
access:

*	Specific search folder: opens a folder of specific searches previously
  saved.
*	Bookmarks folder: Opens a folder of the saved bookmarks.
*	Copy placeMarkers folder: You can save a copy of the bookmarks folder.
*	Restore placeMarkers: You can restore your bookmarks from a previously
  saved placeMarkers folder.

Note: The bookmark position is based on the number of characters; and
therefore in dynamic pages it is better to use the specific search, not
bookmarks.


## Changes for 8.0 ##
*	Removed fragment identifiers from bookmark filenames, which can avoid
  issues in the VitalSource Bookshelf ePUB reader.
*	Added a Notes dialog, to associate comments for saved bookmarks and move
  to the selected position.

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

## Changes for 6.0 ##
* When the add-on features are not usable, gestures are sent to the
  corresponding application.

## ३.० मा गरिएका परिवर्तनहरू ##
* Added case sensitive search.
* Removed option to open documentation from Place markers menu.
* More intuitive key commands.

## ४.० मा गरिएका परिवर्तनहरू ##
* Removed fragment identifiers from bookmark filenames, which can avoid
  issues in ePUBREADER Firefox add-on.
* थप-साधन सहयोग थप-साधन व्यबस्थापकमा उपलब्ध छ ।.

## ३.१ मा गरिएका परिवर्तनहरू ##
* अनुवादको अध्यावधिकरण र अनुदित भाषाहरू
* Bookmark position is not announced in skim reading.

## ३.० मा गरिएका परिवर्तनहरू ##
* योजना वाचनलाई थप गरियो ।

## २.0 मा गरिएका परिवर्तनहरू ##
* हरेक फाइलमा भएका विभिन्न खोजीलाइ मेटाउन र बचत गर्ने विकल्पहरू थप गरियो । 
* गैर ल्याटीन वर्णहरू भएका मार्ग हुदाँ काटिने समस्या हल गरियो ।
* अब नेत्रवाणीको लगानीसङ्केत पातो प्रयोग गरेर द्रुतमार्ग कायम गर्न सक्ने
  बनाइयो ।

## १.० मा गरिएका परिवर्तनहरू ##
* सुरुको संस्करण
* अनुवादीत भाषाहरू: ब्राजेलियन पुर्तगाली, फारसी, फिनिस, फ्रांन्सेली,
  ग्यालेसियन, जर्मनि, इटालि, जापानी, कोरियाली, नेपालि, पुर्तगाली, स्पेनि,
  स्लोभाक, स्लोबिनियन, तामिल ।

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=pm

[2]: http://addons.nvda-project.org/files/get.php?file=pm-dev
