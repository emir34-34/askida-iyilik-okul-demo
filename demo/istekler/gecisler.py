"""Sorunun durum geçişleri ve yetki kuralları (akis.md G1–G5, roller.md).

Bütün kurallar burada, sunucuda uygulanır (T-07). Sayfadaki düğmeleri gizlemek yalnızca
görünüş içindir: biri adresi elle yazsa bile buradaki kontroller işlemi reddeder.

Her geçiş iki soruyu sırayla sorar:
  1. Yetki: Bu kişi bunu yapabilir mi? (ör. yalnızca bildiren onaylar)  -> YetkiYok
  2. Durum: Sorun hâlâ bu işleme uygun durumda mı?                     -> DurumUygunDegil

Durum "önce bak, sonra yaz" ile değiştirilmez. Tek bir koşullu güncellemeyle değiştirilir:
"durumu hâlâ X ise Y yap". İki kişi aynı anda üstlenmeye çalışırsa yalnızca ilki başarılı olur,
ikincisinde koşul artık tutmadığı için hiçbir satır değişmez (akis.md, soru 1).
"""
from django.db import transaction
from django.shortcuts import get_object_or_404
from django.utils import timezone

from .models import DurumGecmisi, Kullanici, Sorun, Yorum

Durum = Sorun.Durum
BILDIREBILEN_ROLLER = (Kullanici.Rol.OGRENCI, Kullanici.Rol.OGRETMEN)


class GecisHatasi(Exception):
    """Kullanıcıya gösterilecek mesajı taşır (ekranlar.md, hata mesajları)."""


class YetkiYok(GecisHatasi):
    """403: Bu kişi bu işlemi yapamaz."""


class DurumUygunDegil(GecisHatasi):
    """Sorun artık bu işleme uygun durumda değil (ör. az önce başkası üstlendi)."""


def _katilabilir_mi(kullanici):
    return kullanici.is_authenticated and kullanici.rol in BILDIREBILEN_ROLLER


def _kosullu_gecis(sorun_id, kullanici, kosullar, yeni_durum, **alanlar):
    """Koşullar hâlâ tutuyorsa sorunu yeni duruma geçirir ve durum geçmişine yazar.
    Dönüş: geçiş yapıldıysa True, başkası önce davrandıysa False."""
    with transaction.atomic():
        eski = Sorun.objects.filter(pk=sorun_id, **kosullar).values_list("durum", flat=True).first()
        degisen = Sorun.objects.filter(pk=sorun_id, **kosullar).update(
            durum=yeni_durum, guncelleme_zamani=timezone.now(), **alanlar
        )
        if degisen == 0:
            return False
        DurumGecmisi.objects.create(sorun_id=sorun_id, eski_durum=eski, yeni_durum=yeni_durum, yapan=kullanici)
        return True


# G1: Sorunu bildir
def bildir(kullanici, baslik, aciklama):
    if not _katilabilir_mi(kullanici):
        raise YetkiYok("Sorun bildirme yetkin yok.")
    baslik, aciklama = baslik.strip(), aciklama.strip()
    if not baslik or not aciklama:
        raise DurumUygunDegil("Sorunu ve nerede olduğunu yaz.")
    with transaction.atomic():
        sorun = Sorun.objects.create(baslik=baslik, aciklama=aciklama, bildiren=kullanici)
        DurumGecmisi.objects.create(sorun=sorun, yeni_durum=Durum.ACIK, yapan=kullanici)
    return sorun


# G2: Üstlen
def ustlen(sorun_id, kullanici):
    sorun = get_object_or_404(Sorun, pk=sorun_id)
    if not _katilabilir_mi(kullanici):
        raise YetkiYok("Sorun üstlenme yetkin yok.")
    if sorun.bildiren_id == kullanici.pk:
        raise YetkiYok("Kendi bildirdiğin sorunu üstlenemezsin.")
    if not _kosullu_gecis(
        sorun_id, kullanici,
        kosullar={"durum": Durum.ACIK, "ustlenen__isnull": True},
        yeni_durum=Durum.USTLENILDI, ustlenen=kullanici,
    ):
        sorun.refresh_from_db()
        if sorun.durum == Durum.USTLENILDI:
            raise DurumUygunDegil("Bu sorun az önce başka biri tarafından üstlenildi.")
        raise DurumUygunDegil("Bu sorun artık bu durumda değil, sayfayı yenile.")


# G3: Bırak
def birak(sorun_id, kullanici):
    sorun = get_object_or_404(Sorun, pk=sorun_id)
    if sorun.ustlenen_id != kullanici.pk:
        raise YetkiYok("Bu işi yalnızca üstlenen kişi bırakabilir.")
    if not _kosullu_gecis(
        sorun_id, kullanici,
        kosullar={"durum": Durum.USTLENILDI, "ustlenen": kullanici},
        yeni_durum=Durum.ACIK, ustlenen=None,
    ):
        raise DurumUygunDegil("Bu sorun artık bu durumda değil, sayfayı yenile.")


# G4: Yapıldı de
def yapildi_de(sorun_id, kullanici):
    sorun = get_object_or_404(Sorun, pk=sorun_id)
    if sorun.ustlenen_id != kullanici.pk:
        raise YetkiYok("'Yapıldı' demeyi yalnızca işi üstlenen kişi yapabilir.")
    if not _kosullu_gecis(
        sorun_id, kullanici,
        kosullar={"durum": Durum.USTLENILDI, "ustlenen": kullanici},
        yeni_durum=Durum.YAPILDI,
    ):
        raise DurumUygunDegil("Bu sorun artık bu durumda değil, sayfayı yenile.")


# G5: Onayla
def onayla(sorun_id, kullanici):
    sorun = get_object_or_404(Sorun, pk=sorun_id)
    if sorun.bildiren_id != kullanici.pk:
        raise YetkiYok("Yapılan işi yalnızca sorunu bildiren kişi onaylayabilir.")
    if not _kosullu_gecis(
        sorun_id, kullanici,
        kosullar={"durum": Durum.YAPILDI, "bildiren": kullanici},
        yeni_durum=Durum.TAMAMLANDI,
    ):
        raise DurumUygunDegil("Bu sorun artık bu durumda değil, sayfayı yenile.")


# Yorum: herkese açık (T-01)
def yorum_yaz(sorun_id, kullanici, metin):
    sorun = get_object_or_404(Sorun, pk=sorun_id)
    if not _katilabilir_mi(kullanici):
        raise YetkiYok("Yorum yazma yetkin yok.")
    if not metin.strip():
        raise DurumUygunDegil("Boş yorum gönderilemez.")
    return Yorum.objects.create(sorun=sorun, yazan=kullanici, metin=metin.strip())


def gorunen_dugmeler(sorun, kullanici):
    """Sorun sayfasında hangi düğmeler görünsün? (ekranlar.md E4 tablosu). Yalnızca görünüş."""
    if not _katilabilir_mi(kullanici):
        return []
    if sorun.durum == Durum.ACIK and sorun.bildiren_id != kullanici.pk:
        return ["ustlen"]
    if sorun.durum == Durum.USTLENILDI and sorun.ustlenen_id == kullanici.pk:
        return ["yapildi", "birak"]
    if sorun.durum == Durum.YAPILDI and sorun.bildiren_id == kullanici.pk:
        return ["onayla"]
    return []
