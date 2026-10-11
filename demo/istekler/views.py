"""Sayfalar (ekranlar.md). Kurallar burada değil gecisler.py'de: view'lar yalnızca formu okur,
ilgili geçiş fonksiyonunu çağırır ve sonucu gösterir."""
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from . import gecisler
from .gecisler import GecisHatasi, YetkiYok
from .models import Istek

Durum = Istek.Durum
AKISTA_GORUNEN = (Durum.ACIK, Durum.USTLENILDI, Durum.YAPILDI)

# İstek sayfasındaki düğme adı -> geçiş fonksiyonu ve başarı mesajı
EYLEMLER = {
    "ustlen": (gecisler.ustlen, "İsteği üstlendin."),
    "birak": (gecisler.birak, "İşi bıraktın. İstek yeniden açık."),
    "yapildi": (gecisler.yapildi_de, "Harika! Şimdi isteği açan kişinin onayı bekleniyor."),
    "geri_cek": (gecisler.geri_cek, "İsteğini geri çektin."),
}


def _yetkisiz(request, mesaj):
    """Adresi elle değiştiren biri de buraya düşer (T-07, ekranlar.md E7)."""
    return render(request, "istekler/403.html", {"mesaj": mesaj}, status=403)


def _yorum_sayili(qs):
    return qs.select_related("acan", "ustlenen").annotate(
        yorum_sayisi=Count("yorumlar", filter=Q(yorumlar__gizli=False))
    )


@login_required
def akis(request):
    """E2: Ana akış. Gizlenen, tamamlanan ve geri çekilen istekler görünmez."""
    sekme = request.GET.get("sekme", "yeni")
    istekler = Istek.objects.filter(durum__in=AKISTA_GORUNEN)
    if sekme == "acik":
        istekler = istekler.filter(durum=Durum.ACIK)
    kategori = request.GET.get("k")
    if kategori in Istek.Kategori.values:
        istekler = istekler.filter(kategori=kategori)
    return render(request, "istekler/akis.html", {
        "istekler": _yorum_sayili(istekler),
        "sekme": sekme,
        "kategori": kategori,
        "kategoriler": Istek.Kategori.choices,
    })


@login_required
def istek_detay(request, pk):
    """E4: İstek sayfası. Düğmeler role ve duruma göre değişir (yalnızca görünüş)."""
    istek = get_object_or_404(Istek.objects.select_related("acan", "ustlenen"), pk=pk)
    if istek.durum == Durum.GIZLENDI and not request.user.ogretmen_mi:
        raise Http404
    return render(request, "istekler/istek.html", {
        "istek": istek,
        "yorumlar": istek.yorumlar.filter(gizli=False).select_related("yazan"),
        "dugmeler": gecisler.gorunen_dugmeler(istek, request.user),
        "yorum_yazilabilir": istek.durum in gecisler.YORUM_YAZILABILEN_DURUMLAR,
    })


@login_required
def yeni_istek(request):
    """E3: Yeni istek (G1)."""
    form = {"baslik": "", "aciklama": "", "kategori": Istek.Kategori.DERS}
    if request.method == "POST":
        form = {k: request.POST.get(k, "") for k in form}
        try:
            istek = gecisler.istek_ac(request.user, form["baslik"], form["aciklama"], form["kategori"])
        except YetkiYok as hata:
            return _yetkisiz(request, str(hata))
        except GecisHatasi as hata:
            messages.error(request, str(hata))
        else:
            messages.success(request, "İsteğin yayında!")
            return redirect("istek", pk=istek.pk)
    return render(request, "istekler/yeni.html", {"form": form, "kategoriler": Istek.Kategori.choices})


@login_required
@require_POST
def istek_eylem(request, pk, eylem):
    """İstek sayfasındaki bütün düğmeler buraya POST eder. Yetki gecisler.py'de kontrol edilir."""
    try:
        if eylem in EYLEMLER:
            fonksiyon, basari = EYLEMLER[eylem]
            fonksiyon(pk, request.user)
        elif eylem == "onayla":
            gecisler.onayla(pk, request.user, request.POST.get("tesekkur", ""))
            basari = "Teşekkürler! İstek tamamlandı."
        elif eylem == "yapilmadi":
            gecisler.yapilmadi_de(pk, request.user, request.POST.get("gerekce", ""))
            basari = "İstek yeniden üstlenen kişiye döndü."
        elif eylem == "yorum":
            gecisler.yorum_yaz(pk, request.user, request.POST.get("metin", ""))
            basari = "Yorumun eklendi."
        else:
            raise Http404
    except YetkiYok as hata:
        return _yetkisiz(request, str(hata))
    except GecisHatasi as hata:
        messages.error(request, str(hata))
    else:
        messages.success(request, basari)
    return redirect("istek", pk=pk)


@login_required
def gorevler(request):
    """E5: Görevler. Kişi başına toplam bir sayı gösterilmez (T-02)."""
    sekme = request.GET.get("sekme", "actiklarim")
    if sekme == "ustlendiklerim":
        istekler = Istek.objects.filter(ustlenen=request.user)
    else:
        sekme = "actiklarim"
        istekler = Istek.objects.filter(acan=request.user)
    istekler = istekler.exclude(durum=Durum.GIZLENDI)
    return render(request, "istekler/gorevler.html", {"istekler": _yorum_sayili(istekler), "sekme": sekme})


@login_required
def profil(request):
    """E8: Profil. Yalnızca veri.md'deki alanlar. Karma ya da iyilik sayısı yok."""
    return render(request, "istekler/profil.html")
