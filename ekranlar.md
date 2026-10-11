# Ekranlar

> **Durum: TASLAK.** Ekranlar `roller.md` ve `akis.md` taslaklarına dayanıyor. Telefon ekranına göre çizildi (V-10). Görünen bütün isimler ve istekler uydurmadır.

- **V-10:** Uygulama çoğunlukla öğrencilerin telefonundan kullanılır. Bu yüzden ekranlar dar ekrana göre tasarlandı, bilgisayarda da aynı düzen geniş hâliyle açılır. (Soru 16)

## Ekran listesi

| # | Ekran | Kim görür | Demoda var mı? |
|---|-------|-----------|:--------------:|
| E1 | Giriş | Herkes | ✅ |
| E2 | İstek listesi (ana sayfa) | Öğrenci, öğretmen | ✅ |
| E3 | Yeni istek | Öğrenci, öğretmen | ✅ |
| E4 | İstek ayrıntısı (düğmeler ve yorumlar) | Öğrenci, öğretmen | ✅ |
| E5 | Benim işlerim | Öğrenci, öğretmen | ✅ |
| E6 | Gizleme (öğretmen) | Öğretmen | ⚠️ Django yönetim paneliyle |
| E7 | Hata ve uyarı mesajları | Herkes | ✅ |

---

## E1. Giriş

```
┌──────────────────────────────┐
│        Askıda İyilik         │
│                              │
│  Kullanıcı adı               │
│  ┌────────────────────────┐  │
│  │ ogrenci1               │  │
│  └────────────────────────┘  │
│  Şifre                       │
│  ┌────────────────────────┐  │
│  │ ••••••••               │  │
│  └────────────────────────┘  │
│                              │
│  [        Giriş yap       ]  │
│                              │
│  Şifreni unuttuysan okul     │
│  yöneticisine başvur.        │
└──────────────────────────────┘
```
- "Kayıt ol" düğmesi yok, hesapları yönetici açar (V-03).
- Şifre sıfırlama e-postayla yapılmaz, çünkü e-posta tutmuyoruz (`veri.md`).

## E2. İstek listesi (ana sayfa)

```
┌──────────────────────────────┐
│ Askıda İyilik     Ayşe K. ☰  │
├──────────────────────────────┤
│ [ + Yeni istek ]             │
│                              │
│ Filtre: (Açık ▾) (Tümü ▾)    │
│                              │
│ ┌──────────────────────────┐ │
│ │ Kimya notları lazım      │ │
│ │ ders · Mehmet A. · 2 sa  │ │
│ │ 🟢 Açık       💬 1       │ │
│ └──────────────────────────┘ │
│ ┌──────────────────────────┐ │
│ │ 2. kat lavabo musluğu    │ │
│ │ akıtıyor                 │ │
│ │ okul · Zeynep T. · 1 gün │ │
│ │ 🟡 Üstlenildi  💬 3      │ │
│ └──────────────────────────┘ │
│ ┌──────────────────────────┐ │
│ │ Hesap makinesi ödünç     │ │
│ │ eşya · Can B. · 3 gün    │ │
│ │ 🔵 Yapıldı    💬 2       │ │
│ └──────────────────────────┘ │
└──────────────────────────────┘
```
- Varsayılan olarak **Açık** istekler gösterilir. Tamamlanan istekler arşive geçer.
- Kategoriler örnektir, gerçek kategorileri hocalar belirleyecek (Soru 8).
- Hiçbir yerde "en çok iyilik yapan" ya da kişi başına bir sayı yoktur (T-02).
- Gizlenen istekler listede görünmez.

## E3. Yeni istek

```
┌──────────────────────────────┐
│ ← Geri         Yeni istek    │
├──────────────────────────────┤
│ Başlık                       │
│ ┌──────────────────────────┐ │
│ │ Kimya notları lazım      │ │
│ └──────────────────────────┘ │
│ Açıklama                     │
│ ┌──────────────────────────┐ │
│ │ Salı günkü dersin        │ │
│ │ notlarına ihtiyacım var. │ │
│ └──────────────────────────┘ │
│ Kategori                     │
│ ( ders ▾ )                   │
│                              │
│ ⓘ Kişisel bilgi (telefon,    │
│   adres, fotoğraf) yazma.    │
│   İstekleri herkes görür.    │
│                              │
│ [        Yayınla          ]  │
└──────────────────────────────┘
```
- Fotoğraf yükleme alanı yok (T-03).
- Hatırlatma notu, açıklamaya kişisel bilgi yazılmasını önlemek için konuldu. Asgari veri ilkesini ekranda da destekliyor.

