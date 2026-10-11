package io.github.emir3434.askidaiyilik;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.Intent;
import android.content.SharedPreferences;
import android.net.Uri;
import android.os.Bundle;
import android.text.InputType;
import android.webkit.JavascriptInterface;
import android.webkit.WebResourceError;
import android.webkit.WebResourceRequest;
import android.webkit.WebResourceResponse;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.EditText;

import java.io.IOException;

/**
 * Askıda İyilik Android uygulaması.
 *
 * Arayüz dosyaları (demo/istemci/: HTML, CSS, JavaScript, yazı tipi) APK'nın içindedir (assets/istemci).
 * WebView sunucunun adresini açar, ama "/" ve "/i/..." isteklerini sunucuya göndermeden APK'nın içinden
 * verir. Sunucuya yalnızca "/api/..." veri istekleri gider (demo-plani.md, mimari değişikliği).
 * Dosyalar sunucuyla aynı adresten geliyormuş gibi davrandığı için oturum çerezi ve CSRF koruması
 * değişmeden çalışır. Kurallar (kim neyi yapabilir) burada değil, sunucuda uygulanır (T-07).
 *
 * Varsayılan adres http://localhost:8000/. Telefon USB ile bağlıyken bilgisayarda
 * "adb reverse tcp:8000 tcp:8000" çalıştırılırsa telefonun localhost'u bilgisayara yönlenir.
 * Sunucuya bağlanılamazsa kullanıcıdan başka bir adres istenir (ör. ev sunucusu).
 */
public class MainActivity extends Activity {

    private static final String VARSAYILAN_ADRES = "http://localhost:8000/";
    private static final String AYAR_ADRES = "sunucu_adresi";

    private WebView web;
    private SharedPreferences ayarlar;
    private boolean pencereAcik = false;

    @Override
    protected void onCreate(Bundle kayitliDurum) {
        super.onCreate(kayitliDurum);
        getWindow().setStatusBarColor(0xFFD93A00); // uygulamanın turuncusu
        ayarlar = getPreferences(MODE_PRIVATE);

        web = new WebView(this);
        WebSettings s = web.getSettings();
        s.setJavaScriptEnabled(true);   // sayfalardaki küçük bildirim betiği için
        s.setDomStorageEnabled(true);
        // Arayüz sunucuya ulaşamazsa adres penceresini açabilsin diye tek bir yöntem açılır.
        web.addJavascriptInterface(new Kopru(), "AskidaUygulama");
        web.setWebViewClient(new WebViewClient() {
            @Override
            public WebResourceResponse shouldInterceptRequest(WebView view, WebResourceRequest istek) {
                return arayuzDosyasi(istek);
            }

            @Override
            public boolean shouldOverrideUrlLoading(WebView view, WebResourceRequest istek) {
                Uri hedef = istek.getUrl();
                Uri sunucu = Uri.parse(adres());
                if (hedef.getHost() != null && hedef.getHost().equals(sunucu.getHost())) {
                    return false; // kendi sayfalarımız uygulamanın içinde açılır
                }
                startActivity(new Intent(Intent.ACTION_VIEW, hedef)); // dış bağlantılar tarayıcıda
                return true;
            }

            @Override
            public void onReceivedError(WebView view, WebResourceRequest istek, WebResourceError hata) {
                if (istek.isForMainFrame()) {
                    adresSor("Sunucuya bağlanılamadı (" + adres() + ").\n\n"
                            + "Bilgisayarda demo çalışıyor mu? USB ile bağlıysan bilgisayarda "
                            + "\"adb reverse tcp:8000 tcp:8000\" komutunu çalıştır ya da başka bir adres yaz.");
                }
            }
        });
        setContentView(web);

        if (kayitliDurum != null) {
            web.restoreState(kayitliDurum);
        } else {
            web.loadUrl(adres());
        }
    }

    /** "/" ve "/i/..." isteklerini APK'nın içindeki arayüz dosyalarından karşılar. Diğerleri sunucuya gider. */
    private WebResourceResponse arayuzDosyasi(WebResourceRequest istek) {
        Uri hedef = istek.getUrl();
        Uri sunucu = Uri.parse(adres());
        if (!"GET".equals(istek.getMethod())
                || hedef.getHost() == null || !hedef.getHost().equals(sunucu.getHost())
                || hedef.getPort() != sunucu.getPort()) {
            return null;
        }
        String yol = hedef.getPath() == null ? "/" : hedef.getPath();
        String dosya;
        if (yol.equals("/")) {
            dosya = "index.html";
        } else if (yol.startsWith("/i/") && !yol.contains("..")) {
            dosya = yol.substring(3);
        } else {
            return null; // /api/, /yonetim/ ... sunucuya gider
        }
        try {
            return new WebResourceResponse(turu(dosya), "UTF-8", getAssets().open("istemci/" + dosya));
        } catch (IOException e) {
            return null;
        }
    }

    private static String turu(String dosya) {
        if (dosya.endsWith(".html")) return "text/html";
        if (dosya.endsWith(".css")) return "text/css";
        if (dosya.endsWith(".js")) return "application/javascript";
        if (dosya.endsWith(".woff2")) return "font/woff2";
        return "application/octet-stream";
    }

    /** JavaScript'in çağırabildiği tek yöntem: sunucuya ulaşılamadığında adres penceresini açmak. */
    private class Kopru {
        @JavascriptInterface
        public void sunucuyaUlasilamadi() {
            runOnUiThread(() -> adresSor("Sunucuya bağlanılamadı (" + adres() + ").\n\n"
                    + "Bilgisayarda demo çalışıyor mu? USB ile bağlıysan bilgisayarda "
                    + "\"adb reverse tcp:8000 tcp:8000\" komutunu çalıştır ya da başka bir adres yaz."));
        }
    }

    private String adres() {
        return ayarlar.getString(AYAR_ADRES, VARSAYILAN_ADRES);
    }

    private void adresSor(String mesaj) {
        if (pencereAcik) return;
        pencereAcik = true;
        final EditText girdi = new EditText(this);
        girdi.setInputType(InputType.TYPE_CLASS_TEXT | InputType.TYPE_TEXT_VARIATION_URI);
        girdi.setText(adres());
        new AlertDialog.Builder(this)
                .setTitle("Askıda İyilik")
                .setMessage(mesaj)
                .setView(girdi)
                .setCancelable(false)
                .setPositiveButton("Bağlan", (d, w) -> {
                    String yeni = girdi.getText().toString().trim();
                    if (!yeni.startsWith("http://") && !yeni.startsWith("https://")) yeni = "http://" + yeni;
                    if (!yeni.endsWith("/")) yeni = yeni + "/";
                    ayarlar.edit().putString(AYAR_ADRES, yeni).apply();
                    pencereAcik = false;
                    web.loadUrl(yeni);
                })
                .setNegativeButton("Varsayılana dön", (d, w) -> {
                    ayarlar.edit().remove(AYAR_ADRES).apply();
                    pencereAcik = false;
                    web.loadUrl(VARSAYILAN_ADRES);
                })
                .show();
    }

    @Override
    protected void onSaveInstanceState(Bundle durum) {
        super.onSaveInstanceState(durum);
        web.saveState(durum);
    }

    @Override
    public void onBackPressed() {
        if (web.canGoBack()) {
            web.goBack(); // geri tuşu önceki sayfaya döner, uygulamadan çıkmaz
        } else {
            super.onBackPressed();
        }
    }
}
