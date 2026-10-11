# Veri: Neyi tutuyoruz, neden?

> **Durum: TASLAK.** İlke: **asgari veri** (T-03). Her alanın neden tutulduğu yazılı. Nedeni yazılamayan alan tutulmaz. Varsayımlar **V-xx** numaralı, ayrıntılar `roller.md` ve `akis.md` dosyalarında.
> Demodaki bütün veriler uydurmadır, gerçek öğrenci verisi yoktur (T-04).

## Kullanıcı

| Alan | Örnek değer | Neden tutuluyor |
|------|-------------|-----------------|
| `kullanici_adi` | `ogrenci1` | Giriş yapmak için. Yönetici verir (V-03) |
| `sifre` | (yalnızca özeti tutulur) | Giriş için. Django şifrenin kendisini değil, geri çevrilemeyen bir özetini saklar |
| `gorunen_ad` | `Ayşe K.` | İsteklerde ve yorumlarda kimin yazdığı görünsün diye. Yalnızca ad ve soyadın baş harfi (V-09) |
| `rol` | `ogrenci` | Kimin neyi yapabileceğine karar vermek için (`roller.md`) |
| `aktif` | `true` | Okuldan ayrılan birinin hesabını silmeden kapatmak için |

- **V-09:** Görünen adda tam soyad yerine baş harf yeterli. (Hocalara sorulacak)

## İstek

| Alan | Örnek değer | Neden tutuluyor |
|------|-------------|-----------------|
| `baslik` | `Kimya defterimi kaybettim, notları paylaşabilecek var mı?` | İsteğin ne olduğu listede tek bakışta görülsün diye |
| `aciklama` | `Salı günkü dersin notlarına ihtiyacım var.` | Karşılayacak kişinin işi anlaması için |
| `kategori` | `ders` | Filtrelemek için. Kategorileri hocalar belirleyecek (Soru 8). Demoda örnek kategoriler kullanılacak |
| `acan` | → `ogrenci1` | Onayı kimin vereceğini ve kimin geri çekebileceğini bilmek için |
| `ustlenen` | → `ogrenci2` (boş olabilir) | "Yapıldı"yı kimin diyebileceğini bilmek ve çift üstlenmeyi önlemek için |
| `durum` | `ustlenildi` | Akışın neresinde olduğumuzu bilmek için (`akis.md`) |
| `olusturma_zamani` | `2026-10-14 10:32` | Listeyi sıralamak ve eski istekleri ayırt etmek için |
| `guncelleme_zamani` | `2026-10-14 12:05` | Bir isteğin ne zamandır beklediğini görmek için (S-03) |

## Yorum

| Alan | Örnek değer | Neden tutuluyor |
|------|-------------|-----------------|
| `istek` | → İstek #12 | Yorumun hangi isteğin altında olduğunu bilmek için |
| `yazan` | → `ogrenci2` | Herkese açık konuşmada kimin yazdığı görünsün diye |
| `metin` | `Yarın teneffüste getirebilirim.` | Konuşmanın kendisi. Özel mesaj yok (T-01) |
| `zaman` | `2026-10-14 11:00` | Konuşmanın sırasını göstermek için |
| `gizli` | `false` | Öğretmen yorumu gizlerse silmeden saklamak için (V-02) |
| `ust_yorum` | → Yorum #31 (boş olabilir) | Yanıtın hangi yorumun altında durduğunu bilmek için. Yalnızca bir seviye (V-11) |

## Oy (yalnızca S-08 kabul edilirse)

| Alan | Örnek değer | Neden tutuluyor |
|------|-------------|-----------------|
| `istek` | → İstek #12 | Oyun hangi isteğe verildiğini bilmek için |
| `veren` | → `ogrenci3` | Aynı kişinin aynı isteğe ikinci kez oy vermesini önlemek için. **Ekranda gösterilmez** |
| `yon` | `+1` (aşağı oy kabul edilirse `-1` de olabilir) | İsteğin oy toplamını hesaplamak için |

Oylar **istek başına** toplanır, **kişi başına asla toplanmaz**. Reddit'teki karma gibi bir kullanıcı puanı yoktur (T-02, S-01).

## Durum geçmişi

| Alan | Örnek değer | Neden tutuluyor |
|------|-------------|-----------------|
| `istek` | → İstek #12 | Hangi isteğin değiştiğini bilmek için |
| `eski_durum` → `yeni_durum` | `yapildi` → `ustlenildi` | Ne değiştiğini bilmek için |
| `yapan` | → `ogrenci1` | Bir anlaşmazlıkta ya da kötüye kullanımda öğretmen ne olduğunu görebilsin diye |
| `zaman` | `2026-10-14 15:20` | Olayların sırasını bilmek için |
| `not` | `Notların yarısı eksik.` | "Yapılmadı" ve gizleme gerekçesini saklamak için (G6, G8) |

Durum geçmişi yalnızca öğretmenlere görünür. Ondan "kim kaç iyilik yaptı" sayısı **çıkarılmaz ve gösterilmez** (T-02).

## Tutulmayacaklar

| Veri | Neden tutulmuyor |
|------|------------------|
| TC kimlik no, telefon, fotoğraf, konum, doğum tarihi | Değişmez ilke (T-03). Uygulamanın hiçbir işi bunlara ihtiyaç duymuyor |
| E-posta adresi | Hesapları yönetici açtığı için gerek yok (V-03). Şifre sıfırlamayı da yönetici yapar |
| Okul numarası, sınıf ve şube | Hiçbir akış bunlara ihtiyaç duymuyor. Hocalar sınıfa göre filtreleme isterse yeniden değerlendirilir |
| Veli bilgisi | Veliler bu sürümde kullanıcı değil (V-04) |
| Özel mesajlar | Özel mesaj özelliği yok (T-01) |
| Puan, kredi, "iyilik sayısı", karma | Kurallar kesinleşmedi (S-01). Sıralama tablosu da yok (T-02) |
| Profil fotoğrafı, biyografi | Asgari veri ilkesi gereği gerek yok |

## Açık konular
- **S-04:** Veriler ne kadar süre saklanacak? Örneğin bir öğrenci mezun olunca hesabı ve istekleri ne olacak? Bu bir KVKK sorusu. → Özgür Hoca'ya sorulacak (okulun KVKK notları).
- Canlıya geçiş ve verinin nerede duracağı okul idaresinin ve MEM'in kararıdır. Demo yalnızca örnek veriyle çalışır.
