# Talepler

Her talep bir satırdır. Talepleri Yasemin Hoca ve Eyüp Hoca verir. Kural, kapsam ve teknoloji soruları için danışman Özgür Hoca'dır.
Anlamadığım ya da birbiriyle çelişen bir talebi uydurmam: "Açık sorular" bölümüne yazar ve sorarım.

**Geri okundu mu?** sütunu, talebi kendi cümlelerimle talep sahibine okuyup "doğru anlamışım" onayını aldığım zaman ✅ olur.

## A. Görev tanımıyla baştan verilen kararlar

| No | Talep | Kim istedi | Tarih | Geri okundu mu? | Tasarımda nerede | Demoda nerede |
|----|-------|------------|-------|-----------------|------------------|---------------|
| T-01 | Özel mesaj yok, konuşma isteğin altında herkese açık yorumlarla olur | Görev tanımı (Özgür Hoca) | 2026-10-10 | — | roller.md (yorum yazmak), veri.md (Yorum) | — |
| T-02 | Sıralama tablosu yok | Görev tanımı (Özgür Hoca) | 2026-10-10 | — | roller.md (son satır), akis.md, veri.md (Durum geçmişi) | — |
| T-03 | TC kimlik no, telefon, fotoğraf, konum ve doğum tarihi tutulmaz, her alanın gerekçesi yazılır | Görev tanımı (Özgür Hoca) | 2026-10-10 | — | veri.md (tamamı) | — |
| T-04 | Demo yalnızca örnek veriyle çalışır | Görev tanımı (Özgür Hoca) | 2026-10-10 | — | roller.md (demo rolleri), veri.md | — |
| T-05 | Temel akış: isteği aç → üstlen → yapıldı → onayla, demoda uçtan uca çalışır | Görev tanımı (Özgür Hoca) | 2026-10-10 | — | akis.md (G1, G2, G4, G5) | — |
| T-06 | Aynı iş iki kişi tarafından aynı anda üstlenilemez | Görev tanımı (Özgür Hoca) | 2026-10-10 | — | akis.md (soru 1) | — |
| T-07 | Yetki kontrolü sunucuda yapılır, yalnızca ekranda yapılmaz | Görev tanımı (Özgür Hoca) | 2026-10-10 | — | roller.md (yetki nerede kontrol edilir) | — |

## B. Yasemin Hoca ve Eyüp Hoca'nın talepleri

İlk görüşmeden sonra doldurulacak. Sorular: [gorusme-1-sorular.md](gorusme-1-sorular.md)

| No | Talep | Kim istedi | Tarih | Geri okundu mu? | Tasarımda nerede | Demoda nerede |
|----|-------|------------|-------|-----------------|------------------|---------------|
| | | | | | | |

## B2. Taslaktaki varsayımlar (hocalara sorulacak)

Hocalarla görüşemediğim için roller, akış ve veri dosyalarının taslağını bu varsayımlarla yazdım. Hiçbiri talep değildir. Görüşmede her birini sorup sonucunu buraya yazacağım: onaylanırsa B tablosuna talep olarak geçer, reddedilirse taslak düzeltilir.

| No | Varsayım | Tasarımda nerede | Hangi soru | Sonuç |
|----|----------|------------------|------------|-------|
| V-01 | Öğrenciler hem istek açabilir hem de karşılayabilir | roller.md | 2 | bekliyor |
| V-02 | Uygunsuz içeriğe öğretmenler müdahale eder, içerik silinmez, gerekçeyle gizlenir | roller.md, veri.md | 13 | bekliyor |
| V-03 | Kimse kendi kendine kayıt olamaz, hesapları yönetici açar, e-posta tutulmaz | roller.md, veri.md | 3 | bekliyor |
| V-04 | Veliler ve personel bu sürümde kullanıcı değil | roller.md | 1 | bekliyor |
| V-05 | Yapılan işi isteği açan kişi onaylar, öğretmen onaylamaz | roller.md, akis.md | 9 | bekliyor |
| V-06 | Üstlenilmiş bir istek açan kişi tarafından geri çekilemez | roller.md, akis.md | 11 | bekliyor |
| V-07 | İstekler öğretmen onayı beklemeden yayına girer | akis.md | 14 | bekliyor |
| V-08 | İşi bırakırken gerekçe yazmak zorunlu değil | akis.md | 11 | bekliyor |
| V-09 | Görünen ad yalnızca ad ve soyadın baş harfi (Ayşe K.) | veri.md | — | bekliyor |
| V-10 | Uygulama çoğunlukla telefondan kullanılır, ekranlar dar ekrana göre tasarlanır | ekranlar.md | 16 | bekliyor |
| V-11 | Yorumlara tek seviye yanıt verilebilir | ekranlar.md, roller.md, veri.md | — | bekliyor |

