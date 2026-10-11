package io.github.emir3434.askidaiyilik;

import android.graphics.drawable.GradientDrawable;
import android.view.Gravity;
import android.view.View;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.ScrollView;
import android.widget.TextView;

import org.json.JSONException;
import org.json.JSONObject;

/** E1: Giriş. Kayıt ol yok, hesapları yönetici açar (V-03). */
public class GirisEkrani extends Ekran {

    public GirisEkrani(MainActivity a) {
        super(a);
    }

    @Override
    protected View kur() {
        ScrollView kaydir = new ScrollView(a);
        kaydir.setFillViewport(true);
        LinearLayout orta = new LinearLayout(a);
        orta.setGravity(Gravity.CENTER);
        orta.setPadding(t.dp(20), t.dp(24), t.dp(20), t.dp(24));
        kaydir.addView(orta);

        LinearLayout k = new LinearLayout(a);
        k.setOrientation(LinearLayout.VERTICAL);
        k.setPadding(t.dp(22), t.dp(26), t.dp(22), t.dp(22));
        k.setBackground(t.yuvarlak(t.kart, 18));
        k.setElevation(t.dp(1));
        orta.addView(k, new LinearLayout.LayoutParams(-1, -2));

        LinearLayout logoSatir = new LinearLayout(a);
        logoSatir.setGravity(Gravity.CENTER);
        TextView logo = t.yazi("🤝", 20, 400, t.markaUstu);
        logo.setGravity(Gravity.CENTER);
        GradientDrawable daire = new GradientDrawable();
        daire.setShape(GradientDrawable.OVAL);
        daire.setColor(t.marka);
        logo.setBackground(daire);
        LinearLayout.LayoutParams lp = new LinearLayout.LayoutParams(t.dp(42), t.dp(42));
        lp.setMargins(0, 0, t.dp(10), 0);
        logoSatir.addView(logo, lp);
        logoSatir.addView(t.yazi("Askıda İyilik", 24, 800, t.metin));
        k.addView(logoSatir);
        TextView alt = t.yazi("Okulumuzun iyilik panosu", 15, 400, t.soluk);
        alt.setGravity(Gravity.CENTER);
        alt.setPadding(0, t.dp(8), 0, t.dp(14));
        k.addView(alt);

        k.addView(etiket("Kullanıcı adı"));
        EditText kullanici = girdi("", false, false);
        // Büyük harf ve otomatik düzeltme olmasın (kullanıcı adları küçük harf)
        kullanici.setInputType(android.text.InputType.TYPE_CLASS_TEXT | android.text.InputType.TYPE_TEXT_FLAG_NO_SUGGESTIONS);
        kullanici.setTypeface(t.yazi(400));
        kullanici.setImeOptions(android.view.inputmethod.EditorInfo.IME_ACTION_NEXT);
        k.addView(kullanici);
        k.addView(etiket("Şifre"));
        EditText sifre = girdi("", true, false);
        sifre.setImeOptions(android.view.inputmethod.EditorInfo.IME_ACTION_DONE);
        k.addView(sifre);

        TextView giris = t.dugme("Giriş yap", true);
        k.addView(giris, kenarli(20, 0));
        giris.setOnClickListener(v -> {
            giris.setEnabled(false);
            giris.setAlpha(0.6f);
            JSONObject govde = new JSONObject();
            try {
                govde.put("kullanici_adi", kullanici.getText().toString().trim());
                govde.put("sifre", sifre.getText().toString());
            } catch (JSONException ignored) {
            }
            // Önce csrftoken çerezini al (Django veri değiştiren istekte ister), sonra giriş yap.
            api.get("ben", c0 -> api.post("giris", govde, c -> {
                giris.setEnabled(true);
                giris.setAlpha(1f);
                if (c.kod == 0) {
                    a.sunucuyuSor();
                } else if (!c.tamam()) {
                    a.bildir(c.hata(), true);
                } else {
                    a.ben = c.veri;
                    api.get("ben", c2 -> a.sekmeyeGec("akis")); // girişten sonra yeni csrftoken
                }
            }));
        });

        // Klavyedeki "Bitti" tuşu doğrudan giriş yapar
        sifre.setOnEditorActionListener((v, eylem, olay) -> {
            if (eylem == android.view.inputmethod.EditorInfo.IME_ACTION_DONE) {
                giris.performClick();
                return true;
            }
            return false;
        });

        TextView unuttum = t.yazi("Şifreni unuttuysan okul yöneticisine başvur.", 13, 400, t.soluk);
        unuttum.setGravity(Gravity.CENTER);
        unuttum.setPadding(0, t.dp(16), 0, t.dp(12));
        k.addView(unuttum);
        TextView demo = t.yazi("Demo · yalnızca örnek kullanıcılar", 13, 500, t.soluk);
        demo.setGravity(Gravity.CENTER);
        demo.setPadding(t.dp(10), t.dp(10), t.dp(10), t.dp(10));
        demo.setBackground(t.yuvarlak(t.hap, 12));
        k.addView(demo);
        return kaydir;
    }
}
