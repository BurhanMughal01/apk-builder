#!/bin/bash
set -e

echo "🔨 Starting APK build..."

# SDK paths
SDK=$ANDROID_HOME
BT=$(ls -d $SDK/build-tools/* | tail -1)
PLATFORM=$SDK/platforms/android-33/android.jar

echo "📦 Build Tools: $BT"

# Check if platform exists, if not install it
if [ ! -f "$PLATFORM" ]; then
    echo "📥 Installing Android platform 33..."
    yes | $SDK/cmdline-tools/latest/bin/sdkmanager "platforms;android-33" > /dev/null 2>&1 || \
    yes | $SDK/tools/bin/sdkmanager "platforms;android-33" > /dev/null 2>&1 || \
    yes | sdkmanager "platforms;android-33" > /dev/null 2>&1
fi

echo "✅ Platform ready: $PLATFORM"

# Compile resources
echo "📦 Compiling resources..."
$BT/aapt2 compile --dir app/res -o compiled.zip

# Link resources
echo "🔗 Linking resources..."
$BT/aapt2 link -o app-unsigned.apk -I $PLATFORM \
    --manifest app/AndroidManifest.xml \
    -R compiled.zip --java app/src \
    --min-sdk-version 21 --target-sdk-version 33 \
    --auto-add-overlay

# Compile Java
echo "☕ Compiling Java..."
javac --release 8 -cp $PLATFORM -d app/build \
    app/src/com/example/myapp/MainActivity.java \
    app/src/com/example/myapp/R.java

# Build DEX
echo "🔧 Building DEX..."
$BT/d8 --output app/ app/build/com/example/myapp/*.class \
    --lib $PLATFORM --min-api 21

# Add to APK
echo "📦 Adding files to APK..."
cd app
zip -j app-unsigned.apk classes.dex
zip -r app-unsigned.apk assets/
cd ..

# Create keystore
echo "🔐 Creating keystore..."
keytool -genkeypair -v -keystore key.jks -alias mykey \
    -keyalg RSA -keysize 2048 -validity 10000 \
    -storepass 123456 -keypass 123456 \
    -dname "CN=App, O=Org, C=PK" 2>/dev/null || true

# Sign APK
echo "✍️ Signing APK..."
$BT/apksigner sign --ks key.jks --ks-pass pass:123456 \
    --key-pass pass:123456 --out output.apk app/app-unsigned.apk

echo "✅ APK built successfully: output.apk"
ls -lh output.apk