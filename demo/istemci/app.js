/* Askıda İyilik istemcisi (demo-plani.md, mimari değişikliği).
 *
 * Arayüzün tamamı burada. Sunucudan yalnızca /api/ adreslerinden veri (JSON) istenir.
 * Kurallar burada DEĞİL, sunucuda (gecisler.py) uygulanır: buradaki düğme gizleme yalnızca görünüş.
 *
 * Sayfalar adresin # kısmıyla seçilir:  #/  #/istek/5  #/yeni  #/gorevler  #/profil  #/giris
 * Güvenlik: kullanıcıların yazdığı her metin ekrana basılmadan önce kac() ile kaçışlanır (XSS önlemi).
 */
"use strict";

const kok = document.getElementById("uygulama");
let ben = null; // giriş yapan kişi (/api/ben)

// --- Yardımcılar ---------------------------------------------------------------------------

/** HTML'de özel anlamı olan karakterleri kaçışlar. Kullanıcı metni ASLA kac() olmadan basılmaz. */
function kac(metin) {
  return String(metin ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]);
}

function cerez(ad) {
  const m = document.cookie.match(new RegExp("(?:^|; )" + ad + "=([^;]*)"));
  return m ? decodeURIComponent(m[1]) : "";
}

/** Sunucuya istek atar. Veri değiştiren isteklerde Django'nun CSRF jetonunu gönderir. */
async function api(yontem, yol, govde) {
  let cevap;
  try {
    cevap = await fetch("/api/" + yol, {
      method: yontem,
      credentials: "same-origin",
      headers: { "Content-Type": "application/json", "X-CSRFToken": cerez("csrftoken") },
      body: govde === undefined ? undefined : JSON.stringify(govde),
    });
  } catch (e) {
    // APK'da arayüz telefonda olduğu için sunucu yokken de açılır: adres penceresini uygulama gösterir.
    if (window.AskidaUygulama) window.AskidaUygulama.sunucuyaUlasilamadi();
    else bildir("Sunucuya bağlanılamadı. İnternet bağlantını kontrol et.", true);
    throw e;
  }
  const veri = await cevap.json().catch(() => ({}));
  if (cevap.status === 401 && yol !== "giris") {
    ben = null;
    git("#/giris");
  }
  return { ok: cevap.ok, durum: cevap.status, veri };
}

// --- Canlı güncelleme (demo-plani.md): ekran açıkken belirli aralıklarla sunucuya sorar -------

let canli = null;

function canliBaslat(fonksiyon, aralikMs) {
  clearInterval(canli);
  canli = setInterval(() => { if (!document.hidden) fonksiyon(); }, aralikMs);
}

/** Sessiz istek: hata bildirimi göstermez (arka planda sorarken). */
async function sessizGetir(yol) {
  try {
    const c = await fetch("/api/" + yol, { credentials: "same-origin" });
    return { durum: c.status, veri: await c.json() };
  } catch (e) {
    return null;
  }
}

/** Kullanıcı o an bir şey yazıyorsa ekranı yeniden çizme (yazdığı kaybolmasın). */
function kullaniciMesgul() {
  const odak = document.activeElement;
  return (odak && (odak.tagName === "INPUT" || odak.tagName === "TEXTAREA")) || !!kok.querySelector("details[open]");
}

/** Ekran açıkken başka biri isteği değiştirdi: ne olduğunu söyle. */
function degisiklikMesaji(eski, yeni) {
  const ad = (k) => (k ? k.gorunen_ad : "Biri");
  const once = eski.durum, simdi = yeni.durum;
  if (once === simdi) return null; // yalnızca yeni yorum: sessizce güncelle
  if (once === "acik" && simdi === "ustlenildi") return `Bu istek az önce ${ad(yeni.ustlenen)} tarafından üstlenildi.`;
  if (once === "ustlenildi" && simdi === "acik") return `${ad(eski.ustlenen)} işi bıraktı. İstek yeniden açık.`;
  if (once === "ustlenildi" && simdi === "yapildi") return `${ad(yeni.ustlenen)} işi yaptığını söyledi.`;
  if (once === "yapildi" && simdi === "tamamlandi") return "İstek onaylandı ve tamamlandı. 🎉";
  if (once === "yapildi" && simdi === "ustlenildi") return `İş yeniden ${ad(yeni.ustlenen)} kişisine döndü.`;
  if (simdi === "geri_cekildi") return "İsteği açan kişi isteğini geri çekti.";
  return "İstek güncellendi: " + yeni.durum_adi;
}

