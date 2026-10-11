package io.github.emir3434.askidaiyilik;

import android.view.View;

import org.json.JSONArray;
import org.json.JSONObject;

/** E2: Ana akış. Sekmeler (Yeni, Açık olanlar) ve kategori çipleri. */
public class AkisEkrani extends ListeEkrani {

    private String sekme = "yeni";
    private String kategori = "";

    public AkisEkrani(MainActivity a) {
        super(a);
    }

    @Override
    protected String adres() {
        return "istekler?sekme=" + sekme + "&k=" + kategori;
    }

    @Override
    protected void cipleriKur() {
        cip("Yeni", !sekme.equals("acik"), () -> degistir("yeni", kategori));
        cip("Açık olanlar", sekme.equals("acik"), () -> degistir("acik", kategori));
        JSONArray kategoriler = a.ben.optJSONArray("kategoriler");
        for (int i = 0; kategoriler != null && i < kategoriler.length(); i++) {
            JSONObject k = kategoriler.optJSONObject(i);
            final String deger = k.optString("deger");
            cip(k.optString("ad"), deger.equals(kategori), () -> degistir(sekme, deger.equals(kategori) ? "" : deger));
        }
    }

    private void degistir(String yeniSekme, String yeniKategori) {
        sekme = yeniSekme;
        kategori = yeniKategori;
        cipleriCiz();
        liste.baslat();
        yenile();
    }

    @Override
    protected View bosGorunum() {
        return bos("🌱", "Şu an açık istek yok",
                "Bir ihtiyacın ya da okulda gördüğün bir sorun varsa ilk isteği sen aç.",
                "＋ İstek aç", () -> a.sekmeyeGec("olustur"));
    }
}
