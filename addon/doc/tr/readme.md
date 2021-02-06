# yerİmleri #

* Yazarlar: Noelia, Chris.
* İndir [kararlı sürüm][1]
* İndir [geliştirilen sürüm][2]

Bu eklenti, NVDA tarama kipinde gösterilen web sayfaları veya belgeler
üzerinde, belirli metin dizeleri veya yer imleri kaydetme ve arama için
kullanılır, Aynı zamanda çoklu-hattı kontrol metinlerin dizeleri kaydetme
veya aramak için de kullanılabilir; Bu durumda, imlecin konumunda güncelleme
yapmak mümkün değil ise, karşılık gelen dize, panoya kopyalanır, böylece
diğer araçlar kullanılarak aranabilir. metin ya da yer imi text ya da pickle
dosyalarına kaydedilir. Bu dosyaların adı, geçerli belgenin başlığı ve URL
adresine dayanmaktadır.

Bu eklenti aynı yazar tarafından geliştirilen SpecificSearch ve Bookmark ve
Arama adlı eklentiye  dayanmaktadır. Ortak tuş komutlarına ve özelliklere
sahip oldukları için eskisini kaldırmanız gerekmektedir.

## Tuş Komutları: ##

*	control+shift+NVDA+s; Opens a dialog that allows you to save a text string   you want to find in the current document. By default, the text previously saved for this file is shown. Delete this text and press Ok button if you wish to remove the text file corresponding to the saved search, or type new text to add another search.
*	control+shift+NVDA+f; opens a dialog with a edit box that shows the last saved search; in this dialog you can also select the previously saved searches from a combo box and choose an action from the next combo box. If there is no available files for specific search in the current document, NVDA will warn you that it is not found any file for specific search.
*	control+shift+NVDA+k; Saves the current position as a bookmark
*	control+shift+NVDA+delete; Deletes the bookmark corresponding to this position.
*	NVDA+k; Moves to the next bookmark.
*	shift+NVDA+k; Moves to the previous bookmark.
*	control+shift+k; Copies to clipboard the file name, without extension, where the place markers data will be saved.

## Yer imi Alt menüsü (NVDA + N) ##


Tercihler menüsünde yer işaretleri alt menüsünü kullanarak:

*	Özel arama klasörü: Önceden kaydedilen özel aramalar klasörü açılır.
*	Yer imleri klasörü; kaydedilen yer imleri klasörü açılır.
*	Yerimleri klasörünü kopyala; yer imleri klasörünün bir kopyasını
  kaydedebilirsiniz.
*	Yer imlerini geri yükle; önceden kaydettiğiniz yer imlerini geri
  yükleyebilirsiniz.
*	Dokümantasyon dosyası, seçtiğiniz dilde kullanılabilirse, ya da varsayılan
  olarak İngilizce.

Not: Yer imi konumu karakter sayısına dayanmaktadır; dinamik bir içeriğe
sahip sayfalarda kesin bir konuma kaydetmek için özel arama değil, yer
imleri kullanmak daha iyidir.

## Changes for 6.0 ##
* When the add-on features are not usable, gestures are sent to the
  corresponding application.

## Changes for 5.0 ##
* Added case sensitive search.
* Removed option to open documentation from Place markers menu.
* More intuitive key commands.

## Changes for 4.0 ##
* Removed fragment identifiers from bookmark filenames, which can avoid
  issues in ePUBREADER Firefox add-on.
* Add-on help is available from the Add-ons Manager.

## Changes for 3.1 ##
* Translation updates and new language.
* Bookmark position is not announced in skim reading.

## 3.0 için Değişiklikler ##
* Tarayarak okuma desteği eklendi.

## 2.0 Değişiklikler ##
* Her dosya için farklı aramaları kaydetmek ve silmek için seçenekler
  eklendi.
* Fixed bug which broke when paths contained non latin characters.
* Kısayollar şimdi NVDA girdi hareketleri iletişim kutusu kullanılarak
  yeniden atanabilir.

## 1.0 Değişiklikler ##
* İlk sürümü.
* Tercüme:, Japonca, Korece, Nepal, Portekizce, İspanyolca, Slovakça,
  Slovence Tamil, İtalyanca, Almanca, Galiçyaca, Fransızca, Brezilya
  Portekizcesi, Farsça, Fince.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=pm

[2]: http://addons.nvda-project.org/files/get.php?file=pm-dev
