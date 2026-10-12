"""python manage.py ornek_veri

Uydurma kullanıcıları ve okul sorunlarını oluşturur (T-04, T-08). Var olanları önce siler.
Şifre .env dosyasındaki DEMO_SIFRE değeridir (sırlar repoda yok).
Sorunlar gecisler.py'deki fonksiyonlarla oluşturulur, böylece durum geçmişi de dolar.
"""
import os

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from istekler import gecisler
from istekler.models import Kullanici, Sorun

KISILER = [
    ("ogrenci1", "Mehmet A.", Kullanici.Rol.OGRENCI),
    ("ogrenci2", "Ayşe K.", Kullanici.Rol.OGRENCI),
    ("ogrenci3", "Can B.", Kullanici.Rol.OGRENCI),
    ("ogrenci4", "Zeynep T.", Kullanici.Rol.OGRENCI),
    ("ogrenci5", "Elif S.", Kullanici.Rol.OGRENCI),
    ("ogretmen1", "Selin Öğretmen", Kullanici.Rol.OGRETMEN),
    ("yonetici1", "Kerem T.", Kullanici.Rol.YONETICI),
]


class Command(BaseCommand):
    help = "Uydurma kullanıcıları ve okul sorunlarını oluşturur (var olanları siler)."

    @transaction.atomic
    def handle(self, *args, **options):
        sifre = os.environ.get("DEMO_SIFRE", "")
        if len(sifre) < 8:
            raise CommandError("DEMO_SIFRE .env dosyasında en az 8 karakter olmalı (.env.example'a bakın).")

        Sorun.objects.all().delete()
        Kullanici.objects.filter(username__in=[k[0] for k in KISILER]).delete()
        k = {}
        for ad, gorunen, rol in KISILER:
            yonetici = rol == Kullanici.Rol.YONETICI
            k[ad] = Kullanici.objects.create_user(username=ad, password=sifre, gorunen_ad=gorunen, rol=rol,
                                                  is_staff=yonetici, is_superuser=yonetici)
        mehmet, ayse, can, zeynep, elif_ = (k[f"ogrenci{i}"] for i in range(1, 6))

        # Senaryo 1'in başlangıcı: açık bir sorun
        gecisler.bildir(zeynep, "2. kat lavabo musluğu damlıyor", "Kız tuvaletindeki soldan ikinci musluk sürekli damlıyor.")

        # Senaryo 2'nin başlangıcı: açık bir sorun
        gecisler.bildir(can, "Spor salonu kapısının kolu kırık", "Giriş kapısının sağ kanadındaki kol yerinden çıkmış.")

        # Üstlenilmiş bir sorun
        cop = gecisler.bildir(elif_, "Bahçedeki çöp kutusu taşıyor", "Kantin önündeki büyük çöp kutusu doldu, etrafa taşıyor.")
        gecisler.ustlen(cop.pk, mehmet)
        gecisler.yorum_yaz(cop.pk, mehmet, "Teneffüste görevliye haber vereceğim.")

        # Yapılmış, Mehmet'in onayını bekleyen sorun
        sabun = gecisler.bildir(mehmet, "Kantin lavabosunda sabun bitti", "Kantin yanındaki lavabonun sabunluğu boş.")
        gecisler.ustlen(sabun.pk, elif_)
        gecisler.yapildi_de(sabun.pk, elif_)

        # Tamamlanmış bir sorun
        priz = gecisler.bildir(ayse, "Kütüphanede priz çalışmıyor", "Okuma salonunda pencere kenarındaki priz çalışmıyor.")
        gecisler.ustlen(priz.pk, can)
        gecisler.yapildi_de(priz.pk, can)
        gecisler.onayla(priz.pk, ayse)

        self.stdout.write(self.style.SUCCESS(
            f"{len(KISILER)} örnek kullanıcı ve {Sorun.objects.count()} okul sorunu oluşturuldu. Şifre: .env'deki DEMO_SIFRE."
        ))
