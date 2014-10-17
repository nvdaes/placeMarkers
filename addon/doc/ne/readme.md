# स्थान चिनो #

* लेखक: Noelia, Chris.
* डाउनलोड[version 1.0][1]
* डाउनलोट [development version][2]

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

*	control+shift+नेत्रवाणी+s; तपाइले चालू कागजातमा कुनै पाठ पदावली खोज्नका लागि सञ्चय गर्ने पातो देखाउने छ ।  पहिले बचत गरिएको पाठलाई स्वतः निर्धारण गरिएको हुन्छ । यो पाठलाई मेटाएर 'ठिक' भन्ने टाँकलाई दबाउनु होला ।यदि तपाइ सञ्चित खोजी पाठ फाइललाइ हटाउन चाहनु हुन्छ अथवा अर्को खोजिएको नयाँ  पाठ बचत गर्न  चाहनु हुन्छ भने पनि । 
*	control+shift+नेत्रवाणी +f; सबै भन्दा पछि बचत भएको खोजी पाठ युक्त सम्पादन कोठा सहितको पातो पल्टाउने छ ।; यो पातोमा पहिले खोजिएका पाठहरू कम्बो कोठा बाट चयन गरी अर्को कम्बो बाकसबाट कार्य रोज्न सकिने छ । यदि हालको कागजातमा कुनै विशेष खोजीका लागी फाइल रहेन छ भने, नेत्रवाणीले तपाइलाई कुनै विशेष खोजिको फाइल नभएको कुरा जनाउ दिनेछ ।n*	control+shift+नेत्रवाणी+k; हालको स्थानलाई पुस्तक चिनो रूपमा बचत गर्ने छ ।
*	control+shift+NVDA+delete; Deletes the bookmark corresponding to this position.
*	control+shift+k; Moves to the next bookmark.
*	shift+NVDA+k; Moves to the previous bookmark.
*	नेत्रवाणी+k; स्थान चिनो तथ्याङ्कलाई राखिएको फाइलको नाम विस्तारित रुप विना  क्लिपपाटीमा उतार्ने छ ।

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

## Changes for 4.0 ##
* Removed fragment identifiers from bookmark filenames, which can avoid
  issues in ePUBREADER Firefox add-on.
* Add-on help is available from the Add-ons Manager.

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
