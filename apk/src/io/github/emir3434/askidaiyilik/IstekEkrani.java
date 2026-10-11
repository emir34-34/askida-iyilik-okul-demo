package io.github.emir3434.askidaiyilik;

import android.app.AlertDialog;
import android.view.Gravity;
import android.view.View;
import android.widget.EditText;
import android.widget.FrameLayout;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

/**
 * E4: İstek sayfası. Düğmeler sunucunun söylediğine göre çizilir ("dugmeler" alanı), yani role ve
 * duruma göre değişir. Bu yalnızca görünüş: biri düğmeyi bir şekilde görse bile sunucu kontrol eder.
 */
public class IstekEkrani extends Ekran {

    private final int no;
    private CekYenile liste;
    private LinearLayout yorumCubugu;
    private EditText yorumGirdi;

    public IstekEkrani(MainActivity a, int no) {
        super(a);
        this.no = no;
    }

    @Override
    String baslik() {
        return "İstek";
    }

    @Override
    protected View kur() {
        LinearLayout sutun = new LinearLayout(a);
        sutun.setOrientation(LinearLayout.VERTICAL);
        liste = new CekYenile(a);
        liste.yenilenince(this::yenile);
        sutun.addView(liste, new LinearLayout.LayoutParams(-1, 0, 1));

        // Altta sabit yorum çubuğu (Reddit gibi). Konuşma herkese açık, özel mesaj yok (T-01).
        yorumCubugu = new LinearLayout(a);
        yorumCubugu.setGravity(Gravity.CENTER_VERTICAL);
        yorumCubugu.setBackgroundColor(t.kart);
        yorumCubugu.setPadding(t.dp(12), t.dp(8), t.dp(8), t.dp(8));
        yorumGirdi = girdi("Yorum ekle...", false, false);
        yorumGirdi.setBackground(t.yuvarlak(t.hap, 999));
        yorumCubugu.addView(yorumGirdi, new LinearLayout.LayoutParams(0, -2, 1));
        TextView gonder = t.dugme("Gönder", true);
        LinearLayout.LayoutParams lp = new LinearLayout.LayoutParams(-2, -2);
        lp.setMargins(t.dp(8), 0, 0, 0);
        yorumCubugu.addView(gonder, lp);
        gonder.setOnClickListener(v -> {
            String metin = yorumGirdi.getText().toString().trim();
            if (metin.isEmpty()) return;
            eylem("yorum", "metin", metin);
            yorumGirdi.setText("");
        });
        yorumCubugu.setVisibility(View.GONE);
        sutun.addView(t.cizgi());
        sutun.addView(yorumCubugu);
        return sutun;
    }

    @Override
    void yenile() {
        api.get("istekler/" + no, c -> {
            liste.bitti();
            if (a.sorunVarMi(c)) return;
            if (!c.tamam()) {
                liste.liste.removeAllViews();
                liste.liste.addView(bos("🔎", "İstek bulunamadı", c.hata(), "Akışa dön", () -> a.sekmeyeGec("akis")));
                yorumCubugu.setVisibility(View.GONE);
                return;
            }
            ciz(c.veri);
        });
    }

