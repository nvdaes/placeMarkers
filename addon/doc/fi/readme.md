# Paikkamerkit #

* Tekijät: Noelia, Chris
* Lataa [vakaa versio][1]
* Lataa [kehitysversio][2]

Tätä lisäosaa käytetään NVDA:n selaustilassa määrättyjen merkkijonojen tai
paikkamerkkien tallentamiseen ja etsimiseen verkkosivuilta tai
dokumenteista. Sitä voidaan käyttää myös merkkijonojen tallentamiseen tai
etsimiseen monirivisistä säätimistä. Mikäli järjestelmäkohdistimen
siirtäminen ei ole tällöin mahdollista, hakua vastaava merkkijono kopioidaan
leikepöydälle, jotta sitä voidaan etsiä muilla tavoilla.  Merkkijonot ja
paikkamerkit tallennetaan tiedostoihin, joiden nimet perustuvat nykyisen
dokumentin nimeen ja URL-osoitteeseen.  Tämä lisäosa perustuu saman tekijän
SpecificSearch- ja Bookmark&Search-lisäosiin. Sinun tulisi poistaa ne tämän
version käyttämiseksi, sillä niissä on samoja näppäinkomentoja ja
ominaisuuksia.

## Näppäinkomennot: ##

*	Ctrl+Shift+NVDA+F: Avaa muokkausruudun sisältävän valintaikkunan, joka
  näyttää viimeksi tallennetun haun. Tässä ikkunassa voit myös valita
  yhdistelmäruudusta aiemmin tallennettuja hakuja  tai poistaa valitun
  merkkijonon hakuhistoriasta valintaruutua käyttäen. Voit lisäksi valita,
  lisätäänkö muokkausruudun sisältämä teksti hakuhistoriaasi. Valitse
  lopuksi toiminto seuraavien valintapainikkeiden ryhmästä (Etsi seuraava,
  Etsi edellinen tai Ei etsintää), ja määrittää, suorittaako NVDA
  kirjainkoon huomioivan haun. Kun painat OK, NVDA etsii antamaasi
  merkkijonoa.
*	Ctrl+Shift+NVDA+K: Tallentaa nykyisen sijainnin paikkamerkiksi.
*	Ctrl+Shift+NVDA+Delete: Poistaa paikkamerkin nykyisestä sijainnista.
*	NVDA+K: Siirtää seuraavaan paikkamerkkiin.
*	Shift+NVDA+K: Siirtää edelliseen paikkamerkkiin.
*	Ctrl+Shift+K: Kopioi paikkamerkkitiedoston nimen leikepöydälle ilman
  tarkennetta.


## Paikkamerkit-alavalikko (NVDA+N) ##

Asetukset-valikosta löytyvästä Paikkamerkit-alavalikosta pääset käyttämään
seuraavia toimintoja:

*	Sivukohtaisen haun kansio: avaa aiemmin tallennettujen sivukohtaisten
  hakujen kansion.
*	Paikkamerkkien kansio: Avaa tallennettujen paikkamerkkien kansion.
*	Kopioi paikkamerkkien kansio: Tallentaa kopion paikkamerkkien kansiosta.
*	Palauta paikkamerkit: Palauttaa paikkamerkit aiemmin tallennetusta
  paikkamerkkien kansiosta.

Huom: Paikkamerkin sijainti perustuu merkkien lukumäärään, joten tämän
vuoksi muuttuvan sisällön sivuilla on parasta käyttää tarkan sijainnin
tallentavien paikkamerkkien sijasta sivukohtaista hakua.

## Muutokset versiossa 7.0 ##
*	Merkkijonon sivukohtaiseen hakuun tallentava valintaikkuna on
  poistettu. Tämä toiminnallisuus on sisällytetty Sivukohtainen haku
  -valintaikkunaan, joka on uudelleensuunniteltu mahdollistamaan eri
  toimintoja OK-painiketta painettaessa.
*	Valintaikkunoiden visuaalista esitystä on parannettu noudattamaan NVDA:n
  ikkunoiden ulkoasua.
*	Etsi seuraava- tai Etsi edellinen -komento suorittaa nyt selaustilassa
  kirjainkoon huomioivan haun, mikäli alkuperäinen haku oli sellainen.
*	Edellyttää NVDA:n 2016.4-versiota tai uudempaa.
*	Paikkamerkkien kopiointi- ja palautusvalintaikkunoille on nyt mahdollista
  määrittää syöte-eleet.
*	NVDA ilmoittaa, kun paikkamerkkejä on kopioitu tai palautettu omilla
  valintaikkunoillaan.

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
