# yer İşaretçileri #

* Yazarlar: Noelia, Chris.

Bu eklenti, belirli metin dizelerini veya yer işaretlerini kaydetmek ve aramak için kullanılır. NVDA'nın tarama modunda web sayfalarında veya belgelerde kullanılabilir. Ayrıca çok satırlı kontrollerde metin dizelerini kaydetmek veya aramak için de kullanılabilir; bu durumda, düzeltme işaretinin güncellenmesi mümkün değilse ilgili dize panoya kopyalanır, böylece diğer araçlar kullanılarak aranabilir.
Eklenti, belirtilen dizeleri ve yer işaretlerini, adı geçerli belgenin başlığına ve URL'sine dayalı olan dosyalara kaydeder.
Bu eklenti, aynı yazar tarafından geliştirilen SpecificSearch ve Bookmark&Search'e dayanmaktadır. Ortak tuş vuruşlarına ve özelliklere sahip olduklarından, bunu kullanmak için bunları kaldırmalısınız.

## Tuş Komutları: ##

*	kontrol+shift+NVDA+f: Son kaydedilen aramayı gösteren düzenleme kutusu içeren bir iletişim kutusu açar; bu iletişim kutusunda ayrıca bir açılan kutudan önceden kaydedilmiş aramaları seçebilir veya bir onay kutusu kullanarak seçilen dizeyi geçmişten kaldırabilirsiniz. Düzenleme kutusunda yer alan metnin kayıtlı metinlerinizin geçmişine eklenip eklenmeyeceğini seçebilirsiniz. Son olarak, bir sonraki radyo düğmesi grubundan (Sonrakini ara, Öncekini ara veya Arama yapma arasında) bir eylem seçin ve NVDA'nın büyük/küçük harfe duyarlı bir arama yapıp yapmayacağını belirtin. Tamam düğmesine bastığınızda, NVDA bu dizeyi arayacaktır.
*	kontrol+shift+NVDA+y: Geçerli konumu yer işareti olarak kaydeder. Bu yer işareti için bir ad vermek istiyorsanız, kaydetmeden önce bu konumdan bir miktar metin seçin.
*	kontrol+shift+NVDA+sil: Bu konuma karşılık gelen yer işaretini siler.
*	NVDA+y: Sonraki yer işaretine gider.
*	shift+NVDA+y: Önceki yer işaretine gider.
*	Atanmamış: Tarama modunda yer işaretleri verilerinin kaydedileceği dosya adını uzantısız olarak gösterir.
*	alt+NVDA+y: Bu belge için kaydedilen yer işaretlerini içeren bir iletişim kutusu açar. Her yer işareti için bir not yazabilirsiniz; Değişiklikleri kaydetmek için Notu kaydet'e basın. Sil'e basarak seçili yer işaretini kaldırabilirsiniz. Tamam'a basarak seçilen konuma geçebilirsiniz.
*	Atanmamış: Bir konumu geçici yer işareti olarak kaydeder.
*	Atanmamış: Geçerli belge için geçici yer işaretine gider.
*	Atanmadı: Belirli bir belge için aranan son metinde sonrakini bulur.
*	Atanmadı: Belirli bir belge için aranan son metinde öncekini bulur.


## Yer işaretleri Alt menüsü (NVDA + N) ##

NVDA'nın Tercihler menüsü altındaki Yer işaretleri alt menüsünü kullanarak şunlara erişebilirsiniz:

*	Özel arama klasörü: Önceden kaydedilen özel aramalar klasörü açılır.
*	Yer imleri klasörü: Kaydedilen yer işaretlerinin bulunduğu bir klasörü açar.
*	Yer işaretleri klasörünü kopyala: Yer işaretleri klasörünün bir kopyasını kaydedebilirsiniz.
*	Yer işaretlerini Geri Yükle: yer işaretlerinizi önceden kaydedilmiş bir Yer işaretleri klasöründen geri yükleyebilirsiniz.
*   Varsayılan Yer işaretleri Klasörünü ayarlayın: Yer İşaretleri için varsayılan klasör bu iletişim kutusundan ayarlanabilir. Normal yapılandırma profiline kaydedilecektir.

Not: Yer işareti konumu, karakter sayısına bağlıdır; ve bu nedenle dinamik sayfalarda, yer işaretlerini değil, belirli aramayı kullanmak daha iyidir.

