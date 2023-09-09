# yerİmleri #

* Yazarlar: Noelia, Chris.

Bu eklenti, belirli metin dizelerini veya yerimlerini kaydetmek ve aramak
için kullanılır. NVDA'nın göz atma modunda web sayfalarında veya belgelerde
kullanılabilir. Çok satırlı kontrollerde metin dizelerini kaydetmek veya
aramak için de kullanılabilir; bu durumda, yerimini güncellemek mümkün
değilse, ilgili dize panoya kopyalanır, böylece diğer araçlar kullanılarak
aranabilir.  Eklenti, belirtilen dizeleri ve yer imlerini, adı geçerli
belgenin başlığına ve URL'sine dayanan dosyalara kaydeder.  Bu eklenti aynı
yazar tarafından geliştirilen SpecificSearch ve Bookmark&Search'e
dayanmaktadır. Ortak tuş vuruşlarına ve özelliklere sahip olduklarından,
bunu kullanmak için onları kaldırmalısınız.

## Tuş Komutları: ##

*	kontrol+shift+NVDA+f: Son kaydedilen aramayı gösteren düzenleme kutusu
  içeren bir iletişim kutusu açar; bu iletişim kutusunda ayrıca bir açılan
  kutudan önceden kaydedilmiş aramaları seçebilir veya bir onay kutusu
  kullanarak seçilen dizeyi geçmişten kaldırabilirsiniz. Düzenleme kutusunda
  yer alan metnin kayıtlı metinlerinizin geçmişine eklenip eklenmeyeceğini
  seçebilirsiniz. Son olarak, bir sonraki radyo düğmesi grubundan (Sonrakini
  ara, Öncekini ara veya Arama yapma arasında) bir eylem seçin ve NVDA'nın
  büyük/küçük harfe duyarlı bir arama yapıp yapmayacağını belirtin. Tamam
  düğmesine bastığınızda, NVDA bu dizeyi arayacaktır.
*	kontrol+shift+NVDA+y: Geçerli konumu yerimi olarak kaydeder. Bu yerimi
  için bir ad vermek istiyorsanız, kaydetmeden önce bu konumdan bir miktar
  metin seçin.
*	kontrol+shift+NVDA+sil: Bu konuma karşılık gelen yer imini siler.
*	NVDA+y: Sonraki yerimine gider.
*	shift+NVDA+y: Önceki yerimine gider.
*	Atanmamış: Tarama modunda yerimleri verilerinin kaydedileceği dosya adını
  uzantısız olarak gösterir.
*	alt+NVDA+y: Bu belge için kaydedilen yerimlerini içeren bir iletişim
  kutusu açar. Her yer imi için bir not yazabilirsiniz; Değişiklikleri
  kaydetmek için Notu kaydet'e basın. Sil'e basarak seçili yer imini
  kaldırabilirsiniz. Tamam'a basarak seçilen konuma geçebilirsiniz.
*	Atanmamış: Bir konumu geçici yer imi olarak kaydeder.
*	Atanmamış: Geçerli belge için geçici yerimine gider.
*	Atanmadı: Belirli bir belge için aranan son metinde sonrakini bulur.
*	Atanmadı: Belirli bir belge için aranan son metinde öncekini bulur.


## Yerimleri Alt menüsü (NVDA + N) ##

NVDA'nın Tercihler menüsü altındaki Yerimleri alt menüsünü kullanarak
şunlara erişebilirsiniz:

*	Özel arama klasörü: Önceden kaydedilen özel aramalar klasörü açılır.
*	Yerimleri klasörü: Kaydedilen yerimlerinin bulunduğu bir klasörü açar.
*	Yerimleri klasörünü kopyala: Yerimleri klasörünün bir kopyasını
  kaydedebilirsiniz.
*	Yerimlerini Geri Yükle: yerimlerinizi önceden kaydedilmiş bir Yerimleri
  klasöründen geri yükleyebilirsiniz.

Not: Yerimi konumu, karakter sayısına bağlıdır; ve bu nedenle dinamik
sayfalarda, yer imlerini değil, belirli aramayı kullanmak daha iyidir.

