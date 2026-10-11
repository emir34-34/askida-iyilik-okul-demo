"""Django yönetim paneli. Demoda öğretmenin gizleme ekranının (E6, D4) ve yöneticinin hesap
işlerinin (E17, D6) yerini tutar. Gizleme de gecisler.py üzerinden yapılır, kurallar aynıdır."""
from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin
from django.template.response import TemplateResponse

from . import gecisler
from .gecisler import GecisHatasi
from .models import DurumGecmisi, Istek, Kullanici, Yorum


@admin.register(Kullanici)
class KullaniciAdmin(UserAdmin):
    list_display = ("gorunen_ad", "username", "rol", "is_active")
    list_filter = ("rol", "is_active")
    search_fields = ("gorunen_ad", "username")
    # Yalnızca veri.md'deki alanlar. E-posta, ad ve soyad formda gösterilmez.
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Askıda İyilik", {"fields": ("gorunen_ad", "rol", "is_active")}),
        ("Yönetim paneli", {"fields": ("is_staff", "is_superuser", "groups", "user_permissions")}),
    )
    add_fieldsets = ((None, {"classes": ("wide",), "fields": ("username", "gorunen_ad", "rol", "password1", "password2")}),)


class DurumGecmisiSatiri(admin.TabularInline):
    model = DurumGecmisi
    extra = 0
    can_delete = False
    readonly_fields = ("zaman", "eski_durum", "yeni_durum", "yapan", "notu")

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(Istek)
class IstekAdmin(admin.ModelAdmin):
    list_display = ("baslik", "kategori", "durum", "acan", "ustlenen", "olusturma_zamani")
    list_filter = ("durum", "kategori")
    search_fields = ("baslik", "aciklama")
    # Durum ve kişiler panelden elle değiştirilemez: değişiklikler yalnızca geçişlerle olur.
    readonly_fields = ("acan", "ustlenen", "durum", "olusturma_zamani", "guncelleme_zamani")
    fields = ("baslik", "aciklama", "kategori") + readonly_fields
    inlines = [DurumGecmisiSatiri]
    actions = ["gizle", "gizlemeyi_kaldir"]

    def has_add_permission(self, request):
        return False

    @admin.action(description="Seçili istekleri gizle (gerekçe sorulur)")
    def gizle(self, request, queryset):
        gerekce = request.POST.get("gerekce", "").strip()
        if "uygula" in request.POST:
            for istek in queryset:
                try:
                    gecisler.gizle(istek.pk, request.user, gerekce)
                except GecisHatasi as hata:
                    self.message_user(request, f"{istek}: {hata}", messages.ERROR)
                    return None
            self.message_user(request, f"{queryset.count()} istek gizlendi.")
            return None
        return TemplateResponse(request, "admin/istekler/gizle.html", {
            **self.admin_site.each_context(request), "istekler": queryset, "title": "İstekleri gizle",
        })

    @admin.action(description="Seçili isteklerde gizlemeyi kaldır")
    def gizlemeyi_kaldir(self, request, queryset):
        for istek in queryset:
            try:
                gecisler.gizlemeyi_kaldir(istek.pk, request.user)
            except GecisHatasi as hata:
                self.message_user(request, f"{istek}: {hata}", messages.ERROR)


@admin.register(Yorum)
class YorumAdmin(admin.ModelAdmin):
    list_display = ("metin", "yazan", "istek", "gizli", "zaman")
    list_filter = ("gizli",)
    readonly_fields = ("istek", "yazan", "metin", "zaman", "tesekkur")
    actions = ["gizle"]

    def has_add_permission(self, request):
        return False

    @admin.action(description="Seçili yorumları gizle")
    def gizle(self, request, queryset):
        queryset.update(gizli=True)
