content = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no,viewport-fit=cover">
<meta name="theme-color" content="#0c1410">
<title>Qibla Compass</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Amiri:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{
  --bg:#0a1410;--bg-card:#152822;--bg-elev:#1e3a30;--bg-input:#0f1e18;
  --text:#d1fae5;--text-muted:#86bfa0;--text-subtle:#4a8b6b;
  --primary:#10b981;--primary-dark:#059669;--accent:#fbbf24;--gold:#f59e0b;
  --kaaba:#dc2626;
  --gold-grad:linear-gradient(135deg,#fbbf24,#f59e0b);
  --green-grad:linear-gradient(135deg,#10b981,#059669);
  --border:rgba(16,185,129,0.2);--border-hover:rgba(16,185,129,0.5);
  --shadow:0 4px 24px rgba(0,0,0,0.5);
  --shadow-glow:0 0 40px rgba(251,191,36,0.4);
  --nav-h:64px;--header-h:60px;
}
[data-theme="light"]{
  --bg:#f0fdf4;--bg-card:#ffffff;--bg-elev:#dcfce7;--bg-input:#ffffff;
  --text:#052e16;--text-muted:#047857;--text-subtle:#6ee7b7;
  --border:rgba(5,150,105,0.2);--border-hover:rgba(5,150,105,0.4);
  --shadow:0 4px 24px rgba(5,46,22,0.1);
}
*{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}
html,body{height:100%;overflow:hidden}
body{
  font-family:'Inter',system-ui,sans-serif;
  background:var(--bg);color:var(--text);
  transition:background .3s,color .3s;
  overscroll-behavior:none;-webkit-font-smoothing:antialiased;
  background-image:radial-gradient(circle at 50% 20%,rgba(16,185,129,0.12),transparent 50%),radial-gradient(circle at 50% 100%,rgba(251,191,36,0.08),transparent 50%);
}
button{font-family:inherit;cursor:pointer;border:none;background:none;color:inherit}
input{font-family:inherit}

/* HEADER */
.header{
  position:fixed;top:0;left:0;right:0;height:var(--header-h);
  background:rgba(10,20,16,0.9);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);
  border-bottom:1px solid var(--border);
  display:flex;align-items:center;padding:0 16px;gap:12px;z-index:50;
}
[data-theme="light"] .header{background:rgba(240,253,244,0.95)}
.header-title{flex:1;font-size:17px;font-weight:700;display:flex;align-items:center;gap:10px}
.logo{width:34px;height:34px;border-radius:10px;background:var(--gold-grad);display:grid;place-items:center;font-size:18px;box-shadow:0 4px 14px rgba(251,191,36,0.5)}
.icon-btn{width:40px;height:40px;border-radius:12px;display:grid;place-items:center;color:var(--text-muted);transition:all .2s}
.icon-btn:active{background:var(--bg-card);color:var(--primary)}
.icon-btn svg{width:20px;height:20px;stroke:currentColor;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}

.main{position:fixed;top:var(--header-h);bottom:var(--nav-h);left:0;right:0;overflow-y:auto;-webkit-overflow-scrolling:touch}
.main::-webkit-scrollbar{width:0}
.view{display:none;padding:16px;min-height:100%}
.view.active{display:block;animation:fadeIn .3s ease}
@keyframes fadeIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}

/* COMPASS VIEW */
.compass-container{
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  min-height:calc(100% - 20px);padding:20px 0;
}

.status-badge{
  display:inline-flex;align-items:center;gap:8px;
  padding:8px 16px;border-radius:20px;
  background:var(--bg-card);border:1px solid var(--border);
  font-size:12px;font-weight:600;margin-bottom:20px;
}
.status-dot{
  width:8px;height:8px;border-radius:50%;
  background:var(--primary);
  box-shadow:0 0 12px var(--primary);
  animation:pulse 2s infinite;
}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:0.5}}

/* COMPASS RING */
.compass-wrap{
  position:relative;width:min(340px,90vw);height:min(340px,90vw);
  margin-bottom:24px;
}

.compass-svg{
  position:absolute;inset:0;width:100%;height:100%;
  transition:transform .15s ease-out;
}

.compass-inner{
  position:absolute;inset:0;border-radius:50%;
  background:radial-gradient(circle at 50% 30%,var(--bg-elev),var(--bg-card) 70%);
  border:4px solid var(--border);
  box-shadow:inset 0 0 60px rgba(16,185,129,0.15),0 8px 40px rgba(0,0,0,0.5);
  overflow:hidden;
}

