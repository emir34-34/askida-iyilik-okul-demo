# Senaryolar

> **Durum: TASLAK.** Senaryo 1 ve 2 görev tanımına göre zorunludur. Senaryo 3 ve 4 **aday senaryolardır**: görev tanımı bunları Yasemin Hoca ve Eyüp Hoca'nın anlattığı en önemli durumlardan seçmemi istiyor (Soru 21). Görüşmeden sonra değiştirilebilirler.
> Bütün isimler uydurmadır. Kullanıcı adları demodaki örnek kullanıcılarla aynıdır.

**Kişiler:** Mehmet A. (`ogrenci1`), Ayşe K. (`ogrenci2`), Can B. (`ogrenci3`), Selin Öğretmen (`ogretmen1`)

---

## Senaryo 1: İstek açılır, başka biri karşılar, istek sahibi onaylar
**Zorunlu · demoda birebir yürütülecek senaryo** (T-05)

| Adım | Kim | Ne yapar | Ekran | Sonuç ve durum |
|------|-----|----------|-------|----------------|
| 1 | Mehmet | Giriş yapar | E1 | Ana sayfa açılır |
| 2 | Mehmet | **Yeni istek** düğmesine basar, "Kimya notları lazım" yazıp yayınlar | E3 | İstek **Açık** (G1) |
| 3 | Ayşe | Giriş yapar, listede isteği görür ve açar | E2 → E4 | **Üstlen** düğmesini görür. Mehmet kendi isteğinde bu düğmeyi görmez |
| 4 | Ayşe | **Üstlen**'e basar | E4 | İstek **Üstlenildi**, üstlenen Ayşe (G2) |
| 5 | Ayşe | "Yarın teneffüste getiririm." yorumunu yazar | E4 | Yorumu herkes görür (T-01) |
| 6 | Ayşe | Notları verdikten sonra **Yapıldı**'ya basar | E4 | İstek **Yapıldı** (G4) |
| 7 | Mehmet | **Benim işlerim**'de "Onayını bekliyor" uyarısını görür | E5 | |
| 8 | Mehmet | İsteği açıp **Onayla**'ya basar | E4 | İstek **Tamamlandı** (G5), arşive geçer |

**Kontrol:** Her adımda durum geçmişine bir satır yazıldı mı? Ayşe 8. adımda **Onayla** düğmesini görmüyor mu, adresi elle yazarsa 403 alıyor mu?

## Senaryo 2: Üstlenen kişi işi yapamayacağını fark eder
**Zorunlu**

| Adım | Kim | Ne yapar | Ekran | Sonuç ve durum |
|------|-----|----------|-------|----------------|
| 1 | Mehmet | "Hesap makinesi ödünç lazım" isteğini açar | E3 | **Açık** |
| 2 | Can | İsteği üstlenir | E4 | **Üstlenildi**, üstlenen Can |
| 3 | Can | Hesap makinesini evde unuttuğunu fark eder. "Kusura bakma, bugün getiremiyorum." yorumunu yazar | E4 | |
| 4 | Can | **Bırak**'a basar | E4 | İstek yeniden **Açık**, üstlenen boşaldı (G3) |
| 5 | Ayşe | Listede isteği yeniden **Açık** olarak görür ve üstlenir | E2 → E4 | **Üstlenildi**, üstlenen Ayşe |
| 6 | Ayşe, Mehmet | Senaryo 1'in 6–8. adımları gibi devam eder | E4 | **Tamamlandı** |

**Kontrol:** Can bıraktıktan sonra **Yapıldı** diyemiyor mu? Can'ın profilinde ya da listede bırakmayı gösteren bir işaret yok mu (`akis.md`)?

## Senaryo 3 (aday): İş yapılmadı, istek sahibi geri çevirir

| Adım | Kim | Ne yapar | Ekran | Sonuç ve durum |
|------|-----|----------|-------|----------------|
| 1 | Mehmet | "Kimya notları lazım" isteğini açar, Ayşe üstlenir | E3, E4 | **Üstlenildi** |
| 2 | Ayşe | **Yapıldı**'ya basar | E4 | **Yapıldı** |
| 3 | Mehmet | Notların yarısının eksik olduğunu görür ve **Yapılmadı**'ya basar | E4 | Gerekçe kutusu açılır |
| 4 | Mehmet | Gerekçe yazmadan göndermeye çalışır | E7 | "Lütfen neyin eksik olduğunu yaz." |
| 5 | Mehmet | "Notların yarısı eksik." yazıp gönderir | E4 | İstek **Üstlenildi**, yine Ayşe'de (G6) |
| 6 | Ayşe | Eksik notları verip yeniden **Yapıldı** der, Mehmet onaylar | E4 | **Tamamlandı** |

## Senaryo 4 (aday): Uygunsuz bir istek gizlenir

| Adım | Kim | Ne yapar | Ekran | Sonuç ve durum |
|------|-----|----------|-------|----------------|
| 1 | Can | Uygunsuz bir istek yayınlar (ör. başka bir öğrenciyle alay eden bir başlık) | E3 | **Açık**, listede görünür (V-07) |
| 2 | Selin Öğretmen | İsteği görür ve **Gizle**'ye basar | E4 → E6 | Gerekçe kutusu açılır |
| 3 | Selin Öğretmen | "Arkadaşını küçük düşüren içerik." gerekçesini yazar | E6 | İstek **Gizlendi** (G8), listeden kalkar |
| 4 | Ayşe | Gizlenen isteğin adresini elle açmaya çalışır | E7 | İsteği göremez |
| 5 | Selin Öğretmen | Durum geçmişinde kimin ne zaman gizlediğini ve gerekçeyi görür | — | İçerik silinmedi, kayıt duruyor |

> Hocalar "istekler yayına girmeden önce öğretmen onaylasın" derse (V-07), bu senaryo "öğretmen isteği yayına almaz" olarak değişir.

---

## Senaryolarla ortaya çıkan açık noktalar
- Senaryo 1'in 7. adımında Mehmet onay vermeyi unutursa ne olacak? → S-03
- Senaryo 2'de aynı kişi bir isteği defalarca üstlenip bırakırsa ne olacak? Taslakta bir sınır yok. → Hocalara sorulacak (yeni soru)
