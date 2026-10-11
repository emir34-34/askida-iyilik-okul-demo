package io.github.emir3434.askidaiyilik;

import android.view.View;

/** D4: Öğretmenin Kontrol sayfası. Demoda yalnızca gizlenenler sekmesi var (şikâyetler tasarımda). */
public class KontrolEkrani extends ListeEkrani {

    public KontrolEkrani(MainActivity a) {
        super(a);
    }

    @Override
    protected String adres() {
        return "gizlenenler";
    }

    @Override
    protected void cipleriKur() {
        cip("Gizlenenler", true, this::yenile);
    }

    @Override
    protected View bosGorunum() {
        return bos("🛡️", "Gizlenen içerik yok", "Uygunsuz bulduğun bir isteği, istek sayfasındaki Öğretmen kutusundan gizleyebilirsin.", null, null);
    }
}
