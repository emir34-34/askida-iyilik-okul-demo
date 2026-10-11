package io.github.emir3434.askidaiyilik;

import android.view.View;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.ScrollView;
import android.widget.TextView;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

/** E3: Yeni istek (G1). Fotoğraf yükleme yok (S-09 kararı bekleniyor). */
public class YeniEkrani extends Ekran {

    private String kategori;

    public YeniEkrani(MainActivity a) {
        super(a);
    }

    @Override
    protected View kur() {
        ScrollView kaydir = new ScrollView(a);
        LinearLayout k = new LinearLayout(a);
        k.setOrientation(LinearLayout.VERTICAL);
        k.setBackgroundColor(t.kart);
        k.setPadding(t.dp(16), t.dp(14), t.dp(16), t.dp(20));
        kaydir.addView(k);

        k.addView(t.yazi("Yeni istek", 20, 800, t.metin));

        k.addView(etiket("Kategori"));
        LinearLayout cipler = new LinearLayout(a);
        k.addView(cipler);
        JSONArray kategoriler = a.ben.optJSONArray("kategoriler");
        kategori = kategoriler != null && kategoriler.length() > 0 ? kategoriler.optJSONObject(0).optString("deger") : "";
        Runnable[] ciz = new Runnable[1];
        ciz[0] = () -> {
            cipler.removeAllViews();
            for (int i = 0; kategoriler != null && i < kategoriler.length(); i++) {
                JSONObject kat = kategoriler.optJSONObject(i);
                String deger = kat.optString("deger");
                TextView c = t.cip(kat.optString("ad"), deger.equals(kategori));
                c.setOnClickListener(v -> { kategori = deger; ciz[0].run(); });
                LinearLayout.LayoutParams lp = new LinearLayout.LayoutParams(-2, -2);
                lp.setMargins(0, 0, t.dp(6), 0);
                cipler.addView(c, lp);
            }
        };
        ciz[0].run();

        k.addView(etiket("Başlık"));
        EditText baslik = girdi("Kimya notları lazım", false, false);
        k.addView(baslik);
        k.addView(etiket("Açıklama"));
        EditText aciklama = girdi("Ne istediğini kısaca anlat.", false, true);
        k.addView(aciklama);

        TextView bilgi = t.yazi("ⓘ Telefon, adres ya da başka kişisel bilgi yazma. İstekleri okuldaki herkes görür.", 13, 400, t.soluk);
        bilgi.setPadding(t.dp(12), t.dp(10), t.dp(12), t.dp(10));
        bilgi.setBackground(t.yuvarlak(t.hap, 12));
        k.addView(bilgi, kenarli(14, 0));

        TextView yayinla = t.dugme("Yayınla", true);
        k.addView(yayinla, kenarli(16, 0));
        yayinla.setOnClickListener(v -> {
            JSONObject govde = new JSONObject();
            try {
                govde.put("baslik", baslik.getText().toString());
                govde.put("aciklama", aciklama.getText().toString());
                govde.put("kategori", kategori);
            } catch (JSONException ignored) {
            }
            yayinla.setEnabled(false);
            api.post("istekler", govde, c -> {
                yayinla.setEnabled(true);
                if (a.sorunVarMi(c)) return;
                if (!c.tamam()) {
                    a.bildir(c.hata(), true);
                    return;
                }
                a.bildir("İsteğin yayında!", false);
                baslik.setText("");
                aciklama.setText("");
                a.sekmeyeGec("akis");
                a.ac(new IstekEkrani(a, c.veri.optInt("no")));
            });
        });
        return kaydir;
    }
}
