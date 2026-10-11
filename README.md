# Askıda İyilik — Okul Sürümü: Sistem Tasarımı ve İlk Demo

Askıda İyilik, okulda insanların birbirine yaptığı iyiliği görünür kılmak için düşünülen bir uygulama: biri bir ihtiyacını ya da okulda gördüğü bir sorunu bildirir, başka biri karşılar, bildiren kişi onaylar. Bu repo, uygulamanın okul sürümünün **sistem tasarımını** (roller, akış, veri, ekranlar, senaryolar) ve bu tasarımın en önemli akışını (isteği aç → üstlen → yapıldı → onayla) uçtan uca yürüten **çalışan bir ilk demoyu** içerir. Uygulamadan ne istendiğini Yasemin Hoca ve Eyüp Hoca belirler. Danışman öğretmen Özgür Girgin'dir.

> **Durum:** Aşama 1 — talepler toplanıyor. Demo henüz başlamadı. Görev tanımına göre demo en erken `roller.md`, `akis.md` ve `veri.md` bittikten sonra başlar.

## Dosyalar

| # | Dosya | İçerik | Durum |
|---|-------|--------|-------|
| 1 | [README.md](README.md) | Özet, dosya listesi, demoyu kurma ve çalıştırma | başladı |
| 2 | [talepler.md](talepler.md) | Talepler, kimin istediği, geri okunup okunmadığı, tasarımda ve demoda nerede olduğu | başladı |
| 3 | roller.md | Rol × eylem tablosu | — |
| 4 | akis.md | İsteğin durumları ve geçişleri | — |
| 5 | veri.md | Tutulan alanlar ve gerekçeleri, tutulmayacaklar | — |
| 6 | ekranlar.md | En az 5 ekran taslağı | — |
| 7 | senaryolar.md | En az 4 senaryo, adım adım | — |
| 8 | [teknoloji.md](teknoloji.md) | Firebase ile Django karşılaştırması ve seçimin gerekçesi | karar: Django |

Yardımcı belge: [gorusme-1-sorular.md](gorusme-1-sorular.md) — Yasemin Hoca ve Eyüp Hoca ile yapılacak ilk görüşmenin soru listesi.

## Demoyu kurma ve çalıştırma

Teknoloji: Django (gerekçe `teknoloji.md` dosyasında). Kurulum adımları demo yazılınca eklenecek.

## Değişmez ilkeler (projenin baştan verilmiş kararları)

1. Özel mesaj yok. Konuşma, isteğin altındaki herkese açık yorumlarla yapılır.
2. Sıralama tablosu yok ("en çok iyilik yapan" gibi bir liste olmaz).
3. Asgari veri: TC kimlik no, telefon, fotoğraf, konum ve doğum tarihi tutulmaz.
4. Demo yalnızca örnek veriyle çalışır, gerçek öğrenci verisi kullanılmaz. Canlıya geçiş kararını okul idaresi ve MEM verir.
5. Kredi ve puan kuralları henüz kesinleşmedi. Kural icat edilmez, açık karar olarak işaretlenir.
