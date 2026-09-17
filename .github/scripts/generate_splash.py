#!/usr/bin/env python3
"""APKForge - Generate splash resources (robust)"""

import json
import os
import re

DEFAULT_COLOR = '#6366f1'

# Try multiple locations
splash = None
for path in ['app/assets/splash_config.json', 'splash_config.json']:
    if os.path.exists(path):
        try:
            with open(path) as f:
                splash = json.load(f)
            print(f"Loaded splash config from: {path}")
            break
        except Exception as e:
            print(f"Failed to read {path}: {e}")

if not splash:
    splash = {
        'style': 'gradient',
        'color': DEFAULT_COLOR,
        'icon': 'rocket',
        'duration': 2000,
        'tagline': 'Powered by APKForge'
    }
    print("Using default splash config")

# ===== VALIDATE COLOR =====
raw_color = str(splash.get('color', DEFAULT_COLOR)).strip()

# Remove leading # if present
if raw_color.startswith('#'):
    raw_color = raw_color[1:]

# Keep only hex characters
raw_color = re.sub(r'[^0-9A-Fa-f]', '', raw_color)

# Handle different hex lengths
if len(raw_color) == 3:
    # Expand #fff -> ffffff
    raw_color = raw_color[0]*2 + raw_color[1]*2 + raw_color[2]*2
elif len(raw_color) == 8:
    # Remove existing alpha (RRGGBBAA -> AARRGGBB format needs adjustment)
    # Simplest: take first 6
    raw_color = raw_color[:6]
elif len(raw_color) != 6:
    # Invalid, use default
    print(f"Invalid color '{raw_color}' (length {len(raw_color)}), using default")
    raw_color = '6366f1'

color = raw_color.upper()
print(f"Final color: #FF{color}")

# ===== VALIDATE OTHER FIELDS =====
style = str(splash.get('style', 'gradient')).strip() or 'gradient'
icon = str(splash.get('icon', 'rocket')).strip() or 'rocket'

try:
    duration = int(splash.get('duration', 2000))
    if duration < 500 or duration > 10000:
        duration = 2000
except:
    duration = 2000

tagline = str(splash.get('tagline', '')).strip()

# XML escape for tagline
def xml_escape(s):
    return (str(s)
        .replace('&', '&amp;')
        .replace('<', '&lt;')
        .replace('>', '&gt;')
        .replace('"', '&quot;')
        .replace("'", '&apos;'))

tagline_safe = xml_escape(tagline)
icon_safe = xml_escape(icon)
style_safe = xml_escape(style)

# ===== WRITE XML =====
os.makedirs('app/res/values', exist_ok=True)

splash_xml = '<?xml version="1.0" encoding="utf-8"?>\n'
splash_xml += '<resources>\n'
splash_xml += '    <color name="splash_bg">#FF' + color + '</color>\n'
splash_xml += '    <integer name="splash_duration">' + str(duration) + '</integer>\n'
splash_xml += '    <string name="splash_icon">' + icon_safe + '</string>\n'
splash_xml += '    <string name="splash_style">' + style_safe + '</string>\n'
splash_xml += '    <string name="splash_tagline">' + tagline_safe + '</string>\n'
splash_xml += '</resources>\n'

with open('app/res/values/splash.xml', 'w') as f:
    f.write(splash_xml)

print("Splash XML written successfully:")
print(splash_xml)
