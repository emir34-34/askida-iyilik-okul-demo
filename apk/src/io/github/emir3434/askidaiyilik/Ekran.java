package io.github.emir3434.askidaiyilik;

import android.view.Gravity;
import android.view.View;
import android.widget.LinearLayout;
import android.widget.TextView;

import org.json.JSONObject;

import java.time.Duration;
import java.time.OffsetDateTime;

/**
 * Bütün ekranların ortak atası ve ekranlarda tekrar kullanılan parçalar (istek kartı, boş durum...).
 * Her ekran görünümünü bir kez kurar, veriyi yenile() ile sunucudan çeker.
 */
public abstract class Ekran {

    protected final MainActivity a;
    protected final Tema t;
    protected final Api api;
    private View gorunum;

    protected Ekran(MainActivity a) {
        this.a = a;
        this.t = a.t;
        this.api = a.api;
    }

    /** Ekranın görünümünü kurar. Bir kez çağrılır. */
    protected abstract View kur();

    /** Veriyi sunucudan yeniden çeker (varsayılan: bir şey yapmaz). */
    void yenile() {
    }

    /** Üst çubukta, geri okunun yanında gösterilen başlık. */
    String baslik() {
        return "";
    }

    final View gorunum() {
        if (gorunum == null) {
            gorunum = kur();
            yenile();
        }
        return gorunum;
    }

    // --- Ortak parçalar --------------------------------------------------------------------

    /** "az önce", "5 dk önce", "2 sa önce", "3 gün önce" */
    static String zamanOnce(String iso) {
        try {
            long sn = Math.max(0, Duration.between(OffsetDateTime.parse(iso), OffsetDateTime.now()).getSeconds());
            if (sn < 60) return "az önce";
            if (sn < 3600) return (sn / 60) + " dk önce";
            if (sn < 86400) return (sn / 3600) + " sa önce";
            return (sn / 86400) + " gün önce";
        } catch (Exception e) {
            return "";
        }
    }

    /** Kartın üst satırı: baş harfler · kategori · açan · zaman */
    protected View meta(JSONObject i) {
        LinearLayout satir = new LinearLayout(a);
        satir.setGravity(Gravity.CENTER_VERTICAL);
        JSONObject acan = i.optJSONObject("acan");
        satir.addView(t.rozet(acan.optString("bas_harfler"), 22, 9));
        TextView kat = t.yazi(i.optString("kategori_adi"), 12, 700, t.metin);
        kat.setPadding(t.dp(6), 0, t.dp(4), 0);
        satir.addView(kat);
        satir.addView(t.yazi("· " + acan.optString("gorunen_ad") + " · " + zamanOnce(i.optString("olusturma")), 12, 400, t.soluk));
        return satir;
    }

    protected View flair(JSONObject i) {
        JSONObject u = i.optJSONObject("ustlenen");
        TextView f = t.flair(i.optString("durum"), i.optString("durum_adi"), u == null ? null : u.optString("gorunen_ad"));
        LinearLayout.LayoutParams lp = new LinearLayout.LayoutParams(-2, -2);
        lp.setMargins(0, t.dp(2), 0, t.dp(8));
        f.setLayoutParams(lp);
        return f;
    }

    /** Akışta ve görevlerde gösterilen Reddit tarzı istek kartı (ekranlar.md E2). */
    protected View istekKarti(JSONObject i) {
        LinearLayout k = new LinearLayout(a);
        k.setOrientation(LinearLayout.VERTICAL);
        k.setPadding(t.dp(16), t.dp(12), t.dp(16), t.dp(12));
        k.setBackground(t.dalga(t.yuvarlak(t.kart, 0), 0));
        k.addView(meta(i));
        TextView b = t.yazi(i.optString("baslik"), 17, 700, t.metin);
        b.setPadding(0, t.dp(6), 0, t.dp(6));
        k.addView(b);
        k.addView(flair(i));
        TextView g = t.yazi(i.optString("aciklama"), 15, 400, t.metin);
        g.setMaxLines(2);
        g.setEllipsize(android.text.TextUtils.TruncateAt.END);
        g.setPadding(0, 0, 0, t.dp(10));
        k.addView(g);
        k.addView(yorumHapi(i.optInt("yorum_sayisi")));
        final int no = i.optInt("no");
        k.setOnClickListener(v -> a.ac(new IstekEkrani(a, no)));
        return k;
    }

