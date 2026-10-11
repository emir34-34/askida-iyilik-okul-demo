package io.github.emir3434.askidaiyilik;

import android.content.Context;
import android.content.res.ColorStateList;
import android.content.res.Configuration;
import android.graphics.Typeface;
import android.graphics.drawable.Drawable;
import android.graphics.drawable.GradientDrawable;
import android.graphics.drawable.RippleDrawable;
import android.util.TypedValue;
import android.view.Gravity;
import android.view.View;
import android.widget.TextView;

/**
 * Renkler, yazı tipi ve sık kullanılan görünüm parçaları.
 * Renkler ekran-taslaklari/index.html ve demo/istemci/stil.css ile aynı (ekranlar.md).
 * Telefon koyu temadaysa koyu renkler kullanılır.
 */
public class Tema {

    public final boolean koyu;
    public final int sayfa, kart, metin, soluk, cizgi, hap, hapBasili, marka, markaUstu, tehlike;
    public final int acik, acikZemin, ustlenildi, ustlenildiZemin, yapildi, yapildiZemin, kapali, kapaliZemin;
    public final int uyari, uyariZemin;

    private final Context c;
    private final Typeface[] agirliklar = new Typeface[9];

    public Tema(Context c) {
        this.c = c;
        koyu = (c.getResources().getConfiguration().uiMode & Configuration.UI_MODE_NIGHT_MASK)
                == Configuration.UI_MODE_NIGHT_YES;
        if (koyu) {
            sayfa = 0xFF0E1113; kart = 0xFF181C1F; metin = 0xFFE3E6E8; soluk = 0xFF8BA2AD; cizgi = 0xFF2A3236;
            hap = 0xFF2A3236; hapBasili = 0xFF333D42; marka = 0xFFFF5A1F; markaUstu = 0xFF1A0A03; tehlike = 0xFFFF7B72;
            acik = 0xFF4AC26B; acikZemin = 0xFF12301C; ustlenildi = 0xFFE3B341; ustlenildiZemin = 0xFF3A2E0B;
            yapildi = 0xFF6EA8FE; yapildiZemin = 0xFF102A4C; kapali = 0xFF9AA4AE; kapaliZemin = 0xFF262C31;
            uyari = 0xFFFFA657; uyariZemin = 0xFF3A250D;
        } else {
            sayfa = 0xFFF6F7F8; kart = 0xFFFFFFFF; metin = 0xFF1C1C1C; soluk = 0xFF576F76; cizgi = 0xFFE5EBEE;
            hap = 0xFFEAEDEF; hapBasili = 0xFFDBE0E3; marka = 0xFFD93A00; markaUstu = 0xFFFFFFFF; tehlike = 0xFFCF222E;
            acik = 0xFF1A7F37; acikZemin = 0xFFDCF5E3; ustlenildi = 0xFF9A6700; ustlenildiZemin = 0xFFFFF1C2;
            yapildi = 0xFF0A58CA; yapildiZemin = 0xFFDBE8FF; kapali = 0xFF57606A; kapaliZemin = 0xFFEAEEF2;
            uyari = 0xFFB35900; uyariZemin = 0xFFFFF0E0;
        }
    }

    public int dp(float d) {
        return Math.round(TypedValue.applyDimension(TypedValue.COMPLEX_UNIT_DIP, d, c.getResources().getDisplayMetrics()));
    }

    /** Reddit Sans yazı tipi, istenen kalınlıkta (400 normal ... 800 çok kalın). Uygulamanın içinden yüklenir. */
    public Typeface yazi(int kalinlik) {
        int i = kalinlik / 100;
        if (agirliklar[i] == null) {
            try {
                agirliklar[i] = new Typeface.Builder(c.getAssets(), "yazitipi/RedditSans.ttf")
                        .setFontVariationSettings("'wght' " + kalinlik).build();
            } catch (Exception e) {
                agirliklar[i] = Typeface.create(Typeface.SANS_SERIF, kalinlik >= 600 ? Typeface.BOLD : Typeface.NORMAL);
            }
        }
        return agirliklar[i];
    }

