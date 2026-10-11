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

**Görsel taslak:** Ekranların tarayıcıda görünen hâli [`ekran-taslaklari/index.html`](ekran-taslaklari/index.html) sayfasında. Yayındaki adresi: https://emir34-34.github.io/askida-iyilik-okul-demo/ekran-taslaklari/ (demo değil, yalnızca görünüş).

**Renk ve simge:** Ana renk Reddit'e uyumlu turuncu (`#d93a00`). Durum etiketleri anlamlarına göre renkli kalıyor (yeşil Açık, sarı Üstlenildi, mavi Yapıldı). Uygulama simgesini Emir tasarlayacak, o zamana kadar yer tutucu olarak 🤝 kullanılıyor.

### Oylama: açık karar (S-08)

Oylama isteği benden geliyor (Emir). Kararı Yasemin Hoca ve Eyüp Hoca verecek, ilkelerle çeliştiği yerlerde Özgür Hoca'ya sorulacak. Gördüğüm riskler:

- **Aşağı oy:** Bir öğrencinin ihtiyacı aşağı oylanırsa kendini kötü hissedebilir, oylama bir zorbalık aracına dönüşebilir. Okulda bildirilen bir sorunu aşağı oylamanın da bir anlamı yok.
- **Kullanıcı puanı:** Oylar kişi başına toplanırsa Reddit'teki karma gibi gizli bir puan ve sıralama ortaya çıkar. Bu, ilke 2 (sıralama yok) ve ilke 5 (puan kuralı icat edilmez) ile çelişir.

Seçenekler:

| | Seçenek | Ekranda | Not |
|---|---------|---------|-----|
| **A** ✔ | **Yukarı ve aşağı oy** | `▲ 5 ▼` | **Tasarımcının tercihi (Emir).** Aşağı oy riski var, aşağıdaki önlemlerle |
| B | Yalnızca destek oyu: "Ben de" | `▲ 5 Ben de` | "Bu sorunu ben de gördüm" ya da "buna ben de ihtiyaç duyuyorum" anlamına gelir. Aşağı oy yok |
| C | Oylama yok | — | En basit seçenek |

**Tasarımcının tercihi A'dır, çizimler buna göre yapıldı.** Hocalar ya da Özgür Hoca B ya da C derse çizimler değiştirilir.

Aşağı oyun riskini azaltmak için önerdiğim önlemler (bunlar da hocalara sorulacak):
- Oylar kişi başına toplanmaz ve gösterilmez, kimin oy verdiği görünmez, kişi kendi isteğine oy veremez.
- Bir isteğin oy toplamı sıfırın altına düşerse ekranda **0** gösterilir. Böylece kimsenin ihtiyacı "−5" olarak herkesin önünde durmaz.
- Aşağı oy bir isteği gizlemez ya da silmez. İçeriği yalnızca öğretmen gizleyebilir (V-02).

## Ekran listesi

