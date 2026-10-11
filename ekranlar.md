# Ekranlar

> **Durum: TASLAK.** Ekranlar `roller.md` ve `akis.md` taslaklarına dayanıyor. Telefon ekranına göre çizildi (V-10). Görünen bütün isimler ve istekler uydurmadır.

- **V-10:** Uygulama çoğunlukla öğrencilerin telefonundan kullanılır. Bu yüzden ekranlar dar ekrana göre tasarlandı, bilgisayarda da aynı düzen geniş hâliyle açılır. (Soru 16)

## Arayüz dili: Reddit tarzı

Arayüz, öğrencilerin büyük kısmının zaten tanıdığı **Reddit'in arayüz diline** göre tasarlandı (Ö-01). Böylece kullanıcının yeni bir düzen öğrenmesi gerekmez. Reddit'ten aldığımız ve bilerek almadığımız şeyler:

| Reddit'te | Askıda İyilik'te | Neden |
|-----------|------------------|-------|
| Gönderi kartı | **İstek kartı** | İstekler akış hâlinde, kart kart okunur |
| Topluluk (`r/…`) | **Kategori** (`k/ders`, `k/eşya`, `k/okul`) | Kategoriye göre filtreleme. Kategorileri hocalar belirleyecek (Soru 8) |
| Gönderi flair'i | **Durum etiketi** (🟢 Açık, 🟡 Üstlenildi, 🔵 Yapıldı, ✅ Tamamlandı) | Akışın neresinde olduğu tek bakışta görülsün diye |
| İç içe yorumlar | **Yorumlar ve bir seviye yanıt** (V-11) | Herkese açık konuşma (T-01). Derin iç içe yorumlar telefonda zor okunur |
| Yukarı ve aşağı oylama | **Açık karar (S-08)**, aşağıya bakın | Değişmez ilkelerle çelişebilir |
| Özel mesaj (chat) | **Yok** | Değişmez ilke (T-01) |
| Karma (kullanıcı puanı) | **Yok** | Sıralama tablosu yok (T-02). Puan kuralları kesinleşmedi (S-01) |
| Profil fotoğrafı ve avatar | **Yok**, adın baş harfi gösterilir | Fotoğraf tutulmaz (T-03) |
| "Popüler" ve "En iyi" sıralaması | Yalnızca **Yeni** ve **Açık olanlar** | Oylama kararı (S-08) verilince yeniden değerlendirilir |

- **V-11:** Yorumlara yanıt verilebilir, ama yanıtlara yanıt verilemez (tek seviye). (Hocalara sorulacak)

### Oylama: açık karar (S-08)

Oylama isteği benden geliyor (Emir). Kararı Yasemin Hoca ve Eyüp Hoca verecek, ilkelerle çeliştiği yerlerde Özgür Hoca'ya sorulacak. Gördüğüm riskler:

- **Aşağı oy:** Bir öğrencinin ihtiyacı aşağı oylanırsa kendini kötü hissedebilir, oylama bir zorbalık aracına dönüşebilir. Okulda bildirilen bir sorunu aşağı oylamanın da bir anlamı yok.
- **Kullanıcı puanı:** Oylar kişi başına toplanırsa Reddit'teki karma gibi gizli bir puan ve sıralama ortaya çıkar. Bu, ilke 2 (sıralama yok) ve ilke 5 (puan kuralı icat edilmez) ile çelişir.

Seçenekler:

| | Seçenek | Ekranda | Not |
|---|---------|---------|-----|
| A | Yukarı ve aşağı oy | `▲ 5 ▼` | Benim ilk önerim. Aşağı oy riski var |
| B | Yalnızca destek oyu: "Ben de" | `▲ 5 Ben de` | "Bu sorunu ben de gördüm" ya da "buna ben de ihtiyaç duyuyorum" anlamına gelir. Aşağı oy yok |
| C | Oylama yok | — | En basit seçenek |

Hangi seçenek seçilirse seçilsin: oylar kişi başına toplanmaz ve gösterilmez, kimin oy verdiği görünmez, kişi kendi isteğine oy veremez. Ekran çizimlerinde oylama `▲ 5 ▼` olarak gösterildi. Karar verilince çizimler güncellenecek.

## Ekran listesi

| # | Ekran | Kim görür | Demoda var mı? |
|---|-------|-----------|:--------------:|
| E1 | Giriş | Herkes | ✅ |
| E2 | Ana akış (istek kartları) | Öğrenci, öğretmen | ✅ |
| E3 | Yeni istek | Öğrenci, öğretmen | ✅ |
| E4 | İstek sayfası (düğmeler ve yorumlar) | Öğrenci, öğretmen | ✅ |
| E5 | Benim işlerim | Öğrenci, öğretmen | ✅ |
| E6 | Gizleme (öğretmen) | Öğretmen | ⚠️ Django yönetim paneliyle |
| E7 | Hata ve uyarı mesajları | Herkes | ✅ |