## E4. İstek ayrıntısı

Bu ekran role ve isteğin durumuna göre **farklı düğmeler** gösterir. Düğmelerin gizlenmesi yalnızca kolaylık içindir, asıl kontrol sunucudadır (T-07).

```
┌──────────────────────────────┐
│ ← Geri                       │
├──────────────────────────────┤
│ Kimya notları lazım          │
│ ders · Mehmet A. · 2 sa önce │
│ 🟡 Üstlenildi — Ayşe K.      │
│                              │
│ Salı günkü dersin notlarına  │
│ ihtiyacım var.               │
│                              │
│ ┌──────────────────────────┐ │
│ │ [ Yapıldı ]   [ Bırak ]  │ │ ← yalnızca üstlenen kişi görür
│ └──────────────────────────┘ │
│                              │
│ Yorumlar (herkese açık)      │
│ ─────────────────────────    │
│ Ayşe K. · 1 sa               │
│ Yarın teneffüste getiririm.  │
│ ─────────────────────────    │
│ ┌──────────────────────────┐ │
│ │ Yorum yaz…               │ │
│ └──────────────────────────┘ │
│ [ Gönder ]                   │
└──────────────────────────────┘
```

**Kim hangi düğmeyi görür?**

| Durum | İsteği açan | Üstlenen | Diğer öğrenciler | Öğretmen |
|-------|-------------|----------|------------------|----------|
| Açık | Geri çek | — | Üstlen | Üstlen, Gizle |
| Üstlenildi | — | Yapıldı, Bırak | — | Gizle |
| Yapıldı | Onayla, Yapılmadı | — | — | Gizle |
| Tamamlandı | — | — | — | Gizle |

- **Yapılmadı** düğmesine basıldığında gerekçe kutusu açılır. Gerekçe yazmadan gönderilemez (G6).
- "Mesaj gönder" düğmesi yoktur. Konuşma yalnızca bu yorumlarda olur (T-01).

## E5. Benim işlerim

```
┌──────────────────────────────┐
│ ← Geri        Benim işlerim  │
├──────────────────────────────┤
│ [Açtıklarım][Üstlendiklerim] │
│                              │
│ ┌──────────────────────────┐ │
│ │ Hesap makinesi ödünç     │ │
│ │ 🔵 Yapıldı               │ │
│ │ ⚠ Onayını bekliyor       │ │
│ └──────────────────────────┘ │
│ ┌──────────────────────────┐ │
│ │ Matematik konu anlatımı  │ │
│ │ 🟢 Açık                  │ │
│ └──────────────────────────┘ │
└──────────────────────────────┘
```
- Kullanıcının kendi takip etmesi gereken işleri gösterir. En önemlisi **onayını bekleyen** işlerdir, çünkü onay verilmezse istek bekler (S-03).
- Burada da toplam bir "iyilik sayısı" gösterilmez (T-02).

## E6. Gizleme (öğretmen)

```
┌──────────────────────────────┐
│ ← Geri       İçeriği gizle   │
├──────────────────────────────┤
│ "2. kat lavabo musluğu       │
│  akıtıyor" isteğini          │
│ gizlemek üzeresin.           │
│                              │
│ Gerekçe (zorunlu)            │
│ ┌──────────────────────────┐ │
│ │                          │ │
│ └──────────────────────────┘ │
│                              │
│ [ Vazgeç ]     [ Gizle ]     │
└──────────────────────────────┘
```
- İçerik silinmez, gizlenir. Gerekçe durum geçmişine yazılır (G8, `veri.md`).
- Demoda bu ekran yerine Django'nun yönetim paneli kullanılacak.

## E7. Hata ve uyarı mesajları

| Ne oldu | Gösterilen mesaj |
|---------|------------------|
| İki kişi aynı anda üstlendi, ikinci kişiye | "Bu istek az önce başka biri tarafından üstlenildi." |
| Yetkisi olmayan biri adresi elle değiştirdi | "Bu işlemi yapma yetkin yok." (403) |
| İsteğin durumu bu işleme uygun değil | "Bu istek artık bu durumda değil, sayfayı yenile." |
| Gerekçe yazılmadan "Yapılmadı" denmek istendi | "Lütfen neyin eksik olduğunu yaz." |
| Yanlış şifre | "Kullanıcı adı ya da şifre hatalı." |
