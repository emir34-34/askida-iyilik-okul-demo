# Demo Planı

> Görev tanımı "önce ne yapacağını yaz, sonra yap" diyor. Bu dosya demoya başlamadan önce yazıldı (2026-10-11). Demo yazılırken plandan sapılırsa önce bu dosya güncellenir.

## Neden şimdi başlıyorum?

`roller.md`, `akis.md` ve `veri.md` taslak olarak bitti, ama hocalar varsayımları henüz onaylamadı. Demonun ilk dilimi yalnızca **görev tanımının kendisinden gelen** kurallara dayanıyor: temel akış (T-05), çift üstlenmenin engellenmesi (T-06), sunucu tarafı yetki (T-07), örnek veri (T-04). Bunlar hocaların cevabına bağlı değil. Hocalar bir varsayımı değiştirirse önce tasarım dosyası, sonra kod düzeltilir.

## Demoda ne olacak? (tasarımın bir dilimi)

| Var ✅ | Tasarımdaki yeri |
|--------|------------------|
| Öğrenci ve öğretmen rolüyle giriş | roller.md, E1 |
| İstek akışı (yeni istekler ve açık olanlar) | E2 |
| Yeni istek açma | E3, G1 |
| İstek sayfası: rol ve duruma göre düğmeler | E4 |
| Üstlen, bırak, yapıldı de, onayla, yapılmadı de (gerekçeyle), geri çek | akis.md G2–G7 |
| Herkese açık yorumlar | E4, T-01 |
| Görevler (açtıklarım, üstlendiklerim) | E5 |
| Durum geçmişi (her geçiş kaydedilir) | veri.md |
| Gizleme ve hesap işleri: Django yönetim paneli | E6, D4, D6 |
| Reddit tarzı, turuncu tema, telefona uygun görünüm | ekranlar.md |

| Demoda yok ❌ (tasarımda var) |
|------------------------------|
| Oylama, resim/video (açık kararlar S-08, S-09) |
| Bildirimler, arşiv, arama, yönetim özeti, şikâyet, tanıtım, sistem ayarları |
| Görevli girişi (okul kelimesi). Zaman kalırsa eklenir |

## Nasıl yapılacak?

- **Teknoloji:** Python 3 + Django 6.1 + SQLite (`teknoloji.md`). Ek kütüphane yok.
- **Klasör:** Demo kodu repoda `demo/` klasöründe durur.
- **Kullanıcı modeli:** Django'nun kullanıcı modeline yalnızca `rol` ve `gorunen_ad` eklenir (`veri.md`). E-posta ve ad-soyad alanları boş bırakılır.
- **Yetki:** Her işlem sunucuda, view içinde kontrol edilir. Düğmenin gizlenmesi yalnızca görünüştür. Yetkisiz istek 403 döner (T-07).
- **Çift üstlenme:** Tek bir koşullu güncelleme: `Istek.objects.filter(pk=…, durum="acik").exclude(acan=…).update(…)`. Değişen satır sayısı 0 ise ikinci kişi reddedilir (akis.md, soru 1).
- **Sırlar:** `SECRET_KEY` ve örnek kullanıcıların şifresi `.env` dosyasında durur. `.env` `.gitignore`'da, repoda yalnızca `.env.example` var.
- **Örnek veri:** `python manage.py ornek_veri` komutu senaryolardaki uydurma kullanıcıları ve istekleri oluşturur (T-04).
- **Telefonda test:** Telefon USB ile bağlıyken `adb reverse tcp:8000 tcp:8000`. Telefonun tarayıcısında `http://localhost:8000` açılır.

## Mimari değişikliği (2026-10-12): arayüz istemcide, sunucu yalnızca veri

İlk sürümde sayfalar Django'da üretiliyordu (sunucu her seferinde HTML gönderiyordu). Telefonda iki cihazla denedikten sonra Emir, Reddit uygulaması gibi **arayüzün uygulamanın içinde olmasını, sunucudan yalnızca verinin gelmesini** istedi. Gerekçe: Uygulama daha hızlı açılır, sayfa geçişleri anında olur, gerçek bir uygulama gibi hissettirir.

