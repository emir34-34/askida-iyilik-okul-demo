# Teknoloji: Firebase mi, Django mu?

> **Durum:** Karar verildi: **Django** (2026-10-11). Gerekçe aşağıda. `roller.md`, `akis.md` ve `veri.md` bittikten sonra kararı bu dosyalara göre yeniden kontrol edeceğim. Bir çelişki çıkarsa önce burayı güncellerim.
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

**Seçimim: Django**

Firebase'in sunucuları Türkiye dışında ve verilerin yurt dışına gitmesini istemiyorum. Bunun yerine evdeki Core 2 Duo'lu bilgisayarı tamir ettirip sunucu olarak kullanacağım. Bu yüzden Django benim için daha iyi bir seçenek.

## Sınırlar

- **Evdeki sunucu yalnızca test ve demo için.** Orada da yalnızca örnek veri olacak. Gerçek öğrenci verisinin nerede duracağına okul idaresi ve MEM karar verir, ev sunucusu bunun için uygun bir yer değil.
- **Demo GitHub Pages'te çalışmaz.** Pages'te yalnızca tasarım belgeleri durur. Demo yerelde (`runserver`) ya da evdeki sunucuda çalışır.
- **Ev sunucusu eski bir bilgisayar** (Core 2 Duo, 3 GB RAM). Demo için yeterli, ama okulun tamamının kullanacağı bir sistem için değil.
- **Sunucunun bakımı benim sorumluluğumda.** Güncellemeleri ve yedekleri ben yapmalıyım.
- **Firebase'deki hazır özellikler** (bildirimler, kendiliğinden ölçeklenme) Django'da yok. Gerekirse kendim yazmam gerekir.

## Ek: Android APK kabuğu (Emir'in isteği, Özgür Hoca'ya sorulacak)

Demo bir Django web uygulamasıdır ve telefon tarayıcısında çalışır. Bunun yanında, aynı sayfaları tam ekran açan bir **Android APK kabuğu** (WebView) yapılacak. Telefonda ikonu olan bir uygulama gibi görünür, ama içinde aynı Django sayfaları çalışır. Ayrı bir uygulama yazılmaz, bütün kurallar yine Django sunucusunda uygulanır.

- **Neden:** Uygulamanın telefonda gerçek bir uygulama gibi nasıl hissettireceğini göstermek.
- **Ne gerektirir:** Android SDK ve Java (bilgisayarda kurulu).
- **2026-10-12 güncellemesi:** Arayüz dosyaları (HTML, CSS, JavaScript, yazı tipi) APK'nın içine kondu. Sunucudan yalnızca veri (JSON) gelir, Reddit uygulaması gibi. Aynı arayüz dosyaları tarayıcıda da kullanılır (`demo-plani.md`, mimari değişikliği).
- **Sınırı:** APK, Django sunucusu çalışmıyorsa veri gösteremez. Arayüz açılır, ama giriş yapılamaz. Görev tanımı yeni teknoloji için Özgür Hoca'ya sormayı istediğinden bu bir **açık soru (S-11)**. Hoca hayır derse APK demodan çıkarılır, web demosu eksiksiz kalır.

## Kaynaklar
- Firestore bölgeleri: https://firebase.google.com/docs/firestore/locations
- Firebase fiyat planları: https://firebase.google.com/docs/projects/billing/firebase-pricing-plans
- Firebase Emulator kurulumu: https://firebase.google.com/docs/emulator-suite/install_and_configure
- Google Cloud Türkiye bölgesi duyurusu: https://www.datacenterdynamics.com/en/news/google-and-turkcell-team-up-for-cloud-region-and-data-center-in-türkiye/
- PythonAnywhere ücretsiz hesap: https://help.pythonanywhere.com/pages/FreeAccountsFeatures/
- Django belgeleri: https://docs.djangoproject.com/
