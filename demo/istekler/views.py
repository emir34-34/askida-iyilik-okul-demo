"""Sayfalar (ekranlar.md E1–E5). Kurallar burada değil gecisler.py'de: view'lar formu okur,
ilgili geçişi çağırır ve sonucu gösterir."""
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from . import gecisler
from .gecisler import GecisHatasi, YetkiYok
from .models import Sorun

EYLEMLER = {
    "ustlen": (gecisler.ustlen, "Sorunu üstlendin."),
    "birak": (gecisler.birak, "İşi bıraktın. Sorun yeniden açık."),
    "yapildi": (gecisler.yapildi_de, "Bildiren kişinin onayı bekleniyor."),
    "onayla": (gecisler.onayla, "Teşekkürler! Sorun tamamlandı."),
}


def _yetkisiz(request, mesaj):
    """Adresi elle yazan yetkisiz biri de buraya düşer (T-07)."""
    return render(request, "istekler/403.html", {"mesaj": mesaj}, status=403)


@login_required
def liste(request):
    """E2: Sorunlar. Varsayılan olarak açık olanlar."""
    hepsi = request.GET.get("sekme") == "hepsi"
    sorunlar = Sorun.objects.select_related("bildiren", "ustlenen")
    if not hepsi:
        sorunlar = sorunlar.exclude(durum=Sorun.Durum.TAMAMLANDI)
    return render(request, "istekler/liste.html", {"sorunlar": sorunlar, "hepsi": hepsi})


@login_required
def bildir(request):
    """E3: Sorun bildir (G1)."""
    form = {"baslik": "", "aciklama": ""}
    if request.method == "POST":
        form = {k: request.POST.get(k, "") for k in form}
        try:
            sorun = gecisler.bildir(request.user, form["baslik"], form["aciklama"])
        except YetkiYok as hata:
            return _yetkisiz(request, str(hata))
        except GecisHatasi as hata:
            messages.error(request, str(hata))
        else:
            messages.success(request, "Sorun bildirildi. Teşekkürler!")
            return redirect("sorun", pk=sorun.pk)
    return render(request, "istekler/bildir.html", {"form": form})


@login_required
def sorun(request, pk):
    """E4: Sorun sayfası. Düğmeler role ve duruma göre değişir (yalnızca görünüş)."""
    s = get_object_or_404(Sorun.objects.select_related("bildiren", "ustlenen"), pk=pk)
    return render(request, "istekler/sorun.html", {
        "sorun": s,
        "yorumlar": s.yorumlar.select_related("yazan"),
        "dugmeler": gecisler.gorunen_dugmeler(s, request.user),
    })


@login_required
@require_POST
def eylem(request, pk, ad):
    """Sorun sayfasındaki düğmeler buraya gönderilir. Yetkiyi gecisler.py kontrol eder."""
    try:
        if ad == "yorum":
            gecisler.yorum_yaz(pk, request.user, request.POST.get("metin", ""))
            basari = "Yorumun eklendi."
        elif ad in EYLEMLER:
            fonksiyon, basari = EYLEMLER[ad]
            fonksiyon(pk, request.user)
        else:
            raise Http404
    except YetkiYok as hata:
        return _yetkisiz(request, str(hata))
    except GecisHatasi as hata:
        messages.error(request, str(hata))
    else:
        messages.success(request, basari)
    return redirect("sorun", pk=pk)


@login_required
def islerim(request):
    """E5: Benim işlerim. Kişi başına toplam sayı gösterilmez (T-02)."""
    ustlendiklerim = request.GET.get("sekme") == "ustlendiklerim"
    sorunlar = (Sorun.objects.filter(ustlenen=request.user) if ustlendiklerim
                else Sorun.objects.filter(bildiren=request.user)).select_related("bildiren", "ustlenen")
    return render(request, "istekler/islerim.html", {"sorunlar": sorunlar, "ustlendiklerim": ustlendiklerim})
