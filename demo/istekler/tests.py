"""Demo testleri (görev tanımı: en az 3 test, her birinde gerçek kontrol).

Çalıştırmak için:  python manage.py test
"""
from django.test import TestCase

from . import gecisler
from .gecisler import DurumUygunDegil, YetkiYok
from .models import DurumGecmisi, Kullanici, Sorun

Durum = Sorun.Durum


class OrnekVeri(TestCase):
    """Senaryolardaki uydurma kişiler (senaryolar.md). Gerçek öğrenci verisi yok (T-04)."""

    def setUp(self):
        def kisi(ad, gorunen, rol=Kullanici.Rol.OGRENCI):
            return Kullanici.objects.create_user(username=ad, password="test-sifresi-123", gorunen_ad=gorunen, rol=rol)

        self.zeynep = kisi("ogrenci4", "Zeynep T.")
        self.ayse = kisi("ogrenci2", "Ayşe K.")
        self.mehmet = kisi("ogrenci1", "Mehmet A.")
        self.sorun = gecisler.bildir(self.zeynep, "2. kat lavabo musluğu damlıyor", "Soldan ikinci musluk.")

    def durum(self):
        self.sorun.refresh_from_db()
        return self.sorun.durum


class RolKuraliTesti(OrnekVeri):
    """roller.md: kim neyi yapabilir? Kurallar sunucuda uygulanır (T-07)."""

    def test_kendi_bildirdigi_sorunu_ustlenemez(self):
        with self.assertRaises(YetkiYok):
            gecisler.ustlen(self.sorun.pk, self.zeynep)
        self.assertEqual(self.durum(), Durum.ACIK)

    def test_yalnizca_bildiren_onaylayabilir(self):
        gecisler.ustlen(self.sorun.pk, self.ayse)
        gecisler.yapildi_de(self.sorun.pk, self.ayse)
        for yabanci in (self.mehmet, self.ayse):  # ne başka biri ne de işi yapan onaylayabilir
            with self.assertRaises(YetkiYok):
                gecisler.onayla(self.sorun.pk, yabanci)
        self.assertEqual(self.durum(), Durum.YAPILDI)

    def test_yalnizca_ustlenen_yapildi_diyebilir(self):
        gecisler.ustlen(self.sorun.pk, self.ayse)
        with self.assertRaises(YetkiYok):
            gecisler.yapildi_de(self.sorun.pk, self.mehmet)
        self.assertEqual(self.durum(), Durum.USTLENILDI)


class CiftUstlenmeTesti(OrnekVeri):
    """akis.md soru 1 / T-06: Aynı iş iki kişi tarafından üstlenilemez."""

    def test_ikinci_kisi_ustlenemez(self):
        gecisler.ustlen(self.sorun.pk, self.ayse)
        with self.assertRaisesMessage(DurumUygunDegil, "az önce başka biri tarafından üstlenildi"):
            gecisler.ustlen(self.sorun.pk, self.mehmet)
        self.sorun.refresh_from_db()
        self.assertEqual(self.sorun.ustlenen, self.ayse)  # iş ilk gelende kaldı
        self.assertEqual(DurumGecmisi.objects.filter(sorun=self.sorun, yeni_durum=Durum.USTLENILDI).count(), 1)

    def test_eski_bilgiyle_yazilamaz(self):
        """Mehmet'in ekranında sorun hâlâ "Açık" görünse bile güncelleme veritabanındaki güncel
        duruma bakar. Önce bakıp sonra yazsaydık bu test başarısız olurdu."""
        eski_kopya = Sorun.objects.get(pk=self.sorun.pk)
        self.assertEqual(eski_kopya.durum, Durum.ACIK)
        gecisler.ustlen(self.sorun.pk, self.ayse)
        with self.assertRaises(DurumUygunDegil):
            gecisler.ustlen(eski_kopya.pk, self.mehmet)
        self.assertEqual(Sorun.objects.get(pk=self.sorun.pk).ustlenen, self.ayse)


