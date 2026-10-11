# Teknoloji: Firebase mi, Django mu?

> **Durum:** Araştırma notları hazır, **karar henüz verilmedi.** Görev tanımına göre karar en erken `roller.md`, `akis.md` ve `veri.md` bittikten sonra verilir. Bu tasarım dosyaları hangi kuralların sunucuda uygulanması gerektiğini gösterecek, karşılaştırmanın en önemli girdisi de bu olacak.
> Araştırma tarihi: 2026-10-11. Fiyatlar ve sınırlar değişebilir, karar vermeden önce resmî sayfalardan yeniden kontrol edilmeli.

## Kısaca iki seçenek

- **Firebase (Google):** Sunucu yazmayız. Uygulama tarayıcıda çalışan bir web sayfasıdır. Veri Google'ın veritabanında (Firestore) durur, giriş Firebase Authentication ile yapılır. "Kim neyi yapabilir" kuralları **Security Rules** adlı kural dosyasıyla Google'ın sunucusunda uygulanır.
- **Django (Python):** Kendi sunucu uygulamamızı yazarız. Giriş, kullanıcı grupları, veritabanı ve hazır bir yönetim paneli Django'nun içinde gelir. Kurallar Python kodunda, sunucuda kontrol edilir. Uygulamayı çalıştırmak için bir sunucu gerekir.

## Karşılaştırma

| Soru | Firebase | Django |
|------|----------|--------|
| **Kurulum** | Google hesabıyla bir proje açılır, Auth ve Firestore etkinleştirilir. Sayfa GitHub Pages'e konur. Yerelde test etmek için Firebase CLI ve emülatör kurulur, bunun için **Node.js ve Java** gerekir. | `pip install django`, ardından `startproject`, `migrate`, `runserver`. Python ile yerelde birkaç dakikada çalışır. İnternette yayınlamak ayrı bir adımdır (sunucu ya da PythonAnywhere gibi bir hizmet). |
| **Giriş ve roller** | Giriş hazır gelir (e-posta/şifre ya da Google). Roller kullanıcı belgesinde ya da "custom claims" ile tutulur. Kurallar **sunucuda** (Security Rules) uygulanır. Ancak kural dili ayrı bir dildir ve karmaşık akışları onunla yazmak zordur. Custom claims atamak için Admin SDK, yani yine bir sunucu ortamı gerekir. | Kullanıcı, grup ve izin sistemi hazır gelir. Kurallar Python'da, her işlemde **sunucuda** kontrol edilir. Hazır **yönetim paneli** sayesinde öğretmenler uygunsuz içeriği kod yazmadan kaldırabilir. |
| **Aynı işi iki kişi üstlenirse** | Firestore **transaction** ile durum okunur ve değiştirilir. Security Rules da "yalnızca durumu `açık` olan istek üstlenilebilir" kuralını sunucuda zorunlu kılar. | Tek bir koşullu güncelleme yeter: `İstek.filter(id=…, durum='acik').update(durum='ustlenildi', ustlenen=…)`. Veritabanı bunu atomik yapar, ikinci kişide sonuç 0 satır döner. |
| **Testler** | Kural testleri `@firebase/rules-unit-testing` ve emülatörle JavaScript'te yazılır (Node.js ve Java gerekir). | Django'nun kendi test sistemi var (`python manage.py test`). Testler de Python'da yazılır, ek kurulum gerekmez. |
| **Veri nerede?** | Google'ın seçtiğimiz bölgesinde. **Türkiye'de Firestore bölgesi yok.** En yakın seçenekler Avrupa'da: Belçika (europe-west1), Frankfurt (europe-west3), Varşova (europe-central2). Google, Kasım 2025'te Turkcell ile birlikte bir Türkiye bölgesi kuracağını duyurdu, ama araştırma tarihinde açılmış görünmüyor. | Uygulama nerede çalışıyorsa veri de orada durur. **Okulun kendi sunucusunda ya da Türkiye'deki bir sağlayıcıda çalıştırılabilir.** Ücretsiz demo seçeneği PythonAnywhere ise ABD ya da AB'de. |
| **Maliyet** | Ücretsiz Spark planı: günde 50.000 okuma ve 20.000 yazma. Bir okulun demosu için fazlasıyla yeter. **Cloud Functions (sunucu kodu) ücretli Blaze planı gerektirir,** bu yüzden demonun tüm mantığı Security Rules'a sığmalı. Ücretsiz kota aşılırsa o ay o ürün durur, ücret çıkmaz. | Django ücretsizdir, para sunucuya ödenir. PythonAnywhere'in ücretsiz planı (1 web uygulaması, 512 MB disk) demo için yeter, ama uygulamanın her ay elle uzatılması gerekir. Okul sunucusu kullanılırsa ek maliyet yok. |
| **Bakım** | Sunucu bakımı yok, Google yapar. Ama projeyi bir Google hesabı "sahiplenir". Ben okuldan ayrılınca hesabın kime devredileceği belli olmalı. Kural dosyasını anlayacak biri gerekir. | Sunucunun güncellemelerini birinin yapması gerekir (Python, Django güvenlik yamaları). Okulda bilişim öğretmeni ya da sonraki öğrenciler Python biliyorsa bakması kolaydır. |
| **Telefonda kullanım** | Web sayfası olduğu için telefon tarayıcısında açılır. Mobil uyumlu tasarlanmalıdır. | Sunucunun ürettiği sayfalar telefon tarayıcısında açılır. Mobil uyumlu tasarlanmalıdır. |
| **GitHub Pages ile uyumu** | **Demo doğrudan GitHub Pages'te açılabilir.** Sayfa statiktir, veri Firebase'de durur. | **Django GitHub Pages'te çalışmaz.** Pages yalnızca tasarım belgelerini gösterir, demo başka bir adreste çalışır. |

