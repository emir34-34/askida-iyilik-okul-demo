"""İsteğin durum geçişleri ve yetki kuralları (akis.md G1–G9, roller.md).

Bütün kurallar burada, sunucuda uygulanır (T-07). Sayfalardaki düğmeleri gizlemek yalnızca
görünüş içindir: biri adresi elle yazsa bile buradaki kontroller işlemi reddeder.

Her geçiş iki soruyu sırayla sorar:
  1. Yetki: Bu kişi bu işlemi yapabilir mi? (ör. yalnızca isteği açan onaylar) -> YetkiYok
  2. Durum: İstek hâlâ bu işleme uygun durumda mı?                          -> DurumUygunDegil

Durum değişikliği "önce oku, sonra yaz" ile yapılmaz. Tek bir koşullu UPDATE ile yapılır:
"durumu hâlâ X ise Y yap". İki kişi aynı anda denerse veritabanı bunları sırayla işler,
ikincisinde koşul artık tutmadığı için 0 satır değişir ve işlem reddedilir (akis.md, soru 1).
"""
from django.db import transaction
from django.shortcuts import get_object_or_404
from django.utils import timezone

from .models import DurumGecmisi, Istek, Kullanici, Yorum

Durum = Istek.Durum
ISTEK_ACABILEN_ROLLER = (Kullanici.Rol.OGRENCI, Kullanici.Rol.OGRETMEN)


class GecisHatasi(Exception):
    """Ekranda kullanıcıya gösterilecek mesajı taşır (ekranlar.md E7)."""


class YetkiYok(GecisHatasi):
    """403: Bu kişi bu işlemi yapamaz."""


class DurumUygunDegil(GecisHatasi):
    """İstek artık bu işleme uygun durumda değil (ör. az önce başkası üstlendi)."""


class GerekceGerekli(GecisHatasi):
    """Gerekçe zorunlu olan bir işlemde gerekçe yazılmadı."""


def _istek_acabilir_mi(kullanici):
    return kullanici.is_authenticated and kullanici.rol in ISTEK_ACABILEN_ROLLER


def _kosullu_gecis(istek_id, kullanici, kosullar, yeni_durum, notu="", **alanlar):
    """Koşullar hâlâ tutuyorsa isteği yeni duruma geçirir ve durum geçmişine yazar.

    Dönüş: Geçiş yapıldıysa True, koşullar artık tutmuyorsa (başkası önce davrandıysa) False.
    """
    with transaction.atomic():
        eski = Istek.objects.filter(pk=istek_id, **kosullar).values_list("durum", flat=True).first()
        degisen = Istek.objects.filter(pk=istek_id, **kosullar).update(
            durum=yeni_durum, guncelleme_zamani=timezone.now(), **alanlar
        )
        if degisen == 0:
            return False
        DurumGecmisi.objects.create(
            istek_id=istek_id, eski_durum=eski or "", yeni_durum=yeni_durum, yapan=kullanici, notu=notu
        )
        return True


# --- G1: İstek aç -------------------------------------------------------------------------

def istek_ac(kullanici, baslik, aciklama, kategori):
    if not _istek_acabilir_mi(kullanici):
        raise YetkiYok("İstek açma yetkin yok.")
    baslik, aciklama = baslik.strip(), aciklama.strip()
    if not baslik or not aciklama:
        raise GerekceGerekli("Başlık ve açıklama boş olamaz.")
    if kategori not in Istek.Kategori.values:
        raise GerekceGerekli("Geçerli bir kategori seç.")
    with transaction.atomic():
        istek = Istek.objects.create(baslik=baslik, aciklama=aciklama, kategori=kategori, acan=kullanici)
        DurumGecmisi.objects.create(istek=istek, eski_durum="", yeni_durum=Durum.ACIK, yapan=kullanici)
    return istek


# --- G2: Üstlen ---------------------------------------------------------------------------

def ustlen(istek_id, kullanici):
    istek = get_object_or_404(Istek, pk=istek_id)
    if not _istek_acabilir_mi(kullanici):
        raise YetkiYok("İstek üstlenme yetkin yok.")
    if istek.acan_id == kullanici.pk:
        raise YetkiYok("Kendi isteğini üstlenemezsin.")
    # acan koşulu da UPDATE'in içinde: kontrol ile yazma arasında hiçbir şey değişemez.
    yapildi = _kosullu_gecis(
        istek_id, kullanici,
        kosullar={"durum": Durum.ACIK, "ustlenen__isnull": True},
        yeni_durum=Durum.USTLENILDI,
        ustlenen=kullanici,
    )
    if not yapildi:
        istek.refresh_from_db()
        if istek.durum == Durum.USTLENILDI:
            raise DurumUygunDegil("Bu istek az önce başka biri tarafından üstlenildi.")
        raise DurumUygunDegil("Bu istek artık bu durumda değil, sayfayı yenile.")


# --- G3: Bırak ----------------------------------------------------------------------------

def birak(istek_id, kullanici):
    istek = get_object_or_404(Istek, pk=istek_id)
    if istek.ustlenen_id != kullanici.pk:
        raise YetkiYok("Bu işi yalnızca üstlenen kişi bırakabilir.")
    if not _kosullu_gecis(
        istek_id, kullanici,
        kosullar={"durum": Durum.USTLENILDI, "ustlenen": kullanici},
        yeni_durum=Durum.ACIK,
        ustlenen=None,
    ):
        raise DurumUygunDegil("Bu istek artık bu durumda değil, sayfayı yenile.")


# --- G4: Yapıldı de -----------------------------------------------------------------------