class OnayAkisiTesti(OrnekVeri):
    """Senaryo 1: bildir → üstlen → yapıldı → onayla, uçtan uca."""

    def test_senaryo_1(self):
        self.assertEqual(self.durum(), Durum.ACIK)
        gecisler.ustlen(self.sorun.pk, self.ayse)
        self.assertEqual(self.durum(), Durum.USTLENILDI)
        gecisler.yorum_yaz(self.sorun.pk, self.ayse, "Hademe ablaya haber verdim.")
        gecisler.yapildi_de(self.sorun.pk, self.ayse)
        self.assertEqual(self.durum(), Durum.YAPILDI)
        gecisler.onayla(self.sorun.pk, self.zeynep)
        self.assertEqual(self.durum(), Durum.TAMAMLANDI)

        gecmis = list(DurumGecmisi.objects.filter(sorun=self.sorun).values_list("yeni_durum", "yapan__username"))
        self.assertEqual(gecmis, [
            (Durum.ACIK, "ogrenci4"),
            (Durum.USTLENILDI, "ogrenci2"),
            (Durum.YAPILDI, "ogrenci2"),
            (Durum.TAMAMLANDI, "ogrenci4"),
        ])

    def test_tamamlanan_sorun_yeniden_onaylanamaz(self):
        gecisler.ustlen(self.sorun.pk, self.ayse)
        gecisler.yapildi_de(self.sorun.pk, self.ayse)
        gecisler.onayla(self.sorun.pk, self.zeynep)
        with self.assertRaises(DurumUygunDegil):
            gecisler.onayla(self.sorun.pk, self.zeynep)


class BirakmaTesti(OrnekVeri):
    """Senaryo 2: üstlenen kişi işi yapamayacağını fark edip bırakır."""

    def test_birakinca_sorun_yeniden_acik_olur(self):
        gecisler.ustlen(self.sorun.pk, self.mehmet)
        gecisler.birak(self.sorun.pk, self.mehmet)
        self.sorun.refresh_from_db()
        self.assertEqual(self.sorun.durum, Durum.ACIK)
        self.assertIsNone(self.sorun.ustlenen)
        gecisler.ustlen(self.sorun.pk, self.ayse)  # başkası üstlenebilir
        self.assertEqual(self.durum(), Durum.USTLENILDI)

    def test_baskasi_birakamaz(self):
        gecisler.ustlen(self.sorun.pk, self.mehmet)
        with self.assertRaises(YetkiYok):
            gecisler.birak(self.sorun.pk, self.ayse)
        self.assertEqual(self.durum(), Durum.USTLENILDI)


class SayfaYetkiTesti(OrnekVeri):
    """T-07: Yetkisiz biri adresi elle yazsa bile başkasının işlemini yapamaz."""

    def test_adresi_elle_yazan_yabanci_403_alir(self):
        gecisler.ustlen(self.sorun.pk, self.ayse)
        gecisler.yapildi_de(self.sorun.pk, self.ayse)
        self.client.force_login(self.mehmet)  # onay düğmesini hiç görmedi ama adrese doğrudan gönderiyor
        cevap = self.client.post(f"/sorun/{self.sorun.pk}/onayla/")
        self.assertEqual(cevap.status_code, 403)
        self.assertEqual(self.durum(), Durum.YAPILDI)

    def test_giris_yapmayan_giris_sayfasina_gider(self):
        cevap = self.client.post(f"/sorun/{self.sorun.pk}/ustlen/")
        self.assertEqual(cevap.status_code, 302)
        self.assertIn("/giris/", cevap["Location"])
        self.assertEqual(self.durum(), Durum.ACIK)

    def test_dugmeler_role_gore_degisir(self):
        self.client.force_login(self.ayse)
        self.assertContains(self.client.get(f"/sorun/{self.sorun.pk}/"), "Üstlen</button>")
        self.client.force_login(self.zeynep)  # kendi bildirdiği sorun: üstlen düğmesi yok
        self.assertNotContains(self.client.get(f"/sorun/{self.sorun.pk}/"), "Üstlen</button>")