function zamanOnce(iso) {
  const sn = Math.max(0, (Date.now() - new Date(iso).getTime()) / 1000);
  if (sn < 60) return "az önce";
  if (sn < 3600) return Math.floor(sn / 60) + " dk önce";
  if (sn < 86400) return Math.floor(sn / 3600) + " sa önce";
  return Math.floor(sn / 86400) + " gün önce";
}

function bildir(metin, hata = false) {
  const t = document.createElement("div");
  t.className = "toast" + (hata ? " hata" : "");
  t.setAttribute("role", "status");
  t.textContent = metin; // textContent: kaçışa gerek yok
  document.body.appendChild(t);
  setTimeout(() => { t.style.opacity = 0; setTimeout(() => t.remove(), 300); }, 3500);
}

function git(adres) {
  if (location.hash === adres) yonlendir();
  else location.hash = adres;
}

// --- Parçalar ------------------------------------------------------------------------------

const IKON = {
  akis: '<path d="M3 10.5 12 3l9 7.5"/><path d="M5 9.5V20h5v-6h4v6h5V9.5"/>',
  yeni: '<path d="M12 5v14M5 12h14"/>',
  gorevler: '<rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4h6v3H9zM9 12l2 2 4-4"/>',
  profil: '<circle cx="12" cy="8" r="4"/><path d="M4 21c1.5-4 4.5-6 8-6s6.5 2 8 6"/>',
};
const MENU = [["akis", "#/", "Akış"], ["yeni", "#/yeni", "Oluştur"], ["gorevler", "#/gorevler", "Görevler"], ["profil", "#/profil", "Profil"]];
const DURUM_SIMGE = { acik: "🟢", ustlenildi: "🟡", yapildi: "🔵", tamamlandi: "✅" };

function ikon(ad) {
  return `<svg class="i" viewBox="0 0 24 24">${IKON[ad]}</svg>`;
}

function cerceve(bolum, icerik) {
  const menu = (sinif) => MENU.map(([ad, adres, etiket]) =>
    `<a href="${adres}" class="${ad === bolum ? "on" : ""}">${ikon(ad)}<span>${etiket}</span></a>`).join("");
  const yonetim = ben.yonetim_paneli ? `<div class="lbl">ÖĞRETMEN</div><a href="/yonetim/">🛡️ Yönetim paneli</a>` : "";
  return `
    <header class="bar">
      <a class="logo" href="#/"><span class="dot">🤝</span>Askıda İyilik</a>
      <span class="spacer"></span>
      <a class="av" href="#/profil" title="${kac(ben.gorunen_ad)}">${kac(ben.bas_harfler)}</a>
    </header>
    <div class="sayfa">
      <nav class="yan" aria-label="Menü">${menu()}${yonetim}</nav>
      <main class="icerik">${icerik}</main>
    </div>
    <nav class="alt" aria-label="Alt menü">${menu()}</nav>`;
}

function flair(i) {
  const kim = i.ustlenen && i.durum !== "acik" ? " · " + kac(i.ustlenen.gorunen_ad) : "";
  return `<span class="flair f-${kac(i.durum)}">${DURUM_SIMGE[i.durum] || "⚪"} ${kac(i.durum_adi)}${kim}</span>`;
}

function meta(i) {
  return `<div class="meta"><span class="av sm">${kac(i.acan.bas_harfler)}</span><b>${kac(i.kategori_adi)}</b>· ${kac(i.acan.gorunen_ad)} · ${zamanOnce(i.olusturma)}</div>`;
}

function kart(i) {
  return `<a class="kart" href="#/istek/${i.no}">
    ${meta(i)}
    <div class="baslik">${kac(i.baslik)}</div>
    ${flair(i)}
    <p class="govde">${kac(i.aciklama)}</p>
    <span class="pill">💬 ${i.yorum_sayisi ?? 0}</span>
  </a>`;
}

function bos(simge, baslik, aciklama, dugme = "") {
  return `<div class="bos"><div class="ic">${simge}</div><h3>${baslik}</h3><p>${aciklama}</p>${dugme}</div>`;
}

// --- Ekranlar ------------------------------------------------------------------------------

