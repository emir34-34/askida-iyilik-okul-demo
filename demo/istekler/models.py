"""Askıda İyilik veri modeli.

Her alan veri.md'deki tablolardan gelir. Orada nedeni yazılı olmayan alan burada da yoktur.
"""
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Kullanici(AbstractUser):
    """Django'nun kullanıcı modeli, üzerine yalnızca rol ve görünen ad eklendi.

    AbstractUser'dan gelen e-posta, ad ve soyad alanları kullanılmaz, boş kalır (veri.md: e-posta tutulmaz).
    """

    class Rol(models.TextChoices):
        OGRENCI = "ogrenci", "Öğrenci"
        OGRETMEN = "ogretmen", "Öğretmen"
        YONETICI = "yonetici", "Yönetici"

    rol = models.CharField(max_length=10, choices=Rol.choices, default=Rol.OGRENCI)
    # Yalnızca ad ve soyadın baş harfi, ör. "Ayşe K." (V-09)
    gorunen_ad = models.CharField(max_length=40)

    @property
    def ogretmen_mi(self):
        return self.rol == self.Rol.OGRETMEN

    @property
    def bas_harfler(self):
        """Profil fotoğrafı yerine gösterilen baş harfler (T-03)."""
        parcalar = self.gorunen_ad.replace(".", "").split()
        return "".join(p[0] for p in parcalar[:2]).upper() or self.username[:2].upper()

    def __str__(self):
        return self.gorunen_ad or self.username


class Istek(models.Model):
    class Kategori(models.TextChoices):
        # Örnek kategoriler. Gerçek listeyi hocalar belirleyecek (Soru 8).
        DERS = "ders", "k/ders"
        ESYA = "esya", "k/eşya"
        OKUL = "okul", "k/okul"

    class Durum(models.TextChoices):
        # akis.md'deki altı durum
        ACIK = "acik", "Açık"
        USTLENILDI = "ustlenildi", "Üstlenildi"
        YAPILDI = "yapildi", "Yapıldı"
        TAMAMLANDI = "tamamlandi", "Tamamlandı"
        GERI_CEKILDI = "geri_cekildi", "Geri çekildi"
        GIZLENDI = "gizlendi", "Gizlendi"

    baslik = models.CharField(max_length=120)
    aciklama = models.TextField(max_length=2000)
    kategori = models.CharField(max_length=10, choices=Kategori.choices)
    acan = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="actigi_istekler"
    )
    ustlenen = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="ustlendigi_istekler",
    )
    durum = models.CharField(max_length=15, choices=Durum.choices, default=Durum.ACIK)
    olusturma_zamani = models.DateTimeField(auto_now_add=True)
    # Not: QuerySet.update() auto_now alanını doldurmaz, bu yüzden geçişlerde elle verilir.
    guncelleme_zamani = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-olusturma_zamani"]
        verbose_name = "istek"
        verbose_name_plural = "istekler"

    def __str__(self):
        return self.baslik


class Yorum(models.Model):
    istek = models.ForeignKey(Istek, on_delete=models.CASCADE, related_name="yorumlar")
    yazan = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    metin = models.TextField(max_length=1000)
    zaman = models.DateTimeField(auto_now_add=True)
    # Öğretmen gizlerse silinmez, saklanır (V-02)
    gizli = models.BooleanField(default=False)
    # Onaylarken yazılan teşekkür notu, vurgulu gösterilir. Hiçbir yerde sayılmaz (E13)
    tesekkur = models.BooleanField(default=False)

    class Meta:
        ordering = ["zaman"]
        verbose_name = "yorum"
        verbose_name_plural = "yorumlar"

    def __str__(self):
        return f"{self.yazan}: {self.metin[:30]}"


class DurumGecmisi(models.Model):
    """Her durum geçişi kim, ne zaman, neden bilgisiyle buraya yazılır (veri.md). Yalnızca öğretmenler görür."""

    istek = models.ForeignKey(Istek, on_delete=models.CASCADE, related_name="gecmis")
    eski_durum = models.CharField(max_length=15, choices=Istek.Durum.choices, blank=True)
    yeni_durum = models.CharField(max_length=15, choices=Istek.Durum.choices)
    yapan = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    zaman = models.DateTimeField(auto_now_add=True)
    # "Yapılmadı" ve gizleme gerekçesi (G6, G8)
    notu = models.CharField(max_length=500, blank=True)

    class Meta:
        ordering = ["zaman"]
        verbose_name = "durum geçmişi"
        verbose_name_plural = "durum geçmişi"