.cardinal{
  position:absolute;font-weight:800;font-size:16px;
  color:var(--text-muted);
  font-family:'Inter',sans-serif;
}
.cardinal.n{top:12px;left:50%;transform:translateX(-50%);color:var(--kaaba);font-size:20px}
.cardinal.s{bottom:12px;left:50%;transform:translateX(-50%)}
.cardinal.e{right:12px;top:50%;transform:translateY(-50%)}
.cardinal.w{left:12px;top:50%;transform:translateY(-50%)}

.cardinal-sub{
  position:absolute;font-size:9px;color:var(--text-subtle);
  letter-spacing:1px;font-weight:600;
}
.cardinal-sub.n{top:38px;left:50%;transform:translateX(-50%)}
.cardinal-sub.s{bottom:38px;left:50%;transform:translateX(-50%)}

/* DEGREE TICKS */
.tick{
  position:absolute;top:0;left:50%;
  width:2px;height:8px;
  background:var(--border-hover);
  transform-origin:center calc(min(340px,90vw)/2);
  margin-left:-1px;
}
.tick.major{
  height:14px;width:3px;
  background:var(--accent);
  margin-left:-1.5px;
}

/* NEEDLE */
.needle{
  position:absolute;top:50%;left:50%;
  transform-origin:center;
  width:100%;height:100%;
  margin-left:calc(min(340px,90vw)/-2);
  margin-top:calc(min(340px,90vw)/-2);
  pointer-events:none;
  transition:transform .2s ease-out;
}
.needle-arrow{
  position:absolute;top:8%;left:50%;
  transform:translateX(-50%);
  width:0;height:0;
  border-left:14px solid transparent;
  border-right:14px solid transparent;
  border-bottom:80px solid var(--gold);
  filter:drop-shadow(0 0 12px rgba(251,191,36,0.7));
}
.needle-tail{
  position:absolute;bottom:8%;left:50%;
  transform:translateX(-50%);
  width:0;height:0;
  border-left:10px solid transparent;
  border-right:10px solid transparent;
  border-top:60px solid var(--text-subtle);
  opacity:0.5;
}
.needle-center{
  position:absolute;top:50%;left:50%;
  transform:translate(-50%,-50%);
  width:20px;height:20px;border-radius:50%;
  background:var(--gold-grad);
  box-shadow:0 0 20px rgba(251,191,36,0.8);
  border:3px solid var(--bg-card);
}

/* KAABA MARKER */
.kaaba-marker{
  position:absolute;top:50%;left:50%;
  transform-origin:center;
  width:100%;height:100%;
  margin-left:calc(min(340px,90vw)/-2);
  margin-top:calc(min(340px,90vw)/-2);
  pointer-events:none;
  transition:transform .15s ease-out;
}
.kaaba-icon{
  position:absolute;top:20px;left:50%;
  transform:translateX(-50%);
  font-size:28px;
  filter:drop-shadow(0 0 12px rgba(220,38,38,0.8));
  animation:bob 2s infinite;
}
@keyframes bob{0%,100%{transform:translateX(-50%) translateY(0)}50%{transform:translateX(-50%) translateY(-4px)}}

/* INFO CARDS */
.info-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px;width:100%;max-width:400px;margin-top:16px}
.info-card{
  background:var(--bg-card);border:1px solid var(--border);
  border-radius:16px;padding:16px;text-align:center;
}
.info-val{
  font-size:22px;font-weight:800;
  background:var(--gold-grad);-webkit-background-clip:text;-webkit-text-fill-color:transparent;
  margin-bottom:4px;font-variant-numeric:tabular-nums;
}
.info-label{font-size:10px;color:var(--text-subtle);text-transform:uppercase;letter-spacing:1px;font-weight:700}

