"""python manage.py ornek_veri

senaryolar.md'deki uydurma kişileri ve istekleri oluşturur. Gerçek öğrenci verisi yoktur (T-04).
Bütün örnek kullanıcıların şifresi .env dosyasındaki DEMO_SIFRE değeridir (sırlar repoda yok).
İstekler doğrudan veritabanına yazılmaz, gecisler.py'deki fonksiyonlarla oluşturulur. Böylece
durum geçmişi de gerçek kullanımdaki gibi dolar.
"""
import os

from django.contrib.auth.models import Permission
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from istekler import gecisler
from istekler.models import Istek, Kullanici

KISILER = [
    # kullanıcı adı, görünen ad, rol
    ("ogrenci1", "Mehmet A.", Kullanici.Rol.OGRENCI),
    ("ogrenci2", "Ayşe K.", Kullanici.Rol.OGRENCI),
    ("ogrenci3", "Can B.", Kullanici.Rol.OGRENCI),
    ("ogrenci4", "Zeynep T.", Kullanici.Rol.OGRENCI),
    ("ogrenci5", "Elif S.", Kullanici.Rol.OGRENCI),
    ("ogretmen1", "Selin Öğretmen", Kullanici.Rol.OGRETMEN),
    ("yonetici1", "Kerem T.", Kullanici.Rol.YONETICI),
]

# Öğretmenin yönetim panelinde yapabilecekleri: istekleri ve yorumları görüp gizlemek
OGRETMEN_IZINLERI = ["view_istek", "change_istek", "view_yorum", "change_yorum", "view_durumgecmisi"]


class Command(BaseCommand):
    help = "Senaryolardaki uydurma kullanıcıları ve istekleri oluşturur (önce var olanları siler)."

    @transaction.atomic
    def handle(self, *args, **options):
        sifre = os.environ.get("DEMO_SIFRE", "")
        if len(sifre) < 8:
            raise CommandError("DEMO_SIFRE .env dosyasında en az 8 karakter olmalı (.env.example'a bakın).")

        Istek.objects.all().delete()
        Kullanici.objects.filter(username__in=[k[0] for k in KISILER]).delete()

        k = {}
        for kullanici_adi, gorunen_ad, rol in KISILER:
            k[kullanici_adi] = Kullanici.objects.create_user(
                username=kullanici_adi, password=sifre, gorunen_ad=gorunen_ad, rol=rol,
                is_staff=rol != Kullanici.Rol.OGRENCI,
                is_superuser=rol == Kullanici.Rol.YONETICI,
            )
        k["ogretmen1"].user_permissions.set(Permission.objects.filter(codename__in=OGRETMEN_IZINLERI))

        mehmet, ayse, can, zeynep, elif_, selin = (k[a] for a in ("ogrenci1", "ogrenci2", "ogrenci3", "ogrenci4", "ogrenci5", "ogretmen1"))

        # Senaryo 1'in başlangıcı: Mehmet'in açık isteği (demoda canlı yürütülecek)
        gecisler.istek_ac(mehmet, "Kimya notları lazım",
                          "Salı günkü dersin notlarına ihtiyacım var. Defterimi kaybettim, fotokopi çekip geri verebilirim.", "ders")

        # Üstlenilmiş bir okul sorunu
        lavabo = gecisler.istek_ac(zeynep, "2. kat lavabo musluğu akıtıyor",
                                   "Kız tuvaletindeki soldan ikinci musluk sürekli akıyor.", "okul")
        gecisler.ustlen(lavabo.pk, ayse)
        gecisler.yorum_yaz(lavabo.pk, ayse, "Hademe ablaya söyleyeceğim, yarın bakarlar.")

        # Yapılmış, Can'ın onayını bekleyen iş
        hesap = gecisler.istek_ac(can, "Hesap makinesi ödünç lazım",
                                  "Perşembe fizik sınavı için bilimsel hesap makinesi lazım, sınavdan sonra geri veririm.", "esya")
        gecisler.ustlen(hesap.pk, mehmet)
        gecisler.yorum_yaz(hesap.pk, mehmet, "Bende yedek var, yarın getiririm.")
        gecisler.yapildi_de(hesap.pk, mehmet)

        # Henüz kimsenin üstlenmediği bir istek
        gecisler.istek_ac(elif_, "İngilizce konuşma pratiği yapacak arkadaş arıyorum",
                          "Öğle arasında 15 dakika konuşma pratiği yapabiliriz.", "ders")

        # Tamamlanmış bir iş, teşekkür notuyla (arşivde görünür)
        priz = gecisler.istek_ac(zeynep, "Kütüphanede priz çalışmıyor",
                                 "Okuma salonundaki pencere kenarındaki priz çalışmıyor.", "okul")
        gecisler.ustlen(priz.pk, can)
        gecisler.yapildi_de(priz.pk, can)
        gecisler.onayla(priz.pk, zeynep, "Hademe abiye haber verdiğin için sağ ol, artık çalışıyor!")

        # Öğretmenin gizlediği uygunsuz istek (Senaryo 4)
        borc = gecisler.istek_ac(can, "Biri bana 50 TL borç versin", "Numaramı yazıyorum, arayın.", "esya")
        gecisler.gizle(borc.pk, selin, "Para isteği ve kişisel bilgi içeriyor.")

        self.stdout.write(self.style.SUCCESS(
            f"{len(KISILER)} örnek kullanıcı ve {Istek.objects.count()} istek oluşturuldu. "
            "Şifre: .env dosyasındaki DEMO_SIFRE."
        ))