## 24.0 için değişiklikler
* NVDA+k, NVDA+shift+k, NVDA+alt+k ve NVDA+control+shift+k gibi hareketlerde
  k yerine y kullanılır.
* NVDA 2023.1 ile uyumludur.

## 23.0 için değişiklikler
* Eklenti, Microsoft Word ile yeniden çalışır duruma getirildi.

## 22.0 için değişiklikler
* Abdel sayesinde yerimlerine gidebilir ve UIA etkinken silebiliriz.

## 21.0 için değişiklikler
* Yerimleri, Abdel sayesinde Chromium tabanlı tarayıcılarda UIA
  etkinleştirilerek kaydedilebilir.

## 20.0 için değişiklikler
* NVDA 2022.1 veya sonraki sürümünü gerektirir.

## 19.0 için değişiklikler ##
* Eklenti, güvenli ekranlarda çalıştırılamaz.

## 18.0 için değişiklikler ##
* Yerimlerinin yolunu görme komutu, geçerli belge için kalıcı yer imleri,
  belirli arama için metin veya geçici bir yer imi olup olmadığını gösterir.

## 17.0 için değişiklikler ##
* Bazı belgelerde yerimlerinin kaydedilmesine izin vermeyen bir hata
  düzeltildi.
* Tercümelerin düzgün çalışmasını sağlayan çevrilmiş dizeler düzeltildi.