    private void ciz(JSONObject i) {
        LinearLayout l = liste.liste;
        l.removeAllViews();

        LinearLayout k = new LinearLayout(a);
        k.setOrientation(LinearLayout.VERTICAL);
        k.setBackgroundColor(t.kart);
        k.setPadding(t.dp(16), t.dp(14), t.dp(16), t.dp(16));
        k.addView(meta(i));
        TextView b = t.yazi(i.optString("baslik"), 21, 700, t.metin);
        b.setPadding(0, t.dp(8), 0, t.dp(8));
        k.addView(b);
        k.addView(flair(i));
        TextView g = t.yazi(i.optString("aciklama"), 16, 400, t.metin);
        g.setLineSpacing(0, 1.25f);
        k.addView(g);
        k.addView(dugmeler(i.optJSONArray("dugmeler")));
        l.addView(k);
        l.addView(t.cizgi());

        // Yorumlar
        LinearLayout y = new LinearLayout(a);
        y.setOrientation(LinearLayout.VERTICAL);
        y.setBackgroundColor(t.kart);
        y.setPadding(t.dp(16), t.dp(14), t.dp(16), t.dp(20));
        LinearLayout.LayoutParams ylp = new LinearLayout.LayoutParams(-1, -2);
        ylp.setMargins(0, t.dp(8), 0, 0);
        LinearLayout ust = new LinearLayout(a);
        ust.setGravity(Gravity.BOTTOM);
        ust.addView(t.yazi("Yorumlar", 15, 700, t.metin));
        ust.addView(t.yazi("  · herkese açık", 13, 400, t.soluk));
        y.addView(ust);
        JSONArray yorumlar = i.optJSONArray("yorumlar");
        if (yorumlar == null || yorumlar.length() == 0) {
            TextView yok = t.yazi("Henüz yorum yok.", 14, 400, t.soluk);
            yok.setPadding(0, t.dp(12), 0, 0);
            y.addView(yok);
        } else {
            for (int n = 0; n < yorumlar.length(); n++) y.addView(yorum(yorumlar.optJSONObject(n)));
        }
        l.addView(y, ylp);
        yorumCubugu.setVisibility(i.optBoolean("yorum_yazilabilir") ? View.VISIBLE : View.GONE);
    }

    private View yorum(JSONObject y) {
        boolean tesekkur = y.optBoolean("tesekkur");
        JSONObject yazan = y.optJSONObject("yazan");
        LinearLayout satir = new LinearLayout(a);
        satir.setPadding(0, t.dp(14), 0, 0);
        satir.addView(t.rozet(yazan.optString("bas_harfler"), 32, 12));
        LinearLayout sag = new LinearLayout(a);
        sag.setOrientation(LinearLayout.VERTICAL);
        sag.setPadding(t.dp(10), tesekkur ? t.dp(6) : 0, t.dp(10), tesekkur ? t.dp(8) : 0);
        if (tesekkur) {
            // Teşekkür notu vurgulu gösterilir, hiçbir yerde sayılmaz (E13)
            android.graphics.drawable.GradientDrawable z = t.yuvarlak((t.marka & 0x00FFFFFF) | 0x14000000, 10);
            sag.setBackground(z);
        }
        String ust = (tesekkur ? "💛 " : "") + yazan.optString("gorunen_ad") + (tesekkur ? " teşekkür etti" : "")
                + " · " + zamanOnce(y.optString("zaman"));
        sag.addView(t.yazi(ust, 12, 600, t.soluk));
        TextView m = t.yazi(y.optString("metin"), 15, 400, t.metin);
        m.setPadding(0, t.dp(4), 0, 0);
        sag.addView(m);
        LinearLayout.LayoutParams lp = new LinearLayout.LayoutParams(0, -2, 1);
        lp.setMargins(t.dp(10), 0, 0, 0);
        satir.addView(sag, lp);
        return satir;
    }

