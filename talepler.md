# Talepler

Her talep bir satırdır. Talepleri Yasemin Hoca ve Eyüp Hoca verir. Kural, kapsam ve teknoloji soruları için danışman Özgür Hoca'dır.
Anlamadığım ya da birbiriyle çelişen bir talebi uydurmam: "Açık sorular" bölümüne yazar ve sorarım.

**Geri okundu mu?** sütunu, talebi kendi cümlelerimle talep sahibine okuyup "doğru anlamışım" onayını aldığım zaman ✅ olur.

## A. Görev tanımıyla baştan verilen kararlar

| No | Talep | Kim istedi | Tarih | Geri okundu mu? | Tasarımda nerede | Demoda nerede |
|----|-------|------------|-------|-----------------|------------------|---------------|
| T-01 | Özel mesaj yok, konuşma sorunun altında herkese açık yorumlarla olur | Görev tanımı (Özgür Hoca) | 2026-10-10 | — | roller.md, veri.md (Yorum) | Sorun sayfasında yorumlar |
| T-02 | Sıralama tablosu yok | Görev tanımı (Özgür Hoca) | 2026-10-10 | — | roller.md (son satır) | Kişi başına hiçbir sayı yok |
| T-03 | TC kimlik no, telefon, fotoğraf, konum ve doğum tarihi tutulmaz, her alanın gerekçesi yazılır | Görev tanımı (Özgür Hoca) | 2026-10-10 | — | veri.md | `demo/istekler/models.py` |
| T-04 | Demo yalnızca örnek veriyle çalışır | Görev tanımı (Özgür Hoca) | 2026-10-10 | — | veri.md | `python manage.py ornek_veri` |
| T-05 | Temel akış demoda uçtan uca çalışır | Görev tanımı (Özgür Hoca) | 2026-10-10 | — | akis.md | `gecisler.py`, test: `OnayAkisiTesti` |
| T-06 | Aynı iş iki kişi tarafından aynı anda üstlenilemez | Görev tanımı (Özgür Hoca) | 2026-10-10 | — | akis.md (soru 1) | `gecisler.ustlen`, test: `CiftUstlenmeTesti` |
| T-07 | Yetki kontrolü sunucuda yapılır, yalnızca ekranda yapılmaz | Görev tanımı (Özgür Hoca) | 2026-10-10 | — | roller.md | `gecisler.py`, test: `RolKuraliTesti`, `SayfaYetkiTesti` |

## A2. Özgür Hoca'nın geri bildirimi (2026-10-11, repoyu inceledikten sonra)

| No | Talep | Kim istedi | Tarih | Geri okundu mu? | Tasarımda nerede | Demoda nerede |
|----|-------|------------|-------|-----------------|------------------|---------------|
| T-08 | Askıya kişisel istekler konmaz. Yalnızca **okulda görülen sorunlar** konur: bozuk kapı, damlayan musluk, biten sabun gibi | Özgür Hoca | 2026-10-11 | — | README, akis.md, senaryolar.md | Örnek veriler |
| T-09 | Tasarım sade olsun. Yalnızca şu akış kalsın: **sorunu bildir → biri üstlensin → yapıldı desin → bildiren onaylasın** | Özgür Hoca | 2026-10-11 | — | akis.md, ekranlar.md | Demonun tamamı |
| T-10 | Kimsenin istemediği özellikler kaldırılsın (aşağıdaki "Kaldırılanlar" tablosu) | Özgür Hoca | 2026-10-11 | — | Bütün tasarım dosyaları | Android uygulaması ve ek özellikler kaldırıldı |
| T-11 | Sadeleştirdikten sonra tasarım Eyüp Hoca'ya gösterilsin, ona danışılsın | Özgür Hoca | 2026-10-11 | — | gorusme-formu.html, sunum-plani.md | — |
| T-12 | `teknoloji.md`'ye süreklilik yazılsın: Ben mezun olunca bu sistemi okulda kim çalıştıracak? | Özgür Hoca | 2026-10-11 | — | teknoloji.md (Süreklilik) | — |

## B. Yasemin Hoca ve Eyüp Hoca'nın talepleri

Görüşmeden sonra doldurulacak. Form: [gorusme-formu.html](gorusme-formu.html)

| No | Talep | Kim istedi | Tarih | Geri okundu mu? | Tasarımda nerede | Demoda nerede |
|----|-------|------------|-------|-----------------|------------------|---------------|
| | | | | | | |

## B2. Taslaktaki varsayımlar (hocalara sorulacak)

Hocalarla görüşemediğim için taslağı bu varsayımlarla yazdım. Hiçbiri talep değildir. Görüşmede her birini sorup sonucunu buraya yazacağım.

