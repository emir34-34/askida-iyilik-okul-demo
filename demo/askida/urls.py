from django.contrib import admin
from django.urls import include, path

# Demoda öğretmenin gizleme ekranının (E6, D4) ve yöneticinin hesap işlerinin (D6) yerini
# Django'nun yönetim paneli tutar (demo-plani.md).
admin.site.site_header = "Askıda İyilik · Yönetim"
admin.site.site_title = "Askıda İyilik"

urlpatterns = [
    path("yonetim/", admin.site.urls),
    path("", include("istekler.urls")),
]
