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

## Testler (görev tanımı: en az 3, her birinde gerçek kontrol)

| Test | Neyi kanıtlar |
|------|---------------|
| Rol kuralı | Öğrenci başkasının isteğini onaylayamaz, adresi elle yazsa bile 403 alır. Kendi isteğini üstlenemez |
| Çift üstlenme | İki kişi aynı isteği üstlenmeye çalışınca yalnızca ilki başarılı olur, istek ilkinde kalır |
| Onay akışı | Aç → üstlen → yapıldı → onayla zinciri baştan sona yürür, her adımda durum ve durum geçmişi doğrudur |
| Bırakma ve yapılmadı | Bırakınca istek yeniden açık olur. Gerekçesiz "yapılmadı" reddedilir |

## Sıra (her adım ayrı commit)

1. Django projesi, ayarlar, `.env` okuma
2. Modeller: kullanıcı, istek, yorum, durum geçmişi
3. Durum geçişleri (G1–G7) ve yetki kuralları, tek bir yerde
4. Testler
5. Sayfalar ve görünüm (Reddit tarzı)
6. Örnek veri komutu, yönetim paneli
7. README'ye kurulum ve çalıştırma adımları
8. Telefonda test, bulunan boşlukları tasarıma geri yazma
9. **Ek: Android APK kabuğu.** Django sayfalarını tam ekran açan bir Android uygulaması (WebView). Ayrı bir uygulama değil, aynı demonun telefona kurulabilen hâli. Android SDK gerektirdiği için görev tanımı gereği Özgür Hoca'ya sorulacak (S-11). Teslim edilen demonun zorunlu parçası değil, ek.
