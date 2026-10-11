package io.github.emir3434.askidaiyilik;

import android.view.View;
import android.widget.HorizontalScrollView;
import android.widget.LinearLayout;
import android.widget.TextView;

import org.json.JSONArray;

/**
 * Akış (E2) ve Görevler (E5) ekranlarının ortak yapısı: üstte çipler, altında aşağı çekip yenilenen
 * istek kartları listesi. Alt sınıflar hangi çiplerin gösterileceğini ve hangi adresten veri
 * çekileceğini söyler.
 */
public abstract class ListeEkrani extends Ekran {

    protected CekYenile liste;
    private LinearLayout cipler;
    private String sonVeri; // son çizilen veri; aynıysa yeniden çizilmez

    protected ListeEkrani(MainActivity a) {
        super(a);
    }

    /** Veri adresi, ör. "istekler?sekme=acik" */
    protected abstract String adres();

    /** Çip satırını doldurur (cip() ile). */
    protected abstract void cipleriKur();

    /** Liste boşken gösterilecek görünüm. */
    protected abstract View bosGorunum();

    @Override
    protected View kur() {
        LinearLayout sutun = new LinearLayout(a);
        sutun.setOrientation(LinearLayout.VERTICAL);

        HorizontalScrollView yatay = new HorizontalScrollView(a);
        yatay.setHorizontalScrollBarEnabled(false);
        yatay.setBackgroundColor(t.kart);
        cipler = new LinearLayout(a);
        cipler.setPadding(t.dp(12), t.dp(10), t.dp(12), t.dp(10));
        yatay.addView(cipler);
        sutun.addView(yatay);
        sutun.addView(t.cizgi());

        liste = new CekYenile(a);
        liste.yenilenince(this::yenile);
        sutun.addView(liste, new LinearLayout.LayoutParams(-1, 0, 1));
        cipleriCiz();
        return sutun;
    }

    protected void cipleriCiz() {
        cipler.removeAllViews();
        cipleriKur();
    }

    protected void cip(String ad, boolean secili, Runnable tikla) {
        TextView c = t.cip(ad, secili);
        c.setOnClickListener(v -> tikla.run());
        LinearLayout.LayoutParams lp = new LinearLayout.LayoutParams(-2, -2);
        lp.setMargins(0, 0, t.dp(6), 0);
        cipler.addView(c, lp);
    }

    @Override
    protected long canliAralik() {
        return 10000; // akış 10 saniyede bir güncellenir
    }

    @Override
    protected void canliSor() {
        api.get(adres(), c -> {
            if (c.tamam() && !c.veri.toString().equals(sonVeri)) listeyiCiz(c.veri);
        });
    }

    @Override
    void yenile() {
        if (liste == null) return;
        api.get(adres(), c -> {
            liste.bitti();
            if (a.sorunVarMi(c)) return;
            if (!c.tamam()) {
                a.bildir(c.hata(), true);
                return;
            }
            listeyiCiz(c.veri);
        });
    }

    private void listeyiCiz(org.json.JSONObject veri) {
        sonVeri = veri.toString();
        {
            JSONArray istekler = veri.optJSONArray("istekler");
            liste.liste.removeAllViews();
            if (istekler == null || istekler.length() == 0) {
                liste.liste.addView(bosGorunum());
                return;
            }
            for (int i = 0; i < istekler.length(); i++) {
                liste.liste.addView(istekKarti(istekler.optJSONObject(i)));
                liste.liste.addView(t.cizgi());
            }
        }
    }
}
