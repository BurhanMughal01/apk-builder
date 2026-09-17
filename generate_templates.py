#!/usr/bin/env python3
"""Bulk generate Islamic + utility templates"""

import os

os.makedirs('templates', exist_ok=True)

TEMPLATES = {}

# ===== 1. CALCULATOR =====
TEMPLATES['calculator'] = '''<!DOCTYPE html>
<html><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no">
<title>Calculator</title>
<style>
*{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}
body{font-family:system-ui;background:#0a0a1a;color:#fff;height:100vh;display:flex;align-items:center;justify-content:center;padding:12px}
.calc{width:100%;max-width:400px;background:#16162e;border-radius:24px;padding:20px}
.display{background:#0a0a1a;border-radius:16px;padding:20px;margin-bottom:20px;text-align:right;min-height:100px;display:flex;flex-direction:column;justify-content:flex-end}
.history{font-size:14px;color:#64748b;min-height:20px;margin-bottom:8px}
.current{font-size:42px;font-weight:700;word-break:break-all}
.buttons{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}
button{aspect-ratio:1;border:none;border-radius:16px;font-size:22px;font-weight:600;color:#fff;font-family:inherit}
button:active{transform:scale(0.95);opacity:0.8}
.num{background:#2a2a4a}.op{background:#6366f1}.func{background:#ec4899}.clear{background:#ef4444}
.equals{background:linear-gradient(135deg,#6366f1,#ec4899);grid-column:span 2;aspect-ratio:2.1}
.zero{grid-column:span 2;aspect-ratio:2.1}
</style></head><body>
<div class="calc">
<div class="display"><div class="history" id="h"></div><div class="current" id="c">0</div></div>
<div class="buttons">
<button class="clear" onclick="ac()">AC</button>
<button class="func" onclick="del()">DEL</button>
<button class="func" onclick="pct()">%</button>
<button class="op" onclick="op(\\'/\\')">/</button>
<button class="num" onclick="n(\\'7\\')">7</button>
<button class="num" onclick="n(\\'8\\')">8</button>
<button class="num" onclick="n(\\'9\\')">9</button>
<button class="op" onclick="op(\\'*\\')">x</button>
<button class="num" onclick="n(\\'4\\')">4</button>
<button class="num" onclick="n(\\'5\\')">5</button>
<button class="num" onclick="n(\\'6\\')">6</button>
<button class="op" onclick="op(\\'-\\')">-</button>
<button class="num" onclick="n(\\'1\\')">1</button>
<button class="num" onclick="n(\\'2\\')">2</button>
<button class="num" onclick="n(\\'3\\')">3</button>
<button class="op" onclick="op(\\'+\\')">+</button>
<button class="num zero" onclick="n(\\'0\\')">0</button>
<button class="num" onclick="n(\\'.\\')">.</button>
<button class="equals" onclick="eq()">=</button>
</div></div>
<script>
let c=\\'0\\',p=\\'\\',o=null,r=false;
function u(){document.getElementById(\\'c\\').textContent=c;document.getElementById(\\'h\\').textContent=p&&o?p+\\' \\'+o:\\'\\'}
function n(x){if(r){c=\\'0\\';r=false}if(x===\\'.\\'&&c.includes(\\'.\\'))return;c=c===\\'0\\'&&x!==\\'.\\'?x:c+x;u()}
function op(x){if(o&&!r)eq();p=c;o=x;r=true;u()}
function eq(){if(!o)return;let a=parseFloat(p),b=parseFloat(c),res=0;
if(o===\\'+\\')res=a+b;else if(o===\\'-\\')res=a-b;else if(o===\\'*\\')res=a*b;else res=b===0?\\'Err\\':a/b;
c=String(Math.round(res*1e10)/1e10);p=\\'\\';o=null;r=true;u()}
function ac(){c=\\'0\\';p=\\'\\';o=null;r=false;u()}
function del(){c=c.length>1?c.slice(0,-1):\\'0\\';u()}
function pct(){c=String(parseFloat(c)/100);u()}
u();
</script></body></html>'''

# ===== 2. TASBEEH (already exists, will skip) =====

