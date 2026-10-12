# Akış: Bir sorunun durumları

> **Durum: TASLAK.** Akış Özgür Hoca'nın istediği dört adımdan oluşur (T-09): **sorunu bildir → biri üstlensin → yapıldı desin → bildiren onaylasın.** Askıya yalnızca okulda görülen sorunlar konur (T-08): bozuk kapı, damlayan musluk, biten sabun gibi.

## Durumlar

| Durum | Anlamı |
|-------|--------|
| **Açık** | Sorun bildirildi, üstlenecek birini bekliyor |
| **Üstlenildi** | Biri sorunu üstlendi |
| **Yapıldı** | Üstlenen kişi işi yaptığını söyledi, bildirenin onayı bekleniyor |
| **Tamamlandı** | Bildiren kişi onayladı. İş bitti |

## Şema

```
            üstlen                 yapıldı de               onayla
┌────────┐ ───────▶ ┌────────────┐ ─────────▶ ┌─────────┐ ───────▶ ┌────────────┐
│  Açık  │          │ Üstlenildi │            │ Yapıldı │          │ Tamamlandı │
└────────┘ ◀─────── └────────────┘            └─────────┘          └────────────┘
     ▲       bırak
     │
  bildir
```

## Geçişler

| # | Geçiş | Kim yapar | Koşul | Sonuç |
|---|-------|-----------|-------|-------|
| G1 | Sorunu bildir | Öğrenci ya da öğretmen | Başlık ve açıklama dolu | **Açık** |
| G2 | Üstlen | Bildiren dışında biri | Durum **Açık** | **Üstlenildi**, üstlenen kişi kaydedilir |
| G3 | Bırak | Yalnızca üstlenen | Durum **Üstlenildi** | **Açık**, üstlenen kişi silinir |
| G4 | Yapıldı de | Yalnızca üstlenen | Durum **Üstlenildi** | **Yapıldı** |
| G5 | Onayla | Yalnızca bildiren | Durum **Yapıldı** | **Tamamlandı** |

Her geçiş, kimin ne zaman yaptığıyla birlikte durum geçmişine yazılır (`veri.md`). Tabloda olmayan bir geçişi sunucu reddeder.

## Görev tanımının üç sorusu

### 1. Aynı sorunu iki kişi aynı anda üstlenirse ne olur?

İlk gelen alır, ikincisine "Bu sorun az önce başka biri tarafından üstlenildi." denir.

Sunucu kontrolü ve değişikliği tek bir adımda yapar: "Durumu hâlâ **Açık** ise **Üstlenildi** yap." Önce bakıp sonra yazsaydı iki kişi de aynı anda "Açık" görüp ikisi de üstlenebilirdi. Bu kuralın demoda testi var (T-06).

### 2. Üstlenen kişi işi yapamazsa nasıl bırakır?

Sorunun sayfasındaki **Bırak** düğmesine basar (G3). Sorun yeniden **Açık** olur, başkası üstlenebilir. Sebep yazmak zorunlu değildir (V-08). İsterse yorum yazabilir.

### 3. Bildiren kişi onaylamazsa ne olur?

Sorun **Yapıldı** durumunda bekler. Belli bir süre sonra ne olacağı (kendiliğinden tamamlansın mı, bir öğretmene mi düşsün?) **hocaların kararı**, açık soru S-03.
