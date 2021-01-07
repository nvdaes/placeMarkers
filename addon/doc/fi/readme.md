# Paikkamerkit #
* Tekijät: Noelia, Chris
* Yhteensopivuus: NVDA 2019.3 tai uudempi
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

*	Ctrl+Vaihto+NVDA+F: Avaa muokkausruudun sisältävän valintaikkunan, joka
  näyttää viimeksi tallennetun haun. Tässä ikkunassa voit myös valita
  yhdistelmäruudusta aiemmin tallennettuja hakuja  tai poistaa valitun
  merkkijonon hakuhistoriasta valintaruutua käyttäen. Voit lisäksi valita,
  lisätäänkö muokkausruudun sisältämä teksti hakuhistoriaasi. Valitse
  lopuksi toiminto seuraavasta valintapainikeryhmästä (Etsi seuraava, Etsi
  edellinen tai Ei hakua) ja määritä, suorittaako NVDA kirjainkoon
  huomioivan haun. Kun painat OK, NVDA etsii antamaasi merkkijonoa.
*	Ctrl+Vaihto+NVDA+K: Tallentaa nykyisen sijainnin paikkamerkiksi. Jos
  haluat antaa sille nimen, valitse sijainnista lyhyt tekstipätkä ennen
  paikkamerkin tallentamista.
*	Ctrl+Vaihto+NVDA+Delete: Poistaa paikkamerkin nykyisestä sijainnista.
*	NVDA+K: Siirtää seuraavaan paikkamerkkiin.
*	Vaihto+NVDA+K: Siirtää edelliseen paikkamerkkiin.
*	Ei määritetty: Näyttää paikkamerkkitiedoston nimen selaustilassa ilman
  tarkennetta.
*	Alt+NVDA+K: Avaa valintaikkunan, jossa näkyvät nykyiselle asiakirjalle
  tallennetut paikkamerkit. Voit kirjoittaa kullekin paikkamerkille
  muistiinpanon. Tallenna muutokset painamalla Tallenna muistiinpano. Voit
  poistaa valitun paikkamerkin painamalla Delete. Siirry valittuun
  sijaintiin painamalla OK.
*	Ei määritetty: Tallentaa nykyisen sijainnin tilapäiseksi paikkamerkiksi.
*	Ei määritetty: Siirtää tilapäiseen kirjanmerkkiin nykyisessä asiakirjassa.
*	Ei määritetty: Etsii viimeksi haetun tekstin seuraavan esiintymän mistä
  tahansa määrätystä asiakirjasta.
*	Ei määritetty: Etsii viimeksi haetun tekstin edellisen esiintymän mistä
  tahansa määrätystä asiakirjasta.


## Paikkamerkit-alavalikko (NVDA+N) ##

Asetukset-valikosta löytyvästä Paikkamerkit-alavalikosta pääset käyttämään
seuraavia toimintoja:

*	Sivukohtaisen haun kansio: avaa tallennettujen sivukohtaisten hakujen
  kansion.
*	Paikkamerkkien kansio: Avaa tallennettujen paikkamerkkien kansion.
*	Kopioi paikkamerkkien kansio: Tallentaa kopion paikkamerkkien kansiosta.
*	Palauta paikkamerkit: Palauttaa paikkamerkit aiemmin tallennetusta
  paikkamerkkien kansiosta.

Huom: Paikkamerkin sijainti perustuu merkkien lukumäärään, joten muuttuvan
sisällön sivuilla kannattaa käyttää tarkan sijainnin tallentavien
paikkamerkkien asemesta sivukohtaista hakua.

## Muutokset versiossa 14.0 ##
*	Paikkamerkkitiedoston nimen kopioiva komento on korvattu komennolla, joka
  näyttää tiedostonimen selaustilassa. Syötekomentoa ei ole määritetty.
*	"Etsittävä teksti" -kenttä ei enää ole "Tallennettu teksti" -kentän
  päällä. (Kiitos Cyrille Bougotille).
*	Edellyttää NVDA 2019.3:a tai uudempaa.

## Muutokset versiossa 13.0 ##
*	Lisätty komennot ilman näppäinkomentoa viimeksi haetun tekstin seuraavan
  ja edellisen esiintymän etsimiseen mistä tahansa  määrätystä asiakirjasta.
