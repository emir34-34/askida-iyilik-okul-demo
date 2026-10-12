# Sunum Planı: Eyüp Hoca'ya gösterim

> Özgür Hoca'nın geri bildirimi (T-11): Önce sadeleştir, sonra Eyüp Hoca'ya git, tasarımı göster, danış. Görüşmenin amacı **Eyüp Hoca'nın taleplerini almak**. Sonunda [görüşme formu](gorusme-formu.html) doldurulmuş olmalı.

## Akış (yaklaşık 15 dakika)

| Süre | Ne | Söyleyeceğin |
|------|----|--------------|
| 1 dk | Amaç | "Özgür Hoca'nın önerisiyle tasarımı sadeleştirdim. Size göstermek ve ne istediğinizi öğrenmek istiyorum." |
| 3 dk | Akış | `akis.md`'deki şemayı göster: **Sorunu bildir → Biri üstlensin → Yapıldı desin → Bildiren onaylasın.** "Askıya yalnızca okulda görülen sorunlar konuyor: bozuk kapı, damlayan musluk, biten sabun." |
| 3 dk | Ekranlar | [Ekran taslakları](https://emir34-34.github.io/askida-iyilik-okul-demo/ekran-taslaklari/) sayfasındaki beş ekran |
| 3 dk | Demo (isteğe bağlı) | Aşağıdaki kısa senaryo |
| 5 dk | Form | Önce 1. bölümdeki soruları sor, en önemlisi: **"Bozuk kapı gibi sorunları kim üstlenir?"** |

## Kısa demo senaryosu

Laptopta sunucuyu başlat (`cd demo && source .venv/bin/activate && python manage.py runserver`), tarayıcıda `http://localhost:8000` aç. İkinci kullanıcı için gizli pencere kullan.

1. **Zeynep** (`ogrenci4`) olarak gir, **Sorun bildir**: "3. kat koridor lambası yanmıyor".
2. Gizli pencerede **Ayşe** (`ogrenci2`) olarak gir, sorunu aç, **Üstlen**, sonra **Yapıldı**.
3. Zeynep'in penceresinde sayfayı yenile, **Onayla**. Sorun tamamlandı.

Şifre: `demo/.env` dosyasındaki `DEMO_SIFRE`.

## Hocanın sorabileceği sorular

| Soru | Cevabın özü (kendi cümlelerinle) |
|------|----------------------------------|
| İki kişi aynı sorunu aynı anda üstlenirse? | Yalnızca biri alır. Sunucu "hâlâ açıksa üstlen" diye tek adımda kontrol ediyor. Bunun testi var. |
| Başkasının bildirdiği sorunu biri onaylayabilir mi? | Hayır. Kurallar sunucuda kontrol ediliyor, adresi elle yazsa bile reddediliyor. |
| Hangi bilgiler tutuluyor? | Kullanıcı adı, görünen ad (Ayşe K.), rol ve şifrenin geri çevrilemez özeti. TC no, telefon, fotoğraf, konum yok. |
| Ben mezun olunca kim çalıştıracak? | Okulun sunucusunda, bir öğretmenin sorumluluğunda çalışması gerekiyor. Tek dil Python ve sade olduğu için devralmak kolay (`teknoloji.md`, Süreklilik). |

## Görüşmeden sonra

- [ ] Formdaki cevapları `talepler.md`'ye yaz (B tablosu).
- [ ] "Kim üstlenir?" cevabına göre `roller.md`'yi güncelle, sonra demoyu.
- [ ] Teslim tarihini README'ye yaz.
- [ ] 3. bölümdeki soruları Özgür Hoca'ya ilet.