    public TextView yazi(String s, float boyut, int kalinlik, int renk) {
        TextView t = new TextView(c);
        t.setText(s);
        t.setTextSize(TypedValue.COMPLEX_UNIT_SP, boyut);
        t.setTypeface(yazi(kalinlik));
        t.setTextColor(renk);
        t.setIncludeFontPadding(false);
        t.setLineSpacing(0, 1.15f);
        return t;
    }

    public GradientDrawable yuvarlak(int renk, float koseDp) {
        GradientDrawable g = new GradientDrawable();
        g.setColor(renk);
        g.setCornerRadius(dp(koseDp));
        return g;
    }

    /** Dokununca Android'in kendi dalga (ripple) efektini gösteren arka plan. */
    public Drawable dalga(Drawable zemin, float koseDp) {
        int r = koyu ? 0x33FFFFFF : 0x22000000;
        return new RippleDrawable(ColorStateList.valueOf(r), zemin, yuvarlak(0xFFFFFFFF, koseDp));
    }

    /** Hap biçimli düğme. ana: turuncu, değilse gri. */
    public TextView dugme(String s, boolean ana) {
        TextView t = yazi(s, 15, 700, ana ? markaUstu : metin);
        t.setGravity(Gravity.CENTER);
        t.setPadding(dp(18), dp(11), dp(18), dp(11));
        t.setBackground(dalga(yuvarlak(ana ? marka : hap, 999), 999));
        t.setClickable(true);
        return t;
    }

    /** Sekme ve kategori çipi. */
    public TextView cip(String s, boolean secili) {
        TextView t = yazi(s, 13, 600, secili ? kart : metin);
        t.setPadding(dp(13), dp(8), dp(13), dp(8));
        t.setBackground(dalga(yuvarlak(secili ? metin : hap, 999), 999));
        t.setClickable(true);
        return t;
    }

    /** Ad baş harfleri dairesi (profil fotoğrafı tutulmaz, T-03). */
    public TextView rozet(String basHarf, int capDp, float yaziBoyut) {
        TextView t = yazi(basHarf, yaziBoyut, 700, soluk);
        t.setGravity(Gravity.CENTER);
        GradientDrawable g = new GradientDrawable();
        g.setShape(GradientDrawable.OVAL);
        g.setColor(hap);
        t.setBackground(g);
        t.setLayoutParams(new android.widget.LinearLayout.LayoutParams(dp(capDp), dp(capDp)));
        return t;
    }

    /** İsteğin durum etiketi (flair). */
    public TextView flair(String durum, String durumAdi, String ustlenen) {
        int renk, zemin;
        String simge;
        switch (durum) {
            case "acik": renk = acik; zemin = acikZemin; simge = "🟢"; break;
            case "ustlenildi": renk = ustlenildi; zemin = ustlenildiZemin; simge = "🟡"; break;
            case "yapildi": renk = yapildi; zemin = yapildiZemin; simge = "🔵"; break;
            case "tamamlandi": renk = kapali; zemin = kapaliZemin; simge = "✅"; break;
            default: renk = kapali; zemin = kapaliZemin; simge = "⚪";
        }
        String metinS = simge + " " + durumAdi + (ustlenen != null && !durum.equals("acik") ? " · " + ustlenen : "");
        TextView t = yazi(metinS, 12, 700, renk);
        t.setPadding(dp(9), dp(3), dp(9), dp(3));
        t.setBackground(yuvarlak(zemin, 999));
        return t;
    }

    public View cizgi() {
        View v = new View(c);
        v.setBackgroundColor(cizgi);
        v.setLayoutParams(new android.widget.LinearLayout.LayoutParams(-1, Math.max(1, dp(0.7f))));
        return v;
    }
}
