"""Veri API'si (demo-plani.md, mimari değişikliği).

Sunucu yalnızca JSON gönderir, arayüz istemcidedir (demo/istemci/). Kurallar burada da değil,
gecisler.py'dedir: buradaki fonksiyonlar isteği okur, ilgili geçişi çağırır, sonucu JSON'a çevirir.

Oturum Django'nun kendi oturum çereziyle tutulur. Veri değiştiren her istek CSRF jetonu ister
(istemci /api/ben çağrısıyla gelen csrftoken çerezini X-CSRFToken başlığında geri gönderir).
"""
import json
from functools import wraps

from django.contrib.auth import authenticate, login, logout
from django.db.models import Count, Q
from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_GET, require_POST

from . import gecisler
from .gecisler import DurumUygunDegil, GerekceGerekli, YetkiYok
from .models import Istek

Durum = Istek.Durum
AKISTA_GORUNEN = (Durum.ACIK, Durum.USTLENILDI, Durum.YAPILDI)

# Hata türü -> HTTP durum kodu (demo-plani.md)
HATA_KODLARI = ((YetkiYok, 403), (DurumUygunDegil, 409), (GerekceGerekli, 400))


def _hata(mesaj, kod):
    return JsonResponse({"hata": mesaj}, status=kod)


def giris_gerekli(view):
    """Giriş yapılmamışsa giriş sayfasına yönlendirmek yerine 401 döner (istemci giriş ekranını açar)."""
    @wraps(view)
    def sarmal(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return _hata("Giriş yapmalısın.", 401)
        try:
            return view(request, *args, **kwargs)
        except tuple(t for t, _ in HATA_KODLARI) as hata:
            kod = next(k for t, k in HATA_KODLARI if isinstance(hata, t))
            return _hata(str(hata), kod)
        except Http404:
            return _hata("Bulunamadı.", 404)
    return sarmal


def _govde(request):
    try:
        return json.loads(request.body or b"{}")
    except ValueError:
        return {}


# --- JSON'a çevirme (yalnızca ekranın ihtiyaç duyduğu alanlar) -----------------------------

def _kisi(k):
    if k is None:
        return None
    return {"gorunen_ad": k.gorunen_ad, "bas_harfler": k.bas_harfler}


def _istek_ozet(i):
    return {
        "no": i.pk,
        "baslik": i.baslik,
        "aciklama": i.aciklama,
        "kategori": i.kategori,
        "kategori_adi": i.get_kategori_display(),
        "durum": i.durum,
        "durum_adi": i.get_durum_display(),
        "acan": _kisi(i.acan),
        "ustlenen": _kisi(i.ustlenen),
        "olusturma": i.olusturma_zamani.isoformat(),
        "yorum_sayisi": getattr(i, "yorum_sayisi", None),
    }


def _yorum_sayili(qs):
    return qs.select_related("acan", "ustlenen").annotate(
        yorum_sayisi=Count("yorumlar", filter=Q(yorumlar__gizli=False))
    )


def _istek_detay(istek, kullanici):
    veri = _istek_ozet(istek)
    veri["yorumlar"] = [
        {"yazan": _kisi(y.yazan), "metin": y.metin, "zaman": y.zaman.isoformat(), "tesekkur": y.tesekkur}
        for y in istek.yorumlar.filter(gizli=False).select_related("yazan")
    ]
    veri["yorum_sayisi"] = len(veri["yorumlar"])
    # Yalnızca görünüş için: hangi düğmeler gösterilsin? Asıl kontrol gecisler.py'de.
    veri["dugmeler"] = gecisler.gorunen_dugmeler(istek, kullanici)
    veri["yorum_yazilabilir"] = istek.durum in gecisler.YORUM_YAZILABILEN_DURUMLAR
    return veri


def _ben(k):
    return {
        "kullanici_adi": k.username,
        "gorunen_ad": k.gorunen_ad,
        "bas_harfler": k.bas_harfler,
        "rol": k.rol,
        "rol_adi": k.get_rol_display(),
        "yonetim_paneli": k.is_staff,
        "kategoriler": [{"deger": d, "ad": a} for d, a in Istek.Kategori.choices],
    }


# --- Oturum -------------------------------------------------------------------------------

@require_GET
@ensure_csrf_cookie
def ben(request):
    """Giriş yapan kişiyi döner. Her durumda csrftoken çerezini de ayarlar."""
    if not request.user.is_authenticated:
        return _hata("Giriş yapmalısın.", 401)
    return JsonResponse(_ben(request.user))


@require_POST
def giris(request):
    veri = _govde(request)
    kullanici = authenticate(request, username=veri.get("kullanici_adi", ""), password=veri.get("sifre", ""))
    if kullanici is None or not kullanici.is_active:
        return _hata("Kullanıcı adı ya da şifre hatalı.", 400)
    login(request, kullanici)
    return JsonResponse(_ben(kullanici))


@require_POST
def cikis(request):
    logout(request)
    return JsonResponse({"tamam": True})


# --- İstekler -----------------------------------------------------------------------------

@giris_gerekli
def istekler(request):
    if request.method == "POST":  # G1: yeni istek
        veri = _govde(request)
        istek = gecisler.istek_ac(request.user, veri.get("baslik", ""), veri.get("aciklama", ""), veri.get("kategori", ""))
        return JsonResponse(_istek_detay(istek, request.user), status=201)
    if request.method != "GET":
        return _hata("Bu yöntem desteklenmiyor.", 405)

    # E2: akış. Gizlenen, tamamlanan ve geri çekilen istekler görünmez.
    qs = Istek.objects.filter(durum__in=AKISTA_GORUNEN)
    if request.GET.get("sekme") == "acik":
        qs = qs.filter(durum=Durum.ACIK)
    kategori = request.GET.get("k")
    if kategori in Istek.Kategori.values:
        qs = qs.filter(kategori=kategori)
    return JsonResponse({"istekler": [_istek_ozet(i) for i in _yorum_sayili(qs)]})


@require_GET
@giris_gerekli
def gorevler(request):
    """E5: açtıklarım ya da üstlendiklerim. Kişi başına toplam sayı yok (T-02)."""
    if request.GET.get("sekme") == "ustlendiklerim":
        qs = Istek.objects.filter(ustlenen=request.user)
    else:
        qs = Istek.objects.filter(acan=request.user)
    qs = qs.exclude(durum=Durum.GIZLENDI)
    return JsonResponse({"istekler": [_istek_ozet(i) for i in _yorum_sayili(qs)]})


@require_GET
@giris_gerekli
def istek(request, no):
    """E4: istek, yorumlar ve bu kişinin görebileceği düğmeler."""
    istek = get_object_or_404(Istek.objects.select_related("acan", "ustlenen"), pk=no)
    if istek.durum == Durum.GIZLENDI and not request.user.ogretmen_mi:
        raise Http404
    return JsonResponse(_istek_detay(istek, request.user))


EYLEMLER = {
    "ustlen": lambda no, k, v: gecisler.ustlen(no, k),
    "birak": lambda no, k, v: gecisler.birak(no, k),
    "yapildi": lambda no, k, v: gecisler.yapildi_de(no, k),
    "geri_cek": lambda no, k, v: gecisler.geri_cek(no, k),
    "onayla": lambda no, k, v: gecisler.onayla(no, k, v.get("tesekkur", "")),
    "yapilmadi": lambda no, k, v: gecisler.yapilmadi_de(no, k, v.get("gerekce", "")),
    "yorum": lambda no, k, v: gecisler.yorum_yaz(no, k, v.get("metin", "")),
}


@require_POST
@giris_gerekli
def istek_eylem(request, no, eylem):
    """İstek sayfasındaki bütün düğmeler. Yetki ve durum kontrolü gecisler.py'de yapılır."""
    if eylem not in EYLEMLER:
        raise Http404
    EYLEMLER[eylem](no, request.user, _govde(request))
    istek = get_object_or_404(Istek.objects.select_related("acan", "ustlenen"), pk=no)
    return JsonResponse(_istek_detay(istek, request.user))