.location-card{
  background:var(--bg-card);border:1px solid var(--border);
  border-radius:16px;padding:14px 16px;width:100%;max-width:400px;margin-top:12px;
  display:flex;align-items:center;gap:12px;
}
.loc-icon{width:36px;height:36px;border-radius:10px;background:var(--green-grad);display:grid;place-items:center;font-size:18px;flex-shrink:0}
.loc-info{flex:1;min-width:0}
.loc-city{font-size:14px;font-weight:700;margin-bottom:2px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.loc-coords{font-size:11px;color:var(--text-subtle);font-variant-numeric:tabular-nums}

/* ALIGNED INDICATOR */
.aligned-toast{
  position:fixed;top:50%;left:50%;
  transform:translate(-50%,-50%) scale(0);
  background:var(--gold-grad);color:#0a1410;
  padding:20px 40px;border-radius:20px;
  font-size:18px;font-weight:800;
  box-shadow:0 10px 40px rgba(251,191,36,0.6);
  z-index:200;text-align:center;
  transition:transform .3s cubic-bezier(0.34,1.56,0.64,1);
  pointer-events:none;
}
.aligned-toast.show{transform:translate(-50%,-50%) scale(1)}
.aligned-toast .sub{font-size:13px;opacity:0.85;margin-top:4px;font-weight:600}

/* CALIBRATION */
.calib-warning{
  background:rgba(239,68,68,0.1);border:1px solid rgba(239,68,68,0.3);
  border-radius:14px;padding:14px 16px;margin-bottom:16px;display:none;
  align-items:center;gap:10px;
}
.calib-warning.show{display:flex}
.calib-warning svg{width:20px;height:20px;stroke:#fca5a5;fill:none;stroke-width:2.5;flex-shrink:0}
.calib-warning p{font-size:12px;color:#fca5a5;line-height:1.5}

/* SETTINGS */
.settings-group{background:var(--bg-card);border:1px solid var(--border);border-radius:16px;margin-bottom:14px;overflow:hidden}
.setting-row{display:flex;align-items:center;justify-content:space-between;padding:16px;gap:12px;border-bottom:1px solid var(--border);flex-direction:column;align-items:stretch}
.setting-row:last-child{border-bottom:none}
.setting-info{display:flex;align-items:center;gap:12px;margin-bottom:12px}
.setting-info svg{width:20px;height:20px;stroke:var(--primary);fill:none;stroke-width:2;flex-shrink:0}
.setting-label{font-size:14px;font-weight:600}
.setting-sub{font-size:11px;color:var(--text-subtle);margin-top:2px}
.input-field{
  width:100%;padding:12px 14px;background:var(--bg-input);border:1px solid var(--border);
  border-radius:12px;color:var(--text);font-size:14px;outline:none;margin-bottom:10px;
}
.input-field:focus{border-color:var(--primary);box-shadow:0 0 0 3px rgba(16,185,129,0.15)}
.btn-primary{
  width:100%;padding:14px;background:var(--gold-grad);color:#0a1410;
  border-radius:12px;font-weight:700;font-size:14px;font-family:inherit;
  box-shadow:0 4px 14px rgba(251,191,36,0.4);
}
.btn-secondary{
  width:100%;padding:14px;background:var(--bg-elev);color:var(--text);
  border-radius:12px;font-weight:600;font-size:14px;font-family:inherit;
  border:1px solid var(--border);
}

/* BOTTOM NAV */
.bottom-nav{
  position:fixed;bottom:0;left:0;right:0;height:var(--nav-h);
  background:rgba(21,40,34,0.95);backdrop-filter:blur(20px);
  border-top:1px solid var(--border);
  display:grid;grid-template-columns:repeat(2,1fr);z-index:50;padding-bottom:env(safe-area-inset-bottom);
}
[data-theme="light"] .bottom-nav{background:rgba(255,255,255,0.95)}
.nav-item{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:3px;color:var(--text-subtle);font-size:10px;font-weight:600;padding:8px}
.nav-item svg{width:22px;height:22px;stroke:currentColor;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.nav-item.active{color:var(--primary)}

/* TOAST */
.toast{position:fixed;bottom:80px;left:50%;transform:translateX(-50%) translateY(20px);background:var(--bg-elev);color:var(--text);padding:12px 22px;border-radius:14px;font-size:13px;font-weight:600;box-shadow:var(--shadow-glow);border:1px solid var(--border-hover);opacity:0;transition:all .3s;pointer-events:none;z-index:200}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
</style>
</head>
<body data-theme="dark">

<header class="header">
  <div class="header-title">
    <div class="logo">🧭</div>
    <span id="headerTitle">Qibla Compass</span>
  </div>
  <button class="icon-btn" onclick="toggleTheme()"><svg viewBox="0 0 24 24" id="themeIcon"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg></button>
</header>

<main class="main" id="mainArea">

  <!-- COMPASS VIEW -->
  <div class="view active" id="view-compass">
    <div class="compass-container">

      <div class="calib-warning" id="calibWarning">
        <svg viewBox="0 0 24 24"><path d="M10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L13.71 3.86a2 2 0 00-3.42 0z"/><path d="M12 9v4M12 17h.01"/></svg>
        <p>Compass needs calibration. Move your phone in a figure-8 motion.</p>
      </div>

      <div class="status-badge">
        <span class="status-dot"></span>
        <span id="statusText">Initializing compass...</span>
      </div>

      <div class="compass-wrap">
        <div class="compass-inner" id="compassInner">
          <div class="cardinal n">N</div>
          <div class="cardinal-sub n">0°</div>
          <div class="cardinal s">S</div>
          <div class="cardinal-sub s">180°</div>
          <div class="cardinal e">E</div>
          <div class="cardinal w">W</div>
        </div>

        <div class="kaaba-marker" id="kaabaMarker">
          <div class="kaaba-icon">🕋</div>
        </div>

        <div class="needle" id="needle">
          <div class="needle-arrow"></div>
          <div class="needle-tail"></div>
          <div class="needle-center"></div>
        </div>
      </div>

      <div class="info-grid">
        <div class="info-card">
          <div class="info-val" id="qiblaAngle">--°</div>
          <div class="info-label">Qibla Direction</div>
        </div>
        <div class="info-card">
          <div class="info-val" id="distanceVal">--</div>
          <div class="info-label">To Makkah</div>
        </div>
      </div>

      <div class="location-card">
        <div class="loc-icon">📍</div>
        <div class="loc-info">
          <div class="loc-city" id="locCity">Detecting location...</div>
          <div class="loc-coords" id="locCoords">--</div>
        </div>
      </div>

      <button class="btn-secondary" onclick="useGPS()" style="max-width:400px;margin-top:12px">
        📍 Update Location (GPS)
      </button>

    </div>
  </div>

  <!-- SETTINGS VIEW -->
  <div class="view" id="view-settings">
    <h2 style="font-size:20px;font-weight:700;margin-bottom:16px">Settings</h2>

    <div class="settings-group">
      <div class="setting-row">
        <div class="setting-info">
          <svg viewBox="0 0 24 24"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg>
          <div>
            <div class="setting-label">Manual City</div>
            <div class="setting-sub" id="citySub">Current: Karachi</div>
          </div>
        </div>
        <input type="text" id="cityInput" class="input-field" placeholder="Enter city name">
        <button class="btn-primary" onclick="saveCity()">Save City</button>
      </div>

      <div class="setting-row">
        <div class="setting-info">
          <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></svg>
          <div>
            <div class="setting-label">About Qibla</div>
            <div class="setting-sub">Direction to Kaaba in Makkah</div>
          </div>
        </div>
        <p style="font-size:12px;color:var(--text-muted);line-height:1.7;margin-top:8px">
          Qibla is the direction that should be faced when a Muslim prays. It is fixed as the direction of the Kaaba in the Sacred Mosque in Makkah, Saudi Arabia.
        </p>
      </div>
    </div>

    <div style="text-align:center;padding:20px 0;font-size:12px;color:var(--text-subtle);line-height:1.8">
      Made with ❤️ for the Ummah<br>
      <strong style="color:var(--accent)">APKForge</strong> · v1.0.0
    </div>
  </div>

</main>

<nav class="bottom-nav">
  <button class="nav-item active" data-view="compass" onclick="switchView('compass')">
    <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/></svg>
    <span>Compass</span>
  </button>
  <button class="nav-item" data-view="settings" onclick="switchView('settings')">
    <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 00.33 1.82l.06.06a2 2 0 11-2.83 2.83l-.06-.06a1.65 1.65 0 00-1.82-.33 1.65 1.65 0 00-1 1.51V21a2 2 0 11-4 0v-.09a1.65 1.65 0 00-1.08-1.51 1.65 1.65 0 00-1.82.33l-.06.06a2 2 0 11-2.83-2.83l.06-.06a1.65 1.65 0 00.33-1.82 1.65 1.65 0 00-1.51-1H3a2 2 0 110-4h.09A1.65 1.65 0 004.6 9a1.65 1.65 0 00-.33-1.82l-.06-.06a2 2 0 112.83-2.83l.06.06a1.65 1.65 0 001.82.33H9a1.65 1.65 0 001-1.51V3a2 2 0 114 0v.09a1.65 1.65 0 001 1.51 1.65 1.65 0 001.82-.33l.06-.06a2 2 0 112.83 2.83l-.06.06a1.65 1.65 0 00-.33 1.82V9a1.65 1.65 0 001.51 1H21a2 2 0 110 4h-.09a1.65 1.65 0 00-1.51 1z"/></svg>
    <span>Settings</span>
  </button>
</nav>

<div class="aligned-toast" id="alignedToast">
  🕋 Qibla Aligned!
  <div class="sub">You are facing the Kaaba</div>
</div>

<div class="toast" id="toast"><span id="toastText">Saved</span></div>

<script>
/* PART 2 WILL BE INJECTED */
</script>
</body>
</html>
'''

with open('templates/qibla.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Chunk 1 saved:', len(content), 'bytes')