def yapildi_de(istek_id, kullanici):
    istek = get_object_or_404(Istek, pk=istek_id)
    if istek.ustlenen_id != kullanici.pk:
        raise YetkiYok("'Yapıldı' demeyi yalnızca işi üstlenen kişi yapabilir.")
    if not _kosullu_gecis(
        istek_id, kullanici,
        kosullar={"durum": Durum.USTLENILDI, "ustlenen": kullanici},
        yeni_durum=Durum.YAPILDI,
    ):
        raise DurumUygunDegil("Bu istek artık bu durumda değil, sayfayı yenile.")


# --- G5: Onayla (isteğe bağlı teşekkür notuyla, E13) --------------------------------------

def onayla(istek_id, kullanici, tesekkur_notu=""):
    istek = get_object_or_404(Istek, pk=istek_id)
    if istek.acan_id != kullanici.pk:
        raise YetkiYok("Yapılan işi yalnızca isteği açan kişi onaylayabilir.")
    with transaction.atomic():
        if not _kosullu_gecis(
            istek_id, kullanici,
            kosullar={"durum": Durum.YAPILDI, "acan": kullanici},
            yeni_durum=Durum.TAMAMLANDI,
        ):
            raise DurumUygunDegil("Bu istek artık bu durumda değil, sayfayı yenile.")
        if tesekkur_notu.strip():
            Yorum.objects.create(istek=istek, yazan=kullanici, metin=tesekkur_notu.strip(), tesekkur=True)


# --- G6: Yapılmadı de (gerekçe zorunlu) ---------------------------------------------------

def yapilmadi_de(istek_id, kullanici, gerekce):
    istek = get_object_or_404(Istek, pk=istek_id)
    if istek.acan_id != kullanici.pk:
        raise YetkiYok("'Yapılmadı' demeyi yalnızca isteği açan kişi yapabilir.")
    if not gerekce.strip():
        raise GerekceGerekli("Lütfen neyin eksik olduğunu yaz.")
    if not _kosullu_gecis(
        istek_id, kullanici,
        kosullar={"durum": Durum.YAPILDI, "acan": kullanici},
        yeni_durum=Durum.USTLENILDI,  # iş aynı kişide kalır
        notu=gerekce.strip(),
    ):
        raise DurumUygunDegil("Bu istek artık bu durumda değil, sayfayı yenile.")


# --- G7: Geri çek -------------------------------------------------------------------------

def geri_cek(istek_id, kullanici):
    istek = get_object_or_404(Istek, pk=istek_id)
    if istek.acan_id != kullanici.pk:
        raise YetkiYok("İsteği yalnızca açan kişi geri çekebilir.")
    if not _kosullu_gecis(
        istek_id, kullanici,
        kosullar={"durum": Durum.ACIK, "acan": kullanici},
        yeni_durum=Durum.GERI_CEKILDI,
    ):
        raise DurumUygunDegil("Üstlenilmiş bir istek geri çekilemez. Önce üstlenen kişiyle yorumlarda konuş.")


# --- G8 / G9: Gizle, gizlemeyi kaldır (öğretmen) ------------------------------------------

def gizle(istek_id, kullanici, gerekce):
    get_object_or_404(Istek, pk=istek_id)
    if not kullanici.ogretmen_mi:
        raise YetkiYok("İçeriği yalnızca öğretmenler gizleyebilir.")
    if not gerekce.strip():
        raise GerekceGerekli("Gizleme gerekçesi zorunlu.")
    if not _kosullu_gecis(
        istek_id, kullanici,
        kosullar={"durum__in": [d for d in Durum.values if d != Durum.GIZLENDI]},
        yeni_durum=Durum.GIZLENDI,
        notu=gerekce.strip(),
    ):
        raise DurumUygunDegil("Bu istek zaten gizli.")


def gizlemeyi_kaldir(istek_id, kullanici):
    get_object_or_404(Istek, pk=istek_id)
    if not kullanici.ogretmen_mi:
        raise YetkiYok("Gizlemeyi yalnızca öğretmenler kaldırabilir.")
    if not _kosullu_gecis(
        istek_id, kullanici,
        kosullar={"durum": Durum.GIZLENDI},
        yeni_durum=Durum.ACIK,
        ustlenen=None,
    ):
        raise DurumUygunDegil("Bu istek gizli değil.")


# --- Yorum (herkese açık, özel mesaj yok: T-01) -------------------------------------------

YORUM_YAZILABILEN_DURUMLAR = (Durum.ACIK, Durum.USTLENILDI, Durum.YAPILDI)


def yorum_yaz(istek_id, kullanici, metin):
    istek = get_object_or_404(Istek, pk=istek_id)
    if not _istek_acabilir_mi(kullanici):
        raise YetkiYok("Yorum yazma yetkin yok.")
    if istek.durum not in YORUM_YAZILABILEN_DURUMLAR:
        raise DurumUygunDegil("Bu isteğe artık yorum yazılamaz.")
    if not metin.strip():
        raise GerekceGerekli("Boş yorum gönderilemez.")
    return Yorum.objects.create(istek=istek, yazan=kullanici, metin=metin.strip())


# --- Ekranda hangi düğmeler görünür? (ekranlar.md E4 tablosu) -----------------------------

def gorunen_dugmeler(istek, kullanici):
    """Yalnızca görünüş için. Asıl kontrol yukarıdaki fonksiyonlarda yapılır."""
    if not _istek_acabilir_mi(kullanici):
        return []
    acan = istek.acan_id == kullanici.pk
    ustlenen = istek.ustlenen_id == kullanici.pk
    if istek.durum == Durum.ACIK:
        return ["geri_cek"] if acan else ["ustlen"]
    if istek.durum == Durum.USTLENILDI and ustlenen:
        return ["yapildi", "birak"]
    if istek.durum == Durum.YAPILDI and acan:
        return ["onayla", "yapilmadi"]
    return []
