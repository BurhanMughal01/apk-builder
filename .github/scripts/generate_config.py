#!/usr/bin/env python3
"""APKForge - Generate config files from Worker payload"""

import json
import os

# Read payload from Worker
with open('payload.json') as f:
    config = json.load(f)

print(f"Received payload for: {config.get('appName', 'Unknown')}")
print(f"Build ID: {config.get('id', 'Unknown')}")

# Package name
pkg_name = config.get('packageName', 'com.example.app')
with open('package_name.txt', 'w') as f:
    f.write(pkg_name)

# Splash config
splash = config.get('splash', {})
with open('splash_config.json', 'w') as f:
    json.dump(splash, f, indent=2)

# Update strings.xml
strings_xml = '''<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string name="app_name">''' + config.get('appName', 'My App') + '''</string>
    <string name="package_name">''' + pkg_name + '''</string>
    <string name="version">''' + config.get('version', '1.0.0') + '''</string>
</resources>
'''

os.makedirs('app/res/values', exist_ok=True)
with open('app/res/values/strings.xml', 'w') as f:
    f.write(strings_xml)

# Update AndroidManifest.xml
orientation = config.get('orientation', 'portrait')
orientation_map = {
    'portrait': 'portrait',
    'landscape': 'landscape',
    'auto': 'unspecified'
}
android_orientation = orientation_map.get(orientation, 'portrait')

manifest = '''<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="''' + pkg_name + '''"
    android:versionCode="1"
    android:versionName="''' + config.get('version', '1.0.0') + '''">

    <uses-sdk android:minSdkVersion="21" android:targetSdkVersion="34" />

    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />

    <application
        android:label="@string/app_name"
        android:icon="@mipmap/ic_launcher"
        android:usesCleartextTraffic="true"
        android:theme="@android:style/Theme.NoTitleBar">

        <activity
            android:name="com.burhan.myapp2.MainActivity"
            android:configChanges="orientation|screenSize|keyboardHidden"
            android:screenOrientation="''' + android_orientation + '''"
            android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
</manifest>
'''

os.makedirs('app', exist_ok=True)
with open('app/AndroidManifest.xml', 'w') as f:
    f.write(manifest)

# Generate HTML content
os.makedirs('app/assets', exist_ok=True)

build_type = config.get('buildType', 'html')
html_content = config.get('htmlContent')
url = config.get('url')

if build_type == 'html' and html_content:
    with open('app/assets/index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("Wrote HTML content from upload")

elif build_type == 'url' and url:
    html = '''<!DOCTYPE html>
<html><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>''' + config.get('appName', 'App') + '''</title>
<style>
body,html{margin:0;padding:0;height:100%;overflow:hidden}
iframe{border:0;width:100%;height:100%;position:absolute;top:0;left:0}
</style>
</head><body>
<iframe src="''' + url + '''" allowfullscreen></iframe>
</body></html>'''
    with open('app/assets/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Wrote iframe HTML for URL")

elif build_type == 'template':
    template = config.get('templateName', 'calculator')
    # Simple template HTML
    html = '''<!DOCTYPE html>
<html><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>''' + config.get('appName', 'App') + '''</title>
<style>
body{font-family:system-ui;background:#111;color:#eee;display:flex;align-items:center;justify-content:center;height:100vh;margin:0;text-align:center;padding:20px}
h1{color:#6366f1}
</style>
</head><body>
<div>
<h1>''' + config.get('appName', 'App') + '''</h1>
<p>Template: ''' + template + '''</p>
<p>Build ID: ''' + config.get('id', '') + '''</p>
</div>
</body></html>'''
    with open('app/assets/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Wrote template HTML: {template}")

else:
    with open('app/assets/index.html', 'w', encoding='utf-8') as f:
        f.write('<!DOCTYPE html><html><body><h1>Hello</h1></body></html>')

print("Config generation complete!")
