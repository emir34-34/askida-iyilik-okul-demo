package io.github.emir3434.askidaiyilik;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.res.ColorStateList;
import android.os.Bundle;
import android.text.InputType;
import android.view.Gravity;
import android.view.View;
import android.view.ViewGroup;
import android.view.Window;
import android.view.animation.DecelerateInterpolator;
import android.widget.EditText;
import android.widget.FrameLayout;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;

import org.json.JSONObject;

import java.util.ArrayDeque;

/**
 * Askıda İyilik native Android uygulaması: ana pencere.
 *
 * Ekranlar Android'in kendi bileşenleriyle çizilir (WebView yok). Sunucudan yalnızca /api/
 * adreslerinden veri gelir (Api sınıfı). Kim neyi yapabilir kuralları sunucudadır (T-07).
 *
 * Pencere düzeni (ekranlar.md):  üst çubuk / değişen ekran / alt menü (Akış, Oluştur, Görevler, Profil)
 * Ekranlar bir yığında tutulur: istek sayfası açılınca yığına eklenir, geri tuşu bir öncekine döner.
 */
public class MainActivity extends Activity {

    Tema t;
    Api api;
    JSONObject ben; // giriş yapan kişi (/api/ben)

    private FrameLayout kokKatman;
    private LinearLayout ustCubuk, altMenu;
    private FrameLayout icerik;
    private final ArrayDeque<Ekran> yigin = new ArrayDeque<>();
    private String seciliSekme = "akis";
    private boolean pencereAcik = false;

    @Override
    protected void onCreate(Bundle kayitliDurum) {
        super.onCreate(kayitliDurum);
        t = new Tema(this);
        api = new Api(this);
        pencereyiBoya();

        LinearLayout sutun = new LinearLayout(this);
        sutun.setOrientation(LinearLayout.VERTICAL);
        ustCubuk = new LinearLayout(this);
        icerik = new FrameLayout(this);
        altMenu = new LinearLayout(this);
        sutun.addView(ustCubuk, new LinearLayout.LayoutParams(-1, t.dp(56)));
        sutun.addView(t.cizgi());
        sutun.addView(icerik, new LinearLayout.LayoutParams(-1, 0, 1));
        sutun.addView(t.cizgi());
        sutun.addView(altMenu, new LinearLayout.LayoutParams(-1, t.dp(60)));

        kokKatman = new FrameLayout(this);
        kokKatman.setBackgroundColor(t.sayfa);
        kokKatman.addView(sutun);
        setContentView(kokKatman);

        baslat();
    }

    /** Durum ve gezinme çubuklarını uygulamanın renklerine boyar (native görünüm). */
    private void pencereyiBoya() {
        Window w = getWindow();
        w.setStatusBarColor(t.kart);
        w.setNavigationBarColor(t.kart);
        if (!t.koyu) {
            w.getDecorView().setSystemUiVisibility(
                    View.SYSTEM_UI_FLAG_LIGHT_STATUS_BAR | View.SYSTEM_UI_FLAG_LIGHT_NAVIGATION_BAR);
        }
    }

    /** Açılışta oturum var mı bakar: varsa akış, yoksa giriş ekranı. */
    void baslat() {
        api.get("ben", c -> {
            if (c.tamam()) {
                ben = c.veri;
                sekmeyeGec("akis");
            } else if (c.kod == 401) {
                girisGoster();
            } else {
                sunucuyuSor();
            }
        });
    }

    // --- Gezinme ---------------------------------------------------------------------------

    void girisGoster() {
        ben = null;
        yigin.clear();
        ustCubuk.setVisibility(View.GONE);
        altMenu.setVisibility(View.GONE);
        ekraniKoy(new GirisEkrani(this), false);
    }

    /** Alt menüden bir sekmeye geçer (yığın sıfırlanır). */
    void sekmeyeGec(String sekme) {
        seciliSekme = sekme;
        yigin.clear();
        ustCubuk.setVisibility(View.VISIBLE);
        altMenu.setVisibility(View.VISIBLE);
        Ekran e;
        switch (sekme) {
            case "olustur": e = new YeniEkrani(this); break;
            case "gorevler": e = new GorevlerEkrani(this); break;
            case "profil": e = new ProfilEkrani(this); break;
            default: e = new AkisEkrani(this);
        }
        yigin.push(e);
        ekraniKoy(e, false);
        cubuklariCiz();
    }