    protected View yorumHapi(int sayi) {
        LinearLayout h = new LinearLayout(a);
        h.setGravity(Gravity.CENTER_VERTICAL);
        h.setPadding(t.dp(12), t.dp(7), t.dp(12), t.dp(7));
        h.setBackground(t.yuvarlak(t.hap, 999));
        h.addView(a.simge(R.drawable.i_yorum, t.metin), new LinearLayout.LayoutParams(t.dp(16), t.dp(16)));
        TextView s = t.yazi(" " + sayi, 13, 700, t.metin);
        h.addView(s);
        h.setLayoutParams(new LinearLayout.LayoutParams(-2, -2));
        return h;
    }

    /** Gösterilecek bir şey yokken (ekranlar.md E14). */
    protected View bos(String simge, String baslik, String aciklama, String dugme, Runnable tikla) {
        LinearLayout k = new LinearLayout(a);
        k.setOrientation(LinearLayout.VERTICAL);
        k.setGravity(Gravity.CENTER_HORIZONTAL);
        k.setPadding(t.dp(24), t.dp(48), t.dp(24), t.dp(48));
        k.addView(t.yazi(simge, 40, 400, t.metin));
        TextView b = t.yazi(baslik, 17, 700, t.metin);
        b.setPadding(0, t.dp(10), 0, t.dp(6));
        k.addView(b);
        TextView ac = t.yazi(aciklama, 14, 400, t.soluk);
        ac.setGravity(Gravity.CENTER);
        ac.setPadding(0, 0, 0, t.dp(16));
        k.addView(ac);
        if (dugme != null) {
            TextView d = t.dugme(dugme, true);
            d.setOnClickListener(v -> tikla.run());
            k.addView(d);
        }
        return k;
    }

    /** Yazı kutusu (giriş, yeni istek, yorum). */
    protected android.widget.EditText girdi(String ipucu, boolean sifre, boolean cokSatir) {
        android.widget.EditText e = new android.widget.EditText(a);
        e.setHint(ipucu);
        e.setHintTextColor(t.soluk);
        e.setTextColor(t.metin);
        e.setTextSize(15);
        e.setTypeface(t.yazi(400));
        e.setPadding(t.dp(14), t.dp(12), t.dp(14), t.dp(12));
        android.graphics.drawable.GradientDrawable g = t.yuvarlak(t.kart, 12);
        g.setStroke(Math.max(1, t.dp(1)), t.cizgi);
        e.setBackground(g);
        if (sifre) {
            e.setInputType(android.text.InputType.TYPE_CLASS_TEXT | android.text.InputType.TYPE_TEXT_VARIATION_PASSWORD);
        } else if (cokSatir) {
            e.setInputType(android.text.InputType.TYPE_CLASS_TEXT | android.text.InputType.TYPE_TEXT_FLAG_MULTI_LINE
                    | android.text.InputType.TYPE_TEXT_FLAG_CAP_SENTENCES);
            e.setMinLines(4);
            e.setGravity(Gravity.TOP | Gravity.START);
        } else {
            e.setInputType(android.text.InputType.TYPE_CLASS_TEXT | android.text.InputType.TYPE_TEXT_FLAG_CAP_SENTENCES);
            e.setSingleLine(true);
        }
        return e;
    }

    /** Küçük gri alan başlığı ("Kullanıcı adı" gibi). */
    protected TextView etiket(String s) {
        TextView e = t.yazi(s, 12, 600, t.soluk);
        e.setPadding(t.dp(2), t.dp(12), 0, t.dp(6));
        return e;
    }

    protected LinearLayout.LayoutParams kenarli(int ust, int alt) {
        LinearLayout.LayoutParams lp = new LinearLayout.LayoutParams(-1, -2);
        lp.setMargins(0, t.dp(ust), 0, t.dp(alt));
        return lp;
    }
}