## 16.0 için değişiklikler ##
* NVDA 2021.1 veya üstü ile uyumludur (gerekli).
* Geçici yerimlerine taşınırken hızlı okuma desteklenir.
* Gerekirse [diğer
  sürümleri](https://github.com/nvdaes/placeMarkers/releases)
  indirebilirsiniz.

## 15.0 için değişiklikler ##
* Gözatma modunda tümünü söyle ile okurken, NVDA 2020.4'teki sonrakini bul
  ve öncekini bul komutlarına göre, göz gezdirerek okumaya izin ver seçeneği
  etkinleştirilmişse belirli sonrakini bul ve belirli öncekini bul komutları
  artık okumayı durdurmaz.
* Belirli öncekini bul komutunu çalıştırdıktan sonra Belirli arama iletişim
  kutusu açıldığında, Öncekini ara seçeneği seçilecektir.

## 14.0 için değişiklikler ##
*	Yerimleri verilerinin kaydedileceği dosyanın adını kopyalama komutu, bu
  dosya adını Tarama modunda gösteren bir komutla değiştirilmiştir. Bu, bir
  harekete atanmamış.
*	"Aranacak metin" alanı artık "Kayıtlı metin" alanıyla örtüşmüyor. (Cyrille
  Bougot'ya teşekkürler).
*	NVDA 2019.3 veya sonraki sürümünü gerektirir.

## 13.0 için değişiklikler ##
*	Belirli bir belge için aranan son metnin sonraki ve önceki oluşumlarını
  bulmak için atanmamış komutlar eklendi.
*	Spesifik arama özelliği, NVDA'nın Hakkında iletişim kutusu açıkken
  çalışır.
*	Belirli arama iletişim kutusunda, bu seçenek son arama için seçilmişse,
  büyük/küçük harfe duyarlı onay kutusu işaretlenecektir.
*	Eklenti güncellendiğinde, NVDA'nın ana yapılandırma klasörüne kaydedilen
  yerimlerini içe aktarmayı tercih etmediğiniz sürece, eklentinin önceki
  sürümünde kaydedilen belirli arama için yer işaretleri ve dizeler otomatik
  olarak yeni sürüme kopyalanacaktır.
*	Yerimlerini kopyalamak için iletişim kutusunu kullanırken, seçilen
  klasörün adı placeMarkersBackup değilse, Documents veya Downloads gibi
  önemli verileri içeren dizinlerin silinmesini önlemek için bu ada sahip
  bir alt klasör oluşturulur.

## 12.0 için değişiklikler ##
*	Yerimleri kaydedilmeden önce Çince karakterler seçilirse, Notlar iletişim
  kutusunu açmaya çalışırken NVDA'nın çökmesine neden olan kritik bir hata
  düzeltildi.

## 11.0 için değişiklikler ##
*	NVDA 2018.3 veya sonrası ile uyumludur (gerekli).
*	Gerekirse [NVDA 2017.3] ile uyumlu son sürümü[3] indirebilirsiniz.

## 10.0 için değişiklikler ##
*	Edge'de, NVDA+k, NVDA+shift+k veya NVDA+alt+k gibi yer imleri seçimiyle
  ilişkili hareketler, özellikle uzun belgelerde hataları önlemek için
  imleci yer imlerine taşımaya çalışmak yerine uygulamaya gönderilir.
*	Artık Edge'de özel arama desteklenmektedir.

## 9.0 için değişiklikler
*	Notlar iletişim kutusundan bir yerimine taşınırken, inceleme imleci sistem
  imlecini takip eder.
*	Önceki yerimini seçme komutu tekrar düzgün çalışıyor.
*	Yer işaretleri, Notlar iletişim kutusundan silinebilir.
*	Artık kaydetmek ve her belge için geçici bir Yerimine taşımak için
  hareketler atayabilirsiniz.

## 8.0 için değişiklikler ##
*	Yerimleri dosya adlarından, VitalSource Bookshelf ePUB okuyucusundaki
  sorunları önleyebilen parça tanımlayıcıları kaldırıldı.
*	Kayıtlı Yerimleri için yorumları ilişkilendirmek ve seçilen konuma taşımak
  için bir Notlar iletişim kutusu eklendi.

## 7.0 için değişiklikler ##
*	Belirli bir arama için bir metin dizesini kaydetme iletişim kutusu
  kaldırıldı. Bu işlev artık, Tamam düğmesine basıldığında farklı eylemlere
  izin verecek şekilde yeniden tasarlanan Özel arama iletişim kutusuna dahil
  edilmiştir.
*	Diyalogların görsel sunumu, NVDA'da gösterilen diyalogların görünümüne
  bağlı kalınarak geliştirildi.
*	Tarama Modunda Sonrakini Bul veya Öncekini Bul komutunun
  gerçekleştirilmesi, orijinal Bul büyük/küçük harfe duyarlıysa artık doğru
  şekilde büyük/küçük harfe duyarlı bir arama yapacaktır.
*	NVDA 2016.4 veya sonraki sürümünü gerektirir.
*	Artık yerimlerini kopyala ve geri yükle iletişim kutularını açmak için
  hareketler atayabilirsiniz.
*	NVDA, yerimleri kopyalandığında veya geri yüklendiğinde ilgili iletişim
  kutularıyla bildirimde bulunmak için bir mesaj sunar.

## 6.0 için değişiklikler ##
* Eklenti özellikleri kullanılamadığında, ilgili uygulamaya hareketler
  gönderilir.

## 5.0 için değişiklikler ##
* Büyük/küçük harfe duyarlı arama eklendi.
* Yerimleri menüsünden belgeleri açma seçeneği kaldırıldı.
* Daha sezgisel tuş komutları.

## 4.0 için değişiklikler ##
* EPUBREADER Firefox eklentisindeki sorunları önleyebilecek yerimi dosya
  adlarından parça tanımlayıcıları kaldırıldı.
* Eklenti yardımına Eklenti Yöneticisinden ulaşılabilir.

## 3.1 için değişiklikler ##
* Var olan diller güncellendi ve yeni diller eklendi.
* Göz atma modu okumasında yerimi konumu bildirilmez.

## 3.0 için Değişiklikler ##
* Tarama modunda okuma desteği eklendi.

## 2.0 için değişiklikler ##
* Her dosya için farklı aramaları kaydetmek ve silmek için seçenekler
  eklendi.
* Yollar latin olmayan karakterler içerdiğinde bozulan hata düzeltildi.
* Kısayollar şimdi NVDA girdi hareketleri iletişim kutusu kullanılarak
  yeniden atanabilir.

## 1.0 için değişiklikler ##
* İlk sürümü.
* Tercüme:, Japonca, Korece, Nepal, Portekizce, İspanyolca, Slovakça,
  Slovence Tamil, İtalyanca, Almanca, Galiçyaca, Fransızca, Brezilya
  Portekizcesi, Farsça, Fince.

[[!tag dev stable]]

[3]: https://www.nvaccess.org/addonStore/legacy?file=pm-o