## B3. Tasarımcının (benim) önerileri

Bunlar hocalardan değil, benden gelen önerilerdir. Hocalara gösterilip onayları alınacak.

| No | Öneri | Tarih | Tasarımda nerede | Sonuç |
|----|-------|-------|------------------|-------|
| Ö-01 | Arayüz Reddit'in arayüz diline göre tasarlansın: istek kartları, kategoriler, durum etiketi (flair), istek altında yorumlar. Öğrenciler bu düzeni zaten tanıyor | 2026-10-11 | ekranlar.md | hocalara gösterilecek |
| Ö-02 | İsteklere yukarı ve aşağı oy verilebilsin (seçenek A). Riskleri bildiğim hâlde aşağı oyun da olmasını tercih ediyorum, önlemleri ekranlar.md'de | 2026-10-11 | ekranlar.md, veri.md | tasarıma A olarak kondu, son onay → S-08 |
| Ö-03 | Alt menü Akış, Oluştur, Görevler ve Profil düğmelerinden oluşsun. Profil ekranı eklensin | 2026-10-11 | ekranlar.md (E2, E5, E8) | hocalara gösterilecek |
| Ö-04 | İsteklere resim ve video eklenebilsin (ör. bozuk musluğun resmi) | 2026-10-11 | ekranlar.md (E2, E3), veri.md (Ek) | ilke 3 ile çelişebilir → S-09 |
| Ö-05 | Telefon arayüzünün yanında bilgisayar arayüzü de olsun (Reddit'in masaüstü düzeni: sol menü, orta akış, sağ bilgi kartları) | 2026-10-11 | ekranlar.md (D1, D2) | hocalara gösterilecek |

## C. Açık sorular ve açık kararlar

| No | Soru | Kime | Durum |
|----|------|------|-------|
| S-01 | Kredi veya puan istenecek mi? İstenirse kural icat edilmez, Özgür Hoca'ya sorulur | Yasemin Hoca, Eyüp Hoca → Özgür Hoca | açık |
| S-02 | Teslim ve sunum tarihi | Yasemin Hoca, Eyüp Hoca | açık |
| S-03 | İsteği açan kişi "Yapıldı" durumundaki isteğe hiç cevap vermezse ne olsun, ne kadar süre sonra? (akis.md, soru 3) | Yasemin Hoca, Eyüp Hoca | açık |
| S-04 | Veriler ne kadar süre saklanacak, mezun olan öğrencinin hesabı ne olacak? (KVKK) | Özgür Hoca | açık |
| S-05 | Hocalarla görüşmeden önce roller, akış ve veri taslağını yazmam uygun mu? | Özgür Hoca | 2026-10-11: Hafta içi bakacağını ve devam etmemi söyledi. Taslak, varsayımları işaretlenerek yazıldı |
| S-06 | Aynı kişi bir isteği defalarca üstlenip bırakırsa bir sınır olsun mu? (senaryolar.md, Senaryo 2) | Yasemin Hoca, Eyüp Hoca | açık |
| S-07 | Senaryo 3 ve 4 için adaylar (yapılmadı diye geri çevirme, uygunsuz içeriği gizleme) uygun mu, yoksa hocaların seçtiği başka durumlar mı yazılmalı? | Yasemin Hoca, Eyüp Hoca | açık |
| S-08 | Oylama olsun mu? A) yukarı ve aşağı oy (tasarımcının tercihi, tasarımda bu var), B) yalnızca "Ben de" destek oyu, C) oylama yok. Aşağı oy zorbalığa dönüşebilir, kişi başına toplanan oy da ilke 2 (sıralama yok) ve ilke 5 (puan kuralı) ile çelişebilir (ekranlar.md) | Yasemin Hoca, Eyüp Hoca → Özgür Hoca | açık |
| S-09 | İsteklere resim ve video eklenebilir mi? Değişmez ilke 3 "fotoğraf tutulmaz" diyor. Önerilen önlemler: konum ve cihaz bilgisi silinir, yüz görünmemesi kuralı, öğretmen gizleyebilir, boyut sınırı, istenirse yalnızca resim (ekranlar.md E3) | Özgür Hoca (ilke), Yasemin Hoca ve Eyüp Hoca (içerik) | açık |
