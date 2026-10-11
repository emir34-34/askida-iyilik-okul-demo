package io.github.emir3434.askidaiyilik;

import android.app.AlertDialog;
import android.text.InputType;
import android.view.Gravity;
import android.view.View;
import android.widget.EditText;
import android.widget.FrameLayout;
import android.widget.LinearLayout;
import android.widget.ScrollView;
import android.widget.TextView;

/** E8: Profil. Yalnızca veri.md'deki alanlar. Karma, iyilik sayısı ya da fotoğraf yok (T-02, T-03). */
public class ProfilEkrani extends Ekran {

    public ProfilEkrani(MainActivity a) {
        super(a);
    }

    @Override
    protected View kur() {
        ScrollView kaydir = new ScrollView(a);
        LinearLayout k = new LinearLayout(a);
        k.setOrientation(LinearLayout.VERTICAL);
        kaydir.addView(k);

        LinearLayout ust = new LinearLayout(a);
        ust.setOrientation(LinearLayout.VERTICAL);
        ust.setGravity(Gravity.CENTER_HORIZONTAL);
        ust.setBackgroundColor(t.kart);
        ust.setPadding(t.dp(16), t.dp(24), t.dp(16), t.dp(20));
        ust.addView(t.rozet(a.ben.optString("bas_harfler"), 76, 26));
        TextView ad = t.yazi(a.ben.optString("gorunen_ad"), 21, 800, t.metin);
        ad.setPadding(0, t.dp(12), 0, t.dp(4));
        ust.addView(ad);
        ust.addView(t.yazi(a.ben.optString("kullanici_adi") + " · " + a.ben.optString("rol_adi"), 14, 400, t.soluk));
        k.addView(ust);
        k.addView(t.cizgi());

        k.addView(satir("Hakkımda hangi bilgiler tutuluyor?", null, () -> bilgiPenceresi()), kenarli(8, 0));
        k.addView(t.cizgi());
        k.addView(satir("Sunucu adresi", api.adres(), this::adresPenceresi));
        k.addView(t.cizgi());
        TextView cikis = (TextView) satir("Çıkış yap", null, this::cikisYap);
        cikis.setTextColor(t.tehlike);
        k.addView(cikis);

        TextView not = t.yazi("ⓘ Profilinde kaç iyilik yaptığın ya da puanın gösterilmez. Askıda İyilik bir yarışma değil.", 13, 400, t.soluk);
        not.setPadding(t.dp(12), t.dp(10), t.dp(12), t.dp(10));
        not.setBackground(t.yuvarlak(t.hap, 12));
        LinearLayout.LayoutParams lp = kenarli(16, 16);
        lp.setMargins(t.dp(16), t.dp(16), t.dp(16), t.dp(16));
        k.addView(not, lp);
        return kaydir;
    }

    private View satir(String baslik, String sag, Runnable tikla) {
        TextView s = t.yazi(baslik + (sag != null ? "\n" + sag : ""), 15, 500, t.metin);
        s.setPadding(t.dp(16), t.dp(15), t.dp(16), t.dp(15));
        s.setBackground(t.dalga(t.yuvarlak(t.kart, 0), 0));
        s.setOnClickListener(v -> tikla.run());
        return s;
    }

    private void bilgiPenceresi() {
        new AlertDialog.Builder(a)
                .setTitle("Hakkında tutulan bilgiler")
                .setMessage("Kullanıcı adı, görünen ad, rol ve şifrenin geri çevrilemez özeti.\n\n"
                        + "Telefon, e-posta, fotoğraf, konum ve doğum tarihi tutulmaz.")
                .setPositiveButton("Tamam", null)
                .show();
    }

    private void adresPenceresi() {
        EditText e = girdi("", false, false);
        e.setInputType(InputType.TYPE_CLASS_TEXT | InputType.TYPE_TEXT_VARIATION_URI);
        e.setText(api.adres());
        FrameLayout sar = new FrameLayout(a);
        sar.setPadding(t.dp(20), t.dp(8), t.dp(20), 0);
        sar.addView(e);
        new AlertDialog.Builder(a)
                .setTitle("Sunucu adresi")
                .setMessage("Adres değişince yeniden giriş yapman gerekir.")
                .setView(sar)
                .setPositiveButton("Kaydet", (d, w) -> {
                    api.adresiDegistir(e.getText().toString());
                    a.baslat();
                })
                .setNegativeButton("Vazgeç", null)
                .show();
    }

    private void cikisYap() {
        api.post("cikis", null, c -> a.girisGoster());
    }
}