*	Sivukohtainen haku toimii, kun NVDA:n Tietoja-valintaikkuna on avoimena.
*	Sama kirjainkoko -valintaruutu valitaan sivukohtaisen haun
  valintaikkunassa, jos se oli valittuna edellistä hakua suoritettaessa.
*	Kun lisäosa päivitetään, aiemmassa versiossa tallennetut paikkamerkit ja
  sivukohtaisen haun merkkijonot kopioidaan automaattisesti uuteen versioon,
  paitsi jos haluat tuoda paikkamerkit NVDA-asetusten pääkansiosta.
*	Jos valitulle kansiolle ei ole paikkamerkkien kopiointivalintaikkunassa
  annettu nimeksi placeMarkersBackup, sen niminen alikansio luodaan, jotta
  estetään tärkeää dataa sisältävien hakemistojen, kuten Tiedostot tai
  Ladatut tiedostot, poistaminen.

## Muutokset versiossa 12.0 ##
*	Korjattu kriittinen bugi, joka kaatoi NVDA:n yritettäessä avata
  Muistiinpanot-valintaikkunaa, mikäli kiinalaisia merkkejä oli valittuna
  ennen paikkamerkkien tallentamista.

## Muutokset versiossa 11.0 ##
*	Yhteensopiva NVDA 2018.3:n tai uudemman kanssa (vaaditaan).
*	Viimeisen NVDA 2017.3:n kanssa yhteensopivan version voi ladata
  [tästä.][3]

## Muutokset versiossa 10.0 ##
*	Virheiden välttämiseksi (erityisesti pitkissä dokumenteissa)
  paikkamerkkien valintaan liittyvät syötekomennot, kuten NVDA+K,
  NVDA+Vaihto+K tai NVDA+Alt+K, lähetetään Edgessä sovellukselle sen sijaan,
  että yritettäisiin siirtää kohdistinta paikkamerkkeihin.
*	Sivukohtaista hakua tuetaan nyt Edgessä.

## Muutokset versiossa 9.0
*	Tarkastelukohdistin seuraa järjestelmän kohdistinta siirryttäessä
  paikkamerkkiin Muistiinpanot-valintaikkunasta.
*	Edellisen paikkamerkin valitseva komento toimii jälleen asianmukaisesti.
*	Paikkamerkkejä on mahdollista poistaa Muistiinpanot-valintaikkunasta.
*	Voit nyt määrittää kullekin dokumentille syötekomennot paikkamerkkien
  tallentamista ja niihin siirtymistä varten.

## Muutokset versiossa 8.0 ##
*	Osatunnisteet poistettu paikkamerkkitiedostojen nimistä VitalSource
  Bookshelf -ePub-lukijaan liittyvien ongelmien välttämiseksi.
*	Lisätty Muistiinpanot-valintaikkuna, jossa on mahdollista liittää
  tallennettuihin paikkamerkkeihin muistiinpanoja sekä siirtyä valittuun
  sijaintiin.

## Muutokset versiossa 7.0 ##
*	Merkkijonon sivukohtaiseen hakuun tallentava valintaikkuna on
  poistettu. Tämä toiminnallisuus on sisällytetty Sivukohtainen haku
  -valintaikkunaan, joka on uudelleensuunniteltu mahdollistamaan eri
  toimintoja OK-painiketta painettaessa.
*	Valintaikkunoiden visuaalista esitystä on parannettu noudattamaan NVDA:n
  ikkunoiden ulkoasua.
*	Etsi seuraava- tai Etsi edellinen -komento suorittaa nyt selaustilassa
  kirjainkoon huomioivan haun, mikäli alkuperäinen haku oli sellainen.
*	Edellyttää NVDA 2016.4:ää tai uudempaa.
*	Paikkamerkkien kopiointi- ja palautusvalintaikkunoille on nyt mahdollista
  määrittää syötekomennot.
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
* Pikanäppäimien uudelleenmäärittely on nyt mahdollista NVDA:n
  Syötekomennot-valintaikkunaa käyttäen.

## Muutokset versiossa 1.0 ##
* Ensimmäinen versio.
* Käännetty kielille: brasilianportugali, espanja, farsi, galego, italia,
  japani, korea, nepali, portugali, ranska, saksa, slovakki, slovenia, suomi
  ja tamili.


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=pm

[2]: https://addons.nvda-project.org/files/get.php?file=pm-dev

[3]: https://addons.nvda-project.org/files/get.php?file=pm-o
