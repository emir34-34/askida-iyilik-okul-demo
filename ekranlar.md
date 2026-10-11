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
| E12 | İlk giriş tanıtımı | Herkes, yalnızca ilk girişte | ❌ yalnızca tasarımda |
| E13 | Onayla ve teşekkür et | İsteği açan kişi | ⚠️ Onay var, teşekkür notu zaman kalırsa |
| E14 | Boş durumlar | Herkes | ✅ akış ve görevler için |
| E15 | Arama sonuçları | Öğrenci, öğretmen | ❌ yalnızca tasarımda |
| E16 | Görevli girişi (kullanıcı adı + şifre + okul kelimesi) | Öğretmen, yönetici | ❌ yalnızca tasarımda |
| E17 | Yönetici paneli | Yönetici | ⚠️ Django yönetim paneliyle |
| E18 | Sistem ayarları | Yönetici | ❌ yalnızca tasarımda |
| D1 | Ana akış (bilgisayar) | Öğrenci, öğretmen | ✅ |
| D2 | İstek sayfası (bilgisayar) | Öğrenci, öğretmen | ✅ |
| D3 | Yönetim özeti (bilgisayar) | Öğretmen, yönetici | ❌ yalnızca tasarımda |
| D4 | Kontrol (bilgisayar) | Öğretmen | ⚠️ Django yönetim paneliyle |
| D5 | Görevli girişi (bilgisayar) | Öğretmen, yönetici | ❌ yalnızca tasarımda |
| D6 | Yönetici paneli (bilgisayar) | Yönetici | ⚠️ Django yönetim paneliyle |
| D7 | Sistem ayarları (bilgisayar) | Yönetici | ❌ yalnızca tasarımda |

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
- Altta **"Öğretmen / yönetici girişi"** bağlantısı E16'yı açar. Öğretmen ve yönetici hesapları bu ekrandan giriş yapamaz.
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

## E12. İlk giriş tanıtımı

Kullanıcı ilk kez giriş yaptığında akıştan önce gösterilir. Uygulamanın nasıl çalıştığını ve kuralları baştan anlatır.

```
  1/4               2/4               3/4               4/4
┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────────┐
│          │     │          │     │          │     │ Birkaç kural │
│    📝    │ ──▶ │    🤝    │ ──▶ │    ✅    │ ──▶ │ • Özel mesaj │
│ İstek aç │     │  Biri    │     │   Sen    │     │   yok        │
│          │     │ üstlenir │     │ onaylarsın│    │ • Kişisel    │
│ ( İleri )│     │ ( İleri )│     │ ( İleri )│     │   bilgi yok  │
└──────────┘     └──────────┘     └──────────┘     │ ☐ Okudum     │
                                                   │ ( Başla )    │
                                                   └──────────────┘
```
- İlk üç ekran temel akışı anlatır: aç, üstlen, onayla (T-05).
- **Tanıtım atlanamaz, "Geç" düğmesi yok.** Her ekranda "İleri" düğmesi **5 saniye kilitli** kalır, kilitliyken düğmenin içi soldan sağa dolar. Amaç, kullanıcının metni okumadan hızla geçip gitmesini önlemek.
- Son ekranda kurallar var. "Başla" düğmesi hem 5 saniye geçmeden hem de **"Kuralları okudum" işaretlenmeden** çalışmaz.
- 5 saniye, bir ekrandaki kısa metni okumaya yetecek süre. Dört ekranla tanıtım toplam yaklaşık 20 saniye sürer. Tanıtım yalnızca bir kez gösterildiği için bu kabul edilebilir. Hocalar uzun bulursa süre kısaltılabilir.
- **Easter egg:** Düğme kilitliyken üst üste 3 kez basılırsa düğme sallanır ve "Sakin ol, sabırsız! 😄" gibi şakacı bir mesaj çıkar (üç mesajdan biri rastgele seçilir). Kurallar ekranında süre dolduğu hâlde "okudum" işaretlenmediyse mesaj "Önce kuralları okuduğunu işaretle." olur. Amaç, beklemeyi sinir bozucu olmaktan çıkarıp gülümseten bir ana çevirmek.
- Kurallar değişmez ilkelerden gelir: özel mesaj yok (T-01), kişisel bilgi yok (T-03), sıralama yok (T-02). Kural metni örnektir, asıl metni hocalar belirleyecek.
- Kurallar daha sonra Profil'deki (E8) **Uygulama kuralları** satırından yeniden okunabilir.

## E13. Onayla ve teşekkür et

İsteği açan kişi **Onayla**'ya bastığında (G5) bu pencere açılır.

