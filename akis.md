# İsteğin Akışı: Durumlar ve Geçişler

> **Durum: TASLAK.** Temel akış (aç → üstlen → yapıldı → onayla) görev tanımından geliyor (T-05). Geri kalan her şey **V-xx** numaralı varsayımdır ve Yasemin Hoca ile Eyüp Hoca'ya sorulacak. Rol varsayımları `roller.md` dosyasında.

## Durumlar

| Durum | Anlamı |
|-------|--------|
| **Açık** | İstek yayında, üstlenecek birini bekliyor |
| **Üstlenildi** | Biri işi üstlendi, üzerinde çalışıyor |
| **Yapıldı** | Üstlenen kişi işi yaptığını söyledi, isteği açan kişinin onayı bekleniyor |
| **Tamamlandı** | İsteği açan kişi onayladı. İş bitti, istek arşive geçer |
| **Geri çekildi** | İsteği açan kişi isteğinden vazgeçti |
| **Gizlendi** | Bir öğretmen isteği uygunsuz bulup gizledi |

## Durum şeması

```
                 üstlen                yapıldı de             onayla
   ┌────────┐ ─────────▶ ┌────────────┐ ──────────▶ ┌─────────┐ ────────▶ ┌────────────┐
   │  Açık  │            │ Üstlenildi │             │ Yapıldı │           │ Tamamlandı │
   └────────┘ ◀───────── └────────────┘ ◀────────── └─────────┘           └────────────┘
     │   ▲       bırak                   yapılmadı de
     │   │                               (gerekçeyle)
     │   └── öğretmen gizlemeyi kaldırır
     │
     ├── geri çek (yalnızca açan kişi) ──▶ Geri çekildi
     └── gizle (yalnızca öğretmen) ─────▶ Gizlendi    (her durumdan gizlenebilir)
```

## Geçişler

| # | Geçiş | Kim yapar | Koşul | Sonuç |
|---|-------|-----------|-------|-------|
| G1 | İstek aç | Öğrenci ya da öğretmen | Başlık ve açıklama dolu | **Açık** (V-07) |
| G2 | Üstlen | Açan kişi dışında biri | Durum **Açık** | **Üstlenildi**, üstlenen kişi kaydedilir |
| G3 | Bırak | Yalnızca üstlenen | Durum **Üstlenildi** | **Açık**, üstlenen kişi silinir |
| G4 | Yapıldı de | Yalnızca üstlenen | Durum **Üstlenildi** | **Yapıldı** |
| G5 | Onayla | Yalnızca açan | Durum **Yapıldı** | **Tamamlandı** |
| G6 | Yapılmadı de | Yalnızca açan | Durum **Yapıldı**, gerekçe yazılmış | **Üstlenildi** (aynı kişide kalır) |
| G7 | Geri çek | Yalnızca açan | Durum **Açık** | **Geri çekildi** |
| G8 | Gizle | Öğretmen | Gerekçe yazılmış | **Gizlendi** |
| G9 | Gizlemeyi kaldır | Öğretmen | Durum **Gizlendi** | **Açık** |

Her geçiş, kimin ne zaman yaptığıyla birlikte durum geçmişine yazılır (bkz. `veri.md`). Tabloda olmayan bir geçişi sunucu reddeder. Örneğin **Açık** bir istek doğrudan **Tamamlandı** olamaz.

- **V-07:** İstekler öğretmen onayı beklemeden hemen yayına girer, uygunsuz olanı öğretmen sonradan gizler. (Soru 14) Hocalar "önce öğretmen onaylasın" derse **Açık**'tan önce bir **Onay bekliyor** durumu eklenir.

## Görev tanımının üç sorusu

### 1. Aynı isteği iki kişi aynı anda üstlenirse ne olur?

İlk gelen alır, ikincisine "Bu istek az önce başka biri tarafından üstlenildi" mesajı gösterilir.

**Nasıl sağlanır:** Sunucu, kontrolü ve değişikliği tek bir veritabanı işleminde yapar: "Durumu hâlâ **Açık** ise **Üstlenildi** yap ve üstleneni yaz." İki istek aynı anda gelirse veritabanı bunları sırayla işler. İlki 1 satırı değiştirir, ikincisi 0 satır değiştirir ve reddedilir. "Önce oku, sonra yaz" yapılmaz, çünkü iki kişi aynı anda okuyup ikisi de **Açık** görebilir. Bu kural demoda bir testle kanıtlanacak (T-06).

### 2. Üstlenen kişi işi yapamazsa nasıl bırakır?

İsteğin sayfasındaki **Bırak** düğmesine basar (G3). İstek yeniden **Açık** olur ve başkası üstlenebilir. Bırakırken bir yorum yazması önerilir ama zorunlu değildir (V-08). Bırakma bir ceza değildir, bırakan kişiye görünür bir işaret konmaz.

- **V-08:** Bırakırken gerekçe zorunlu değil. (Soru 11)

### 3. İsteği açan kişi onaylamazsa ne olur?

İki durum var:
- **"Yapılmadı" der (G6):** Gerekçe yazmak zorundadır. İstek **Üstlenildi** durumuna, aynı kişiye geri döner. İki taraf yorumlarda konuşur.
- **Hiç cevap vermez:** İstek **Yapıldı** durumunda bekler. Bu konuda **karar vermedim**, çünkü kuralı hocaların koyması gerekiyor. Seçenekler:
  - a) Belli bir süre sonra istek kendiliğinden **Tamamlandı** olur.
  - b) Belli bir süre sonra karar bir öğretmene düşer.
  - c) İstek süresiz bekler.

  Süre ne olmalı? → **Açık soru S-03** (Soru 10). Demoda bu durum yalnızca beklemeyle temsil edilecek.

## Akışta bilerek olmayanlar
- **Puan ya da kredi verilmez.** Kurallar henüz kesinleşmedi (S-01). Kesinleşirse **Tamamlandı** geçişine bağlanır.
- Kimin kaç istek tamamladığı bir listede gösterilmez (T-02).
- Bildirimler demoda yok, yalnızca tasarımda yer alacak.