## 45.0.0 için değişiklikler
* Varsayılan yer işaretleri klasörünü ayarlama yeteneği eklendi.
* Bu eklenti etkinken eklentiler yeniden yüklenirse, son kaydedilen yapılandırma uygulanır.
* Yer imlerinin ve belirli arama dizelerinin kaydedildiği geçerli dosyayı gösterirken taranabilir mesaja kopyala ve kapat düğmeleri eklendi.

## 35.0 için değişiklikler
* Yer imlerinin farklı oturumlardaki belirli web siteleri için geçerli olması amacıyla dosya adlarından URL parametreleri kaldırıldı.

## 24.0 için değişiklikler
* NVDA+k, NVDA+shift+k, NVDA+alt+k ve NVDA+control+shift+k gibi hareketlerde k yerine Y kullanılır.
* NVDA 2023.1 ile uyumludur.

## 23.0 için değişiklikler
* Eklenti, Microsoft Word ile yeniden çalışabilir duruma getirildi.

## 22.0 için değişiklikler
* Abdel sayesinde UIA etkinken yer imlerine gidebilir ve bunları silebiliriz.

## 21.0 için değişiklikler
* Abdel sayesinde yer imleri, Chromium tabanlı tarayıcılarda UIA etkinleştirilerek kaydedilebilir.

## 20.0 için değişiklikler
* NVDA 2022.1 veya sonraki sürümlerini gerektirir.

## 19.0 için değişiklikler ##
* Eklenti, güvenli ekranlarda çalıştırılamaz.

## 18.0 için değişiklikler ##
* Yer işaretlerinin yolunu görme komutu, geçerli belge için kalıcı yer imleri, belirli arama için metin veya geçici bir yer imi olup olmadığını gösterir.

## 17.0 için değişiklikler ##
* Bazı belgelerde yer işaretlerinin kaydedilmesine izin vermeyen bir hata düzeltildi.
* Tercümelerin düzgün çalışmasını sağlayan çevrilmiş dizeler düzeltildi.