# ===== 3. DUAS =====
TEMPLATES['dua'] = '''<!DOCTYPE html>
<html lang="ar" dir="rtl"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Duas</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:system-ui;background:#0a0a1a;color:#fff;min-height:100vh;padding:16px}
h1{font-size:22px;text-align:center;margin-bottom:6px;background:linear-gradient(135deg,#6366f1,#ec4899);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.sub{text-align:center;color:#94a3b8;font-size:12px;margin-bottom:20px}
.card{background:#16162e;border-radius:16px;padding:20px;margin-bottom:14px;border:1px solid rgba(99,102,241,0.2)}
.card h3{color:#a5b4fc;font-size:16px;margin-bottom:12px}
.arabic{font-size:22px;line-height:1.8;color:#e0e7ff;margin-bottom:10px;text-align:right}
.urdu{font-size:14px;color:#94a3b8;margin-bottom:8px;text-align:right}
.ref{font-size:11px;color:#64748b;text-align:left;font-style:italic}
</style></head><body>
<h1>Daily Duas</h1>
<p class="sub">Masnoon Duain</p>

<div class="card"><h3>Morning Dua</h3>
<div class="arabic">اللَّهُمَّ بِكَ أَصْبَحْنَا وَبِكَ أَمْسَيْنَا وَبِكَ نَحْيَا وَبِكَ نَمُوتُ وَإِلَيْكَ النُّشُورُ</div>
<div class="urdu">اے اللہ! تیری مدد سے ہم نے صبح کی...</div>
<div class="ref">Tirmidhi</div></div>

<div class="card"><h3>Evening Dua</h3>
<div class="arabic">اللَّهُمَّ بِكَ أَمْسَيْنَا وَبِكَ أَصْبَحْنَا وَبِكَ نَحْيَا وَبِكَ نَمُوتُ وَإِلَيْكَ الْمَصِيرُ</div>
<div class="urdu">اے اللہ! تیری مدد سے ہم نے شام کی...</div>
<div class="ref">Tirmidhi</div></div>

<div class="card"><h3>Before Eating</h3>
<div class="arabic">بِسْمِ اللَّهِ وَعَلَى بَرَكَةِ اللَّهِ</div>
<div class="urdu">اللہ کے نام سے اور اللہ کی برکت پر</div>
<div class="ref">Abu Dawud</div></div>

<div class="card"><h3>After Eating</h3>
<div class="arabic">الْحَمْدُ لِلَّهِ الَّذِي أَطْعَمَنَا وَسَقَانَا وَجَعَلَنَا مُسْلِمِينَ</div>
<div class="urdu">تمام تعریف اللہ کے لیے جس نے کھلایا پلایا اور مسلمان بنایا</div>
<div class="ref">Tirmidhi</div></div>

<div class="card"><h3>Before Sleeping</h3>
<div class="arabic">بِاسْمِكَ اللَّهُمَّ أَمُوتُ وَأَحْيَا</div>
<div class="urdu">اے اللہ! تیرے نام سے مرتا اور جیتا ہوں</div>
<div class="ref">Bukhari</div></div>

<div class="card"><h3>Upon Waking</h3>
<div class="arabic">الْحَمْدُ لِلَّهِ الَّذِي أَحْيَانَا بَعْدَ مَا أَمَاتَنَا وَإِلَيْهِ النُّشُورُ</div>
<div class="urdu">تمام تعریف اللہ کے لیے جس نے مارنے کے بعد زندہ کیا</div>
<div class="ref">Bukhari</div></div>
</body></html>'''

# ===== 4. 99 NAMES =====
TEMPLATES['names99'] = '''<!DOCTYPE html>
<html><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>99 Names of Allah</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:system-ui;background:#0a0a1a;color:#fff;padding:16px}
h1{text-align:center;font-size:22px;background:linear-gradient(135deg,#6366f1,#ec4899);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:6px}
.sub{text-align:center;color:#94a3b8;font-size:12px;margin-bottom:20px}
.grid{display:grid;gap:10px}
.name{background:#16162e;border-radius:12px;padding:14px;border:1px solid rgba(99,102,241,0.2);display:flex;justify-content:space-between;align-items:center;gap:12px}
.num{background:linear-gradient(135deg,#6366f1,#ec4899);width:32px;height:32px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:13px;flex-shrink:0}
.content{flex:1;text-align:right}
.arabic{font-size:20px;color:#a5b4fc;line-height:1.4;margin-bottom:2px}
.translit{font-size:12px;color:#e0e7ff;margin-bottom:2px}
.meaning{font-size:11px;color:#64748b}
</style></head><body>
<h1>99 Names of Allah</h1>
<p class="sub">Asma ul Husna</p>
<div class="grid">
<div class="name"><div class="num">1</div><div class="content"><div class="arabic">الرَّحْمَنُ</div><div class="translit">Ar-Rahman</div><div class="meaning">The Most Gracious</div></div></div>
<div class="name"><div class="num">2</div><div class="content"><div class="arabic">الرَّحِيمُ</div><div class="translit">Ar-Raheem</div><div class="meaning">The Most Merciful</div></div></div>
<div class="name"><div class="num">3</div><div class="content"><div class="arabic">الْمَلِكُ</div><div class="translit">Al-Malik</div><div class="meaning">The King</div></div></div>
<div class="name"><div class="num">4</div><div class="content"><div class="arabic">الْقُدُّوسُ</div><div class="translit">Al-Quddus</div><div class="meaning">The Most Holy</div></div></div>
<div class="name"><div class="num">5</div><div class="content"><div class="arabic">السَّلَامُ</div><div class="translit">As-Salam</div><div class="meaning">The Source of Peace</div></div></div>
<div class="name"><div class="num">6</div><div class="content"><div class="arabic">الْمُؤْمِنُ</div><div class="translit">Al-Mumin</div><div class="meaning">The Guarantor</div></div></div>
<div class="name"><div class="num">7</div><div class="content"><div class="arabic">الْمُهَيْمِنُ</div><div class="translit">Al-Muhaymin</div><div class="meaning">The Guardian</div></div></div>
<div class="name"><div class="num">8</div><div class="content"><div class="arabic">الْعَزِيزُ</div><div class="translit">Al-Aziz</div><div class="meaning">The Almighty</div></div></div>
<div class="name"><div class="num">9</div><div class="content"><div class="arabic">الْجَبَّارُ</div><div class="translit">Al-Jabbar</div><div class="meaning">The Compeller</div></div></div>
<div class="name"><div class="num">10</div><div class="content"><div class="arabic">الْمُتَكَبِّرُ</div><div class="translit">Al-Mutakabbir</div><div class="meaning">The Supreme</div></div></div>
</div></body></html>'''

print("Templates defined:", len(TEMPLATES))

# Write all templates
for name, content in TEMPLATES.items():
    path = 'templates/' + name + '.html'
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Created:", path)

print("Done! Total templates:", len(TEMPLATES))