## Görev tanımının kabul ölçütleri açısından

| Ölçüt | Firebase | Django |
|-------|----------|--------|
| Yetki kontrolü sunucu tarafında | Security Rules ile ✅ (kuralların doğru yazılması kritik) | View'larda kontrol ✅ |
| Aynı iş iki kişi tarafından üstlenilemez | Transaction ve kural ✅ | Koşullu güncelleme ✅ |
| En az 3 gerçek test | Emülatörle ✅ (Node.js ve Java gerekir) | Yerleşik test sistemiyle ✅ |
| README'den başkası kurabilsin | Firebase projesi ve yapılandırma gerekir | Python ve `pip install` yeter |
| Sırlar repoda olmasın | Web yapılandırma anahtarı gizli değildir, sayfada görünmesi normaldir. Güvenliği kurallar sağlar. Servis hesabı dosyası asla repoya girmez. | `SECRET_KEY` `.env` dosyasında tutulur |

## Bilgisayarımdaki durum
- Python 3 kurulu.
- Node.js kurulu değil. Firebase seçilirse emülatör için Node.js ve Java kurulmalı.

## Seçimim ve gerekçem

_Bu bölümü ben (Emir) kendi cümlelerimle yazacağım. Görev tanımına göre "yapay zekâ önerdi" bir gerekçe değil._

Karar verirken kendime soracağım sorular:
1. Hocaların taleplerinde öğretmen onayı ya da moderasyon gibi karmaşık kurallar var mı? Varsa bunları Security Rules ile yazmak mı, Python ile yazmak mı bana daha kolay?
2. Demoyu sunumda nereden açacağım? GitHub Pages linki mi, başka bir adres mi?
3. Verinin Türkiye'de durması ileride okul için ne kadar önemli? (Demo örnek veriyle çalıştığı için şimdilik sorun yok, ama tasarımda bunu nasıl anlatacağım?)
4. Ben okuldan ayrıldıktan sonra uygulamayı okulda kim yönetecek?
5. Testleri hangi dilde yazmak bana daha kolay?

## Sınırlar
_Seçtiğim teknolojinin sınırları karardan sonra yazılacak._

## Kaynaklar
- Firestore bölgeleri: https://firebase.google.com/docs/firestore/locations
- Firebase fiyat planları: https://firebase.google.com/docs/projects/billing/firebase-pricing-plans
- Firebase Emulator kurulumu: https://firebase.google.com/docs/emulator-suite/install_and_configure
- Google Cloud Türkiye bölgesi duyurusu: https://www.datacenterdynamics.com/en/news/google-and-turkcell-team-up-for-cloud-region-and-data-center-in-türkiye/
- PythonAnywhere ücretsiz hesap: https://help.pythonanywhere.com/pages/FreeAccountsFeatures/
- Django belgeleri: https://docs.djangoproject.com/
