#Otomotiv Satış Tahmini: Geleceği Şekillendiren Analizler
**Proje Hakkında**
Bu proje, otomotiv sektöründeki gelecekteki satışları yüksek doğrulukla tahmin etmek için tasarlanmış bir makine öğrenmesi modelidir. Yanlış tahminlerin yol açabileceği kaynak israfını veya fırsat kaçırılmasını engellemeyi ve işletmelerin üretim, pazarlama ve stok yönetimi gibi kritik kararları daha bilinçli ve veri odaklı almasını sağlayarak rekabet avantajı yaratmayı hedefler. Geliştirilen model, geçmiş satış verilerini ve ilişkili ekonomik göstergeleri analiz ederek gelecekteki satış eğilimlerini öngörür.



**Temel Hedefler**


Tarihsel verileri kullanarak otomotiv satışlarını yüksek doğrulukla tahmin etmek.

İşletmelerin daha bilinçli kararlar almasını sağlayarak rekabet avantajı yaratmak.

Üretim, envanter ve pazarlama stratejilerini optimize etmek için sağlam bir temel sunmak.

**Kullanılan Teknolojiler**


Modelin geliştirilmesi, dağıtılması ve servis edilmesi aşamalarında aşağıdaki teknolojiler kullanılmıştır:


Prophet (Facebook): Güçlü zaman serisi analizleri ve tahminleri için kullanılan temel kütüphane.


Python: Veri işleme, model geliştirme ve API oluşturma için ana programlama dili.


Flask: Geliştirilen tahmin modelini hızlı ve hafif bir web servisi olarak sunmak için kullanılan mikro çerçeve.



Docker: Uygulamanın farklı ortamlar arasında kolayca dağıtılabilmesi, izole edilmesi ve yönetilmesi için konteynerleştirme platformu.

** Veri Seti**
Modelin temeli, "Veri-Seti.xlsx" dosyasından elde edilen kapsamlı tarihsel otomotiv satış verileridir.


Temel Boyut (ds): Date (Ay ve yıl bilgisi).




Tahmin Değişkeni (y): Otomotiv Satış (Belirli dönemdeki otomotiv satış adetleri).



Diğer Değişkenler (Gelecek Geliştirmeler): ÖTV Oranı, Faiz, EUR/TL, Kredi Stok gibi bu iterasyonda doğrudan kullanılmayan ancak gelecekte potansiyel aday olan ek sütunlar mevcuttur.

** Model Geliştirme Süreci**
Veri Hazırlığı: Ham veri seti, Prophet kütüphanesinin gerektirdiği formata dönüştürülmüştür. Bu, Date sütununun ds ve Otomotiv Satış sütununun y olarak yeniden adlandırılmasını içerir.


Model Eğitimi: Dönüştürülmüş verilerle Prophet modeli eğitilmiş; bu aşamada geçmiş trendler, mevsimsellikler ve tatil etkileri öğrenilmiştir.


Model Doğrulama: Eğitilmiş modelin ürettiği tahminler, gerçek verilerle (ground truth) karşılaştırılarak modelin güvenilirliği ve doğruluğu değerlendirilmiştir.

**API ve Servis**


Tahmin modelini harici sistemlerin kullanımına sunmak için bir Web API'si geliştirilmiştir.



Model Serileştirme: Eğitilen Prophet modeli, kolay yükleme ve kullanım için serialized_model.json dosyasına kaydedilmiştir.


Web API: Flask mikro çerçevesi kullanılarak basit ve etkili bir POST API'si (app.py) geliştirilmiştir.


Tahmin Mekanizması: API'ye belirli bir tarih veya tarihler listesi gönderildiğinde, kayıtlı model o tarihe ait otomotiv satış tahminini döndürür. Bu, işletmelerin anlık ve dinamik tahminler almasını sağlar.