Oylama demoya ancak S-08 kararından sonra eklenir. Demonun zorunlu akışı (aç, üstlen, yapıldı, onayla) oylamaya bağlı değil.

---

## E1. Giriş

```
┌────────────────────────────────┐
│                                │
│        🤝 Askıda İyilik        │
│     Okulumuzun iyilik panosu   │
│                                │
│  ┌──────────────────────────┐  │
│  │ Kullanıcı adı            │  │
│  └──────────────────────────┘  │
│  ┌──────────────────────────┐  │
│  │ Şifre                    │  │
│  └──────────────────────────┘  │
│                                │
│  (         Giriş yap        )  │
│                                │
│  Şifreni unuttuysan okul       │
│  yöneticisine başvur.          │
└────────────────────────────────┘
```
- "Kayıt ol" düğmesi yok, hesapları yönetici açar (V-03).
- Şifre sıfırlama e-postayla yapılmaz, çünkü e-posta tutmuyoruz (`veri.md`).

## E2. Ana akış (istek kartları)

```
┌────────────────────────────────┐
│ 🤝 Askıda İyilik    🔍   (AK)  │  ← üst çubuk, sağda adın baş harfleri
├────────────────────────────────┤
│ (Yeni) (Açık olanlar) (k/ders▾)│  ← sekmeler ve kategori filtresi
├────────────────────────────────┤
│ k/ders · Mehmet A. · 2 sa      │
│ Kimya notları lazım            │
│ [🟢 Açık]                      │
│ Salı günkü dersin notlarına    │
│ ihtiyacım var...               │
│ (▲ 3 ▼)  (💬 1)                │
├────────────────────────────────┤
│ k/okul · Zeynep T. · 1 gün     │
│ 2. kat lavabo musluğu akıtıyor │
│ [🟡 Üstlenildi]                │
│ (▲ 12 ▼)  (💬 3)               │
├────────────────────────────────┤
│ k/eşya · Can B. · 3 gün        │
│ Hesap makinesi ödünç lazım     │
│ [🔵 Yapıldı]                   │
│ (▲ 1 ▼)  (💬 2)                │
├────────────────────────────────┤
│   🏠 Akış    (＋)    📋 İşlerim │  ← alt menü, ortada "Yeni istek"
└────────────────────────────────┘
```
- Kart düzeni Reddit gibi: üstte kategori, yazan ve zaman, sonra kalın başlık, durum etiketi (flair), açıklamanın ilk satırları, altta oy ve yorum düğmeleri.
- Varsayılan sekme **Yeni**. Tamamlanan istekler arşive geçer, akışta görünmez.
- Oylama (`▲ 3 ▼`) açık karardır (S-08).
- Hiçbir yerde "en çok iyilik yapan" ya da kişi başına bir sayı yoktur (T-02).
- Gizlenen istekler akışta görünmez.

## E3. Yeni istek

```
┌────────────────────────────────┐
│ ✕               (  Yayınla  )  │
├────────────────────────────────┤
│ (k/ders ▾)  ← kategori seç     │
│                                │
│ Başlık                         │
│ ────────────────────────────── │
│ Kimya notları lazım            │
│                                │
│ Açıklama                       │
│ ────────────────────────────── │
│ Salı günkü dersin notlarına    │
│ ihtiyacım var.                 │
│                                │
│ ⓘ Telefon, adres ya da başka   │
│   kişisel bilgi yazma. İstek-  │
│   leri okuldaki herkes görür.  │
└────────────────────────────────┘
```
- Reddit'teki "gönderi oluştur" ekranı gibi: üstte kategori seçimi, sağ üstte **Yayınla**.
- Fotoğraf ya da dosya yükleme alanı yok (T-03).
- Hatırlatma notu, açıklamaya kişisel bilgi yazılmasını önlemek için konuldu. Asgari veri ilkesini ekranda da destekliyor.

## E4. İstek sayfası

Bu ekran role ve isteğin durumuna göre **farklı düğmeler** gösterir. Düğmelerin gizlenmesi yalnızca kolaylık içindir, asıl kontrol sunucudadır (T-07).

