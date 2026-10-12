# Ekranlar

> **Durum: TASLAK.** Yalnızca dört adımlık akışın gerektirdiği beş ekran var (T-09). Görünüm sade tutuldu. Bütün isimler ve sorunlar uydurmadır.
> Tarayıcıda görmek için: [ekran-taslaklari/](https://emir34-34.github.io/askida-iyilik-okul-demo/ekran-taslaklari/)

| # | Ekran | Kim görür |
|---|-------|-----------|
| E1 | Giriş | Herkes |
| E2 | Sorunlar (liste) | Öğrenci, öğretmen |
| E3 | Sorun bildir | Öğrenci, öğretmen |
| E4 | Sorun sayfası | Öğrenci, öğretmen |
| E5 | Benim işlerim | Öğrenci, öğretmen |

## E1. Giriş

```
┌──────────────────────────────┐
│        Askıda İyilik         │
│  Okulda gördüğün sorunlar    │
│                              │
│  Kullanıcı adı [__________]  │
│  Şifre         [__________]  │
│                              │
│  [        Giriş yap       ]  │
└──────────────────────────────┘
```
- "Kayıt ol" yok, hesapları yönetici açar (V-03).

## E2. Sorunlar

```
┌──────────────────────────────┐
│ Askıda İyilik   [Sorun bildir]│
│ (Açık olanlar) (Hepsi)        │
├──────────────────────────────┤
│ 2. kat lavabo musluğu damlıyor│
│ Zeynep T. · 2 saat önce       │
│ [Açık]                        │
├──────────────────────────────┤
│ Spor salonu kapısının kolu    │
│ kırık                         │
│ Can B. · dün                  │
│ [Üstlenildi · Ayşe K.]        │
├──────────────────────────────┤
│ Kantin lavabosunda sabun bitti│
│ Mehmet A. · dün               │
│ [Yapıldı · Elif S.]           │
└──────────────────────────────┘
```
- Varsayılan olarak **açık** sorunlar görünür. "Hepsi" sekmesi tamamlananları da gösterir.
- Kişi başına bir sayı ya da sıralama yoktur (T-02).

## E3. Sorun bildir

```
┌──────────────────────────────┐
│ ← Geri        Sorun bildir   │
├──────────────────────────────┤
│ Ne sorunu var?               │
│ [Spor salonu kapısının kolu ]│
│ Nerede, nasıl? (açıklama)    │
│ [Giriş kapısının sağ kanadı ]│
│ [kolu yerinden çıkmış.      ]│
│                              │
│ ⓘ Yalnızca okulda gördüğün   │
│   sorunları bildir. Kişisel  │
│   bilgi yazma.               │
│                              │
│ [         Bildir          ]  │
└──────────────────────────────┘
```
- Askıya yalnızca okul sorunları konur (T-08), ekrandaki not bunu hatırlatır.
- Sorunun yeri açıklamaya yazılır (V-15).

## E4. Sorun sayfası

```
┌──────────────────────────────┐
│ ← Geri                       │
├──────────────────────────────┤
│ 2. kat lavabo musluğu damlıyor│
│ Zeynep T. · 2 saat önce      │
│ [Açık]                       │
│ Kız tuvaletindeki soldan     │
│ ikinci musluk sürekli damlıyor│
│                              │
│ [ Üstlen ]   ← duruma ve role göre değişir
├──────────────────────────────┤
│ Yorumlar (herkese açık)      │
│ Ayşe K.: Hademe ablaya haber │
│ verdim.                      │
│ [Yorum yaz...      ] [Gönder]│
└──────────────────────────────┘
```

**Kim hangi düğmeyi görür?**

| Durum | Bildiren | Üstlenen | Diğerleri |
|-------|----------|----------|-----------|
| Açık | — | — | Üstlen |
| Üstlenildi | — | Yapıldı, Bırak | — |
| Yapıldı | Onayla | — | — |
| Tamamlandı | — | — | — |

Düğmelerin gizlenmesi yalnızca görünüştür, asıl kontrol sunucudadır (T-07).

## E5. Benim işlerim

```
┌──────────────────────────────┐
│ ← Geri        Benim işlerim  │
│ (Bildirdiklerim) (Üstlendiklerim)
├──────────────────────────────┤
│ Kantin lavabosunda sabun bitti│
│ [Yapıldı] ⚠ Onayını bekliyor │
├──────────────────────────────┤
│ Bahçedeki çöp kutusu taşıyor │
│ [Açık]                       │
└──────────────────────────────┘
```
- Kişinin kendi takip etmesi gereken işler. En önemlisi onayını bekleyen işler.

## Hata mesajları

| Ne oldu | Mesaj |
|---------|-------|
| İki kişi aynı anda üstlendi, ikinci kişiye | "Bu sorun az önce başka biri tarafından üstlenildi." |
| Yetkisiz biri adresi elle yazdı | "Bu işlemi yapma yetkin yok." (403) |
| Sorunun durumu işleme uygun değil | "Bu sorun artık bu durumda değil, sayfayı yenile." |
| Yanlış şifre | "Kullanıcı adı ya da şifre hatalı." |
