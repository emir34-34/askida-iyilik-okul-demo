# Sunum Planı: 12 Ekim 2026, Yasemin Hoca ve Eyüp Hoca ile görüşme

> Bu görüşmenin asıl amacı **hocaların taleplerini almak** (görev tanımı, bölüm 5). Demo ve tasarım, hocaların tepki verebileceği somut bir başlangıç noktası. Görüşmenin sonunda [görüşme formu](gorusme-formu.html) doldurulmuş olmalı.

## Akış (yaklaşık 25 dakika)

| Süre | Ne | Nasıl |
|------|----|-------|
| 2 dk | **Amaç** | "Sizinle görüşemediğim için taslağı tahminlerle yazdım ve çalışan bir demo yaptım. Bugün tahminlerimin doğru olup olmadığını sizden öğrenmek istiyorum." |
| 3 dk | **Tasarım** | GitHub'daki README'yi aç. 8 dosyayı kısaca göster. `roller.md`'deki rol × eylem tablosunu ve `akis.md`'deki durum şemasını göster. |
| 3 dk | **Ekran taslakları** | [Ekran taslakları](https://emir34-34.github.io/askida-iyilik-okul-demo/ekran-taslaklari/) sayfasını aç. Telefon ve bilgisayar ekranlarını kaydırarak göster. "Reddit'i tanıyan öğrenciler bu düzene alışık." |
| 7 dk | **Canlı demo** | Aşağıdaki senaryo. |
| 10 dk | **Görüşme formu** | Formu hocalarla birlikte doldur. Her "Hayır"ın yanına ne istediklerini yaz. |

## Canlı demo senaryosu (iki telefon)

**Hazırlık:** 📱1'de `ogrenci1` (Mehmet), 📱2'de `ogrenci2` (Ayşe) ile önceden giriş yapılmış olsun.

1. **Mehmet istek açar (📱1):** Oluştur → k/ders → "Fizik formül kâğıdı lazım" → Yayınla.
   - 📱2'nin akışında 10 saniye içinde kendiliğinden belirir. *"Sayfayı yenilemeden geldi, canlı güncelleme."*
2. **Ayşe üstlenir (📱2):** İsteğe dokun → Üstlen → "Yarın getiririm" yorumu → Yapıldı.
   - 📱1'de istek sayfası açıksa 3 saniye içinde düğmeler değişir, bildirim çıkar.
3. **Mehmet onaylar (📱1):** Onayla → teşekkür notu → Onayla. *"Teşekkür görünür, ama hiçbir yerde sayılmaz. Sıralama tablosu yok."*
4. **Çift üstlenme gösterisi:** İki telefonda başka bir açık isteği aç ("İngilizce konuşma pratiği"). İki telefona **aynı anda** "Üstlen". Biri alır, diğeri "az önce başka biri tarafından üstlenildi" der.
5. **Öğretmen (isteğe bağlı):** 📱2'de çıkış yap → `ogretmen1` ile gir → bir isteğe "Gizle…" → gerekçe yaz. Kontrol sekmesinde gizlenenleri göster. 📱1'de istek kaybolur.

**Kullanıcılar:** `ogrenci1`…`ogrenci5`, `ogretmen1`. Şifre: `.env` dosyasındaki `DEMO_SIFRE`.

## Kurulum kontrol listesi

**Akşamdan (evde):**
- [ ] Laptop ve iki telefon şarjda.
- [ ] `cd demo && source .venv/bin/activate && python manage.py test`: 22 test geçiyor mu?
- [ ] Örnek veriyi tazele: `python manage.py ornek_veri` (bütün denemeler silinir, istekler baştan oluşur).
- [ ] **Yedek video çek:** Canlı demo senaryosunu iki telefonla videoya al (görev tanımı, bölüm 10). Okulda bir şey bozulursa bunu gösterirsin.
- [ ] Görüşme formunu yazdır (2 kopya) ya da laptopta aç.

**Okulda (Wi-Fi gerekmez, her şey USB ile çalışır):**
1. Laptopta sunucuyu başlat: `cd demo && source .venv/bin/activate && python manage.py runserver`
2. 📱1'i USB ile tak: `adb reverse tcp:8000 tcp:8000`
3. 📱2'nin USB'si yalnızca şarj alıyorsa: Telefon ve laptop **aynı ağda** olmalı (okul Wi-Fi'si ya da laptopun ya da telefonun hotspot'u). Kablosuz hata ayıklamayı aç → `adb connect IP:PORT` → `adb reverse tcp:8000 tcp:8000`.
   - Ağ yoksa: 📱2'yi tarayıcı yerine laptopta göster (`http://localhost:8000`, gizli pencere = ikinci kullanıcı).
4. Uygulamaları aç. Bağlanamazsa: USB kablosunu kontrol et, `adb reverse` komutunu yeniden çalıştır.

**Bir şey bozulursa:** Panik yok. "Canlı demo bazen bozulur, bu yüzden videosunu çektim" deyip videoyu göster.

## Hocaların sorabileceği sorular

| Soru | Cevabın (kendi cümlelerinle anlat) |
|------|-----------------------------------|
| Neden Django, Firebase değil? | Firebase'in sunucuları Türkiye dışında. Öğrenci verisi yurt dışına gitmesin istedim. Django okulun ya da benim sunucumda çalışabiliyor (`teknoloji.md`). |
| Veriler nerede duruyor? | Şu an yalnızca benim bilgisayarımda, uydurma örnek verilerle. Gerçek veriyle canlıya geçiş kararı okul idaresinin ve MEM'in. |
| Hangi bilgiler tutuluyor? | Kullanıcı adı, görünen ad (Ayşe K.), rol ve şifrenin geri çevrilemez özeti. TC no, telefon, e-posta, fotoğraf, konum, doğum tarihi yok (`veri.md`). |
| Bir öğrenci başkasının isteğini onaylayabilir mi? | Hayır. Kurallar sunucuda kontrol ediliyor. Adresi elle yazsa bile 403 alıyor. Bunun testi var. |
| İki kişi aynı anda üstlenirse? | Yalnızca biri alır. Veritabanına "durumu hâlâ açıksa üstlen" diye tek bir komut gidiyor. (Az önceki gösteri.) |
| Uygunsuz içerik olursa? | Öğretmen gerekçe yazarak gizler, içerik silinmez. Kim, ne zaman, neden gizledi kaydediliyor. |
| Neden sıralama ya da puan yok? | Projenin baştan verilmiş ilkesi. İyilik bir yarışmaya dönüşmesin. Puan istenirse kuralı ben koymam, Özgür Hoca'ya sorulur. |
| Bu uygulama telefona nasıl yükleniyor? | Şimdilik demo olarak Android uygulaması (APK). Ayrıca tarayıcıdan da açılıyor. İkisi aynı sunucuyu kullanıyor. |
| Yapay zekâ mı yazdı? | Claude ile birlikte çalıştım. Kararları ve gerekçeleri ben verdim, her değişiklik ayrı commit'te neden yapıldığıyla yazılı. Kodun her yerini açıklayabilirim. *(Bunu dürüstçe söyleyebilmen için kodu birlikte gözden geçirelim.)* |

## Görüşmeden sonra

- [ ] Formdaki her cevabı `talepler.md`'ye işle (B tablosu: talep, kim istedi, tarih).
- [ ] Reddedilen varsayımlar için tasarım dosyalarını düzelt, sonra demoyu.
- [ ] Teslim tarihini (S-02) README'ye yaz.
- [ ] Özgür Hoca'ya 5. bölümdeki soruları ilet.