| No | Varsayım | Tasarımda nerede | Sonuç |
|----|----------|------------------|-------|
| V-01 | Sorunu öğrenciler ve öğretmenler bildirebilir | roller.md | bekliyor |
| V-03 | Kimse kendi kendine kayıt olamaz, hesapları okul yöneticisi açar, e-posta tutulmaz | roller.md, veri.md | bekliyor |
| V-04 | Veliler bu sürümde kullanıcı değil | roller.md | bekliyor |
| V-05 | İş yapılınca onayı sorunu bildiren kişi verir | roller.md, akis.md | bekliyor |
| V-08 | Üstlenen kişi işi bırakırken sebep yazmak zorunda değil | akis.md | bekliyor |
| V-09 | Görünen ad yalnızca ad ve soyadın baş harfi (Ayşe K.) | veri.md | bekliyor |
| V-15 | Sorunun okulda nerede olduğu ayrı bir alan değil, açıklamaya yazılır ("2. kat kız tuvaleti, soldan ikinci musluk") | veri.md | bekliyor |

## C. Açık sorular

| No | Soru | Kime | Durum |
|----|------|------|-------|
| S-14 | **Bozuk kapı, damlayan musluk gibi sorunları kim üstlenir?** Öğrenciler mi, öğretmenler mi, okulun görevli personeli mi? (Taslakta: bildiren dışında herhangi bir öğrenci ya da öğretmen) | Eyüp Hoca | açık |
| S-13 | Uygunsuz bir bildirim ya da yorum olursa kim müdahale eder? | Eyüp Hoca | açık |
| S-03 | Bildiren kişi iş yapıldıktan sonra hiç onay vermezse ne olsun, ne kadar süre sonra? (akis.md, soru 3) | Eyüp Hoca | açık |
| S-06 | Aynı kişi bir sorunu defalarca üstlenip bırakırsa bir sınır olsun mu? | Eyüp Hoca | açık |
| S-07 | Zorunlu iki senaryonun yanına hangi iki durum yazılsın? | Eyüp Hoca | açık |
| S-01 | Kredi veya puan istenecek mi? İstenirse kural icat edilmez, Özgür Hoca'ya sorulur | Eyüp Hoca → Özgür Hoca | açık |
| S-02 | Teslim ve sunum tarihi | Eyüp Hoca, Yasemin Hoca | açık |
| S-04 | Veriler ne kadar süre saklanacak, mezun olan öğrencinin hesabı ne olacak? (KVKK) | Özgür Hoca | açık |
| S-05 | Hocalarla görüşmeden önce taslak yazmam uygun mu? | Özgür Hoca | 2026-10-11: Devam etmemi söyledi. Akşam repoyu inceleyip geri bildirim verdi (A2) |

## Kaldırılanlar (Özgür Hoca'nın geri bildirimi, 2026-10-11)

Bunlar hocalardan gelmeyen, benim eklediğim özellikler ve tahminlerdi. Tasarımı karmaşıklaştırdıkları için kaldırıldı (T-10). Git geçmişinde duruyorlar.

| Ne | Neden kaldırıldı |
|----|------------------|
| Reddit görünümü (Ö-01), alt menü ve profil (Ö-03), bilgisayar düzeni (Ö-05) | İstenmedi. Tasarım sade bir listeye ve sorun sayfasına indi |
| Yukarı/aşağı oy (Ö-02, S-08) | İstenmedi. Özgür Hoca'nın örneği: Bir öğrenci bozuk musluğu bildirir, beş kişi aşağı oy verir. O öğrenci bir daha bir şey bildirmez. Askının amacı sorunların bildirilmesi, aşağı oy bunu engeller |
| Resim ve video ekleme (Ö-04, S-09) | İstenmedi. Fotoğraf ilkesiyle de çelişiyordu |
| Bildirimler (Ö-06) | İstenmedi |
| Okul kelimesiyle öğretmen girişi (Ö-07, S-10) | İstenmedi |
| Sistem ayarları ve yönetici paneli ekranları (Ö-08) | İstenmedi. Hesap işleri Django'nun hazır yönetim panelinde |
| İlk giriş tanıtımı ve easter egg | İstenmedi |
| Arşiv, yönetim özeti, şikâyet, öğretmen kontrol sayfası, arama, teşekkür notu, canlı güncelleme (V-11…V-14) | İstenmedi. Akışın dışında kalıyorlar |
| Geri çekme ve "yapılmadı" diye geri çevirme (V-06) | Akış yalnızca dört adım olsun (T-09). Bildiren onaylamazsa ne olacağı açık soru (S-03) |
| Öğretmen onayıyla yayına girme (V-07), öğretmenin gizlemesi (V-02) | Uygunsuz içerikte kimin müdahale edeceği Eyüp Hoca'ya soruluyor (S-13) |
| Native Android uygulaması (S-11) | İstenmedi. Görev tanımı tarayıcıda çalışan bir demo istiyor |
| Ev sunucusunda internete açma (S-12) | Süreklilik açısından uygun değil (teknoloji.md, Süreklilik) |