| | Önce | Sonra |
|---|------|-------|
| Sunucu (Django) | Sayfaları HTML olarak üretir | Yalnızca veri gönderir: `/api/...` adreslerinden JSON |
| Arayüz | Django şablonları | `demo/istemci/` klasöründe tek bir JavaScript uygulaması (HTML + CSS + JS + yazı tipi) |
| Tarayıcıda (web) | Django sayfaları | Django `demo/istemci/` dosyalarını verir, arayüz tarayıcıda çalışır |
| APK'da | Sayfalar sunucudan gelir | `demo/istemci/` dosyaları APK'nın içine konur, **sunucudan yalnızca veri gelir** |
| Kurallar | `gecisler.py` | **Değişmedi**, yine `gecisler.py`'de, sunucuda (T-07) |

**Neden tek arayüz:** Görev tanımı tarayıcıda açılan bir demo istiyor. Web ve APK için ayrı ayrı arayüz yazmak işi ikiye katlar ve ikisi zamanla birbirinden farklılaşır. Aynı dosyalar iki yerde de çalışır.

**APK'da nasıl çalışır:** APK, arayüz dosyalarını (`/`, `/i/...`) sunucuya sormadan kendi içinden verir. Yalnızca `/api/...` istekleri gerçekten sunucuya gider. Dosyalar sunucuyla aynı adresten geliyormuş gibi davrandığı için oturum çerezi ve CSRF koruması değişmeden çalışır.

**API (`/api/`):**

| Adres | Ne yapar |
|-------|----------|
| `GET /api/ben` | Giriş yapan kişi (yoksa 401) |
| `POST /api/giris`, `POST /api/cikis` | Giriş, çıkış (Django oturumu) |
| `GET /api/istekler?sekme=&k=` | Akış (E2) |
| `GET /api/gorevler?sekme=` | Görevler (E5) |
| `POST /api/istekler` | Yeni istek (G1) |
| `GET /api/istekler/<no>` | İstek, yorumlar ve bu kişinin görebileceği düğmeler (E4) |
| `POST /api/istekler/<no>/<eylem>` | üstlen, bırak, yapıldı, onayla, yapılmadı, geri çek, yorum |

Hatalar: yetki yok → **403**, durum uygun değil (ör. az önce başkası üstlendi) → **409**, eksik gerekçe → **400**, giriş yapılmamış → **401**.

**Güvenlik:** Kullanıcıların yazdığı her metin (başlık, açıklama, yorum) ekrana basılmadan önce kaçış işlemine (escape) uğrar. Böylece birinin isteğine yazdığı bir kod başkasının telefonunda çalışamaz (XSS).

## Native Android uygulaması (2026-10-12)

WebView'li APK'yı telefonda denedikten sonra Emir, uygulamanın Reddit uygulaması gibi **tamamen native** olmasını istedi. Gerekçe: WebView içinde kaydırma, dokunma ve geçişler hâlâ bir web sayfası gibi hissettiriyor.

| | WebView APK | Native APK |
|---|-------------|------------|
| Ekranlar | HTML/CSS, WebView içinde | Android'in kendi bileşenleri (View), Java ile |
| Veri | `/api/` | `/api/` (değişmedi) |
| Kurallar | Sunucuda | Sunucuda (değişmedi) |
| Oturum | WebView çerezleri | Uygulama Django'nun `sessionid` ve `csrftoken` çerezlerini kendisi saklar ve gönderir |

- **Neden Java ve Android'in kendi bileşenleri (ek kütüphane yok):** Kotlin ve Jetpack Compose için Gradle ve onlarca kütüphane indirmek gerekir. Bilgisayardaki Java 27 sürümüyle uyum sorunu çıkma riski yüksek. Java ile Android'in kendi bileşenleri mevcut derleme betiğiyle (`apk/derle.sh`) çalışır ve sonuç yine tamamen native olur.
- **Tarayıcı demosu kalıyor:** Görev tanımı tarayıcıda açılan bir demo istediği için `demo/istemci/` silinmez. Bundan sonra iki arayüz var (web ve native), ikisi de aynı API'yi kullanır. Kurallar yalnızca sunucuda olduğu için iki arayüz birbirinden farklı davranamaz.
- **Ekranlar:** Giriş, Akış (sekmeler, kategoriler, aşağı çekip yenileme), İstek (düğmeler, yorumlar), Yeni istek, Görevler, Profil (çıkış, sunucu adresi). Alt menü ve renkler ekran taslaklarıyla aynı.
- **En düşük Android sürümü:** 8.0 (API 26). Yazı tipinin (Reddit Sans) ağırlıklarını native olarak ayarlayabilmek için gerekli.

