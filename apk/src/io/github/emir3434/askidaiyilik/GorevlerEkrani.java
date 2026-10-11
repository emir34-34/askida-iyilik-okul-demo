package io.github.emir3434.askidaiyilik;

import android.view.View;

/** E5: Görevler. Açtıklarım ve üstlendiklerim. Kişi başına toplam sayı gösterilmez (T-02). */
public class GorevlerEkrani extends ListeEkrani {

    private String sekme = "actiklarim";

    public GorevlerEkrani(MainActivity a) {
        super(a);
    }

    @Override
    protected String adres() {
        return "gorevler?sekme=" + sekme;
    }

    @Override
    protected void cipleriKur() {
        cip("Açtıklarım", sekme.equals("actiklarim"), () -> degistir("actiklarim"));
        cip("Üstlendiklerim", sekme.equals("ustlendiklerim"), () -> degistir("ustlendiklerim"));
    }

    private void degistir(String s) {
        sekme = s;
        cipleriCiz();
        liste.baslat();
        yenile();
    }

    @Override
    protected View bosGorunum() {
        return bos("📋", "Henüz bir işin yok", "Açtığın ve üstlendiğin istekler burada görünür.",
                "Açık isteklere bak", () -> a.sekmeyeGec("akis"));
    }
}
