"""Demo testleri (demo-plani.md, görev tanımı: en az 3 test, her birinde gerçek kontrol).

Çalıştırmak için:  python manage.py test
"""
from django.test import TestCase

from . import gecisler
from .gecisler import DurumUygunDegil, GerekceGerekli, YetkiYok
from .models import DurumGecmisi, Istek, Kullanici, Yorum

Durum = Istek.Durum


class OrnekVeri(TestCase):
    """Senaryolardaki uydurma kişiler (senaryolar.md). Gerçek öğrenci verisi yok (T-04)."""

    def setUp(self):
        def kisi(ad, gorunen, rol=Kullanici.Rol.OGRENCI):
            return Kullanici.objects.create_user(username=ad, password="test-sifresi-123", gorunen_ad=gorunen, rol=rol)

        self.mehmet = kisi("ogrenci1", "Mehmet A.")
        self.ayse = kisi("ogrenci2", "Ayşe K.")
        self.can = kisi("ogrenci3", "Can B.")
        self.selin = kisi("ogretmen1", "Selin Öğretmen", Kullanici.Rol.OGRETMEN)
        self.istek = gecisler.istek_ac(self.mehmet, "Kimya notları lazım", "Salı günkü dersin notları.", "ders")

    def durum(self):
        self.istek.refresh_from_db()
        return self.istek.durum


class RolKuraliTesti(OrnekVeri):
    """roller.md: kim neyi yapabilir? Kurallar sunucuda uygulanır (T-07)."""

    def test_kendi_istegini_ustlenemez(self):
        with self.assertRaises(YetkiYok):
            gecisler.ustlen(self.istek.pk, self.mehmet)
        self.assertEqual(self.durum(), Durum.ACIK)
        self.assertIsNone(self.istek.ustlenen)

    def test_baskasinin_istegini_onaylayamaz(self):
        gecisler.ustlen(self.istek.pk, self.ayse)
        gecisler.yapildi_de(self.istek.pk, self.ayse)
        # Can isteği açan kişi değil: onaylayamaz. İşi yapan Ayşe de kendi işini onaylayamaz.
        for yabanci in (self.can, self.ayse):
            with self.assertRaises(YetkiYok):
                gecisler.onayla(self.istek.pk, yabanci)
        self.assertEqual(self.durum(), Durum.YAPILDI)

    def test_yalnizca_ustlenen_yapildi_diyebilir(self):
        gecisler.ustlen(self.istek.pk, self.ayse)
        with self.assertRaises(YetkiYok):
            gecisler.yapildi_de(self.istek.pk, self.can)
        self.assertEqual(self.durum(), Durum.USTLENILDI)

    def test_ogrenci_gizleyemez_ogretmen_gizleyebilir(self):
        with self.assertRaises(YetkiYok):
            gecisler.gizle(self.istek.pk, self.ayse, "deneme")
        gecisler.gizle(self.istek.pk, self.selin, "Kişisel bilgi içeriyor.")
        self.assertEqual(self.durum(), Durum.GIZLENDI)


class CiftUstlenmeTesti(OrnekVeri):
    """akis.md soru 1 / T-06: Aynı iş iki kişi tarafından üstlenilemez."""

    def test_ikinci_kisi_ustlenemez(self):
        # Ayşe ve Can isteği "Açık" olarak gördü. Ayşe önce basıyor.
        gecisler.ustlen(self.istek.pk, self.ayse)
        with self.assertRaisesMessage(DurumUygunDegil, "az önce başka biri tarafından üstlenildi"):
            gecisler.ustlen(self.istek.pk, self.can)

        self.istek.refresh_from_db()
        self.assertEqual(self.istek.durum, Durum.USTLENILDI)
        self.assertEqual(self.istek.ustlenen, self.ayse)  # iş ilk basanda kaldı
        # Durum geçmişinde yalnızca bir üstlenme var
        self.assertEqual(
            DurumGecmisi.objects.filter(istek=self.istek, yeni_durum=Durum.USTLENILDI).count(), 1
        )

    def test_kosullu_guncelleme_eski_bilgiyle_yazmaz(self):
        """Can'ın elinde isteğin eski ("Açık") hâli olsa bile UPDATE koşulu veritabanındaki
        güncel duruma bakar. Önce-oku-sonra-yaz yapılsaydı bu test başarısız olurdu."""
        eski_kopya = Istek.objects.get(pk=self.istek.pk)
        self.assertEqual(eski_kopya.durum, Durum.ACIK)
        gecisler.ustlen(self.istek.pk, self.ayse)
        with self.assertRaises(DurumUygunDegil):
            gecisler.ustlen(eski_kopya.pk, self.can)
        self.assertEqual(Istek.objects.get(pk=self.istek.pk).ustlenen, self.ayse)