## Telefonda test (2026-10-12, iki cihaz)

Cihazlar: LineageOS telefon (USB) ve Xiaomi 11T (kablosuz hata ayıklama). İkisi aynı bilgisayardaki Django'ya bağlı.

**Senaryo 1 iki cihazda native uygulamayla baştan sona yürütüldü:** Ayşe 2. telefonda üstlendi, yorum yazdı ve "Yapıldı" dedi. Mehmet 1. telefonda onayladı ve teşekkür notu yazdı. Durum geçmişi: Açık → Üstlenildi → Yapıldı → Tamamlandı, her adım doğru kişiyle kaydedildi.

| Bulunan | Ne yapıldı |
|---------|------------|
| Dokunurken Android'in mavi vurgusu çıkıyordu (WebView) | Kaldırıldı, sonra native uygulamaya geçildi (dokunma dalgası) |
| WebView'li uygulama web sayfası gibi hissettiriyordu | Tamamen native uygulama yazıldı (yukarıda) |
| Kullanıcı adı kutusu eşit aralıklı yazı tipiyle görünüyordu | Yazı tipi giriş türünden sonra yeniden veriliyor |
| Alt menü yazıları sola yaslıydı | Ortalandı |
| Klavyenin İleri/Bitti tuşları çalışmıyordu | İleri şifreye geçiyor, Bitti giriş yapıyor |
| USB kablosu çıkınca `adb reverse` siliniyor, uygulama sunucuya ulaşamıyor | README'ye yazıldı. Uygulama bu durumda adres penceresi açıyor |
| Telefonda örnek şifreyi yazmak zordu (rastgele üretilmişti) | `.env` dosyasında daha kolay bir şifre seçilebileceği README'de |

## Testler (görev tanımı: en az 3, her birinde gerçek kontrol)

| Test | Neyi kanıtlar |
|------|---------------|
| Rol kuralı | Öğrenci başkasının isteğini onaylayamaz, adresi elle yazsa bile 403 alır. Kendi isteğini üstlenemez |
| Çift üstlenme | İki kişi aynı isteği üstlenmeye çalışınca yalnızca ilki başarılı olur, istek ilkinde kalır |
| Onay akışı | Aç → üstlen → yapıldı → onayla zinciri baştan sona yürür, her adımda durum ve durum geçmişi doğrudur |
| Bırakma ve yapılmadı | Bırakınca istek yeniden açık olur. Gerekçesiz "yapılmadı" reddedilir |
| API yetkisi | Yetkisiz biri API adresine doğrudan istek atsa bile 403 alır, giriş yapmayan 401 alır, gizlenen istek öğrenciye 404 döner |

## Sıra (her adım ayrı commit)

1. Django projesi, ayarlar, `.env` okuma
2. Modeller: kullanıcı, istek, yorum, durum geçmişi
3. Durum geçişleri (G1–G7) ve yetki kuralları, tek bir yerde
4. Testler
5. Sayfalar ve görünüm (Reddit tarzı)
6. Örnek veri komutu, yönetim paneli
7. README'ye kurulum ve çalıştırma adımları
8. Telefonda test, bulunan boşlukları tasarıma geri yazma
10. **Mimari değişikliği:** API, istemci uygulaması, APK'nın arayüzü kendi içinden vermesi (yukarıda).
9. **Ek: Android APK kabuğu.** Django sayfalarını tam ekran açan bir Android uygulaması (WebView). Ayrı bir uygulama değil, aynı demonun telefona kurulabilen hâli. Android SDK gerektirdiği için görev tanımı gereği Özgür Hoca'ya sorulacak (S-11). Teslim edilen demonun zorunlu parçası değil, ek.
