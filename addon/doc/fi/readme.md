# Paikkamerkit #

* Tekijät: Noelia, Chris
* Lataa [vakaa versio][1]
* Lataa [kehitysversio][2]

Tätä lisäosaa käytetään NVDA:n selaustilassa määrättyjen merkkijonojen tai
paikkamerkkien tallentamiseen ja etsimiseen verkkosivuilta tai
asiakirjoista. Sitä voidaan käyttää myös merkkijonojen tallentamiseen tai
etsimiseen monirivisistä säätimistä. Mikäli järjestelmäkohdistimen
siirtäminen ei ole tällöin mahdollista, hakua vastaava merkkijono kopioidaan
leikepöydälle, jotta sitä voidaan etsiä muilla tavoilla.  Merkkijonot ja
paikkamerkit tallennetaan teksti- ja pickle-tiedostoihin. Tiedostojen nimet
perustuvat nykyisen asiakirjan nimeen ja URL-osoitteeseen.

Tämä lisäosa perustuu saman tekijän kehittämiin SpecificSearch- ja
Bookmark&Search-lisäosiin. Sinun tulisi poistaa ne tämän version
käyttämiseksi, sillä niissä on samoja näppäinkomentoja ja ominaisuuksia.

## Näppäinkomennot: ##

*	control+shift+NVDA+s; Opens a dialog that allows you to save a text string   you want to find in the current document. By default, the text previously saved for this file is shown. Delete this text and press Ok button if you wish to remove the text file corresponding to the saved search, or type new text to add another search.
*	control+shift+NVDA+f; opens a dialog with a edit box that shows the last saved search; in this dialog you can also select the previously saved searches from a combo box and choose an action from the next combo box. If there is no available files for specific search in the current document, NVDA will warn you that it is not found any file for specific search.
*	control+shift+NVDA+k; Saves the current position as a bookmark
*	control+shift+NVDA+delete; Deletes the bookmark corresponding to this position.
*	NVDA+k; Moves to the next bookmark.
*	shift+NVDA+k; Moves to the previous bookmark.
*	control+shift+k; Copies to clipboard the file name, without extension, where the place markers data will be saved.

## Paikkamerkit-alavalikko (NVDA+N) ##


Asetukset-valikosta löytyvästä Paikkamerkit-alavalikosta pääset käyttämään
seuraavia toimintoja:

*	Sivukohtaisen haun kansio: avaa aiemmin tallennettujen sivukohtaisten
  hakujen kansion.
*	Paikkamerkkien kansio: avaa tallennettujen paikkamerkkien kansion.
*	Kopioi paikkamerkkien kansio: tallentaa kopion paikkamerkkien kansiosta.
*	Palauta paikkamerkit: palauttaa paikkamerkit aiemmin tallennetusta
  paikkamerkkien kansiosta.
*	Avaa ohjetiedoston nykyisellä kielellä tai englanniksi, mikäli käännöstä
  ei ole saatavilla.

Huomautus: Paikkamerkin sijainti perustuu merkkien lukumäärään. Muuttuvaa
sisältöä sisältävillä sivuilla on parasta käyttää tarkan sijainnin
tallentavien paikkamerkkien sijasta sivukohtaista hakua.


## Changes for 5.0 ##
* Added case sensitive search.
* Removed option to open documentation from Place markers menu.
* More intuitive key commands.

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
