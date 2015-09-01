# स्थान चिनो #

* लेखक: Noelia, Chris.
* अनुबहन[version 1.0][1]
* अनुबहन [development version][2]

This addon is used for saving and searching specific text strings or
bookmarks, on web pages or documents in NVDA's browse mode. It can also be
used for saving or searching strings of text in multi-line controls; in this
case, if it's not possible to update the caret, the corresponding string
will be copied to the clipboard, so that it can be searched using other
tools.  The plugin saves the specified strings and bookmarks to text and
pickle files. The name of these files is based on the title and URL of the
current document.

This addon is based on SpecificSearch and Bookmark&Search, developed by the
same author. You should uninstall them to use this one, since they have
common keystrokes and features.

## कुञ्जी आदेस: ##

*	control+shift+NVDA+s; Opens a dialog that allows you to save a text string   you want to find in the current document. By default, the text previously saved for this file is shown. Delete this text and press Ok button if you wish to remove the text file corresponding to the saved search, or type new text to add another search.
*	control+shift+NVDA+f; opens a dialog with a edit box that shows the last saved search; in this dialog you can also select the previously saved searches from a combo box and choose an action from the next combo box. If there is no available files for specific search in the current document, NVDA will warn you that it is not found any file for specific search.
*	control+shift+NVDA+k; Saves the current position as a bookmark
*	control+shift+NVDA+delete; Deletes the bookmark corresponding to this position.
*	NVDA+k; Moves to the next bookmark.
*	shift+NVDA+k; Moves to the previous bookmark.
*	control+shift+k; Copies to clipboard the file name, without extension, where the place markers data will be saved.

## स्थान आदेस उप मेनु(नेत्रवानी+N) ##


प्राथमिकता मेनु भित्र रहेको  स्थानचिनो उपमेनुलाई प्रयोग गरेर तपाइले पहुंच
पुर्‍याउन सक्नु हुन्छ ।

*	Specific search folder: opens a folder of specific searches previously
  saved.
*	पुस्तकचिनो थैली; पुस्तकचिनो बचत गरिएको थैलि पल्टाउने छ ।
*	Copy placeMarkers folder; you can save a copy of the bookmarks folder.
*	स्थानचिनोको पुनर्स्थापन; तपाइले पहिले बचत गरिएको पुस्तकचिनोबाट स्थानचिनलाई
  पुनर्स्थापन गर्न सक्नु हुन्छ ।
*	Documentation file, in your selected language if available, or English by
  default.

टिप्पणी: पुस्तकचिनोको स्थान वर्णहरुको सङ्ख्या; गतिसील सामाग्री युक्त पृष्ठमा
हुने भएकोले विसेष खोजी गर्नु राम्रो हुन्छ  तर निदिर्ट पुस्तकचिनो मा होइन ।


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
