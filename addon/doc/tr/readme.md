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

*	control+shift+NVDA+s; Geçerli belgede bulmak istediğiniz bir metin dizesi kaydetmenizi sağlayan bir iletişim kutusu açar. Varsayılan olarak, Daha önce bu dosya için kaydettiğiniz metin gösterilir. Bu metni silmek ve kayıtlı aramaya karşılık gelen metin dosyasını kaldırmak istiyorsanız Tamam düğmesine basın, veya başka bir arama eklemek için yeni metni yazın.
*	control+shift+NVDA+f; En son kaydedilen aramayı gösteren bir yazı alanı içiren bir iletişim kutusu açılır; Bu iletişim kutusunda Ayrıca açılan kutudan daha önce kaydedilen aramaları seçebilir ve bir sonraki seçim kutusundan bir eylem seçebilirsiniz. Geçerli belgede spesifik bir arama için herhangi bir uygun dosya yoksa, NVDA spesifik bir arama için herhangi bir dosya bulunamadığı konusunda sizi uyarır.
*	control+shift+NVDA+k; Yerimi olarak geçerli konumu kaydeder
*	control+shift+NVDA+delete; Bu konumdaki yerimini siler.
*	control+shift+k; Bir sonraki yer işaretine gider.
*	shift+NVDA+k; Önceki yer işaretine gider.
*	NVDA+k; Panoya uzantısı olmadan dosya adını kopyalar.

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

## Changes for 3.1 ##
* Translation updates and new language.

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