## 16.0 için değişiklikler ##
*	NVDA 2021.1 veya sonrası ile uyumludur (gerekli).
* Geçici yer imlerine giderken hızlı okuma desteklenir.
*	Gerekirse [diğer sürümleri buradan](https://github.com/nvdaes/placemarkers/releases) indirebilirsiniz.

## 15.0 için değişiklikler ##
* NVDA 2020.4 sürümündeki “Sonrakini Bul” ve “Öncekini Bul” komutlarına göre, “Hızlı okumaya izin ver” seçeneği etkinleştirildiğinde, “Tümünü Oku” gibi komutlarla Tarama modunda okuma yaparken, “Belirli Sonrakini Bul” ve “Belirli Öncekini Bul” komutları artık okumayı durdurmamaktadır.
* Belirli öncekini bul komutunu çalıştırdıktan sonra Belirli arama iletişim kutusu açıldığında, Öncekini ara seçeneği seçilecektir.

## 14.0 için değişiklikler ##
*	Yer işaretleri verilerinin kaydedileceği dosyanın adını kopyalama komutu, bu dosya adını Tarama modunda gösteren bir komutla değiştirilmiştir. Bu, bir harekete atanmamış.
*	"Aranacak metin" alanı artık "Kayıtlı metin" alanıyla örtüşmüyor. (Cyrille Bougot'ya teşekkürler).
*	NVDA 2019.3 veya sonraki sürümlerini gerektirir.

## 13.0 için değişiklikler ##
*	Belirli bir belge için aranan son metnin sonraki ve önceki sonuçlarını bulmak için atanmamış komutlar eklendi.
*	Spesifik arama özelliği, NVDA'nın Hakkında iletişim kutusu açıkken çalışır.
*	Belirli arama iletişim kutusunda, bu seçenek son arama için seçilmişse, büyük/küçük harfe duyarlı onay kutusu işaretlenecektir.
*	Eklenti güncellendiğinde, NVDA'nın ana yapılandırma klasörüne kaydedilen yerimlerini içe aktarmayı tercih etmediğiniz sürece, eklentinin önceki sürümünde kaydedilen belirli arama için yer işaretleri ve dizeler otomatik olarak yeni sürüme kopyalanacaktır.
*	Yer işaretçilerini kopyalamak için iletişim kutusunu kullanırken, seçilen klasörün adı placeMarkersBackup değilse, Belgeler veya İndirilenler gibi önemli verileri içeren dizinlerin silinmesini önlemek için bu adda bir alt klasör oluşturulacaktır.

## 12.0 için değişiklikler ##
*	Yerimleri kaydedilmeden önce Çince karakterler seçilirse, Notlar iletişim kutusunu açmaya çalışırken NVDA'nın çökmesine neden olan kritik bir hata düzeltildi.

## 11.0 için değişiklikler ##
*	NVDA 2018.3 veya sonrası ile uyumludur (gerekli).

## 10.0 için değişiklikler ##
*	Edge'de, NVDA+k, NVDA+shift+k veya NVDA+alt+k gibi yer imleri seçimiyle ilişkili hareketler, özellikle uzun belgelerde hataları önlemek için imleci yer imlerine taşımaya çalışmak yerine uygulamaya gönderilir.
*	Artık Edge'de özel arama desteklenmektedir.

## 9.0 için değişiklikler
*	Notlar iletişim kutusundan bir yer imine geçtiğinizde inceleme imleci sistem imlecini takip eder.
*	Önceki yerimini seçme komutu artık düzgün çalışıyor.
*	Yer imleri, Notlar iletişim kutusundan silinebilir.
*	Artık kaydetmek ve her belge için geçici bir Yerimine taşımak için hareketler atayabilirsiniz.

## 8.0 için değişiklikler ##
*	Yerimleri dosya adlarından, VitalSource Bookshelf ePUB okuyucusundaki sorunları önleyebilen parça tanımlayıcıları kaldırıldı.
*	Kayıtlı Yer imleri için yorumları ilişkilendirmek ve seçilen konuma taşımak için bir Notlar iletişim kutusu eklendi.

## 7.0 için değişiklikler ##
*	Belirli bir arama için bir metin dizesini kaydetme iletişim kutusu kaldırıldı. Bu işlev artık, Tamam düğmesine basıldığında farklı eylemlere izin verecek şekilde yeniden tasarlanan Özel arama iletişim kutusuna dahil edilmiştir.
*	Diyalogların görsel sunumu, NVDA'da gösterilen diyalogların görünümüne bağlı kalınarak geliştirildi.
*	Tarama Modunda Sonrakini Bul veya Öncekini Bul komutunun gerçekleştirilmesi, orijinal Bul büyük/küçük harfe duyarlıysa artık doğru şekilde büyük/küçük harfe duyarlı bir arama yapacaktır.
*	NVDA 2016.4 veya sonraki sürümlerini gerektirir.
*	Artık yer işaretlerini kopyala ve geri yükle iletişim kutularını açmak için hareketler atayabilirsiniz.
*	NVDA, yer işaretleri kopyalandığında veya geri yüklendiğinde ilgili iletişim kutularıyla bildirimde bulunmak için bir mesaj sunar.

## 6.0 için değişiklikler ##
* Eklenti özellikleri kullanılamadığında hareketler ilgili uygulamaya gönderilir.

## 5.0 için değişiklikler ##
* Büyük/küçük harfe duyarlı arama eklendi.
* Yer işaretleri menüsünden belgeleri açma seçeneği kaldırıldı.
* Daha sezgisel tuş komutları.

## 4.0 için değişiklikler ##
* EPUBREADER Firefox eklentisindeki sorunları önleyebilecek yerimi dosya adlarından parça tanımlayıcıları kaldırıldı.
* Eklenti yardımına Eklenti Mağazası'ndan ulaşılabilir.

## 3.1 için değişiklikler ##
* Mevcut diller güncellendi ve yeni diller eklendi.
* Hızlı okumada yer imi konumu belirtilmez.

## 3.0 için değişiklikler ##
* Hızlı okuma desteği eklendi.

## 2.0 için değişiklikler ##
* Her dosya için farklı aramaları kaydetmek ve silmek için seçenekler eklendi.
* Yollar latin olmayan karakterler içerdiğinde bozulan hata düzeltildi.
* Kısayollar şimdi NVDA girdi hareketleri iletişim kutusu kullanılarak yeniden atanabilir.

## 1.0 için değişiklikler ##
* İlk sürüm.
* Çeviri: Brezilya Portekizcesi, Farsça, Fince, Fransızca, Galiçyaca, Almanca, İtalyanca, Japonca, Korece, Nepalce, Portekizce, İspanyolca, Slovakça, Slovence, Tamilce.
