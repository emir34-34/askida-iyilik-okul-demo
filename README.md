# Askıda İyilik — Okul Sürümü: Sistem Tasarımı ve İlk Demo

Askıda İyilik, okulda insanların birbirine yaptığı iyiliği görünür kılmak için düşünülen bir uygulama: biri bir ihtiyacını ya da okulda gördüğü bir sorunu bildirir, başka biri karşılar, bildiren kişi onaylar. Bu repo, uygulamanın okul sürümünün **sistem tasarımını** (roller, akış, veri, ekranlar, senaryolar) ve bu tasarımın en önemli akışını (isteği aç → üstlen → yapıldı → onayla) uçtan uca yürüten **çalışan bir ilk demoyu** içerir. Uygulamadan ne istendiğini Yasemin Hoca ve Eyüp Hoca belirler. Danışman öğretmen Özgür Girgin'dir.

> **Durum:** Tasarım dosyalarının hepsi taslak olarak hazır, hocaların varsayımları onaylaması bekleniyor. Demonun ilk dilimi çalışıyor: giriş, istek aç → üstlen → yapıldı → onayla, yorumlar ve 20 test. Arayüz istemcide (tarayıcı ve Android APK), Django yalnızca veri gönderir (`demo-plani.md`).

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
- [Görüşme formu](https://emir34-34.github.io/askida-iyilik-okul-demo/gorusme-formu.html): 12 Ekim görüşmesi için hocaların işaretleyeceği, yazdırılabilir form (bütün varsayımlar, öneriler ve açık sorular)
- [demo-plani.md](demo-plani.md): Demoya başlamadan önce yazılan plan: neyin olacağı, testler, sıra
- [Ekran taslakları (tarayıcıda)](https://emir34-34.github.io/askida-iyilik-okul-demo/ekran-taslaklari/): ekranlar.md'deki ekranların görsel hâli, demo değil

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

# 5. Testleri çalıştır (20 test, hepsi geçmeli)
python manage.py test

# 6. Sunucuyu başlat
python manage.py runserver
```

Tarayıcıda **http://localhost:8000** adresini aç. Bütün örnek kullanıcıların şifresi `.env` dosyasındaki `DEMO_SIFRE` değeridir.

| Kullanıcı adı | Kim | Rol |
|---------------|-----|-----|
| `ogrenci1` | Mehmet A. | Öğrenci |
| `ogrenci2` | Ayşe K. | Öğrenci |
| `ogrenci3` | Can B. | Öğrenci |
| `ogrenci4`, `ogrenci5` | Zeynep T., Elif S. | Öğrenci |
| `ogretmen1` | Selin Öğretmen | Öğretmen. Yönetim panelinde istek ve yorum gizleyebilir |
| `yonetici1` | Kerem T. | Yönetici. Yönetim paneli: **http://localhost:8000/yonetim/** |

**Senaryo 1'i demoda yürütmek** (`senaryolar.md`): `ogrenci1` ile gir, "Kimya notları lazım" isteğini gör → çıkış yap, `ogrenci2` ile gir, isteği **Üstlen**, yorum yaz, **Yapıldı** de → `ogrenci1` ile gir, **Onayla**. İki farklı kullanıcıyı aynı anda denemek için birini gizli pencerede aç.

**Telefonda denemek:** Telefon USB ile bağlıyken (USB hata ayıklama açık) `adb reverse tcp:8000 tcp:8000` komutunu çalıştır, telefonun tarayıcısında `http://localhost:8000` adresini aç.

**Android uygulaması (APK, ek):** `apk/` klasöründe, **tamamen native** bir Android uygulaması (Java, Android'in kendi bileşenleri, ek kütüphane yok). Sunucudan yalnızca `/api/` üzerinden veri gelir (Reddit uygulaması gibi). Tarayıcıdaki demo (`demo/istemci/`) ayrıca durur, ikisi de aynı API'yi kullanır. Kurallar yalnızca sunucuda uygulanır. Görev tanımı gereği Özgür Hoca'ya sorulacak bir ek (S-11). Derlemek için Android SDK (`platforms;android-34`, `build-tools;35.0.0`) ve JDK gerekir:

```bash
cd apk && ./derle.sh                       # çıktı: apk/build/AskidaIyilik.apk
adb install -r build/AskidaIyilik.apk      # telefona kur (USB hata ayıklama açık)
adb reverse tcp:8000 tcp:8000              # telefonun localhost'unu bilgisayardaki Django'ya yönlendir
```
Uygulama sunucuya bağlanamazsa başka bir adres sorar (ör. ev sunucusu). Adres Profil sayfasından da değiştirilebilir.

Kablosuz bağlanmak için (telefonun USB portu yalnızca şarj alıyorsa): Telefonda Geliştirici seçenekleri → Kablosuz hata ayıklama → "Eşleştirme koduyla eşle", sonra bilgisayarda `adb pair IP:PORT KOD` ve `adb connect IP:PORT`. Ardından `adb reverse` yine çalışır.

**Bilinen durum:** USB kablosu bir an bile çıkarsa `adb reverse` yönlendirmesi silinir ve uygulama "Sunucuya bağlanılamadı" der. Kabloyu takıp `adb reverse tcp:8000 tcp:8000` komutunu yeniden çalıştırmak yeter.

**Örnek veriyi sıfırlamak:** `python manage.py ornek_veri` komutunu yeniden çalıştırmak bütün istekleri silip baştan oluşturur.

## Değişmez ilkeler (projenin baştan verilmiş kararları)

1. Özel mesaj yok. Konuşma, isteğin altındaki herkese açık yorumlarla yapılır.
2. Sıralama tablosu yok ("en çok iyilik yapan" gibi bir liste olmaz).
3. Asgari veri: TC kimlik no, telefon, fotoğraf, konum ve doğum tarihi tutulmaz.
4. Demo yalnızca örnek veriyle çalışır, gerçek öğrenci verisi kullanılmaz. Canlıya geçiş kararını okul idaresi ve MEM verir.
5. Kredi ve puan kuralları henüz kesinleşmedi. Kural icat edilmez, açık karar olarak işaretlenir.
