content = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no,viewport-fit=cover">
<meta name="theme-color" content="#0c1e3a">
<title>Prayer Times</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Amiri:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{
  --bg:#0a1428;--bg-card:#142544;--bg-elev:#1c3160;--bg-input:#0f1c38;
  --text:#e0e7ff;--text-muted:#93a5c8;--text-subtle:#5a6f99;
  --primary:#0ea5e9;--primary-dark:#0284c7;--accent:#f59e0b;--green:#10b981;
  --sky-grad:linear-gradient(135deg,#0ea5e9,#38bdf8);
  --sunset-grad:linear-gradient(135deg,#f59e0b,#ef4444);
  --border:rgba(14,165,233,0.2);--border-hover:rgba(14,165,233,0.5);
  --shadow:0 4px 24px rgba(0,0,0,0.4);
  --shadow-glow:0 0 30px rgba(14,165,233,0.3);
  --nav-h:64px;--header-h:60px;
}
[data-theme="light"]{
  --bg:#f0f9ff;--bg-card:#ffffff;--bg-elev:#e0f2fe;--bg-input:#ffffff;
  --text:#0c1e3a;--text-muted:#0369a1;--text-subtle:#7dd3fc;
  --border:rgba(3,105,161,0.15);--border-hover:rgba(3,105,161,0.35);
  --shadow:0 4px 24px rgba(12,30,58,0.1);
}
*{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}
html,body{height:100%;overflow:hidden}
body{
  font-family:'Inter',system-ui,sans-serif;
  background:var(--bg);color:var(--text);
  transition:background .3s,color .3s;
  overscroll-behavior:none;-webkit-font-smoothing:antialiased;
}
button{font-family:inherit;cursor:pointer;border:none;background:none;color:inherit}

/* HEADER */
.header{
  position:fixed;top:0;left:0;right:0;height:var(--header-h);
  background:rgba(10,20,40,0.85);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);
  border-bottom:1px solid var(--border);
  display:flex;align-items:center;padding:0 16px;gap:12px;z-index:50;
}
[data-theme="light"] .header{background:rgba(240,249,255,0.9)}
.header-title{flex:1;font-size:17px;font-weight:700;display:flex;align-items:center;gap:10px}
.logo{width:34px;height:34px;border-radius:10px;background:var(--sky-grad);display:grid;place-items:center;font-size:18px;box-shadow:0 4px 14px rgba(14,165,233,0.5)}
.icon-btn{width:40px;height:40px;border-radius:12px;display:grid;place-items:center;color:var(--text-muted);transition:all .2s}
.icon-btn:active{background:var(--bg-card);color:var(--primary)}
.icon-btn svg{width:20px;height:20px;stroke:currentColor;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}

.main{position:fixed;top:var(--header-h);bottom:var(--nav-h);left:0;right:0;overflow-y:auto;-webkit-overflow-scrolling:touch}
.main::-webkit-scrollbar{width:0}
.view{display:none;padding:16px;min-height:100%}
.view.active{display:block;animation:fadeIn .3s ease}
@keyframes fadeIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}

