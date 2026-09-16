#!/usr/bin/env python3
"""APKForge - Generate splash config"""

import json
import os

try:
    with open('splash_config.json') as f:
        splash = json.load(f)
except:
    splash = {'style': 'gradient', 'color': '#6366f1', 'icon': 'rocket', 'duration': 2000, 'tagline': 'Powered by APKForge'}

os.makedirs('app/res/values', exist_ok=True)

color = splash.get('color', '#6366f1').lstrip('#')

splash_xml = '''<?xml version="1.0" encoding="utf-8"?>
<resources>
    <color name="splash_bg">#FF''' + color.upper() + '''</color>
    <integer name="splash_duration">''' + str(splash.get('duration', 2000)) + '''</integer>
    <string name="splash_icon">''' + splash.get('icon', 'rocket') + '''</string>
    <string name="splash_style">''' + splash.get('style', 'gradient') + '''</string>
    <string name="splash_tagline">''' + splash.get('tagline', '') + '''</string>
</resources>
'''

with open('app/res/values/splash.xml', 'w') as f:
    f.write(splash_xml)

print(f"Splash generated: style={splash.get('style')}, color=#{color}")