```
┌────────────────────────────────┐
│ İşi onayla                     │
│ Ayşe K. isteğini yaptığını     │
│ söylüyor. Onaylıyor musun?     │
│                                │
│ Teşekkür notu (isteğe bağlı)   │
│ (Çok sağ ol! 🙏) (Eline sağlık👏)│
│ ┌────────────────────────────┐ │
│ │ Sınavda çok işime yaradı...│ │
│ └────────────────────────────┘ │
│ 💬 Notun herkese görünür.      │
│          ( Vazgeç ) ( Onayla ) │
└────────────────────────────────┘
```
- Amaç, iyiliği puan ya da sıralama olmadan görünür kılmak. Teşekkür bir sayıya dönüşmez, yalnızca bir yorumdur (T-02, S-01).
- Not **isteğe bağlıdır**. Boş bırakılırsa istek yine tamamlanır.
- Hazır cümleler hızlı yazmak için. Not, isteğin altında vurgulu bir yorum olarak görünür, arşivde (E10) de gösterilir.
- Not herkese açık bir yorum olduğu için uygunsuzsa şikâyet edilebilir ve öğretmen gizleyebilir.

## E14. Boş durumlar

Gösterilecek bir şey olmadığında ekran boş kalmaz. Kullanıcıya neden boş olduğu ve ne yapabileceği söylenir.

| Ekran | Ne zaman | Gösterilen | Düğme |
|-------|----------|------------|-------|
| Akış (E2) | Açık istek yok | 🌱 "Şu an açık istek yok. Bir ihtiyacın ya da okulda gördüğün bir sorun varsa ilk isteği sen aç." | ＋ İstek aç |
| Görevler (E5) | Kullanıcı hiç istek açmamış ya da üstlenmemiş | 📋 "Henüz bir işin yok. Açtığın ve üstlendiğin istekler burada görünür." | Açık isteklere bak |
| Bildirimler (E9) | Bildirim yok | 🔔 "Yeni bildirim yok. İsteğine yorum gelince ya da biri üstlenince burada göreceksin." | — |
| Arşiv (E10) | Seçilen kategoride tamamlanan istek yok | 🗂️ "Bu kategoride henüz tamamlanan istek yok. Başka bir kategoriye göz at." | — |
| Arama (E15) | Sonuç yok | E15'te | — |

- Boş ekranlar yeni bir kullanıcının ilk gördüğü şeydir. Okulda uygulama yeni açıldığında akış boş olacak, bu yüzden "ilk isteği sen aç" çağrısı önemli.
- Metinlerde suçlayıcı ya da kıyaslayan bir dil yok ("henüz kimseye yardım etmedin" gibi ifadeler kullanılmaz).

## E15. Arama sonuçları

Üst çubuktaki 🔍 düğmesiyle (bilgisayarda arama kutusuyla) açılır.

```
┌────────────────────────────────┐
│ ←  [ 🔍 hesap            ]  ✕  │
├────────────────────────────────┤
│ (Tümü) (Açık) (Tamamlanan) (Kategori▾)
├────────────────────────────────┤
│ "hesap" için 2 istek bulundu.  │
├────────────────────────────────┤
│ k/eşya · Can B. · 3 gün        │
│ [Hesap] makinesi ödünç lazım   │
│ [🔵 Yapıldı]                   │
├────────────────────────────────┤
│ k/ders · Elif S. · 2 hafta     │
│ Faiz [hesap]lama konusu...     │
│ [✅ Tamamlandı]                │
└────────────────────────────────┘
```
- Arama **yalnızca isteklerin başlık ve açıklamalarında** yapılır. Yorumlarda ve kişi adlarında arama yapılmaz.
- **Kişi aranamaz.** Bir öğrencinin adını yazıp bütün isteklerini ve yaptığı işleri listelemek mümkün olsaydı, bu bir kişi profili ve gizli bir sıralama oluştururdu (T-02). Ayrıca asgari veri ilkesinin ruhuna aykırı olurdu (T-03).
- Gizlenen istekler arama sonuçlarında çıkmaz.
- Eşleşen kelime turuncu arka planla vurgulanır. Sonuç yoksa "farklı bir kelime dene ya da yeni bir istek aç" önerilir (E14).

## E16 ve D5. Görevli girişi

Öğretmen ve yönetici hesapları ayrı bir giriş ekranından, **üç bilgiyle birlikte** giriş yapar: **kullanıcı adı + şifre + okul kelimesi** (Ö-07). Okul kelimesi, öğretmenlerin ve yöneticilerin aralarında belirlediği ortak bir kelimedir. Amaç, bir öğretmenin kullanıcı adını ve şifresini öğrenen bir öğrencinin, kelimeyi bilmediği için o hesapla giriş yapamaması.