    /** Sunucunun bu kişi için izin verdiği düğmeler (ekranlar.md E4 tablosu). */
    private View dugmeler(JSONArray d) {
        LinearLayout kutu = new LinearLayout(a);
        if (d == null || d.length() == 0) return kutu;
        kutu.setOrientation(LinearLayout.VERTICAL);
        kutu.setPadding(t.dp(12), t.dp(10), t.dp(12), t.dp(12));
        android.graphics.drawable.GradientDrawable z = t.yuvarlak(t.kart, 12);
        z.setStroke(Math.max(1, t.dp(1)), t.cizgi, t.dp(4), t.dp(3));
        kutu.setBackground(z);
        LinearLayout.LayoutParams klp = new LinearLayout.LayoutParams(-1, -2);
        klp.setMargins(0, t.dp(14), 0, 0);
        kutu.setLayoutParams(klp);
        kutu.addView(t.yazi("Senin için:", 12, 500, t.soluk));
        LinearLayout satir = new LinearLayout(a);
        satir.setPadding(0, t.dp(8), 0, 0);
        kutu.addView(satir);
        for (int n = 0; n < d.length(); n++) {
            String ad = d.optString(n);
            TextView b;
            switch (ad) {
                case "ustlen": b = t.dugme("Üstlen", true); b.setOnClickListener(v -> eylem("ustlen", null, null)); break;
                case "yapildi": b = t.dugme("Yapıldı", true); b.setOnClickListener(v -> eylem("yapildi", null, null)); break;
                case "birak": b = t.dugme("Bırak", false); b.setOnClickListener(v -> eylem("birak", null, null)); break;
                case "geri_cek": b = t.dugme("Geri çek", false); b.setOnClickListener(v -> eylem("geri_cek", null, null)); break;
                case "onayla": b = t.dugme("Onayla", true); b.setOnClickListener(v -> onayPenceresi()); break;
                case "yapilmadi": b = t.dugme("Yapılmadı", false); b.setOnClickListener(v -> yapilmadiPenceresi()); break;
                default: continue;
            }
            LinearLayout.LayoutParams lp = new LinearLayout.LayoutParams(-2, -2);
            lp.setMargins(0, 0, t.dp(8), 0);
            satir.addView(b, lp);
        }
        return kutu;
    }

    /** E13: Onayla, isteğe bağlı teşekkür notuyla. */
    private void onayPenceresi() {
        EditText not = girdi("Çok sağ ol! 🙏", false, true);
        pencere("İşi onayla", "Teşekkür notu isteğe bağlı. Yazarsan isteğin altında herkese görünür.", not, "Onayla",
                () -> eylem("onayla", "tesekkur", not.getText().toString()));
    }

    /** G6: Yapılmadı, gerekçe zorunlu (sunucu da kontrol eder). */
    private void yapilmadiPenceresi() {
        EditText gerekce = girdi("Neyin eksik olduğunu yaz", false, true);
        pencere("Yapılmadı", "İş, üstlenen kişiye geri döner. Gerekçe yazmak zorunlu.", gerekce, "Gönder",
                () -> eylem("yapilmadi", "gerekce", gerekce.getText().toString()));
    }

    private void pencere(String baslik, String mesaj, EditText alan, String dugme, Runnable tamam) {
        FrameLayout sar = new FrameLayout(a);
        sar.setPadding(t.dp(20), t.dp(8), t.dp(20), 0);
        sar.addView(alan);
        new AlertDialog.Builder(a)
                .setTitle(baslik)
                .setMessage(mesaj)
                .setView(sar)
                .setPositiveButton(dugme, (d, w) -> tamam.run())
                .setNegativeButton("Vazgeç", null)
                .show();
    }

    private static final java.util.Map<String, String> BASARI = new java.util.HashMap<>();
    static {
        BASARI.put("ustlen", "İsteği üstlendin.");
        BASARI.put("birak", "İşi bıraktın. İstek yeniden açık.");
        BASARI.put("yapildi", "Harika! Şimdi isteği açan kişinin onayı bekleniyor.");
        BASARI.put("geri_cek", "İsteğini geri çektin.");
        BASARI.put("onayla", "Teşekkürler! İstek tamamlandı.");
        BASARI.put("yapilmadi", "İstek yeniden üstlenen kişiye döndü.");
        BASARI.put("yorum", "Yorumun eklendi.");
    }

    /** Bütün düğmeler aynı adrese gider: /api/istekler/<no>/<eylem>. Yetkiyi sunucu kontrol eder. */
    private void eylem(String ad, String alan, String deger) {
        JSONObject govde = new JSONObject();
        try {
            if (alan != null) govde.put(alan, deger);
        } catch (JSONException ignored) {
        }
        liste.baslat();
        api.post("istekler/" + no + "/" + ad, govde, c -> {
            liste.bitti();
            if (a.sorunVarMi(c)) return;
            if (c.tamam()) {
                a.bildir(BASARI.get(ad), false);
                ciz(c.veri);
            } else {
                a.bildir(c.hata(), true); // ör. "Bu istek az önce başka biri tarafından üstlenildi."
                yenile();
            }
        });
    }
}