function girisEkrani() {
  kok.innerHTML = `
    <div class="giris">
      <form class="kutu" id="giris-formu">
        <div style="text-align:center;margin-bottom:24px">
          <div class="logo" style="justify-content:center;font-size:22px"><span class="dot" style="width:40px;height:40px;font-size:20px">🤝</span>Askıda İyilik</div>
          <div style="color:var(--muted);margin-top:6px">Okulumuzun iyilik panosu</div>
        </div>
        <label class="alan"><span>Kullanıcı adı</span><input class="girdi" name="kullanici_adi" autocomplete="username" autocapitalize="none" required></label>
        <label class="alan"><span>Şifre</span><input class="girdi" type="password" name="sifre" autocomplete="current-password" required></label>
        <button class="btn ana tam" type="submit">Giriş yap</button>
        <p style="text-align:center;color:var(--muted);font-size:13px;margin:16px 0 0">Şifreni unuttuysan okul yöneticisine başvur.</p>
        <p class="bilgi" style="text-align:center">Demo · yalnızca örnek kullanıcılar</p>
      </form>
    </div>`;
  document.getElementById("giris-formu").addEventListener("submit", async (e) => {
    e.preventDefault();
    const f = new FormData(e.target);
    const c = await api("POST", "giris", { kullanici_adi: f.get("kullanici_adi"), sifre: f.get("sifre") });
    if (!c.ok) return bildir(c.veri.hata || "Giriş yapılamadı.", true);
    await api("GET", "ben"); // giriş sonrası yeni CSRF jetonunu al
    ben = c.veri;
    git("#/");
  });
}

async function akisEkrani(parametre) {
  const sekme = parametre.get("sekme") || "yeni";
  const k = parametre.get("k") || "";
  const c = await api("GET", `istekler?sekme=${encodeURIComponent(sekme)}&k=${encodeURIComponent(k)}`);
  if (!c.ok) return;
  const adres = (s, kat) => `#/?sekme=${s}${kat ? "&k=" + kat : ""}`;
  const sekmeler = `<div class="sekmeler">
      <a class="chip ${sekme !== "acik" ? "on" : ""}" href="${adres("yeni", k)}">Yeni</a>
      <a class="chip ${sekme === "acik" ? "on" : ""}" href="${adres("acik", k)}">Açık olanlar</a>
      ${ben.kategoriler.map((x) => `<a class="chip ${k === x.deger ? "on" : ""}" href="${adres(sekme, k === x.deger ? "" : x.deger)}">${kac(x.ad)}</a>`).join("")}
    </div>`;
  const liste = c.veri.istekler.length
    ? c.veri.istekler.map(kart).join("")
    : bos("🌱", "Şu an açık istek yok", "Bir ihtiyacın ya da okulda gördüğün bir sorun varsa ilk isteği sen aç.", '<a class="btn ana" href="#/yeni">＋ İstek aç</a>');
  kok.innerHTML = cerceve("akis", sekmeler + liste);
  const son = JSON.stringify(c.veri);
  canliBaslat(async () => {
    const y = await sessizGetir(`istekler?sekme=${encodeURIComponent(sekme)}&k=${encodeURIComponent(k)}`);
    if (y && y.durum === 200 && JSON.stringify(y.veri) !== son && !kullaniciMesgul()) akisEkrani(parametre);
  }, 10000);
}

function dugmelerHTML(i) {
  if (!i.dugmeler.length) return "";
  const d = {
    ustlen: `<button class="btn ana" data-eylem="ustlen">Üstlen</button>`,
    yapildi: `<button class="btn ana" data-eylem="yapildi">Yapıldı</button>`,
    birak: `<button class="btn ikincil" data-eylem="birak">Bırak</button>`,
    geri_cek: `<button class="btn ikincil" data-eylem="geri_cek">Geri çek</button>`,
    onayla: `<details class="ac"><summary class="btn ana">Onayla</summary>
        <form data-eylem="onayla"><label class="alan"><span>Teşekkür notu (isteğe bağlı, herkese görünür)</span>
        <textarea class="girdi" name="tesekkur" placeholder="Çok sağ ol! 🙏"></textarea></label><button class="btn ana">Onayla</button></form></details>`,
    yapilmadi: `<details class="ac"><summary class="btn ikincil">Yapılmadı</summary>
        <form data-eylem="yapilmadi"><label class="alan"><span>Neyin eksik olduğunu yaz (zorunlu)</span>
        <textarea class="girdi" name="gerekce"></textarea></label><button class="btn ikincil">Gönder</button></form></details>`,
  };
  return `<div class="islem"><div class="not">Senin için:</div>${i.dugmeler.map((x) => d[x] || "").join("")}</div>`;
}

