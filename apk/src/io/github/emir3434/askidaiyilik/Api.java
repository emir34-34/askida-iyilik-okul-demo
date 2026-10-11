package io.github.emir3434.askidaiyilik;

import android.content.Context;
import android.content.SharedPreferences;
import android.os.Handler;
import android.os.Looper;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.StandardCharsets;
import java.util.List;
import java.util.Map;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

/**
 * Django API'siyle konuşan sınıf (demo-plani.md: /api/ adresleri).
 *
 * Uygulama sunucudan yalnızca veri (JSON) ister. Kurallar sunucuda uygulanır (T-07):
 * sunucu 403 derse işlem yapılmamıştır, uygulama yalnızca mesajı gösterir.
 *
 * Oturum: Django giriş yapınca "sessionid", her istekte de "csrftoken" çerezi gönderir.
 * Uygulama bu iki çerezi saklar ve sonraki isteklerde geri gönderir. Veri değiştiren isteklerde
 * csrftoken ayrıca X-CSRFToken başlığında gönderilir (Django'nun CSRF koruması).
 *
 * Ağ işlemleri arka planda yapılır, sonuç ana iş parçacığında (ekranı çizen) geri verilir.
 */
public class Api {

    /** Sunucudan dönen cevap. kod == 0: sunucuya hiç ulaşılamadı. */
    public static class Cevap {
        public final int kod;
        public final JSONObject veri;

        Cevap(int kod, JSONObject veri) {
            this.kod = kod;
            this.veri = veri;
        }

        public boolean tamam() {
            return kod >= 200 && kod < 300;
        }

        /** Sunucunun gönderdiği hata mesajı (ekranlar.md E7 metinleri). */
        public String hata() {
            if (kod == 0) return "Sunucuya bağlanılamadı.";
            return veri.optString("hata", "Bir şeyler ters gitti.");
        }
    }

    public interface Sonuc {
        void geldi(Cevap c);
    }

    public static final String VARSAYILAN_ADRES = "http://localhost:8000/";

    private final SharedPreferences ayarlar;
    private final ExecutorService arkaPlan = Executors.newSingleThreadExecutor();
    private final Handler ana = new Handler(Looper.getMainLooper());

    public Api(Context c) {
        ayarlar = c.getSharedPreferences("askida", Context.MODE_PRIVATE);
    }

    public String adres() {
        return ayarlar.getString("sunucu", VARSAYILAN_ADRES);
    }

    public void adresiDegistir(String yeni) {
        yeni = yeni.trim();
        if (!yeni.startsWith("http://") && !yeni.startsWith("https://")) yeni = "http://" + yeni;
        if (!yeni.endsWith("/")) yeni += "/";
        ayarlar.edit().putString("sunucu", yeni).remove("cerez_sessionid").remove("cerez_csrftoken").apply();
    }

    public void get(String yol, Sonuc s) {
        istek("GET", yol, null, s);
    }

    public void post(String yol, JSONObject govde, Sonuc s) {
        istek("POST", yol, govde == null ? new JSONObject() : govde, s);
    }

    private void istek(String yontem, String yol, JSONObject govde, Sonuc s) {
        arkaPlan.execute(() -> {
            Cevap c = calistir(yontem, yol, govde);
            ana.post(() -> s.geldi(c));
        });
    }

    private Cevap calistir(String yontem, String yol, JSONObject govde) {
        HttpURLConnection b = null;
        try {
            b = (HttpURLConnection) new URL(adres() + "api/" + yol).openConnection();
            b.setRequestMethod(yontem);
            b.setConnectTimeout(5000);
            b.setReadTimeout(10000);
            b.setRequestProperty("Accept", "application/json");
            b.setRequestProperty("Cookie", cerezler());
            if (govde != null) {
                b.setDoOutput(true);
                b.setRequestProperty("Content-Type", "application/json; charset=utf-8");
                b.setRequestProperty("X-CSRFToken", ayarlar.getString("cerez_csrftoken", ""));
                try (OutputStream o = b.getOutputStream()) {
                    o.write(govde.toString().getBytes(StandardCharsets.UTF_8));
                }
            }
            int kod = b.getResponseCode();
            cerezleriSakla(b.getHeaderFields());
            InputStream g = kod >= 400 ? b.getErrorStream() : b.getInputStream();
            String metin = g == null ? "" : oku(g);
            JSONObject veri;
            try {
                veri = metin.isEmpty() ? new JSONObject() : new JSONObject(metin);
            } catch (JSONException e) {
                veri = new JSONObject(); // ör. CSRF hatasında Django HTML döner
            }
            return new Cevap(kod, veri);
        } catch (IOException e) {
            return new Cevap(0, new JSONObject());
        } finally {
            if (b != null) b.disconnect();
        }
    }

    private String cerezler() {
        StringBuilder sb = new StringBuilder();
        for (String ad : new String[]{"sessionid", "csrftoken"}) {
            String deger = ayarlar.getString("cerez_" + ad, null);
            if (deger != null) sb.append(ad).append('=').append(deger).append("; ");
        }
        return sb.toString();
    }

    /** Django'nun Set-Cookie başlıklarından yalnızca sessionid ve csrftoken saklanır. */
    private void cerezleriSakla(Map<String, List<String>> basliklar) {
        SharedPreferences.Editor e = ayarlar.edit();
        for (Map.Entry<String, List<String>> b : basliklar.entrySet()) {
            if (b.getKey() == null || !b.getKey().equalsIgnoreCase("Set-Cookie")) continue;
            for (String satir : b.getValue()) {
                String ilk = satir.split(";", 2)[0];
                int esit = ilk.indexOf('=');
                if (esit < 0) continue;
                String ad = ilk.substring(0, esit).trim();
                String deger = ilk.substring(esit + 1).trim();
                if (!ad.equals("sessionid") && !ad.equals("csrftoken")) continue;
                // Çıkışta Django çerezi boş değerle siler
                if (deger.isEmpty() || deger.equals("\"\"")) e.remove("cerez_" + ad);
                else e.putString("cerez_" + ad, deger);
            }
        }
        e.apply();
    }

    private static String oku(InputStream g) throws IOException {
        ByteArrayOutputStream cikti = new ByteArrayOutputStream();
        byte[] tampon = new byte[8192];
        int n;
        while ((n = g.read(tampon)) > 0) cikti.write(tampon, 0, n);
        return cikti.toString("UTF-8");
    }
}