```
┌────────────────────────────────┐
│ ←  k/ders                  ⋯   │  ← ⋯ menüsü: öğretmene "Gizle"
├────────────────────────────────┤
│ k/ders · Mehmet A. · 2 sa      │
│ Kimya notları lazım            │
│ [🟡 Üstlenildi · Ayşe K.]      │
│                                │
│ Salı günkü dersin notlarına    │
│ ihtiyacım var.                 │
│                                │
│ (▲ 3 ▼)  (💬 2)                │
│ ┌────────────────────────────┐ │
│ │ (  Yapıldı  )  ( Bırak )   │ │  ← yalnızca üstlenen kişi görür
│ └────────────────────────────┘ │
├────────────────────────────────┤
│ ┌────────────────────────────┐ │
│ │ Yorum ekle...              │ │
│ └────────────────────────────┘ │
│                                │
│ (AK) Ayşe K. · 1 sa            │
│ │ Yarın teneffüste getiririm.  │
│ │ ↩ Yanıtla                    │
│ │                              │
│ │  (MA) Mehmet A. · 50 dk      │
│ │  │ Çok sağ ol! 🙏            │
└────────────────────────────────┘
```
- Yorumlar Reddit'teki gibi solda dikey bir çizgiyle gösterilir. Yanıtlar bir seviye içeride durur (V-11).
- Yorumlarda oylama yok. Oylama yalnızca istekte olabilir (S-08).
- "Mesaj gönder" ya da "sohbet" düğmesi yoktur. Konuşma yalnızca bu yorumlarda olur (T-01).

**Kim hangi düğmeyi görür?**

| Durum | İsteği açan | Üstlenen | Diğer öğrenciler | Öğretmen |
|-------|-------------|----------|------------------|----------|
| Açık | Geri çek | — | Üstlen | Üstlen, ⋯ Gizle |
| Üstlenildi | — | Yapıldı, Bırak | — | ⋯ Gizle |
| Yapıldı | Onayla, Yapılmadı | — | — | ⋯ Gizle |
| Tamamlandı | — | — | — | ⋯ Gizle |

- **Yapılmadı** düğmesine basıldığında gerekçe kutusu açılır. Gerekçe yazmadan gönderilemez (G6).

## E5. Benim işlerim

```
┌────────────────────────────────┐
│ ←  Benim işlerim               │
├────────────────────────────────┤
│ (Açtıklarım)  (Üstlendiklerim) │
├────────────────────────────────┤
│ k/eşya · 3 gün                 │
│ Hesap makinesi ödünç lazım     │
│ [🔵 Yapıldı]                   │
│ ⚠ Onayını bekliyor             │
├────────────────────────────────┤
│ k/ders · 5 gün                 │
│ Matematik konu anlatımı        │
│ [🟢 Açık]                      │
├────────────────────────────────┤
│   🏠 Akış    (＋)    📋 İşlerim │
└────────────────────────────────┘
```
- Kullanıcının kendi takip etmesi gereken işleri gösterir. En önemlisi **onayını bekleyen** işlerdir, çünkü onay verilmezse istek bekler (S-03).
- Reddit profillerindeki gibi bir karma ya da toplam "iyilik sayısı" gösterilmez (T-02).

## E6. Gizleme (öğretmen)

```
┌────────────────────────────────┐
│ ✕  İçeriği gizle               │
├────────────────────────────────┤
│ "2. kat lavabo musluğu         │
│  akıtıyor" isteğini gizlemek   │
│ üzeresin.                      │
│                                │
│ Gerekçe (zorunlu)              │
│ ────────────────────────────── │
│                                │
│                                │
│ ( Vazgeç )        ( Gizle )    │
└────────────────────────────────┘
```
- İsteğin ya da yorumun `⋯` menüsünden açılır.
- İçerik silinmez, gizlenir. Gerekçe durum geçmişine yazılır (G8, `veri.md`).
- Demoda bu ekran yerine Django'nun yönetim paneli kullanılacak.

## E7. Hata ve uyarı mesajları

Mesajlar Reddit'teki gibi ekranın altında kısa süreli bir bildirim (toast) olarak gösterilir.

| Ne oldu | Gösterilen mesaj |
|---------|------------------|
| İki kişi aynı anda üstlendi, ikinci kişiye | "Bu istek az önce başka biri tarafından üstlenildi." |
| Yetkisi olmayan biri adresi elle değiştirdi | "Bu işlemi yapma yetkin yok." (403) |
| İsteğin durumu bu işleme uygun değil | "Bu istek artık bu durumda değil, sayfayı yenile." |
| Gerekçe yazılmadan "Yapılmadı" denmek istendi | "Lütfen neyin eksik olduğunu yaz." |
| Kendi isteğine oy vermeye çalıştı (S-08) | "Kendi isteğine oy veremezsin." |
| Yanlış şifre | "Kullanıcı adı ya da şifre hatalı." |
