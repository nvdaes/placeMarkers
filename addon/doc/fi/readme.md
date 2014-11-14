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

*	Control+Shift+NVDA+S: Avaa valintaikkunan, joka mahdollistaa nykyisestä asiakirjasta etsittävän merkkijonon tallentamisen. Oletusarvoisesti näytetään kyseiselle tiedostolle tallennettu teksti. Poista teksti ja paina OK-painiketta, mikäli haluat poistaa tallennettua hakua vastaavan tekstitiedoston, tai kirjoita uutta tekstiä lisätäksesi toisen haun.
*	Control+Shift+NVDA+F: Avaa valintaikkunan, joka näyttää muokkausruudussa viimeksi tallennetun haun. Tässä valintaikkunassa voit myös valita yhdistelmäruudusta aiemmin tallennettuja hakuja sekä valita viereisestä yhdistelmäruudusta toimenpiteen. Mikäli nykyiselle asiakirjalle ei ole sivukohtaisen haun tiedostoja, NVDA varoittaa, että yhtään sivukohtaisen haun tiedostoa ei löydy.
*	Control+Shift+NVDA+K: Tallentaa nykyisen sijainnin paikkamerkiksi.
*	Control+Shift+NVDA+delete: Poistaa paikkamerkin nykyisestä sijainnista.
*	Control+Shift+K: Siirtää seuraavaan paikkamerkkiin.
*	Shift+NVDA+K: Siirtää edelliseen paikkamerkkiin.
*	NVDA+K: Kopioi leikepöydälle paikkamerkkien tiedot sisältävän tiedoston nimen ilman päätettä.

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
