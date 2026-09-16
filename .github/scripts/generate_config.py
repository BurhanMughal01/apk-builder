#!/usr/bin/env python3
"""APKForge - Generate config files from Worker payload"""

import json
import os

# Read payload from Worker
with open('payload.json') as f:
    _raw = json.load(f)

# Support nested structure { data: {...} }
if isinstance(_raw, dict) and 'data' in _raw:
    config = _raw['data']
else:
    config = _raw

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
strings_xml = '<?xml version="1.0" encoding="utf-8"?>\n'
strings_xml += '<resources>\n'
strings_xml += '    <string name="app_name">' + config.get('appName', 'My App') + '</string>\n'
strings_xml += '    <string name="package_name">' + pkg_name + '</string>\n'
strings_xml += '    <string name="version">' + config.get('version', '1.0.0') + '</string>\n'
strings_xml += '</resources>\n'

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

manifest = '<?xml version="1.0" encoding="utf-8"?>\n'
manifest += '<manifest xmlns:android="http://schemas.android.com/apk/res/android"\n'
manifest += '    package="' + pkg_name + '"\n'
manifest += '    android:versionCode="1"\n'
manifest += '    android:versionName="' + config.get('version', '1.0.0') + '">\n'
manifest += '    <uses-sdk android:minSdkVersion="21" android:targetSdkVersion="34" />\n'
manifest += '    <uses-permission android:name="android.permission.INTERNET" />\n'
manifest += '    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />\n'
manifest += '    <uses-permission android:name="android.permission.VIBRATE" />\n'
manifest += '    <application\n'
manifest += '        android:label="@string/app_name"\n'
manifest += '        android:icon="@mipmap/ic_launcher"\n'
manifest += '        android:usesCleartextTraffic="true"\n'
manifest += '        android:theme="@android:style/Theme.NoTitleBar">\n'
manifest += '        <activity\n'
manifest += '            android:name="com.burhan.myapp2.MainActivity"\n'
manifest += '            android:configChanges="orientation|screenSize|keyboardHidden"\n'
manifest += '            android:screenOrientation="' + android_orientation + '"\n'
manifest += '            android:exported="true">\n'
manifest += '            <intent-filter>\n'
manifest += '                <action android:name="android.intent.action.MAIN" />\n'
manifest += '                <category android:name="android.intent.category.LAUNCHER" />\n'
manifest += '            </intent-filter>\n'
manifest += '        </activity>\n'
manifest += '    </application>\n'
manifest += '</manifest>\n'

os.makedirs('app', exist_ok=True)
with open('app/AndroidManifest.xml', 'w') as f:
    f.write(manifest)

# Create assets folder
os.makedirs('app/assets', exist_ok=True)

# Generate HTML content based on build type
build_type = config.get('buildType', 'html')

if build_type == 'html' and config.get('htmlContent'):
    with open('app/assets/index.html', 'w', encoding='utf-8') as f:
        f.write(config['htmlContent'])
    print("Wrote HTML content from upload")

elif build_type == 'url' and config.get('url'):
    html = '<!DOCTYPE html><html><head>'
    html += '<meta charset="utf-8">'
    html += '<meta name="viewport" content="width=device-width,initial-scale=1">'
    html += '<style>body,html{margin:0;padding:0;height:100%;overflow:hidden}iframe{border:0;width:100%;height:100%}</style>'
    html += '</head><body>'
    html += '<iframe src="' + config['url'] + '" allowfullscreen></iframe>'
    html += '</body></html>'
    with open('app/assets/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Wrote iframe HTML for URL")

elif build_type == 'template':
    template_name = config.get('templateName', 'calculator')
    template_loaded = False
    
    # Try multiple paths
    possible_paths = [
        'templates/' + template_name + '.html',
        'templates/' + template_name.lower() + '.html',
        'templates/' + template_name.replace('-', '') + '.html',
    ]
    
    for tpath in possible_paths:
        if os.path.exists(tpath):
            with open(tpath, 'r', encoding='utf-8') as tf:
                template_html = tf.read()
            with open('app/assets/index.html', 'w', encoding='utf-8') as f:
                f.write(template_html)
            print("Loaded real template: " + tpath)
            template_loaded = True
            break
    
    if not template_loaded:
        # Fallback placeholder
        html = '<!DOCTYPE html><html><head>'
        html += '<meta charset="utf-8">'
        html += '<meta name="viewport" content="width=device-width,initial-scale=1">'
        html += '<title>' + config.get('appName', 'App') + '</title>'
        html += '<style>body{font-family:system-ui;background:#111;color:#eee;display:flex;align-items:center;justify-content:center;height:100vh;margin:0;text-align:center;padding:20px}h1{color:#6366f1}</style>'
        html += '</head><body>'
        html += '<div><h1>' + config.get('appName', 'App') + '</h1>'
        html += '<p>Template: ' + template_name + '</p>'
        html += '<p>Build ID: ' + config.get('id', '') + '</p></div>'
        html += '</body></html>'
        with open('app/assets/index.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print("Placeholder used (no template file found)")

else:
    with open('app/assets/index.html', 'w', encoding='utf-8') as f:
        f.write('<!DOCTYPE html><html><body><h1>Hello</h1></body></html>')
    print("Default HTML used")

print("Config generation complete!")
