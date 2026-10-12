from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path("", views.liste, name="liste"),
    path("giris/", auth_views.LoginView.as_view(template_name="istekler/giris.html", redirect_authenticated_user=True), name="giris"),
    path("cikis/", auth_views.LogoutView.as_view(), name="cikis"),
    path("bildir/", views.bildir, name="bildir"),
    path("sorun/<int:pk>/", views.sorun, name="sorun"),
    path("sorun/<int:pk>/<slug:ad>/", views.eylem, name="eylem"),
    path("islerim/", views.islerim, name="islerim"),
]
