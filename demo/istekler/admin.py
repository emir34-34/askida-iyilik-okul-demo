"""Django'nun hazır yönetim paneli: yöneticinin hesap işleri (V-03). Kod bilmeden kullanılabilir."""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import DurumGecmisi, Kullanici, Sorun, Yorum

admin.site.site_header = "Askıda İyilik · Yönetim"


@admin.register(Kullanici)
class KullaniciAdmin(UserAdmin):
    list_display = ("gorunen_ad", "username", "rol", "is_active")
    list_filter = ("rol", "is_active")
    # Yalnızca veri.md'deki alanlar. E-posta, ad ve soyad formda yok.
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Askıda İyilik", {"fields": ("gorunen_ad", "rol", "is_active")}),
        ("Yönetim paneli", {"fields": ("is_staff", "is_superuser")}),
    )
    add_fieldsets = ((None, {"fields": ("username", "gorunen_ad", "rol", "password1", "password2")}),)


class DurumGecmisiSatiri(admin.TabularInline):
    model = DurumGecmisi
    extra = 0
    can_delete = False
    readonly_fields = ("zaman", "eski_durum", "yeni_durum", "yapan")


@admin.register(Sorun)
class SorunAdmin(admin.ModelAdmin):
    list_display = ("baslik", "durum", "bildiren", "ustlenen", "olusturma_zamani")
    list_filter = ("durum",)
    # Durum yalnızca geçişlerle değişir, panelden elle değiştirilemez.
    readonly_fields = ("bildiren", "ustlenen", "durum")
    inlines = [DurumGecmisiSatiri]


admin.site.register(Yorum)
