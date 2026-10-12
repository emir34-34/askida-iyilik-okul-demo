# Demo Planı

> Görev tanımı "önce ne yapacağını yaz, sonra yap" diyor. Bu plan demodan önce yazıldı (2026-10-11) ve Özgür Hoca'nın geri bildirimiyle sadeleştirildi (2026-10-12).

## Demoda ne var? (tasarımın bir dilimi)

| Var | Tasarımdaki yeri |
|-----|------------------|
| Öğrenci ve öğretmen rolüyle giriş | roller.md, E1 |
| Sorunlar listesi (açık olanlar / hepsi) | E2 |
| Sorun bildirme | E3, G1 |
| Sorun sayfası: role ve duruma göre düğmeler | E4 |
| Üstlen, bırak, yapıldı de, onayla | akis.md G2–G5 |
| Herkese açık yorumlar | E4, T-01 |
| Benim işlerim (bildirdiklerim, üstlendiklerim) | E5 |
| Durum geçmişi (her geçiş kaydedilir) | veri.md |
| Hesap işleri: Django'nun hazır yönetim paneli | roller.md (yönetici) |

Demoda olmayan her şey `talepler.md`'deki "Kaldırılanlar" tablosunda.

## Nasıl yapıldı?

- **Teknoloji:** Python + Django + SQLite (`teknoloji.md`). Ek kütüphane yok. Sayfalar Django şablonlarıyla üretilir, JavaScript yok.
- **Yetki:** Bütün kurallar `demo/istekler/gecisler.py`'de, sunucuda. Yetkisiz istek 403 döner (T-07).
- **Çift üstlenme:** Tek bir koşullu güncelleme: "durumu hâlâ Açık ise üstlen". Değişen satır yoksa ikinci kişi reddedilir (akis.md, soru 1).
- **Sırlar:** `SECRET_KEY` ve örnek kullanıcı şifresi `.env` dosyasında. `.env` repoda yok, örneği `.env.example`'da.
- **Örnek veri:** `python manage.py ornek_veri` uydurma kullanıcıları ve okul sorunlarını oluşturur (T-04, T-08).

## Testler (görev tanımı: en az 3, her birinde gerçek kontrol)

| Test | Neyi kanıtlar |
|------|---------------|
| `RolKuraliTesti` | Kendi sorununu üstlenemez, yalnızca bildiren onaylar, yalnızca üstlenen "yapıldı" der |
| `CiftUstlenmeTesti` | İki kişi aynı sorunu üstlenmeye çalışınca yalnızca ilki başarılı olur |
| `OnayAkisiTesti` | Senaryo 1 baştan sona: her adımda durum ve durum geçmişi doğru |
| `BirakmaTesti` | Senaryo 2: bırakınca sorun yeniden açık olur, başkası bırakamaz |
| `SayfaYetkiTesti` | Adresi elle yazan yabancı 403 alır, giriş yapmayan giriş sayfasına gider, düğmeler role göre değişir |

Çift üstlenme korumasını bilerek bozunca testlerin kırmızıya döndüğü denendi (testler boş değil).

## Telefonda test (2026-10-11)

İki telefonla (biri USB, biri kablosuz hata ayıklama) Senaryo 1 baştan sona yürütüldü ve iki kişinin aynı anda üstlenmeye çalıştığı durum denendi: biri aldı, diğeri "az önce başka biri tarafından üstlenildi" uyarısını gördü. Bulunan bir boşluk: USB kablosu çıkınca `adb reverse` siliniyor, yeniden çalıştırmak gerekiyor (README).

## Geçmiş

Demo önce daha geniş yazılmıştı (Reddit görünümü, JavaScript arayüzü, native Android uygulaması, canlı güncelleme, öğretmen kontrol sayfası). Bunlar hocaların istemediği özelliklerdi ve Özgür Hoca'nın geri bildirimiyle kaldırıldı. Kodları git geçmişinde duruyor.