const BASARI = {
  ustlen: "İsteği üstlendin.", birak: "İşi bıraktın. İstek yeniden açık.",
  yapildi: "Harika! Şimdi isteği açan kişinin onayı bekleniyor.", geri_cek: "İsteğini geri çektin.",
  onayla: "Teşekkürler! İstek tamamlandı.", yapilmadi: "İstek yeniden üstlenen kişiye döndü.", yorum: "Yorumun eklendi.",
};

async function istekEkrani(no) {
  const c = await api("GET", `istekler/${no}`);
  if (!c.ok) {
    kok.innerHTML = cerceve("akis", bos("🔎", "İstek bulunamadı", kac(c.veri.hata || ""), '<a class="btn ikincil" href="#/">Akışa dön</a>'));
    return;
  }
  const i = c.veri;
  const yorumlar = i.yorumlar.length ? i.yorumlar.map((y) => `
      <div class="yorum${y.tesekkur ? " tesekkur" : ""}"><span class="av">${kac(y.yazan.bas_harfler)}</span>
        <div><div class="cm">${y.tesekkur ? "💛 " : ""}<b>${kac(y.yazan.gorunen_ad)}</b>${y.tesekkur ? " teşekkür etti" : ""} · ${zamanOnce(y.zaman)}</div><p>${kac(y.metin)}</p></div>
      </div>`).join("") : '<p style="color:var(--muted);font-size:13px">Henüz yorum yok.</p>';
  const yorumFormu = i.yorum_yazilabilir ? `
      <form data-eylem="yorum" style="margin-top:10px;display:flex;gap:8px">
        <input class="girdi" name="metin" placeholder="Yorum ekle..." maxlength="1000" required>
        <button class="btn ana">Gönder</button>
      </form>` : "";
  kok.innerHTML = cerceve("akis", `
    <div class="kart" style="cursor:default">
      ${meta(i)}
      <div class="baslik" style="font-size:20px">${kac(i.baslik)}</div>
      ${flair(i)}
      <p class="govde tam">${kac(i.aciklama)}</p>
      ${dugmelerHTML(i)}
    </div>
    <section class="yorumlar">
      <b>Yorumlar</b> <span style="color:var(--muted);font-size:13px">· herkese açık</span>
      ${yorumFormu}${yorumlar}
    </section>`);

  // Düğmeler ve formlar: hepsi aynı API adresine gider, sonuç sunucudan gelir.
  const calistir = async (eylem, govde) => {
    const s = await api("POST", `istekler/${no}/${eylem}`, govde);
    if (s.ok) bildir(BASARI[eylem]);
    else if (s.durum !== 401) bildir(s.veri.hata || "Bir şeyler ters gitti.", true);
    istekEkrani(no);
  };
  kok.querySelectorAll("button[data-eylem]").forEach((b) =>
    b.addEventListener("click", () => { b.disabled = true; calistir(b.dataset.eylem, {}); }));
  kok.querySelectorAll("form[data-eylem]").forEach((f) =>
    f.addEventListener("submit", (e) => {
      e.preventDefault();
      calistir(f.dataset.eylem, Object.fromEntries(new FormData(f)));
    }));

  // Başka biri isteği değiştirirse (ör. üstlenirse) düğmeler 3 saniye içinde güncellenir.
  const son = JSON.stringify(i);
  canliBaslat(async () => {
    const y = await sessizGetir(`istekler/${no}`);
    if (!y) return;
    if (y.durum === 404) return istekEkrani(no);
    if (y.durum !== 200 || JSON.stringify(y.veri) === son || kullaniciMesgul()) return;
    const mesaj = degisiklikMesaji(i, y.veri);
    if (mesaj) bildir(mesaj);
    istekEkrani(no);
  }, 3000);
}

