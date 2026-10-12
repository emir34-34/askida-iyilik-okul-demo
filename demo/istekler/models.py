"""Askıda İyilik veri modeli.

Her alan veri.md'deki tablolardan gelir. Orada nedeni yazılı olmayan alan burada da yoktur.
Askıya yalnızca okulda görülen sorunlar konur (T-08): bozuk kapı, damlayan musluk, biten sabun.
"""
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Kullanici(AbstractUser):
    """Django'nun kullanıcı modeli, üzerine yalnızca rol ve görünen ad eklendi.

    Django'dan gelen e-posta, ad ve soyad alanları kullanılmaz, boş kalır (veri.md).
    """

    class Rol(models.TextChoices):
        OGRENCI = "ogrenci", "Öğrenci"
        OGRETMEN = "ogretmen", "Öğretmen"
        YONETICI = "yonetici", "Yönetici"

    rol = models.CharField(max_length=10, choices=Rol.choices, default=Rol.OGRENCI)
    gorunen_ad = models.CharField(max_length=40)  # ör. "Ayşe K." (V-09)

    def __str__(self):
        return self.gorunen_ad or self.username


class Sorun(models.Model):
    class Durum(models.TextChoices):
        # akis.md'deki dört durum
        ACIK = "acik", "Açık"
        USTLENILDI = "ustlenildi", "Üstlenildi"
        YAPILDI = "yapildi", "Yapıldı"
        TAMAMLANDI = "tamamlandi", "Tamamlandı"

    baslik = models.CharField(max_length=120)
    aciklama = models.TextField(max_length=1000)  # sorunun yeri de buraya yazılır (V-15)
    bildiren = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="bildirdigi_sorunlar")
    ustlenen = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True, related_name="ustlendigi_sorunlar"
    )
    durum = models.CharField(max_length=12, choices=Durum.choices, default=Durum.ACIK)
    olusturma_zamani = models.DateTimeField(auto_now_add=True)
    guncelleme_zamani = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-olusturma_zamani"]
        verbose_name = "sorun"
        verbose_name_plural = "sorunlar"

    def __str__(self):
        return self.baslik


class Yorum(models.Model):
    """Konuşma sorunun altında, herkese açık (T-01). Özel mesaj yok."""

    sorun = models.ForeignKey(Sorun, on_delete=models.CASCADE, related_name="yorumlar")
    yazan = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    metin = models.TextField(max_length=1000)
    zaman = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["zaman"]
        verbose_name_plural = "yorumlar"


class DurumGecmisi(models.Model):
    """Her durum değişikliği kim ve ne zaman bilgisiyle buraya yazılır (veri.md)."""

    sorun = models.ForeignKey(Sorun, on_delete=models.CASCADE, related_name="gecmis")
    eski_durum = models.CharField(max_length=12, choices=Sorun.Durum.choices, blank=True)
    yeni_durum = models.CharField(max_length=12, choices=Sorun.Durum.choices)
    yapan = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    zaman = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["zaman"]
        verbose_name_plural = "durum geçmişi"
