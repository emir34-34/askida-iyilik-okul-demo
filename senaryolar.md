# Senaryolar

> **Durum: TASLAK.** Senaryo 1 ve 2 görev tanımına göre zorunludur. Senaryo 3 ve 4 **aday**: görev tanımı bunları hocaların anlattığı durumlardan seçmemi istiyor (S-07).
> Bütün isimler uydurmadır, kullanıcı adları demodaki örnek kullanıcılarla aynıdır.

**Kişiler:** Zeynep T. (`ogrenci4`), Ayşe K. (`ogrenci2`), Can B. (`ogrenci3`), Mehmet A. (`ogrenci1`)

## Senaryo 1: Sorun bildirilir, biri üstlenir, bildiren onaylar
**Zorunlu · demoda birebir yürütülen senaryo**

| Adım | Kim | Ne yapar | Ekran | Sonuç |
|------|-----|----------|-------|-------|
| 1 | Zeynep | Giriş yapar, **Sorun bildir**'e basar, "2. kat lavabo musluğu damlıyor" yazıp bildirir | E1, E3 | Sorun **Açık** (G1) |
| 2 | Ayşe | Giriş yapar, listede sorunu görür ve açar | E2, E4 | **Üstlen** düğmesini görür. Zeynep kendi sorununda bu düğmeyi görmez |
| 3 | Ayşe | **Üstlen**'e basar, "Hademe ablaya haber verdim." yorumunu yazar | E4 | **Üstlenildi** (G2), yorumu herkes görür |
| 4 | Ayşe | Musluk tamir edilince **Yapıldı**'ya basar | E4 | **Yapıldı** (G4) |
| 5 | Zeynep | **Benim işlerim**'de "Onayını bekliyor" uyarısını görür, sorunu açıp **Onayla**'ya basar | E5, E4 | **Tamamlandı** (G5) |

## Senaryo 2: Üstlenen kişi işi yapamayacağını fark eder
**Zorunlu**

| Adım | Kim | Ne yapar | Ekran | Sonuç |
|------|-----|----------|-------|-------|
| 1 | Can | "Spor salonu kapısının kolu kırık" sorununu bildirir | E3 | **Açık** |
| 2 | Mehmet | Sorunu üstlenir | E4 | **Üstlenildi**, üstlenen Mehmet |
| 3 | Mehmet | Kolu kendisinin değiştiremeyeceğini fark eder, "Bunu ben yapamam, bir öğretmene haber vermek lazım." yorumunu yazar | E4 | |
| 4 | Mehmet | **Bırak**'a basar | E4 | Sorun yeniden **Açık** (G3) |
| 5 | Ayşe | Sorunu listede yeniden açık görür ve üstlenir | E2, E4 | **Üstlenildi**, üstlenen Ayşe |

## Senaryo 3 (aday): İki kişi aynı sorunu aynı anda üstlenmeye çalışır

| Adım | Kim | Ne yapar | Sonuç |
|------|-----|----------|-------|
| 1 | Ayşe ve Mehmet | İkisi de "Kantin lavabosunda sabun bitti" sorununu açık olarak görür | Düğme ikisinde de görünür |
| 2 | Ayşe ve Mehmet | İkisi aynı anda **Üstlen**'e basar | Yalnızca ilk gelen alır |
| 3 | Mehmet | "Bu sorun az önce başka biri tarafından üstlenildi." mesajını görür | Sorun Ayşe'de kalır (akis.md, soru 1) |

## Senaryo 4 (aday): Bildiren kişi onay vermez

| Adım | Kim | Ne yapar | Sonuç |
|------|-----|----------|-------|
| 1 | Ayşe | Zeynep'in bildirdiği sorunu üstlenir ve **Yapıldı** der | **Yapıldı** |
| 2 | Zeynep | Onay vermeyi unutur | Sorun **Yapıldı**'da bekler |
| 3 | — | Belli bir süre sonra ne olacağı | **Açık soru (S-03)**, hocalar karar verecek |
