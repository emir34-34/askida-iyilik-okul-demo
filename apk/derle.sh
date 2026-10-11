#!/usr/bin/env bash
# Askıda İyilik APK kabuğunu Gradle olmadan, Android SDK'nın kendi araçlarıyla derler.
# Kullanım:  cd apk && ./derle.sh      Çıktı: apk/build/AskidaIyilik.apk
# Gerekenler: Android SDK (platforms;android-34, build-tools;35.0.0), JDK (javac, keytool), python3
set -euo pipefail
cd "$(dirname "$0")"

SDK="${ANDROID_HOME:-$HOME/Android/Sdk}"
BT="$SDK/build-tools/35.0.0"
JAR="$SDK/platforms/android-34/android.jar"
ANAHTAR="${ANAHTAR:-$HOME/.android/debug.keystore}"

rm -rf build && mkdir -p build/gen build/obj build/dex build/assets

# Arayüz dosyaları APK'nın içine konur: sunucudan yalnızca veri gelir (demo-plani.md).
cp -r ../demo/istemci build/assets/istemci

echo "1/6 Kaynaklar (simge, metinler) derleniyor"
"$BT/aapt2" compile --dir res -o build/kaynaklar.zip

echo "2/6 Manifest, kaynaklar ve arayüz dosyaları birleştiriliyor"
"$BT/aapt2" link build/kaynaklar.zip -I "$JAR" --manifest AndroidManifest.xml \
  -A build/assets --java build/gen -o build/ham.apk \
  --min-sdk-version 24 --target-sdk-version 34 --version-code 1 --version-name 0.1

echo "3/6 Java kodu derleniyor"
javac --release 11 -classpath "$JAR" -d build/obj $(find src build/gen -name '*.java')

echo "4/6 Android'in çalıştırdığı biçime (DEX) çevriliyor"
"$BT/d8" --min-api 24 --lib "$JAR" --output build/dex $(find build/obj -name '*.class')

echo "5/6 Paketleniyor ve hizalanıyor"
python3 - <<'PY'
import shutil, zipfile
shutil.copy("build/ham.apk", "build/imzasiz.apk")
with zipfile.ZipFile("build/imzasiz.apk", "a", zipfile.ZIP_DEFLATED) as z:
    z.write("build/dex/classes.dex", "classes.dex")
PY
"$BT/zipalign" -f 4 build/imzasiz.apk build/hizali.apk

echo "6/6 İmzalanıyor (deneme anahtarı)"
if [ ! -f "$ANAHTAR" ]; then
  mkdir -p "$(dirname "$ANAHTAR")"
  # Android'in herkese açık, standart deneme (debug) anahtarı. Yalnızca test için, mağazaya konmaz.
  keytool -genkeypair -keystore "$ANAHTAR" -storepass android -keypass android -alias androiddebugkey \
    -keyalg RSA -keysize 2048 -validity 10000 -dname "CN=Android Debug,O=Android,C=US" >/dev/null 2>&1
fi
"$BT/apksigner" sign --ks "$ANAHTAR" --ks-pass pass:android --key-pass pass:android \
  --out build/AskidaIyilik.apk build/hizali.apk

echo "Hazır: apk/build/AskidaIyilik.apk"
echo "Telefona kurmak için:  adb install -r build/AskidaIyilik.apk && adb reverse tcp:8000 tcp:8000"