    /** Yeni bir ekranı yığının üstüne açar (ör. istek sayfası), sağdan kayarak gelir. */
    void ac(Ekran e) {
        yigin.push(e);
        ekraniKoy(e, true);
        cubuklariCiz();
    }

    void geri() {
        if (yigin.size() > 1) {
            yigin.pop();
            Ekran onceki = yigin.peek();
            ekraniKoy(onceki, false);
            onceki.yenile(); // geri dönünce veri güncellensin (ör. az önce onaylanan istek)
            cubuklariCiz();
        } else {
            finish();
        }
    }

    @Override
    public void onBackPressed() {
        if (ben != null && yigin.size() <= 1 && !seciliSekme.equals("akis")) sekmeyeGec("akis");
        else geri();
    }

    private void ekraniKoy(Ekran e, boolean kaydir) {
        icerik.removeAllViews();
        View v = e.gorunum();
        if (v.getParent() != null) ((ViewGroup) v.getParent()).removeView(v);
        icerik.addView(v, new FrameLayout.LayoutParams(-1, -1));
        if (kaydir) {
            v.setTranslationX(t.dp(80));
            v.setAlpha(0f);
            v.animate().translationX(0).alpha(1f).setDuration(180).setInterpolator(new DecelerateInterpolator()).start();
        }
    }

    // --- Üst çubuk ve alt menü ---------------------------------------------------------------

    private void cubuklariCiz() {
        ustCubuk.removeAllViews();
        ustCubuk.setBackgroundColor(t.kart);
        ustCubuk.setGravity(Gravity.CENTER_VERTICAL);
        ustCubuk.setPadding(t.dp(8), 0, t.dp(14), 0);

        if (yigin.size() > 1) {
            ImageView geriDugme = simge(R.drawable.i_geri, t.metin);
            geriDugme.setPadding(t.dp(10), t.dp(10), t.dp(10), t.dp(10));
            geriDugme.setBackground(t.dalga(t.yuvarlak(0x00000000, 999), 999));
            geriDugme.setOnClickListener(v -> geri());
            ustCubuk.addView(geriDugme, new LinearLayout.LayoutParams(t.dp(44), t.dp(44)));
            ustCubuk.addView(t.yazi(yigin.peek().baslik(), 17, 700, t.metin));
        } else {
            TextView logo = t.yazi("🤝", 16, 400, t.markaUstu);
            logo.setGravity(Gravity.CENTER);
            android.graphics.drawable.GradientDrawable daire = new android.graphics.drawable.GradientDrawable();
            daire.setShape(android.graphics.drawable.GradientDrawable.OVAL);
            daire.setColor(t.marka);
            logo.setBackground(daire);
            LinearLayout.LayoutParams lp = new LinearLayout.LayoutParams(t.dp(32), t.dp(32));
            lp.setMargins(t.dp(6), 0, t.dp(8), 0);
            ustCubuk.addView(logo, lp);
            ustCubuk.addView(t.yazi("Askıda İyilik", 18, 800, t.metin));
        }
        View bosluk = new View(this);
        ustCubuk.addView(bosluk, new LinearLayout.LayoutParams(0, 1, 1));
        if (ben != null) {
            TextView r = t.rozet(ben.optString("bas_harfler"), 34, 12);
            r.setOnClickListener(v -> sekmeyeGec("profil"));
            ustCubuk.addView(r);
        }

        altMenu.removeAllViews();
        altMenu.setBackgroundColor(t.kart);
        String[][] menu = {{"akis", "Akış"}, {"olustur", "Oluştur"}, {"gorevler", "Görevler"}, {"profil", "Profil"}};
        int[] simgeler = {R.drawable.i_akis, R.drawable.i_olustur, R.drawable.i_gorevler, R.drawable.i_profil};
        for (int i = 0; i < menu.length; i++) {
            final String ad = menu[i][0];
            boolean secili = ad.equals(seciliSekme);
            LinearLayout oge = new LinearLayout(this);
            oge.setOrientation(LinearLayout.VERTICAL);
            oge.setGravity(Gravity.CENTER);
            oge.setBackground(t.dalga(t.yuvarlak(0x00000000, 0), 0));
            ImageView s = simge(simgeler[i], secili ? t.metin : t.soluk);
            oge.addView(s, new LinearLayout.LayoutParams(t.dp(24), t.dp(24)));
            TextView etiket = t.yazi(menu[i][1], 11, secili ? 700 : 500, secili ? t.metin : t.soluk);
            etiket.setPadding(0, t.dp(3), 0, 0);
            oge.addView(etiket, new LinearLayout.LayoutParams(-2, -2)); // yazı simgenin altında ortalı dursun
            oge.setOnClickListener(v -> {
                if (ad.equals(seciliSekme) && yigin.size() == 1) yigin.peek().yenile(); // aynı sekmeye basınca yenile
                else sekmeyeGec(ad);
            });
            altMenu.addView(oge, new LinearLayout.LayoutParams(0, -1, 1));
        }
    }

