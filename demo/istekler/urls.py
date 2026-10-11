from django.contrib.auth import views as auth_views
from django.urls import path

from . import api, views

urlpatterns = [
    path("", views.akis, name="akis"),
    path("giris/", auth_views.LoginView.as_view(template_name="istekler/giris.html", redirect_authenticated_user=True), name="giris"),
    path("cikis/", auth_views.LogoutView.as_view(), name="cikis"),
    path("yeni/", views.yeni_istek, name="yeni"),
    path("istek/<int:pk>/", views.istek_detay, name="istek"),
    path("istek/<int:pk>/<slug:eylem>/", views.istek_eylem, name="istek_eylem"),
    path("gorevler/", views.gorevler, name="gorevler"),
    path("profil/", views.profil, name="profil"),

    # Veri API'si (demo-plani.md, mimari değişikliği)
    path("api/ben", api.ben),
    path("api/giris", api.giris),
    path("api/cikis", api.cikis),
    path("api/istekler", api.istekler),
    path("api/gorevler", api.gorevler),
    path("api/istekler/<int:no>", api.istek),
    path("api/istekler/<int:no>/<slug:eylem>", api.istek_eylem),
]