| # | Ekran | Kim görür | Demoda var mı? |
|---|-------|-----------|:--------------:|
| E1 | Giriş | Herkes | ✅ |
| E2 | Ana akış (istek kartları) | Öğrenci, öğretmen | ✅ |
| E3 | Yeni istek | Öğrenci, öğretmen | ✅ |
| E4 | İstek sayfası (düğmeler ve yorumlar) | Öğrenci, öğretmen | ✅ |
| E5 | Görevler | Öğrenci, öğretmen | ✅ |
| E6 | Gizleme (öğretmen) | Öğretmen | ⚠️ Django yönetim paneliyle |
| E7 | Hata ve uyarı mesajları | Herkes | ✅ |
| E8 | Profil | Herkes | ✅ |
| E9 | Bildirimler | Öğrenci, öğretmen | ❌ yalnızca tasarımda |
| E10 | Arşiv | Herkes | ❌ yalnızca tasarımda |
| E11 | Şikâyet et | Öğrenci, öğretmen | ❌ yalnızca tasarımda |
| D1 | Ana akış (bilgisayar) | Öğrenci, öğretmen | ✅ |
| D2 | İstek sayfası (bilgisayar) | Öğrenci, öğretmen | ✅ |
| D3 | Yönetim özeti (bilgisayar) | Öğretmen, yönetici | ❌ yalnızca tasarımda |
| D4 | Kontrol (bilgisayar) | Öğretmen | ⚠️ Django yönetim paneliyle |

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
│ 🤝 Askıda İyilik  🔍 🔔³ (AK)  │  ← üst çubuk: arama, bildirimler, profil
├────────────────────────────────┤
│ (Yeni) (Açık olanlar) (Arşiv)  │  ← sekmeler ve kategori filtresi
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
│  🏠      ＋      📋      👤    │  ← alt menü
│ Akış  Oluştur Görevler Profil  │
└────────────────────────────────┘
```
- Alt menüde dört düğme var: **Akış**, **Oluştur** (＋, yeni istek), **Görevler** (E5) ve **Profil** (E8). Sohbet sekmesi yok, çünkü özel mesaj yok (T-01).
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
│ ( 📷 Resim ekle ) ( 🎬 Video )  │  ← açık karar S-09
│                                │
│ ⓘ Telefon, adres ya da başka   │
│   kişisel bilgi yazma. Resim-  │
│   de kimsenin yüzü görünmesin. │
│   İstekleri herkes görür.      │
└────────────────────────────────┘
```
- Reddit'teki "gönderi oluştur" ekranı gibi: üstte kategori seçimi, sağ üstte **Yayınla**.
- **Resim ve video ekleme: açık karar (S-09).** Bu benim önerim (Ö-04). Değişmez ilke 3 "fotoğraf tutulmaz" diyor, bu yüzden son onay Özgür Hoca'da. Onaylanmazsa bu düğmeler kaldırılır. Önerdiğim önlemler:
  - Dosyadaki **konum ve cihaz bilgisi (EXIF)** sunucuya kaydedilmeden önce silinir.
  - Ekranda "kimsenin yüzü görünmesin" uyarısı gösterilir. Kurala uymayan içeriği öğretmen gizler (V-02).
  - Her isteğe en fazla 1 resim ya da 1 kısa video eklenir, boyut sınırı olur (ör. resim 5 MB, video 30 saniye).
  - Profil fotoğrafı hâlâ yok. Bu öneri yalnızca isteklere eklenen dosyalar için.
  - Video, resimden daha fazla risk ve depolama getirir (ses, yüzler, büyük dosya, eski ev sunucusu). İlk sürümde yalnızca resim olabilir, video sonraya kalabilir.
- Hatırlatma notu, açıklamaya kişisel bilgi yazılmasını önlemek için konuldu. Asgari veri ilkesini ekranda da destekliyor.

## E4. İstek sayfası

Bu ekran role ve isteğin durumuna göre **farklı düğmeler** gösterir. Düğmelerin gizlenmesi yalnızca kolaylık içindir, asıl kontrol sunucudadır (T-07).