```
  Öğrenci girişi (E1)              Görevli girişi (E16)
┌──────────────────────┐        ┌──────────────────────────┐
│ Kullanıcı adı        │        │ 🛡 ÖĞRETMEN / YÖNETİCİ   │
│ Şifre                │        │ Kullanıcı adı            │
│ ( Giriş yap )        │        │ Şifre                    │
│                      │        │ Okul kelimesi            │
│ 🛡 Öğretmen /        │  ──▶   │ ✕ Bilgiler hatalı.       │
│   yönetici girişi →  │        │   2 deneme hakkın kaldı. │
└──────────────────────┘        │ ( Giriş yap )            │
                                │ ← Öğrenci girişine dön   │
                                └──────────────────────────┘
```
**Nasıl çalışır?**
1. Öğrenciler E1'de kullanıcı adı ve şifreyle girer.
2. Öğretmen ve yöneticiler E1'deki **"Öğretmen / yönetici girişi"** bağlantısıyla E16'yı açar ve üç bilgiyi birlikte girer.
3. **Öğretmen ya da yönetici hesabıyla E1'den giriş yapılamaz.** Sunucu bu hesapları yalnızca okul kelimesiyle birlikte kabul eder. Öğretmenin kullanıcı adını ve şifresini bilen biri öğrenci ekranından da giremez.
4. Üç bilgiden biri bile yanlışsa yalnızca **"Bilgiler hatalı"** denir. **Hangisinin yanlış olduğu söylenmez.** Böylece öğretmenin şifresini bilen bir öğrenci "şifre doğruymuş, yalnızca kelime yanlışmış" diye bir ipucu alamaz.
5. Bütün kontroller sunucuda yapılır (T-07). Kelime doğru girilmeden hiçbir öğretmen sayfası açılmaz, adres elle yazılsa bile.

**Güvenlik önlemleri**
- **3 yanlış denemede** hesap **15 dakika** kilitlenir ve yöneticiye bildirim gider. Böylece kelime tahmin edilerek bulunamaz. (Sayılar örnektir, sistem ayarlarından değiştirilebilir.)
- Kelime veritabanında düz metin olarak değil, şifreler gibi **geri çevrilemez bir özet** olarak saklanır (`veri.md`).
- Kelimeyi yalnızca yönetici, sistem ayarlarından **değiştirebilir**. Örneğin her dönem başında ya da bir öğrencinin kelimeyi öğrendiğinden şüphelenildiğinde.

**Sınırı:** Okul kelimesi bütün öğretmenlerin paylaştığı tek bir kelimedir. Bir öğrenci kelimeyi bir kez duyarsa bütün öğretmen hesapları için işe yarar. Daha güçlü bir seçenek, her öğretmenin telefonundaki bir uygulamanın ürettiği **kişisel doğrulama kodu** (iki adımlı doğrulama, TOTP) olurdu. Hangisinin kullanılacağı açık bir karar (S-10).

## E17 ve D6. Yönetici paneli

Yönetici görevli girişinden (E16) girince bu panel açılır. Yönetici istek açmaz ya da üstlenmez, yalnızca hesap ve sistem işleriyle ilgilenir (`roller.md`).

```
┌───────────────┬──────────────────────────────────────────────────────────────┐
│ YÖNETİCİ      │ Hesaplar        [🔍 Ad ya da kullanıcı adı] (⇪ Toplu) (＋ Hesap aç)│
│ 👥 Hesaplar   │ 🔒 ogretmen1 hesabı kilitli: 3 yanlış deneme.   Kilidi aç    │
│ ⚙ Sistem      │ (Tümü 452) (Öğrenci) (Öğretmen) (Yönetici) (Kapalı)          │
│   ayarları    │ ┌──────────────────────────────────────────────────────────┐ │
│ 📊 Yönetim    │ │ Görünen ad     Kullanıcı adı  Rol       Durum            │ │
│   özeti       │ │ Selin Öğretmen ogretmen1      Öğretmen  Kilitli  Kilidi aç│ │
│               │ │ Ayşe K.        ogrenci2       Öğrenci   Aktif  Şifre sıfırla│ │
│               │ │ Deniz Y.       ogrenci58      Öğrenci   Kapalı  Yeniden aç│ │
│               │ └──────────────────────────────────────────────────────────┘ │
└───────────────┴──────────────────────────────────────────────────────────────┘
```

**Yönetici neler yapabilir?**

