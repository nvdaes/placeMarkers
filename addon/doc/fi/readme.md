# Paikkamerkit #

* Tekijät: Noelia, Chris
* Lataa [vakaa versio][1]
* Lataa [kehitysversio][2]

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

## Näppäinkomennot: ##

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


## Paikkamerkit-alavalikko (NVDA+N) ##

Using the Place markers submenu under NVDA's Preferences menu, you can
access:

*	Sivukohtaisen haun kansio: avaa aiemmin tallennettujen sivukohtaisten
  hakujen kansion.
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

## Muutokset versiossa 6.0 ##
* Kun lisäosan toiminnot eivät ole käytettävissä, komennot lähetetään
  suoraan aktiiviselle sovellukselle.

## Muutokset versiossa 5.0 ##
* Lisätty kirjainkoon huomioiva haku.
* Poistettu vaihtoehto ohjeen avaamiseen Paikkamerkit-valikosta.
* Intuitiivisemmat näppäinkomennot.

## Muutokset versiossa 4.0 ##
* Poistettu osatunnisteet kirjanmerkkitiedostojen nimistä, mikä saattaa
  välttää ongelmia Firefoxin ePUBREADER-lisäosan kanssa.
* Ohje on käytettävissä Lisäosien hallinnasta.

## Muutokset versiossa 3.1 ##
* Käännöksiä päivitetty ja lisätty uusi kieli.
* Kirjanmerkin sijaintia ei ilmoiteta pikaluvun aikana.

## Muutokset versiossa 3.0 ##
* Lisätty tuki pikaluvulle.

## Muutokset versiossa 2.0 ##
* Lisätty vaihtoehdot eri hakujen tallentamiseksi ja poistamiseksi kullekin
  tiedostolle.
* Korjattu ohjelmavirhe, joka rikkoi lisäosan toiminnan, kun polut
  sisälsivät muita kuin latinalaisia merkkejä.
* Näppäinyhdistelmien uudelleenmäärittely on nyt mahdollista NVDA:n
  syöte-eleet-valintaikkunaa käyttäen.

## Muutokset versiossa 1.0 ##
* Ensimmäinen versio.
* Käännetty kielille: brasilianportugali, espanja, farsi, galego, italia,
  japani, korea, nepali, portugali, ranska, saksa, slovakki, slovenia, suomi
  ja tamili.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=pm

[2]: http://addons.nvda-project.org/files/get.php?file=pm-dev