    ImageView simge(int kaynak, int renk) {
        ImageView v = new ImageView(this);
        v.setImageResource(kaynak);
        v.setImageTintList(ColorStateList.valueOf(renk));
        return v;
    }

    // --- Bildirimler ve hatalar -------------------------------------------------------------

    /** Ekranın altında kısa süreli bildirim (ekranlar.md E7). */
    void bildir(String mesaj, boolean hata) {
        TextView b = t.yazi(mesaj, 14, 500, hata ? 0xFFFFFFFF : (t.koyu ? 0xFF0E1113 : 0xFFFFFFFF));
        b.setPadding(t.dp(16), t.dp(13), t.dp(16), t.dp(13));
        b.setBackground(t.yuvarlak(hata ? t.tehlike : (t.koyu ? 0xFFE3E6E8 : 0xFF1C1C1C), 12));
        b.setElevation(t.dp(6));
        FrameLayout.LayoutParams lp = new FrameLayout.LayoutParams(-1, -2, Gravity.BOTTOM);
        lp.setMargins(t.dp(16), 0, t.dp(16), t.dp(altMenu.getVisibility() == View.VISIBLE ? 76 : 24));
        kokKatman.addView(b, lp);
        b.setAlpha(0f);
        b.setTranslationY(t.dp(20));
        b.animate().alpha(1f).translationY(0).setDuration(160).start();
        b.postDelayed(() -> b.animate().alpha(0f).setDuration(250).withEndAction(() -> kokKatman.removeView(b)).start(), 3200);
    }

    /** Bir API cevabını ortak şekilde ele alır: oturum bittiyse giriş ekranı, sunucu yoksa adres sorusu. */
    boolean sorunVarMi(Api.Cevap c) {
        if (c.kod == 401) {
            girisGoster();
            return true;
        }
        if (c.kod == 0) {
            sunucuyuSor();
            return true;
        }
        return false;
    }

    /** Sunucuya ulaşılamadığında adresi sorar (ör. ev sunucusu). */
    void sunucuyuSor() {
        if (pencereAcik) return;
        pencereAcik = true;
        EditText girdi = new EditText(this);
        girdi.setInputType(InputType.TYPE_CLASS_TEXT | InputType.TYPE_TEXT_VARIATION_URI);
        girdi.setText(api.adres());
        new AlertDialog.Builder(this)
                .setTitle("Sunucuya bağlanılamadı")
                .setMessage("Adres: " + api.adres() + "\n\nBilgisayarda demo çalışıyor mu? USB ile bağlıysan bilgisayarda "
                        + "\"adb reverse tcp:8000 tcp:8000\" komutunu çalıştır ya da başka bir adres yaz.")
                .setView(girdi)
                .setCancelable(false)
                .setPositiveButton("Bağlan", (d, w) -> {
                    api.adresiDegistir(girdi.getText().toString());
                    pencereAcik = false;
                    baslat();
                })
                .setNegativeButton("Yeniden dene", (d, w) -> {
                    pencereAcik = false;
                    baslat();
                })
                .show();
    }
}
