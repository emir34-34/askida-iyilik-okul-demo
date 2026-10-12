# Roller

> **Durum: TASLAK.** Hocalarla henüz görüşemediğim için görev tanımına ve Özgür Hoca'nın geri bildirimine (T-08, T-09) dayanarak yazdım. Görev tanımında olmayan her karar **V-xx** numaralı bir varsayımdır ve hocalara sorulacak (`talepler.md`).

## Roller

| Rol | Kim | Neden bu rol var |
|-----|-----|------------------|
| **Öğrenci** | Okulun öğrencileri | Okulda gördükleri sorunları bildirirler, başkasının bildirdiği sorunu üstlenebilirler |
| **Öğretmen** | Okulun öğretmenleri | Öğrencilerle aynı işleri yapar (V-01) |
| **Yönetici** | Okul idaresinden belirlenen kişi | Hesapları açar ve kapatır. Kimse kendi kendine kayıt olmadığı için gerekli (V-03) |

## Rol × eylem tablosu

✅ yapabilir · ❌ yapamaz · 🔸 yalnızca belirtilen koşulda yapabilir

| Eylem | Öğrenci | Öğretmen | Yönetici | Not |
|-------|:-------:|:--------:|:--------:|-----|
| Giriş yapmak | ✅ | ✅ | ✅ | |
| Bildirilen sorunları görmek | ✅ | ✅ | ✅ | |
| Sorun bildirmek | ✅ | ✅ | ❌ | V-01 |
| Sorunu üstlenmek | 🔸 | 🔸 | ❌ | Kendi bildirdiği sorunu üstlenemez. Yalnızca durumu **Açık** olan sorun üstlenilebilir. Kimin üstleneceği açık soru (S-14) |
| Üstlendiği işi bırakmak | 🔸 | 🔸 | ❌ | Yalnızca o işi üstlenen kişi |
| "Yapıldı" demek | 🔸 | 🔸 | ❌ | Yalnızca o işi üstlenen kişi |
| Yapılan işi onaylamak | 🔸 | 🔸 | ❌ | Yalnızca sorunu bildiren kişi (V-05) |
| Yorum yazmak | ✅ | ✅ | ❌ | Herkese açık, özel mesaj yok (T-01) |
| Hesap açmak ya da kapatmak | ❌ | ❌ | ✅ | Django'nun hazır yönetim panelinden (V-03) |
| Kimin kaç sorun çözdüğünü gösteren bir liste görmek | ❌ | ❌ | ❌ | Sıralama tablosu yok (T-02) |

Uygunsuz bir bildirime ya da yoruma kimin müdahale edeceği Eyüp Hoca'ya soruluyor (S-13).

## Yetki nerede kontrol edilir?

Tablodaki her kural **sunucuda** (Django'da) kontrol edilir (T-07). Ekranda düğmeleri gizlemek yalnızca kolaylık içindir. Biri adresi elle yazıp, örneğin `/sorun/5/onayla` adresine giderek başkasının bildirdiği sorunu onaylamaya çalışırsa sunucu reddeder (403). Bu kuralın demoda testi var.

## Demoda hangi roller var?

Öğrenci ve öğretmen. Yönetici işlerini Django'nun yönetim paneli karşılar. Örnek kullanıcılar (`ogrenci1`, `ogrenci2`…, `ogretmen1`) uydurmadır, gerçek öğrenci verisi yoktur (T-04).