class OnayAkisiTesti(OrnekVeri):
    """Senaryo 1 (senaryolar.md): aç → üstlen → yapıldı → onayla, uçtan uca."""

    def test_senaryo_1(self):
        self.assertEqual(self.durum(), Durum.ACIK)

        gecisler.ustlen(self.istek.pk, self.ayse)
        self.assertEqual(self.durum(), Durum.USTLENILDI)

        gecisler.yorum_yaz(self.istek.pk, self.ayse, "Yarın teneffüste getiririm.")

        gecisler.yapildi_de(self.istek.pk, self.ayse)
        self.assertEqual(self.durum(), Durum.YAPILDI)

        gecisler.onayla(self.istek.pk, self.mehmet, tesekkur_notu="Çok sağ ol! 🙏")
        self.assertEqual(self.durum(), Durum.TAMAMLANDI)

        # Her geçiş, doğru kişiyle ve doğru sırayla durum geçmişine yazıldı
        gecmis = list(DurumGecmisi.objects.filter(istek=self.istek).values_list("yeni_durum", "yapan__username"))
        self.assertEqual(gecmis, [
            (Durum.ACIK, "ogrenci1"),
            (Durum.USTLENILDI, "ogrenci2"),
            (Durum.YAPILDI, "ogrenci2"),
            (Durum.TAMAMLANDI, "ogrenci1"),
        ])
        # Teşekkür notu, vurgulu bir yorum olarak eklendi (E13)
        self.assertTrue(Yorum.objects.filter(istek=self.istek, tesekkur=True, metin="Çok sağ ol! 🙏").exists())

    def test_tamamlanan_istek_yeniden_onaylanamaz(self):
        gecisler.ustlen(self.istek.pk, self.ayse)
        gecisler.yapildi_de(self.istek.pk, self.ayse)
        gecisler.onayla(self.istek.pk, self.mehmet)
        with self.assertRaises(DurumUygunDegil):
            gecisler.onayla(self.istek.pk, self.mehmet)


class BirakmaVeYapilmadiTesti(OrnekVeri):
    """Senaryo 2 ve 3: işi bırakmak, "yapılmadı" demek."""

    def test_birakinca_istek_yeniden_acik_olur(self):
        gecisler.ustlen(self.istek.pk, self.can)
        gecisler.birak(self.istek.pk, self.can)
        self.istek.refresh_from_db()
        self.assertEqual(self.istek.durum, Durum.ACIK)
        self.assertIsNone(self.istek.ustlenen)
        # Bıraktıktan sonra başkası üstlenebilir
        gecisler.ustlen(self.istek.pk, self.ayse)
        self.assertEqual(self.durum(), Durum.USTLENILDI)

    def test_gerekcesiz_yapilmadi_reddedilir(self):
        gecisler.ustlen(self.istek.pk, self.ayse)
        gecisler.yapildi_de(self.istek.pk, self.ayse)
        with self.assertRaises(GerekceGerekli):
            gecisler.yapilmadi_de(self.istek.pk, self.mehmet, "   ")
        self.assertEqual(self.durum(), Durum.YAPILDI)

        gecisler.yapilmadi_de(self.istek.pk, self.mehmet, "Notların yarısı eksik.")
        self.istek.refresh_from_db()
        self.assertEqual(self.istek.durum, Durum.USTLENILDI)
        self.assertEqual(self.istek.ustlenen, self.ayse)  # iş aynı kişide kalır
        self.assertEqual(self.istek.gecmis.last().notu, "Notların yarısı eksik.")

    def test_ustlenilmis_istek_geri_cekilemez(self):
        gecisler.ustlen(self.istek.pk, self.ayse)
        with self.assertRaises(DurumUygunDegil):
            gecisler.geri_cek(self.istek.pk, self.mehmet)
        self.assertEqual(self.durum(), Durum.USTLENILDI)
