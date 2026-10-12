# Veri: Neyi tutuyoruz, neden?

> **Durum: TASLAK.** İlke: **asgari veri** (T-03). Her alanın nedeni yazılı. Nedeni yazılamayan alan tutulmaz.
> Demodaki bütün veriler uydurmadır, gerçek öğrenci verisi yoktur (T-04).

## Kullanıcı

| Alan | Örnek değer | Neden tutuluyor |
|------|-------------|-----------------|
| `kullanici_adi` | `ogrenci1` | Giriş yapmak için. Yönetici verir (V-03) |
| `sifre` | (yalnızca geri çevrilemez özeti) | Giriş için. Şifrenin kendisi saklanmaz |
| `gorunen_ad` | `Ayşe K.` | Sorunu kimin bildirdiği ve kimin üstlendiği görünsün diye. Ad ve soyadın baş harfi (V-09) |
| `rol` | `ogrenci` | Kimin neyi yapabileceğine karar vermek için (`roller.md`) |
| `aktif` | `true` | Okuldan ayrılan birinin hesabını silmeden kapatmak için |

## Sorun

| Alan | Örnek değer | Neden tutuluyor |
|------|-------------|-----------------|
| `baslik` | `2. kat lavabo musluğu damlıyor` | Sorunun ne olduğu listede tek bakışta görülsün diye |
| `aciklama` | `Kız tuvaletindeki soldan ikinci musluk sürekli damlıyor.` | Üstlenecek kişinin sorunu ve yerini anlaması için (V-15) |
| `bildiren` | → `ogrenci1` | Onayı kimin vereceğini bilmek için |
| `ustlenen` | → `ogrenci2` (boş olabilir) | "Yapıldı"yı kimin diyebileceğini bilmek ve çift üstlenmeyi önlemek için |
| `durum` | `ustlenildi` | Akışın neresinde olduğumuzu bilmek için (`akis.md`) |
| `olusturma_zamani` | `2026-10-12 10:32` | Listeyi sıralamak için |
| `guncelleme_zamani` | `2026-10-12 12:05` | Bir sorunun ne zamandır beklediğini görmek için (S-03) |

## Yorum

| Alan | Örnek değer | Neden tutuluyor |
|------|-------------|-----------------|
| `sorun` | → Sorun #3 | Yorumun hangi sorunun altında olduğunu bilmek için |
| `yazan` | → `ogrenci2` | Herkese açık konuşmada kimin yazdığı görünsün diye (T-01) |
| `metin` | `Hademe ablaya haber verdim.` | Konuşmanın kendisi |
| `zaman` | `2026-10-12 11:00` | Yorumları sıraya koymak için |

## Durum geçmişi

| Alan | Örnek değer | Neden tutuluyor |
|------|-------------|-----------------|
| `sorun` | → Sorun #3 | Hangi sorunun değiştiğini bilmek için |
| `eski_durum` → `yeni_durum` | `acik` → `ustlenildi` | Ne değiştiğini bilmek için |
| `yapan` | → `ogrenci2` | Bir anlaşmazlıkta kimin ne yaptığı görülebilsin diye |
| `zaman` | `2026-10-12 11:02` | Olayların sırasını bilmek için |

Durum geçmişinden "kim kaç sorun çözdü" sayısı çıkarılmaz ve gösterilmez (T-02).

## Tutulmayacaklar

| Veri | Neden tutulmuyor |
|------|------------------|
| TC kimlik no, telefon, fotoğraf, konum, doğum tarihi | Değişmez ilke (T-03). Hiçbir adım bunlara ihtiyaç duymuyor |
| E-posta | Hesapları yönetici açtığı için gerek yok (V-03) |
| Okul numarası, sınıf, şube | Hiçbir adım bunlara ihtiyaç duymuyor |
| Puan, kredi, "çözülen sorun sayısı" | Kurallar kesinleşmedi (S-01), sıralama tablosu yok (T-02) |
| Resim, video | İstenmedi (T-10) |

## Açık konu
- Veriler ne kadar süre saklanacak, mezun olan öğrencinin hesabı ne olacak? (S-04, Özgür Hoca)
