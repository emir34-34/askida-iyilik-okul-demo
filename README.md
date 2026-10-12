# Askıda İyilik — Okul Sürümü: Sistem Tasarımı ve İlk Demo

Askıda İyilik, okulda görülen sorunların (bozuk kapı, damlayan musluk, biten sabun gibi) bildirilip çözülmesini kolaylaştıran bir uygulama: biri okulda gördüğü bir sorunu bildirir, başka biri üstlenir, iş yapılınca "yapıldı" der, bildiren kişi onaylar. Bu repo, uygulamanın okul sürümünün **sistem tasarımını** ve bu akışı uçtan uca yürüten **çalışan bir ilk demoyu** içerir. Uygulamadan ne istendiğini Yasemin Hoca ve Eyüp Hoca belirler. Danışman öğretmen Özgür Girgin'dir.

> **Durum (2026-10-12):** Özgür Hoca'nın geri bildirimiyle tasarım ve demo sadeleştirildi: yalnızca **bildir → üstlen → yapıldı → onayla** akışı kaldı, istenmeyen özellikler kaldırıldı (`talepler.md`, A2 ve Kaldırılanlar). Sıradaki adım: tasarımı Eyüp Hoca'ya göstermek.

## Dosyalar

| # | Dosya | İçerik | Durum |
|---|-------|--------|-------|
| 1 | [README.md](README.md) | Özet, dosya listesi, demoyu kurma ve çalıştırma | başladı |
| 2 | [talepler.md](talepler.md) | Talepler, kimin istediği, geri okunup okunmadığı, tasarımda ve demoda nerede olduğu | başladı |
| 3 | [roller.md](roller.md) | Rol × eylem tablosu | taslak, hocalara sorulacak |
| 4 | [akis.md](akis.md) | İsteğin durumları ve geçişleri | taslak, hocalara sorulacak |
| 5 | [veri.md](veri.md) | Tutulan alanlar ve gerekçeleri, tutulmayacaklar | taslak, hocalara sorulacak |
| 6 | [ekranlar.md](ekranlar.md) | Ekran taslakları | taslak, 5 ekran |
| 7 | [senaryolar.md](senaryolar.md) | En az 4 senaryo, adım adım | taslak, 3 ve 4 aday |
| 8 | [teknoloji.md](teknoloji.md) | Firebase / Django karşılaştırması, seçim, süreklilik | karar: Django |

Yardımcı belgeler:
- [Görüşme formu](https://emir34-34.github.io/askida-iyilik-okul-demo/gorusme-formu.html): Eyüp Hoca ile görüşmede işaretlenecek, yazdırılabilir form
- [sunum-plani.md](sunum-plani.md): Eyüp Hoca'ya gösterim akışı ve demo senaryosu
- [demo-plani.md](demo-plani.md): Demonun kapsamı, testler ve telefonda test notları
- [Ekran taslakları (tarayıcıda)](https://emir34-34.github.io/askida-iyilik-okul-demo/ekran-taslaklari/): ekranlar.md'deki beş ekranın görsel hâli
- [gorusme-1-sorular.md](gorusme-1-sorular.md): İlk görüşme için hazırlanan soru listesi

## Demoyu kurma ve çalıştırma

Teknoloji: Python + Django (gerekçe `teknoloji.md` dosyasında). Demo yalnızca uydurma örnek verilerle çalışır.

**Gerekenler:** Python 3.12 ya da üstü, Git.

```bash
# 1. Repoyu indir ve demo klasörüne gir
git clone https://github.com/emir34-34/askida-iyilik-okul-demo.git
cd askida-iyilik-okul-demo/demo

# 2. Sanal ortam kur ve Django'yu yükle
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 3. Ayar dosyasını oluştur
cp .env.example .env               # Windows: copy .env.example .env
#    .env dosyasını açıp doldur:
#    DJANGO_SECRET_KEY=  -> python -c "import secrets; print(secrets.token_urlsafe(50))" çıktısı
#    DEMO_SIFRE=         -> örnek kullanıcıların şifresi, en az 8 karakter

# 4. Veritabanını kur ve örnek verileri yükle
python manage.py migrate
python manage.py ornek_veri

# 5. Testleri çalıştır (12 test, hepsi geçmeli)
python manage.py test

# 6. Sunucuyu başlat
python manage.py runserver
```

Tarayıcıda **http://localhost:8000** adresini aç. Bütün örnek kullanıcıların şifresi `.env` dosyasındaki `DEMO_SIFRE` değeridir.

| Kullanıcı adı | Kim | Rol |
|---------------|-----|-----|
| `ogrenci1`…`ogrenci5` | Mehmet A., Ayşe K., Can B., Zeynep T., Elif S. | Öğrenci |
| `ogretmen1` | Selin Öğretmen | Öğretmen |
| `yonetici1` | Kerem T. | Yönetici. Hesap işleri: **http://localhost:8000/yonetim/** |

**Senaryo 1'i demoda yürütmek** (`senaryolar.md`): `ogrenci4` (Zeynep) ile gir, "2. kat lavabo musluğu damlıyor" sorununu gör → `ogrenci2` (Ayşe) ile gir, sorunu **Üstlen**, yorum yaz, **Yapıldı** de → `ogrenci4` ile gir, **Onayla**. İki kullanıcıyı aynı anda denemek için birini gizli pencerede aç.

**Telefonda denemek:** Telefon USB ile bağlıyken (USB hata ayıklama açık) `adb reverse tcp:8000 tcp:8000` komutunu çalıştır, telefonun tarayıcısında `http://localhost:8000` adresini aç.

**Örnek veriyi sıfırlamak:** `python manage.py ornek_veri` bütün sorunları silip baştan oluşturur.

## Değişmez ilkeler (projenin baştan verilmiş kararları)

1. Özel mesaj yok. Konuşma, isteğin altındaki herkese açık yorumlarla yapılır.
2. Sıralama tablosu yok ("en çok iyilik yapan" gibi bir liste olmaz).
3. Asgari veri: TC kimlik no, telefon, fotoğraf, konum ve doğum tarihi tutulmaz.
4. Demo yalnızca örnek veriyle çalışır, gerçek öğrenci verisi kullanılmaz. Canlıya geçiş kararını okul idaresi ve MEM verir.
5. Kredi ve puan kuralları henüz kesinleşmedi. Kural icat edilmez, açık karar olarak işaretlenir.