| İşlem | Açıklama |
|-------|----------|
| Hesap açmak | Kullanıcı adı, görünen ad ve rol girilir. Sistem geçici bir şifre üretir, kullanıcı ilk girişte değiştirir. E-posta ya da telefon istenmez (V-03) |
| Toplu hesap açmak | Dönem başında bir listeden (CSV) çok sayıda hesap açmak için. **Listede yalnızca kullanıcı adı, görünen ad ve rol sütunları kabul edilir.** TC no, numara, sınıf gibi sütunlar varsa yüklenmez (T-03) |
| Şifre sıfırlamak | Şifreler hiçbir zaman görünmez, yalnızca yeni geçici şifre üretilir |
| Kilidi açmak | Görevli girişinde 3 yanlış denemeyle kilitlenen hesabın kilidini 15 dakika dolmadan açmak için (E16) |
| Hesabı kapatmak / yeniden açmak | Okuldan ayrılan ya da mezun olan birinin hesabı silinmeden kapatılır (`aktif` alanı). Kapalı hesaplar ne kadar süre tutulacak, S-04'e bağlı |
| Rolü değiştirmek | `⋯` menüsünden. Örneğin yeni gelen bir öğretmene öğretmen rolü vermek |

**Bilerek olmayanlar**
- Hesap listesinde **kimin kaç istek açtığı ya da kaç iyilik yaptığı yoktur** (T-02). Yönetici kişilerin uygulamadaki etkinliğini görmez, yalnızca hesap işlerini yapar.
- "Son giriş zamanı" sütunu yok. Bu bilgi hiçbir işe gerekmiyor ve kimin ne zaman uygulamaya girdiğini izlemeye dönüşebilir.
- Demoda bu panelin yerini Django'nun yönetim paneli tutacak.

## E18 ve D7. Sistem ayarları

Yönetici, bazı kuralları kod değiştirmeden açıp kapatabilir (Ö-08). En büyük faydası şu: Hocalarla konuştuğumuz **açık kararların çoğu birer ayar hâline geliyor.** Hocalar "öğretmen onayı olsun" ya da "aşağı oy olmasın" derse yönetici bunu tek bir anahtarla ayarlar.

| Grup | Ayar | Varsayılan | Bağlı karar |
|------|------|-----------|-------------|
| Güvenlik | Okul kelimesini değiştir | — | Ö-07, S-10 |
| Güvenlik | Yanlış deneme sınırı | 3 | E16 |
| Güvenlik | Kilit süresi | 15 dakika | E16 |
| İstekler | İstekler öğretmen onayıyla yayına girsin | Kapalı | V-07 |
| İstekler | Onay bekleyen işi öğretmene bildir (gün) | Boş | S-03 |
| İstekler | Yeni istek açmayı durdur (tatil, bakım) | Kapalı | — |
| Etkileşim | Oylama | Açık | S-08 |
| Etkileşim | Aşağı oy | **Kilitli** | S-08 |
| Etkileşim | Resim ekleme / video ekleme | **Kilitli** | S-09 |
| Etkileşim | Yorumlara yanıt | Açık | V-11 |
| Etkileşim | Onaylarken teşekkür notu | Açık | E13 |
| Etkileşim | Tanıtım bekleme süresi | 5 saniye | E12 |
| Kategoriler | Kategori ekle / kaldır | ders, eşya, okul | Soru 8 |

**Kilitli ayarlar (turuncu etiketli):** Aşağı oy ve resim/video ekleme değişmez ilkelerle çelişebileceği için (S-08, S-09), Özgür Hoca ve hocaların kararı gelene kadar ayarlardan açılamaz. Karar gelince kilit kaldırılır. Ekran çizimlerinde aşağı oy (`▲ ▼`) tasarımcının tercihi olarak gösteriliyor, ama gerçek uygulamada bu ayar karar gelene kadar kapalı kalır.

**Değişmez ilkeler ayarlarda yoktur, yalnızca kilitli olarak gösterilir:** özel mesaj (T-01), sıralama tablosu ve kişi başına sayı (T-02), TC no, telefon, profil fotoğrafı, konum ve doğum tarihi (T-03). Bunlar projenin baştan verilmiş kararlarıdır. Bir anahtarla açılabilselerdi ilke olmaktan çıkarlardı. Değişmeleri ancak okul idaresinin kararı ve kod değişikliğiyle olabilir.

**Değişiklik geçmişi:** Her ayar değişikliği kimin, ne zaman, neyi neye çevirdiğiyle birlikte kaydedilir (`veri.md`). Böylece "aşağı oyu kim açtı?" gibi soruların cevabı bellidir.

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
