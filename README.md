# Askıda İyilik — Okul Sürümü: Sistem Tasarımı ve İlk Demo

Askıda İyilik, okulda insanların birbirine yaptığı iyiliği görünür kılmak için düşünülen bir uygulama: biri bir ihtiyacını ya da okulda gördüğü bir sorunu bildirir, başka biri karşılar, bildiren kişi onaylar. Bu repo, uygulamanın okul sürümünün **sistem tasarımını** (roller, akış, veri, ekranlar, senaryolar) ve bu tasarımın en önemli akışını (isteği aç → üstlen → yapıldı → onayla) uçtan uca yürüten **çalışan bir ilk demoyu** içerir. Uygulamadan ne istendiğini Yasemin Hoca ve Eyüp Hoca belirler. Danışman öğretmen Özgür Girgin'dir.

> **Durum:** Aşama 1 — talepler toplanıyor. Demo henüz başlamadı. Görev tanımına göre demo en erken `roller.md`, `akis.md` ve `veri.md` bittikten sonra başlar.

## Dosyalar

| # | Dosya | İçerik | Durum |
|---|-------|--------|-------|
| 1 | [README.md](README.md) | Özet, dosya listesi, demoyu kurma ve çalıştırma | başladı |
| 2 | [talepler.md](talepler.md) | Talepler, kimin istediği, geri okunup okunmadığı, tasarımda ve demoda nerede olduğu | başladı |
| 3 | [roller.md](roller.md) | Rol × eylem tablosu | taslak, hocalara sorulacak |
| 4 | [akis.md](akis.md) | İsteğin durumları ve geçişleri | taslak, hocalara sorulacak |
| 5 | [veri.md](veri.md) | Tutulan alanlar ve gerekçeleri, tutulmayacaklar | taslak, hocalara sorulacak |
| 6 | [ekranlar.md](ekranlar.md) | En az 5 ekran taslağı | taslak, 7 ekran |
| 7 | [senaryolar.md](senaryolar.md) | En az 4 senaryo, adım adım | taslak, 3 ve 4 aday |
| 8 | [teknoloji.md](teknoloji.md) | Firebase ile Django karşılaştırması ve seçimin gerekçesi | karar: Django |

Yardımcı belgeler:
- [gorusme-1-sorular.md](gorusme-1-sorular.md): Yasemin Hoca ve Eyüp Hoca ile yapılacak ilk görüşmenin soru listesi
- [demo-plani.md](demo-plani.md): Demoya başlamadan önce yazılan plan: neyin olacağı, testler, sıra
- [Ekran taslakları (tarayıcıda)](https://emir34-34.github.io/askida-iyilik-okul-demo/ekran-taslaklari/): ekranlar.md'deki ekranların görsel hâli, demo değil

## Demoyu kurma ve çalıştırma

Teknoloji: Django (gerekçe `teknoloji.md` dosyasında). Kurulum adımları demo yazılınca eklenecek.

## Değişmez ilkeler (projenin baştan verilmiş kararları)

1. Özel mesaj yok. Konuşma, isteğin altındaki herkese açık yorumlarla yapılır.
2. Sıralama tablosu yok ("en çok iyilik yapan" gibi bir liste olmaz).
3. Asgari veri: TC kimlik no, telefon, fotoğraf, konum ve doğum tarihi tutulmaz.
4. Demo yalnızca örnek veriyle çalışır, gerçek öğrenci verisi kullanılmaz. Canlıya geçiş kararını okul idaresi ve MEM verir.
5. Kredi ve puan kuralları henüz kesinleşmedi. Kural icat edilmez, açık karar olarak işaretlenir.