function yeniEkrani() {
  kok.innerHTML = cerceve("yeni", `
    <form class="kutu" id="yeni-formu">
      <h2 style="margin:0 0 14px;font-size:19px">Yeni istek</h2>
      <label class="alan"><span>Kategori</span>
        <select class="girdi" name="kategori">${ben.kategoriler.map((x) => `<option value="${kac(x.deger)}">${kac(x.ad)}</option>`).join("")}</select>
      </label>
      <label class="alan"><span>Başlık</span><input class="girdi" name="baslik" maxlength="120" required placeholder="Kimya notları lazım"></label>
      <label class="alan"><span>Açıklama</span><textarea class="girdi" name="aciklama" maxlength="2000" required placeholder="Ne istediğini kısaca anlat."></textarea></label>
      <div class="bilgi">ⓘ Telefon, adres ya da başka kişisel bilgi yazma. İstekleri okuldaki herkes görür.</div>
      <button class="btn ana tam">Yayınla</button>
    </form>`);
  document.getElementById("yeni-formu").addEventListener("submit", async (e) => {
    e.preventDefault();
    const c = await api("POST", "istekler", Object.fromEntries(new FormData(e.target)));
    if (!c.ok) return bildir(c.veri.hata || "İstek açılamadı.", true);
    bildir("İsteğin yayında!");
    git(`#/istek/${c.veri.no}`);
  });
}

async function gorevlerEkrani(parametre) {
  const sekme = parametre.get("sekme") === "ustlendiklerim" ? "ustlendiklerim" : "actiklarim";
  const c = await api("GET", `gorevler?sekme=${sekme}`);
  if (!c.ok) return;
  const liste = c.veri.istekler.length
    ? c.veri.istekler.map(kart).join("")
    : bos("📋", "Henüz bir işin yok", "Açtığın ve üstlendiğin istekler burada görünür.", '<a class="btn ikincil" href="#/?sekme=acik">Açık isteklere bak</a>');
  kok.innerHTML = cerceve("gorevler", `
    <div class="sekmeler">
      <a class="chip ${sekme === "actiklarim" ? "on" : ""}" href="#/gorevler?sekme=actiklarim">Açtıklarım</a>
      <a class="chip ${sekme === "ustlendiklerim" ? "on" : ""}" href="#/gorevler?sekme=ustlendiklerim">Üstlendiklerim</a>
    </div>${liste}`);
}

function profilEkrani() {
  kok.innerHTML = cerceve("profil", `
    <div class="kutu" style="text-align:center">
      <div class="av" style="width:72px;height:72px;font-size:24px;margin:0 auto 10px">${kac(ben.bas_harfler)}</div>
      <div style="font-weight:800;font-size:19px">${kac(ben.gorunen_ad)}</div>
      <div style="color:var(--muted);font-size:13px">${kac(ben.kullanici_adi)} · ${kac(ben.rol_adi)}</div>
      <div class="bilgi">ⓘ Profilinde kaç iyilik yaptığın ya da puanın gösterilmez. Askıda İyilik bir yarışma değil.</div>
      <div class="bilgi" style="text-align:left"><b style="color:var(--text)">Hakkında tutulan bilgiler:</b> kullanıcı adı, görünen ad, rol ve şifrenin geri çevrilemez özeti. Telefon, e-posta, fotoğraf, konum ve doğum tarihi tutulmaz.</div>
      <button class="btn ikincil tam" id="cikis" style="color:var(--danger)">Çıkış yap</button>
    </div>`);
  document.getElementById("cikis").addEventListener("click", async () => {
    await api("POST", "cikis");
    ben = null;
    await api("GET", "ben"); // yeni (oturumsuz) CSRF jetonu
    git("#/giris");
  });
}

// --- Yönlendirme ---------------------------------------------------------------------------

async function yonlendir() {
  clearInterval(canli); // önceki ekranın canlı güncellemesi durur
  const [yol, sorgu] = (location.hash.slice(1) || "/").split("?");
  const parametre = new URLSearchParams(sorgu || "");
  if (yol === "/giris") return ben ? git("#/") : girisEkrani();
  if (!ben) {
    const c = await api("GET", "ben");
    if (!c.ok) return; // 401: api() giriş ekranına yönlendirdi
    ben = c.veri;
  }
  window.scrollTo(0, 0);
  const istek = yol.match(/^\/istek\/(\d+)$/);
  if (istek) return istekEkrani(istek[1]);
  if (yol === "/yeni") return yeniEkrani();
  if (yol === "/gorevler") return gorevlerEkrani(parametre);
  if (yol === "/profil") return profilEkrani();
  return akisEkrani(parametre);
}

window.addEventListener("hashchange", yonlendir);
yonlendir();