```
┌────────────────────────────────┐
│ ←  k/ders                  ⋯   │  ← ⋯ menüsü: herkese "Şikâyet et", öğretmene ayrıca "Gizle"
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

## E5. Görevler

```
┌────────────────────────────────┐
│ ←  Görevler                    │
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
│  🏠      ＋      📋      👤    │
│ Akış  Oluştur Görevler Profil  │
└────────────────────────────────┘
```
- Kullanıcının kendi takip etmesi gereken işleri gösterir. En önemlisi **onayını bekleyen** işlerdir, çünkü onay verilmezse istek bekler (S-03).
- Reddit profillerindeki gibi bir karma ya da toplam "iyilik sayısı" gösterilmez (T-02).

## E8. Profil

```
┌────────────────────────────────┐
│ Profil                         │
├────────────────────────────────┤
│              (AK)              │
│             Ayşe K.            │
│       ogrenci2 · Öğrenci       │
├────────────────────────────────┤
│ Görünüm           Açık / koyu ›│
│ Şifremi değiştir              ›│
│ Hakkımda hangi bilgiler        │
│ tutuluyor?                    ›│
│ Uygulama kuralları            ›│
│ Çıkış yap                      │
├────────────────────────────────┤
│ ⓘ Profilinde kaç iyilik yap-   │
│   tığın ya da puanın gösteril- │
│   mez.                         │
├────────────────────────────────┤
│  🏠      ＋      📋      👤    │
│ Akış  Oluştur Görevler Profil  │
└────────────────────────────────┘
```
- Profilde yalnızca `veri.md`'deki alanlar var: görünen ad, kullanıcı adı, rol. Fotoğraf yerine adın baş harfleri (T-03).
- Reddit profilindeki karma, gönderi sayısı ya da rozet yok (T-02, S-01).
- "Hakkımda hangi bilgiler tutuluyor?" sayfası kullanıcıya kendisi hakkında tutulan veriyi gösterir. Bu, KVKK'nın aydınlatma yükümlülüğüne uygun bir tasarım. İçeriğini Özgür Hoca'nın KVKK notlarıyla birlikte yazacağız (S-04).

## Bilgisayar arayüzü (D1, D2)

Uygulama okul bilgisayarından ya da akıllı tahtadan açıldığında Reddit'in masaüstü düzeni kullanılır (Ö-05). Kartlar, renkler ve düğmeler telefondakiyle aynıdır. Yalnızca yerleşim değişir: alt menü sol menüye dönüşür, sağa bilgi kartları eklenir.

```
┌──────────────────────────────────────────────────────────────────────────────┐
│ 🤝 Askıda İyilik     [ 🔍 İsteklerde ara            ]  (＋ Oluştur) 🔔³ (AK) │
├───────────────┬──────────────────────────────────────┬───────────────────────┤
│ 🏠 Akış       │ (Yeni) (Açık olanlar)                │ 🤝 Askıda İyilik      │
│ 📋 Görevler   │ ┌──────────────────────────────────┐ │ Okulumuzun iyilik     │
│ 👤 Profil     │ │ k/ders · Mehmet A. · 2 sa        │ │ panosu...             │
│───────────────│ │ Kimya notları lazım              │ │ ( ＋ Yeni istek )     │
│ KATEGORİLER   │ │ [🟢 Açık]                        │ ├───────────────────────┤
│ 📘 k/ders     │ │ Salı günkü dersin notlarına...   │ │ Durumlar              │
│ 🎒 k/eşya     │ │ (▲ 3 ▼) (💬 1)                   │ │ 🟢 🟡 🔵 ✅            │
│ 🏫 k/okul     │ └──────────────────────────────────┘ ├───────────────────────┤
│───────────────│ ┌──────────────────────────────────┐ │ Kurallar              │
│ BİLGİ         │ │ k/okul · Zeynep T. · 1 gün       │ │ 1. Özel mesaj yok     │
│ Kurallar      │ │ 2. kat lavabo musluğu akıtıyor   │ │ 2. Kişisel bilgi yok  │
│ Hangi bilgiler│ │ ...                              │ │ ...                   │
└───────────────┴──────────────────────────────────────┴───────────────────────┘
```
- **D1 Ana akış:** Ortada telefondaki istek kartları, sağda uygulamanın ne olduğu, durum etiketlerinin anlamı ve kurallar.
- **D2 İstek sayfası:** Ortada istek, rol düğmeleri ve yorumlar. Sağda **"Bu istek nerede?"** kartı isteğin akıştaki yerini adım adım gösterir (Açıldı → Üstlenildi → Yapıldı → Onay). Bu kart durum geçmişini değil, yalnızca şu anki durumu gösterir. Durum geçmişi yalnızca öğretmenlere açıktır (`veri.md`).
- Kategori açıklamaları ve kurallar metni örnektir. Asıl metni hocalar belirleyecek.

## E9. Bildirimler

Sağ üstteki 🔔 düğmesiyle açılır (Ö-06). Okunmamış bildirim sayısı düğmenin üstünde turuncu bir rozetle gösterilir. Bilgisayarda aynı liste, düğmenin altında açılan bir panelde görünür.

```
┌────────────────────────────────┐
│ ←  Bildirimler                 │
├────────────────────────────────┤
│ 3 okunmamış  Tümünü okundu say │
├────────────────────────────────┤
│ 💬 Ayşe K. isteğine yorum      │
│    yaptı: Kimya notları lazım ●│
│    "Yarın teneffüste getiririm"│
├────────────────────────────────┤
│ 🟡 Ayşe K. isteğini üstlendi  ●│
├────────────────────────────────┤
│ 🔵 Hesap makinesi ödünç lazım  │
│    yapıldı. Onayını bekliyor. ●│
├────────────────────────────────┤
│ ↩  Can B. yorumuna yanıt verdi │
├────────────────────────────────┤
│ ✅ Zeynep T. yaptığın işi      │
│    onayladı 🙏                 │
└────────────────────────────────┘
```

**Hangi olaylar bildirim olur?**

| Olay | Kime gider |
|------|------------|
| İsteğine yorum yazıldı | İsteği açan kişiye |
| Yorumuna yanıt verildi | Yorumu yazan kişiye |
| İsteğin üstlenildi | İsteği açan kişiye |
| İş "Yapıldı" olarak işaretlendi, onay bekleniyor | İsteği açan kişiye |
| İş onaylandı ya da "Yapılmadı" dendi | Üstlenen kişiye |
| Üstlenen kişi işi bıraktı | İsteği açan kişiye |
| Öğretmen içeriği gizledi | İçeriği yazan kişiye, gerekçesiyle |

- **Oylar bildirim olmaz.** "İsteğin 5 oy aldı" gibi bildirimler bir popülerlik yarışı hissi yaratır (T-02).
- Bildirimler yalnızca uygulamanın içinde görünür. Telefon numarası ya da e-posta tutmadığımız için SMS ya da e-posta gönderilmez (T-03).
- Bildirim, herkese açık olayları haber verir. Özel mesaj değildir (T-01).
- Görev tanımına göre bildirimler demoda olmayabilir. Önce zorunlu akış (aç, üstlen, yapıldı, onayla) yapılacak, zaman kalırsa bildirimler eklenecek.

## E10. Arşiv

Tamamlanan istekler akıştan kalkıp arşive taşınır. Arşive akıştaki **Arşiv** sekmesinden, bilgisayarda sol menüden girilir.

```
┌────────────────────────────────┐
│ ←  Arşiv                       │
├────────────────────────────────┤
│ (Tümü) (k/ders) (k/eşya) (k/okul)
├────────────────────────────────┤
│ ✅ Okulumuzda yapılan iyilikler│
├────────────────────────────────┤
│ k/okul · Zeynep T. · 12 Eki    │
│ Kütüphanede priz çalışmıyor    │
│ [✅ Tamamlandı · Can B.]       │
│ (💬 4)                         │
├────────────────────────────────┤
│ k/ders · Elif S. · 9 Eki       │
│ Geometri konu anlatımı         │
│ [✅ Tamamlandı · Mehmet A.]    │
└────────────────────────────────┘
```
- Amaç, okulda yapılan iyilikleri görünür kılmak (görev tanımı, bölüm 2).
- Yalnızca **kategoriye** göre filtrelenir. **Kişiye göre filtre ya da arama yoktur.** "Ayşe'nin yaptığı iyilikler" diye bir liste çıkarılabilseydi bu, gizli bir sıralama tablosuna dönüşürdü (T-02).
- Arşivdeki isteklerde oy düğmesi yok, yorumlar okunabilir ama yeni yorum yazılamaz.
- Arşivin ne kadar süre tutulacağı saklama süresi kararına bağlı (S-04).

## D3. Yönetim özeti

Öğretmenlerin ve okul idaresinin uygulamanın nasıl kullanıldığını görmesi için hazırlanmış sayfa. Genelde bilgisayardan açılacağı için yalnızca bilgisayar düzeni çizildi. Bilgisayarda sol menünün **Öğretmen** bölümünden açılır.

```
┌───────────────┬──────────────────────────────────────────────────────────────┐
│ 🏠 Akış       │ Yönetim özeti                 (Bu hafta) (Bu ay) (Bu dönem)  │
│ 🗄 Arşiv      │ 🔒 Yalnızca toplam sayılar. Kişi bazında bilgi yok.          │
│───────────────│ ┌──────────┐┌──────────┐┌──────────┐┌─────────────────┐      │
│ ÖĞRETMEN      │ │Açılan    ││Tamamlanan││Ort. süre ││⚠ Uzun süredir   │      │
│ 📊 Yönetim    │ │   58     ││   42     ││ 1,8 gün  ││  bekleyen: 5    │      │
│    özeti      │ └──────────┘└──────────┘└──────────┘└─────────────────┘      │
│               │ Kategoriye göre        │ 🏫 Okulda bildirilen açık sorunlar  │
│               │ k/okul ████████ 24     │ 2. kat lavabo musluğu   🟡 1 gün    │
│               │ k/ders ███████  21     │ Spor salonu kapı kolu   🟢 4 gün    │
│               │ k/eşya ████     13     │                                     │
│               │ ⚠ Uzun süredir bekleyen istekler                             │
│               │ Hesap makinesi ödünç lazım · Yapıldı, onay bekliyor   4 gün  │
└───────────────┴──────────────────────────────────────────────────────────────┘
```

**Sayfada neler var, neden?**

| Bölüm | Neden |
|-------|-------|
| Açılan, tamamlanan, ortalama süre | Uygulamanın gerçekten kullanılıp kullanılmadığını görmek için |
| Uzun süredir bekleyen istekler | Onay verilmeden ya da üstlenilmeden bekleyen işleri fark etmek için. Eşik (ör. 3 gün) S-03 kararıyla belirlenecek |
| Kategoriye göre dağılım | Okulda en çok neye ihtiyaç duyulduğunu görmek için |
| Okulda bildirilen açık sorunlar | `k/okul` kategorisindeki bozuk musluk, kırık kapı gibi sorunlar idarenin doğrudan ilgilenmesi gereken işler olabilir |

**Bilerek olmayanlar**
- **Kişi bazında hiçbir sayı yok.** "En çok istek açan", "en çok iyilik yapan", "en az onay veren" gibi listeler yok. Uzun süredir bekleyenler listesinde de **kişi değil istek** gösterilir (T-02).
- Sınıf ya da şube bazında kırılım yok, çünkü sınıf bilgisini tutmuyoruz (`veri.md`).
- Bütün sayılar mevcut verilerden (istek, durum, zaman, kategori) hesaplanır. Bu sayfa için yeni bir veri tutulmaz.

## E11. Şikâyet et

İsteğin ya da yorumun `⋯` menüsünden açılır. Öğretmenler her isteği tek tek okuyamaz, bu yüzden uygunsuz içeriği öğrencilerin de bildirebilmesi gerekir (Soru 15).

```
┌────────────────────────────────┐
│ Bu isteği neden bildiriyorsun? │
│ ◉ Kişisel bilgi içeriyor       │
│ ○ Birini küçük düşürüyor       │
│ ○ Uygunsuz dil                 │
│ ○ Okulla ilgisi yok / para     │
│ ○ Diğer                        │
│ 🔒 Bildirimin öğretmenlere     │
│    gider. Yazan kişi kimin     │
│    bildirdiğini görmez.        │
│          ( Vazgeç ) ( Bildir ) │
└────────────────────────────────┘
```
- Şikâyet **içeriği otomatik gizlemez** ve isteğin durumunu değiştirmez. Karar her zaman öğretmenindir (V-14). Böylece bir grup öğrencinin toplu şikâyetle birinin isteğini kaldırması önlenir.
- İçeriği yazan kişi kimin şikâyet ettiğini görmez. Öğretmen görür, böylece şikâyetin kötüye kullanılması fark edilebilir (V-13).
- Kişi kendi içeriğini şikâyet edemez, aynı içeriği bir kez şikâyet edebilir.
- Şikâyet sebepleri örnektir, asıl listeyi hocalar belirleyecek.

## D4. Kontrol (öğretmen)

Şikâyet edilen (E11) ve gizlenen (E6) içerikler tek bir sayfada toplanır. Öğretmen menüsündeki **Kontrol** bağlantısının yanında bekleyen şikâyet sayısı görünür. Telefonda da aynı liste tek sütun olarak açılır.

```
┌───────────────┬──────────────────────────────────────────────────────────────┐
│ ÖĞRETMEN      │ Kontrol           (Şikâyetler 3) (Gizlenenler) (İncelenenler)│
│ 📊 Yönetim    │ ┌──────────────────────────────────────────────────────────┐ │
│    özeti      │ │ [🔒 Kişisel bilgi] İstek · k/eşya · Can B.  2 kişi bildirdi│ │
│ 🛡 Kontrol ③  │ │ Biri bana 50 TL borç versin                              │ │
│               │ │ Numaram 05xx xxx xx xx, yazın.                           │ │
│               │ │ ( Gizle… ) ( Sorun yok ) ( İsteğe git )                  │ │
│               │ └──────────────────────────────────────────────────────────┘ │
└───────────────┴──────────────────────────────────────────────────────────────┘
```

| Sekme | Ne gösterir | Öğretmen ne yapabilir |
|-------|-------------|-----------------------|
| Şikâyetler | Durumu `bekliyor` olan şikâyetler, aynı içerik için gelen şikâyetler tek kartta | **Gizle…** (gerekçe ister, E6) ya da **Sorun yok** (şikâyet kapanır, içerik yayında kalır) |
| Gizlenenler | Gizlenen istekler ve yorumlar, gerekçesi ve kimin gizlediği | **Geri aç** (G9) |
| İncelenenler | "Sorun yok" denen şikâyetler | Yeniden açma |

- "2 kişi bildirdi ›" bağlantısı, kimin şikâyet ettiğini yalnızca öğretmene gösterir (V-13).
- Her karar durum geçmişine yazılır (`veri.md`).
- Demoda bu sayfa yerine Django'nun yönetim paneli kullanılacak.

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
- İsteğin ya da yorumun `⋯` menüsünden, ya da Kontrol sayfasındaki (D4) **Gizle…** düğmesinden açılır.
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
