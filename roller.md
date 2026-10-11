# Roller

> **Durum: TASLAK.** Yasemin Hoca ve Eyüp Hoca ile henüz görüşemediğim için bu taslağı görev tanımına dayanarak yazdım. Görev tanımında olmayan her karar **V-xx** numaralı bir varsayımdır. Görüşmede her birini tek tek soracağım. Onaylanan varsayım `talepler.md`'ye talep olarak geçer, reddedilen varsayım burada düzeltilir.

## Roller

| Rol | Kim | Neden bu rol var |
|-----|-----|------------------|
| **Öğrenci** | Okulun öğrencileri | İstek açan ve karşılayan asıl kullanıcılar |
| **Öğretmen** | Okulun öğretmenleri | Hem istek açıp karşılayabilir, hem de uygunsuz içeriğe müdahale eder (V-02) |
| **Yönetici** | Okul idaresinden ya da bilişim öğretmenlerinden belirlenen kişi | Hesapları açar ve kapatır. Kimsenin kendi kendine kayıt olmadığı bir sistemde bu rol gereklidir (V-03) |

**Varsayımlar**
- **V-01:** Öğrenciler hem istek açabilir hem de karşılayabilir. (Hocalara soru 2)
- **V-02:** Uygunsuz içeriğe öğretmenler müdahale eder. Ayrı bir "moderatör" rolü yok. (Soru 13)
- **V-03:** Herkes kendi kendine kayıt olamaz, hesapları yönetici açar. Böylece okul dışından kimse giremez ve e-posta adresi tutmamıza gerek kalmaz. (Soru 3)
- **V-04:** Veliler ve okul personeli bu sürümde kullanıcı değil. (Soru 1)

## Rol × eylem tablosu

✅ yapabilir · ❌ yapamaz · 🔸 yalnızca belirtilen koşulda yapabilir

| Eylem | Öğrenci | Öğretmen | Yönetici | Not |
|-------|:-------:|:--------:|:--------:|-----|
| Giriş yapmak | ✅ | ✅ | ✅ | |
| Açık istekleri görmek | ✅ | ✅ | ✅ | |
| Arşivi (tamamlanan istekleri) görmek | ✅ | ✅ | ✅ | Kişiye göre filtrelenemez (T-02) |
| İstek açmak | ✅ | ✅ | ❌ | V-01. Yönetici yalnızca hesap işleriyle ilgilenir |
| İsteği üstlenmek | 🔸 | 🔸 | ❌ | Kendi açtığı isteği üstlenemez. Yalnızca durumu **Açık** olan istek üstlenilebilir |
| Üstlendiği işi bırakmak | 🔸 | 🔸 | ❌ | Yalnızca o işi üstlenen kişi bırakabilir |
| "Yapıldı" demek | 🔸 | 🔸 | ❌ | Yalnızca o işi üstlenen kişi diyebilir |
| Yapılan işi onaylamak | 🔸 | 🔸 | ❌ | Yalnızca isteği açan kişi onaylayabilir (V-05) |
| "Yapılmadı" diye geri çevirmek | 🔸 | 🔸 | ❌ | Yalnızca isteği açan kişi, gerekçe yazarak |
| Kendi isteğini geri çekmek | 🔸 | 🔸 | ❌ | Yalnızca durum **Açık** iken (V-06) |
| Yorum yazmak | ✅ | ✅ | ❌ | Herkese açık. Özel mesaj yok (T-01) |
| Yoruma yanıt vermek | ✅ | ✅ | ❌ | Tek seviye, yanıta yanıt verilemez (V-11) |
| İsteğe oy vermek | 🔸 | 🔸 | ❌ | **Açık karar (S-08).** Kabul edilirse: kendi isteğine oy veremez, aynı isteğe bir kez oy verir, kimin oy verdiği görünmez |
| İsteği ya da yorumu şikâyet etmek | 🔸 | 🔸 | ❌ | Kendi içeriğini şikâyet edemez, aynı içeriği bir kez şikâyet eder. Kimin şikâyet ettiğini içeriği yazan görmez, öğretmen görür (V-13) |
| Yönetim özetini görmek | ❌ | ✅ | ✅ | Yalnızca toplam sayılar, kişi bazında bilgi yok (V-12) |
| İsteği ya da yorumu gizlemek | ❌ | ✅ | ❌ | Gerekçe yazmak zorunlu (V-02) |
| Gizlenen içeriği geri açmak | ❌ | ✅ | ❌ | |
| Kontrol sayfasını görmek, şikâyeti "sorun yok" diye kapatmak | ❌ | ✅ | ❌ | `ekranlar.md` D4 |
| Hesap açmak ya da kapatmak | ❌ | ❌ | ✅ | V-03 |
| Kimin kaç iyilik yaptığını gösteren bir liste görmek | ❌ | ❌ | ❌ | Sıralama tablosu yok (T-02). Bu liste kimseye gösterilmez |

- **V-05:** Onayı isteği açan kişi verir, öğretmen vermez. (Soru 9)
- **V-13:** Şikâyet edenin kimliğini içeriği yazan kişi görmez, öğretmen görür. (Soru 15)
- **V-14:** Şikâyet içeriği otomatik olarak gizlemez, kararı öğretmen verir. (Soru 13, 15)
- **V-12:** Yönetim özetini öğretmenler ve yönetici görür, öğrenciler görmez. (Hocalara sorulacak)
- **V-06:** Üstlenilmiş bir isteği açan kişi tek başına geri çekemez. Önce üstlenen kişiyle yorumlarda konuşulur. (Soru 11)

## Yetki nerede kontrol edilir?

Tablodaki her kural **sunucuda** (Django'da) kontrol edilir (T-07). Ekrandaki düğmeleri gizlemek yalnızca kolaylık içindir. Biri adresi elle değiştirip, örneğin `/istek/5/onayla` adresine giderek başkasının isteğini onaylamaya çalışırsa, sunucu isteği reddeder (403). Bu kural demoda test edilecek.

## Demoda hangi roller olacak?

Demoda **öğrenci** ve **öğretmen** rolleri olacak. Yönetici işlerini Django'nun yönetim paneli karşılar. Örnek kullanıcılar: `ogrenci1`, `ogrenci2`, `ogretmen1`. Hepsi uydurma isimlerdir, gerçek öğrenci verisi yoktur (T-04).
