from django.conf import settings
from django.http import FileResponse
from django.urls import path, re_path
from django.views.static import serve

from . import api


def istemci(request):
    """Arayüzün giriş sayfası. Tarayıcıda Django verir, APK'da ise APK kendi içinden verir."""
    return FileResponse(open(settings.ISTEMCI_DIR / "index.html", "rb"), content_type="text/html; charset=utf-8")


urlpatterns = [
    # Arayüz dosyaları (demo/istemci/). Demo için Django'nun basit dosya sunucusu yeterli.
    path("", istemci),
    re_path(r"^i/(?P<path>.+)$", serve, {"document_root": settings.ISTEMCI_DIR}),

    # Veri API'si (demo-plani.md, mimari değişikliği)
    path("api/ben", api.ben),
    path("api/giris", api.giris),
    path("api/cikis", api.cikis),
    path("api/istekler", api.istekler),
    path("api/gorevler", api.gorevler),
    path("api/gizlenenler", api.gizlenenler),
    path("api/istekler/<int:no>", api.istek),
    path("api/istekler/<int:no>/<slug:eylem>", api.istek_eylem),
]