/* HERO CARD */
.hero{
  background:linear-gradient(135deg,#0c1e3a 0%,#1e3a8a 50%,#7c3aed 100%);
  border-radius:24px;padding:24px;margin-bottom:16px;
  position:relative;overflow:hidden;
  box-shadow:0 8px 30px rgba(14,165,233,0.3);
  color:#fff;
}
.hero::before{
  content:'';position:absolute;top:-50px;right:-50px;
  width:200px;height:200px;border-radius:50%;
  background:radial-gradient(circle,rgba(251,191,36,0.3),transparent 70%);
}
.hero::after{
  content:'';position:absolute;bottom:-30px;left:-30px;
  width:150px;height:150px;border-radius:50%;
  background:radial-gradient(circle,rgba(14,165,233,0.4),transparent 70%);
}
.hero-content{position:relative;z-index:1}
.hero-location{font-size:12px;opacity:0.85;margin-bottom:4px;display:flex;align-items:center;gap:6px}
.hero-location svg{width:12px;height:12px;stroke:currentColor;fill:none;stroke-width:2.5}
.hero-city{font-size:22px;font-weight:800;margin-bottom:16px;letter-spacing:-0.5px}
.hero-next-label{font-size:11px;text-transform:uppercase;letter-spacing:1.5px;opacity:0.85;margin-bottom:6px;font-weight:600}
.hero-next-name{font-family:'Amiri',serif;font-size:32px;font-weight:700;margin-bottom:2px}
.hero-next-time{font-size:34px;font-weight:800;letter-spacing:-1px;margin-bottom:2px}
.hero-countdown{
  display:inline-block;padding:6px 14px;background:rgba(255,255,255,0.15);
  border-radius:20px;font-size:13px;font-weight:600;backdrop-filter:blur(10px);
  margin-top:8px;
}
.hero-hijri{position:absolute;top:20px;right:20px;text-align:right;font-size:11px;opacity:0.9;z-index:1}
.hero-hijri .h-day{font-size:20px;font-weight:700;display:block;line-height:1}

/* PRAYER LIST */
.prayers-title{font-size:13px;font-weight:700;color:var(--text-muted);text-transform:uppercase;letter-spacing:1.5px;margin-bottom:12px;padding-left:4px}
.prayer-list{display:flex;flex-direction:column;gap:10px}
.prayer-card{
  background:var(--bg-card);border:1px solid var(--border);border-radius:16px;
  padding:16px 18px;display:flex;align-items:center;gap:14px;
  transition:all .3s;position:relative;overflow:hidden;
}
.prayer-card.active{
  background:linear-gradient(135deg,rgba(14,165,233,0.15),rgba(56,189,248,0.1));
  border-color:var(--primary);box-shadow:var(--shadow-glow);
}
.prayer-card.active::before{
  content:'';position:absolute;left:0;top:0;bottom:0;width:4px;
  background:var(--sky-grad);border-radius:0 4px 4px 0;
}
.prayer-icon{
  width:42px;height:42px;border-radius:12px;
  background:var(--bg-elev);display:grid;place-items:center;
  font-size:20px;flex-shrink:0;
}
.prayer-card.active .prayer-icon{background:var(--sky-grad);box-shadow:0 4px 12px rgba(14,165,233,0.4)}
.prayer-info{flex:1;min-width:0}
.prayer-name{font-size:15px;font-weight:700;margin-bottom:2px}
.prayer-arabic{font-family:'Amiri',serif;font-size:13px;color:var(--text-muted);font-weight:400}
.prayer-time{font-size:18px;font-weight:800;color:var(--primary);font-variant-numeric:tabular-nums}
.prayer-card.active .prayer-time{color:#38bdf8}

/* BOTTOM NAV */
.bottom-nav{
  position:fixed;bottom:0;left:0;right:0;height:var(--nav-h);
  background:rgba(20,37,68,0.95);backdrop-filter:blur(20px);
  border-top:1px solid var(--border);
  display:grid;grid-template-columns:repeat(3,1fr);z-index:50;padding-bottom:env(safe-area-inset-bottom);
}
[data-theme="light"] .bottom-nav{background:rgba(255,255,255,0.95)}
.nav-item{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:3px;color:var(--text-subtle);font-size:10px;font-weight:600;padding:8px}
.nav-item svg{width:22px;height:22px;stroke:currentColor;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.nav-item.active{color:var(--primary)}

/* SETTINGS */
.settings-group{background:var(--bg-card);border:1px solid var(--border);border-radius:16px;margin-bottom:14px;overflow:hidden}
.setting-row{display:flex;align-items:center;justify-content:space-between;padding:16px;gap:12px;border-bottom:1px solid var(--border)}
.setting-row:last-child{border-bottom:none}
.setting-info{flex:1;display:flex;align-items:center;gap:12px}
.setting-info svg{width:20px;height:20px;stroke:var(--primary);fill:none;stroke-width:2;flex-shrink:0}
.setting-label{font-size:14px;font-weight:600}
.setting-sub{font-size:11px;color:var(--text-subtle);margin-top:2px}
.input-field{
  width:100%;padding:12px 14px;background:var(--bg-input);border:1px solid var(--border);
  border-radius:12px;color:var(--text);font-size:14px;font-family:inherit;outline:none;
}
.input-field:focus{border-color:var(--primary);box-shadow:0 0 0 3px rgba(14,165,233,0.15)}
.btn-primary{
  width:100%;padding:14px;background:var(--sky-grad);color:#fff;
  border-radius:12px;font-weight:700;font-size:14px;font-family:inherit;
  box-shadow:0 4px 14px rgba(14,165,233,0.4);transition:all .2s;
}
.btn-primary:active{transform:scale(0.98)}
.btn-secondary{
  width:100%;padding:14px;background:var(--bg-elev);color:var(--text);
  border-radius:12px;font-weight:600;font-size:14px;font-family:inherit;
  border:1px solid var(--border);transition:all .2s;
}
.btn-secondary:active{transform:scale(0.98)}

/* LOADING */
.loading{text-align:center;padding:60px 20px;color:var(--text-subtle)}
.spinner{
  width:40px;height:40px;border:3px solid var(--border);
  border-top-color:var(--primary);border-radius:50%;
  animation:spin 1s linear infinite;margin:0 auto 16px;
}
@keyframes spin{to{transform:rotate(360deg)}}

/* ERROR */
.error-box{background:rgba(239,68,68,0.1);border:1px solid rgba(239,68,68,0.3);border-radius:14px;padding:20px;text-align:center;margin:20px 0}
.error-box p{color:#fca5a5;font-size:14px;margin-bottom:14px}
.error-box button{padding:10px 20px;background:var(--sky-grad);color:#fff;border-radius:10px;font-size:13px;font-weight:700;font-family:inherit}

/* TOAST */
.toast{position:fixed;bottom:80px;left:50%;transform:translateX(-50%) translateY(20px);background:var(--bg-elev);color:var(--text);padding:12px 22px;border-radius:14px;font-size:13px;font-weight:600;box-shadow:var(--shadow-glow);border:1px solid var(--border-hover);opacity:0;transition:all .3s;pointer-events:none;z-index:200;display:flex;align-items:center;gap:8px}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}

/* MONTHLY TABLE */
.month-view{display:flex;flex-direction:column;gap:8px}
.month-row{background:var(--bg-card);border:1px solid var(--border);border-radius:14px;padding:12px 14px;display:grid;grid-template-columns:50px repeat(5,1fr);gap:6px;align-items:center;font-size:11px}
.month-row.header{background:var(--bg-elev);font-weight:700;color:var(--text-muted);text-transform:uppercase;letter-spacing:0.5px;font-size:9px}
.month-row.today{background:linear-gradient(135deg,rgba(14,165,233,0.15),rgba(56,189,248,0.1));border-color:var(--primary)}
.month-day{font-weight:700;color:var(--primary);font-size:12px}
.month-time{font-weight:600;color:var(--text);font-variant-numeric:tabular-nums}
</style>
</head>
<body data-theme="dark">

<header class="header">
  <div class="header-title">
    <div class="logo">🕌</div>
    <span id="headerTitle">Prayer Times</span>
  </div>
  <button class="icon-btn" onclick="toggleTheme()"><svg viewBox="0 0 24 24" id="themeIcon"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg></button>
</header>

<main class="main" id="mainArea">

  <div class="view active" id="view-today">
    <div id="todayContent">
      <div class="loading"><div class="spinner"></div><p>Loading prayer times...</p></div>
    </div>
  </div>

  <div class="view" id="view-month">
    <h2 style="font-size:20px;font-weight:700;margin-bottom:16px">Monthly Timetable</h2>
    <div id="monthContent" class="month-view">
      <div class="loading"><div class="spinner"></div><p>Loading...</p></div>
    </div>
  </div>

  <div class="view" id="view-settings">
    <h2 style="font-size:20px;font-weight:700;margin-bottom:16px">Settings</h2>

    <div class="settings-group">
      <div class="setting-row" style="flex-direction:column;align-items:stretch">
        <div class="setting-info" style="margin-bottom:12px">
          <svg viewBox="0 0 24 24"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg>
          <div><div class="setting-label">City</div><div class="setting-sub" id="citySub">Current: Karachi</div></div>
        </div>
        <input type="text" id="cityInput" class="input-field" placeholder="Enter city name (e.g. Karachi)" style="margin-bottom:10px">
        <button class="btn-primary" onclick="saveCity()">Save City</button>
      </div>

      <div class="setting-row">
        <div class="setting-info">
          <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>
          <div><div class="setting-label">Method</div><div class="setting-sub" id="methodSub">Karachi (Univ. of Islamic Sciences)</div></div>
        </div>
      </div>
    </div>

    <div class="settings-group">
      <button class="btn-secondary" onclick="useGPS()" style="margin:14px">
        📍 Use My Location (GPS)
      </button>
    </div>

    <div style="text-align:center;padding:20px 0;font-size:12px;color:var(--text-subtle);line-height:1.8">
      Timings by Aladhan API<br>
      Made with ❤️ for the Ummah<br>
      <strong style="color:var(--primary)">APKForge</strong> · v1.0.0
    </div>
  </div>

</main>

<nav class="bottom-nav">
  <button class="nav-item active" data-view="today" onclick="switchView('today')">
    <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>
    <span>Today</span>
  </button>
  <button class="nav-item" data-view="month" onclick="switchView('month')">
    <svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></svg>
    <span>Month</span>
  </button>
  <button class="nav-item" data-view="settings" onclick="switchView('settings')">
    <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 00.33 1.82l.06.06a2 2 0 11-2.83 2.83l-.06-.06a1.65 1.65 0 00-1.82-.33 1.65 1.65 0 00-1 1.51V21a2 2 0 11-4 0v-.09a1.65 1.65 0 00-1.08-1.51 1.65 1.65 0 00-1.82.33l-.06.06a2 2 0 11-2.83-2.83l.06-.06a1.65 1.65 0 00.33-1.82 1.65 1.65 0 00-1.51-1H3a2 2 0 110-4h.09A1.65 1.65 0 004.6 9a1.65 1.65 0 00-.33-1.82l-.06-.06a2 2 0 112.83-2.83l.06.06a1.65 1.65 0 001.82.33H9a1.65 1.65 0 001-1.51V3a2 2 0 114 0v.09a1.65 1.65 0 001 1.51 1.65 1.65 0 001.82-.33l.06-.06a2 2 0 112.83 2.83l-.06.06a1.65 1.65 0 00-.33 1.82V9a1.65 1.65 0 001.51 1H21a2 2 0 110 4h-.09a1.65 1.65 0 00-1.51 1z"/></svg>
    <span>Settings</span>
  </button>
</nav>

<div class="toast" id="toast"><span id="toastText">Saved</span></div>

<script>
/* PART 2 WILL BE INJECTED */
</script>
</body>
</html>
'''

with open('templates/prayer.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Chunk 1 saved:', len(content), 'bytes')
