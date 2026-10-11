package io.github.emir3434.askidaiyilik;

import android.content.res.ColorStateList;
import android.view.Gravity;
import android.view.MotionEvent;
import android.view.ViewConfiguration;
import android.widget.FrameLayout;
import android.widget.LinearLayout;
import android.widget.ProgressBar;
import android.widget.ScrollView;

/**
 * Aşağı çekince yenileyen kaydırılabilir liste (Reddit uygulamasındaki gibi).
 * Liste en üstteyken parmak aşağı çekilirse dönen bir halka görünür. Yeterince çekilip bırakılırsa
 * yenile çağrılır. Veri gelince bitti() ile halka gizlenir.
 */
public class CekYenile extends FrameLayout {

    public final LinearLayout liste;
    private final ScrollView kaydir;
    private final ProgressBar halka;
    private final Tema t;
    private final int esik, egim;
    private Runnable yenile;
    private float baslangicY;
    private boolean cekiliyor, yenileniyor;

    public CekYenile(MainActivity a) {
        super(a);
        t = a.t;
        esik = t.dp(64);
        egim = ViewConfiguration.get(a).getScaledTouchSlop();

        kaydir = new ScrollView(a);
        kaydir.setFillViewport(true);
        kaydir.setOverScrollMode(OVER_SCROLL_NEVER);
        liste = new LinearLayout(a);
        liste.setOrientation(LinearLayout.VERTICAL);
        kaydir.addView(liste, new LayoutParams(-1, -2));
        addView(kaydir, new LayoutParams(-1, -1));

        halka = new ProgressBar(a);
        halka.setIndeterminateTintList(ColorStateList.valueOf(t.marka));
        halka.setBackground(t.yuvarlak(t.kart, 999));
        halka.setElevation(t.dp(4));
        halka.setPadding(t.dp(6), t.dp(6), t.dp(6), t.dp(6));
        LayoutParams lp = new LayoutParams(t.dp(38), t.dp(38), Gravity.CENTER_HORIZONTAL | Gravity.TOP);
        addView(halka, lp);
        halka.setTranslationY(-t.dp(48));
        halka.setAlpha(0f);
    }

    public void yenilenince(Runnable r) {
        yenile = r;
    }

    /** Veri geldi: halkayı gizle. */
    public void bitti() {
        yenileniyor = false;
        halka.animate().translationY(-t.dp(48)).alpha(0f).setDuration(200).start();
    }

    /** Kodla yenileme başlatıldığında da halka görünsün. */
    public void baslat() {
        yenileniyor = true;
        halka.animate().translationY(t.dp(12)).alpha(1f).setDuration(150).start();
    }

    @Override
    public boolean onInterceptTouchEvent(MotionEvent e) {
        if (yenileniyor) return false;
        switch (e.getActionMasked()) {
            case MotionEvent.ACTION_DOWN:
                baslangicY = e.getY();
                cekiliyor = false;
                break;
            case MotionEvent.ACTION_MOVE:
                if (kaydir.getScrollY() == 0 && e.getY() - baslangicY > egim) {
                    cekiliyor = true;
                    return true; // dokunuşu liste yerine biz alıyoruz
                }
                break;
        }
        return false;
    }

    @Override
    public boolean onTouchEvent(MotionEvent e) {
        if (!cekiliyor) return super.onTouchEvent(e);
        float mesafe = Math.max(0, (e.getY() - baslangicY) * 0.5f);
        switch (e.getActionMasked()) {
            case MotionEvent.ACTION_MOVE:
                halka.setAlpha(Math.min(1f, mesafe / esik));
                halka.setTranslationY(Math.min(mesafe, esik * 1.4f) - t.dp(40));
                halka.setRotation(mesafe * 2);
                return true;
            case MotionEvent.ACTION_UP:
            case MotionEvent.ACTION_CANCEL:
                cekiliyor = false;
                if (mesafe >= esik && yenile != null) {
                    baslat();
                    yenile.run();
                } else {
                    bitti();
                }
                return true;
        }
        return true;
    }
}
