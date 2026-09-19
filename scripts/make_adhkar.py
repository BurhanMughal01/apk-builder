content = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no,viewport-fit=cover">
<meta name="theme-color" content="#061a14">
<title>Adhkar</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Noto+Naskh+Arabic:wght@400;600;700&display=swap" rel="stylesheet">
<style>
:root{
  --bg:#061a14;--bg-card:#0d3328;--bg-elev:#134a3a;--bg-input:#0a261e;
  --text:#d1fae5;--text-muted:#7dd3b0;--text-subtle:#3d8a6b;
  --primary:#10b981;--primary-dark:#059669;--accent:#fbbf24;
  --grad:linear-gradient(135deg,#10b981,#059669);
  --gold-grad:linear-gradient(135deg,#fbbf24,#f59e0b);
  --border:rgba(16,185,129,0.18);--border-hover:rgba(16,185,129,0.45);
  --shadow:0 4px 24px rgba(0,0,0,0.5);
  --shadow-glow:0 0 30px rgba(16,185,129,0.3);
  --nav-h:64px;--header-h:60px;
  --font-arabic:26px;
}
[data-theme="light"]{
  --bg:#f0fdf4;--bg-card:#ffffff;--bg-elev:#dcfce7;--bg-input:#ffffff;
  --text:#052e16;--text-muted:#047857;--text-subtle:#6ee7b7;
  --border:rgba(5,150,105,0.18);--border-hover:rgba(5,150,105,0.4);
  --shadow:0 4px 24px rgba(5,46,22,0.1);
}
*{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}
html,body{height:100%;overflow:hidden}
body{
  font-family:'Inter',system-ui,sans-serif;
  background:var(--bg);color:var(--text);
  transition:background .3s,color .3s;
  overscroll-behavior:none;-webkit-font-smoothing:antialiased;
  background-image:radial-gradient(circle at 20% 10%,rgba(16,185,129,0.08),transparent 40%),radial-gradient(circle at 80% 90%,rgba(251,191,36,0.06),transparent 40%);
}
button{font-family:inherit;cursor:pointer;border:none;background:none;color:inherit}

.header{
  position:fixed;top:0;left:0;right:0;height:var(--header-h);
  background:rgba(6,26,20,0.9);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);
  border-bottom:1px solid var(--border);
  display:flex;align-items:center;padding:0 16px;gap:12px;z-index:50;
}
[data-theme="light"] .header{background:rgba(240,253,244,0.95)}
.header-title{flex:1;font-size:17px;font-weight:700;display:flex;align-items:center;gap:10px}
.logo{width:34px;height:34px;border-radius:10px;background:var(--grad);display:grid;place-items:center;font-size:18px;box-shadow:0 4px 14px rgba(16,185,129,0.5)}
.icon-btn{width:40px;height:40px;border-radius:12px;display:grid;place-items:center;color:var(--text-muted);transition:all .2s}
.icon-btn:active{background:var(--bg-card);color:var(--primary)}
.icon-btn svg{width:20px;height:20px;stroke:currentColor;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}

.main{position:fixed;top:var(--header-h);bottom:var(--nav-h);left:0;right:0;overflow-y:auto;-webkit-overflow-scrolling:touch}
.main::-webkit-scrollbar{width:0}
.view{display:none;padding:16px;min-height:100%}
.view.active{display:block;animation:fadeIn .25s ease}
@keyframes fadeIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}

/* TABS */
.tabs{
  display:grid;grid-template-columns:1fr 1fr;gap:6px;
  background:var(--bg-card);border:1px solid var(--border);
  border-radius:14px;padding:5px;margin-bottom:16px;
}
.tab{
  padding:12px;border-radius:10px;font-size:14px;font-weight:700;
  color:var(--text-muted);text-align:center;transition:all .25s;
  display:flex;align-items:center;justify-content:center;gap:6px;
}
.tab.active{
  background:var(--grad);color:#fff;
  box-shadow:0 4px 14px rgba(16,185,129,0.4);
}
.tab:active{transform:scale(0.97)}

/* PROGRESS */
.progress-wrap{
  background:var(--bg-card);border:1px solid var(--border);
  border-radius:16px;padding:16px;margin-bottom:16px;
}
.progress-head{display:flex;align-items:center;justify-content:space-between;margin-bottom:10px}
.progress-title{font-size:12px;color:var(--text-subtle);font-weight:700;text-transform:uppercase;letter-spacing:1px}
.progress-count{font-size:13px;font-weight:700;color:var(--primary)}
.progress-bar{height:8px;background:var(--bg-elev);border-radius:4px;overflow:hidden}
.progress-fill{height:100%;background:var(--grad);border-radius:4px;transition:width .4s;box-shadow:0 0 12px rgba(16,185,129,0.5)}

/* ADHKAR CARD */
.adhkar-card{
  background:var(--bg-card);border:1px solid var(--border);
  border-radius:18px;padding:18px;margin-bottom:12px;
  transition:all .3s;position:relative;
}
.adhkar-card.completed{border-color:var(--primary);background:linear-gradient(135deg,rgba(16,185,129,0.08),rgba(16,185,129,0.02))}
.adhkar-card.completed::before{
  content:'✓';position:absolute;top:12px;right:12px;
  width:24px;height:24px;border-radius:50%;
  background:var(--grad);color:#fff;
  display:grid;place-items:center;font-size:14px;font-weight:800;
  box-shadow:0 4px 12px rgba(16,185,129,0.5);
}
.adhkar-top{display:flex;align-items:center;gap:10px;margin-bottom:14px;flex-wrap:wrap}
.adhkar-title{font-size:15px;font-weight:700;flex:1;min-width:0}
.adhkar-count-badge{
  font-size:10px;padding:4px 10px;border-radius:8px;
  background:rgba(251,191,36,0.15);color:var(--accent);
  font-weight:800;letter-spacing:0.5px;text-transform:uppercase;
  flex-shrink:0;
}
.adhkar-arabic{
  font-family:'Noto Naskh Arabic',serif;font-size:var(--font-arabic);
  line-height:2;color:var(--text);direction:rtl;text-align:right;
  margin-bottom:14px;
}
.adhkar-trans{
  font-size:13px;color:var(--text-muted);line-height:1.7;
  margin-bottom:12px;
}
.adhkar-ref{
  font-size:11px;color:var(--text-subtle);font-style:italic;
  padding-top:10px;border-top:1px solid var(--border);
}

/* COUNTER ROW */
.counter-row{
  display:flex;align-items:center;gap:10px;margin-top:14px;
  padding-top:14px;border-top:1px solid var(--border);
}
.counter-btn{
  flex:1;padding:14px;border-radius:12px;
  background:var(--grad);color:#fff;
  font-size:15px;font-weight:800;font-family:inherit;
  display:flex;align-items:center;justify-content:center;gap:8px;
  box-shadow:0 4px 14px rgba(16,185,129,0.4);
  transition:all .2s;
}
.counter-btn:active{transform:scale(0.97)}
.counter-btn:disabled{opacity:0.5;box-shadow:none}
.counter-btn svg{width:18px;height:18px;stroke:currentColor;fill:none;stroke-width:3;stroke-linecap:round;stroke-linejoin:round}
.counter-display{
  min-width:70px;padding:14px 16px;border-radius:12px;
  background:var(--bg-elev);border:1px solid var(--border);
  text-align:center;font-size:18px;font-weight:800;
  color:var(--primary);font-variant-numeric:tabular-nums;
  flex-shrink:0;
}
.reset-mini{
  width:44px;height:44px;border-radius:12px;
  background:rgba(239,68,68,0.1);color:#fca5a5;
  display:grid;place-items:center;flex-shrink:0;
  border:1px solid rgba(239,68,68,0.2);
}
.reset-mini:active{transform:scale(0.95)}
.reset-mini svg{width:18px;height:18px;stroke:currentColor;fill:none;stroke-width:2.5}

/* SETTINGS */
.settings-group{background:var(--bg-card);border:1px solid var(--border);border-radius:16px;margin-bottom:14px;overflow:hidden}
.setting-row{display:flex;align-items:center;justify-content:space-between;padding:16px;gap:12px;border-bottom:1px solid var(--border)}
.setting-row:last-child{border-bottom:none}
.setting-info{flex:1;display:flex;align-items:center;gap:12px}
.setting-info svg{width:20px;height:20px;stroke:var(--primary);fill:none;stroke-width:2;flex-shrink:0}
.setting-label{font-size:14px;font-weight:600}
.setting-sub{font-size:11px;color:var(--text-subtle);margin-top:2px}
.font-controls{display:flex;gap:4px;background:var(--bg-elev);border-radius:12px;padding:4px;border:1px solid var(--border)}
.font-btn{width:36px;height:30px;border-radius:8px;display:grid;place-items:center;font-weight:700;color:var(--text-muted);font-family:inherit;transition:all .2s}
.font-btn.active{background:var(--grad);color:#fff}
.font-btn[data-size="small"]{font-size:12px}
.font-btn[data-size="medium"]{font-size:14px}
.font-btn[data-size="large"]{font-size:16px}

/* BOTTOM NAV */
.bottom-nav{
  position:fixed;bottom:0;left:0;right:0;height:var(--nav-h);
  background:rgba(13,51,40,0.95);backdrop-filter:blur(20px);
  border-top:1px solid var(--border);
  display:grid;grid-template-columns:repeat(3,1fr);z-index:50;padding-bottom:env(safe-area-inset-bottom);
}
[data-theme="light"] .bottom-nav{background:rgba(255,255,255,0.95)}
.nav-item{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:3px;color:var(--text-subtle);font-size:10px;font-weight:600;padding:8px}
.nav-item svg{width:22px;height:22px;stroke:currentColor;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.nav-item.active{color:var(--primary)}

/* EMPTY */
.empty{text-align:center;padding:60px 20px;color:var(--text-subtle)}
.empty svg{width:64px;height:64px;stroke:var(--border-hover);fill:none;stroke-width:1.5;margin:0 auto 16px}
.empty h3{font-size:16px;color:var(--text-muted);margin-bottom:6px;font-weight:600}
.empty p{font-size:13px}

/* TOAST */
.toast{position:fixed;bottom:80px;left:50%;transform:translateX(-50%) translateY(20px);background:var(--bg-elev);color:var(--text);padding:12px 22px;border-radius:14px;font-size:13px;font-weight:600;box-shadow:var(--shadow-glow);border:1px solid var(--border-hover);opacity:0;transition:all .3s;pointer-events:none;z-index:200}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}

/* COMPLETED BANNER */
.complete-banner{
  background:linear-gradient(135deg,#10b981,#059669);color:#fff;
  border-radius:16px;padding:20px;text-align:center;margin-bottom:16px;
  box-shadow:0 8px 30px rgba(16,185,129,0.4);
  display:none;
}
.complete-banner.show{display:block;animation:fadeIn .3s}
.complete-banner h3{font-size:18px;font-weight:800;margin-bottom:4px}
.complete-banner p{font-size:13px;opacity:0.9}
</style>
</head>
<body data-theme="dark">

<header class="header">
  <div class="header-title">
    <div class="logo">🌅</div>
    <span id="headerTitle">Adhkar</span>
  </div>
  <button class="icon-btn" onclick="toggleTheme()"><svg viewBox="0 0 24 24" id="themeIcon"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg></button>
</header>

<main class="main" id="mainArea">

  <!-- ADHKAR VIEW -->
  <div class="view active" id="view-adhkar">
    <div class="tabs">
      <button class="tab active" id="tabMorning" onclick="switchTab('morning')">🌅 Morning</button>
      <button class="tab" id="tabEvening" onclick="switchTab('evening')">🌆 Evening</button>
    </div>

    <div class="progress-wrap">
      <div class="progress-head">
        <span class="progress-title" id="progressTitle">Morning Progress</span>
        <span class="progress-count" id="progressCount">0 / 0</span>
      </div>
      <div class="progress-bar"><div class="progress-fill" id="progressFill" style="width:0%"></div></div>
    </div>

    <div class="complete-banner" id="completeBanner">
      <h3>✨ MashaAllah!</h3>
      <p>You completed all adhkar for this session</p>
    </div>

    <div id="adhkarList"></div>
  </div>

  <!-- STATS VIEW -->
  <div class="view" id="view-stats">
    <h2 style="font-size:20px;font-weight:700;margin-bottom:16px">Your Progress</h2>

    <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:20px">
      <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:16px;padding:18px">
        <div style="font-size:28px;font-weight:800;background:var(--grad);-webkit-background-clip:text;-webkit-text-fill-color:transparent;line-height:1;margin-bottom:6px" id="statToday">0</div>
        <div style="font-size:11px;color:var(--text-subtle);text-transform:uppercase;letter-spacing:.5px;font-weight:700">Today</div>
      </div>
      <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:16px;padding:18px">
        <div style="font-size:28px;font-weight:800;background:var(--gold-grad);-webkit-background-clip:text;-webkit-text-fill-color:transparent;line-height:1;margin-bottom:6px" id="statTotal">0</div>
        <div style="font-size:11px;color:var(--text-subtle);text-transform:uppercase;letter-spacing:.5px;font-weight:700">Total Count</div>
      </div>
      <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:16px;padding:18px">
        <div style="font-size:28px;font-weight:800;background:var(--grad);-webkit-background-clip:text;-webkit-text-fill-color:transparent;line-height:1;margin-bottom:6px" id="statStreak">0</div>
        <div style="font-size:11px;color:var(--text-subtle);text-transform:uppercase;letter-spacing:.5px;font-weight:700">Day Streak</div>
      </div>
      <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:16px;padding:18px">
        <div style="font-size:28px;font-weight:800;background:var(--gold-grad);-webkit-background-clip:text;-webkit-text-fill-color:transparent;line-height:1;margin-bottom:6px" id="statSessions">0</div>
        <div style="font-size:11px;color:var(--text-subtle);text-transform:uppercase;letter-spacing:.5px;font-weight:700">Sessions</div>
      </div>
    </div>

    <button class="tab" style="width:100%;padding:14px;background:rgba(239,68,68,0.1);color:#fca5a5;border:1px solid rgba(239,68,68,0.2);border-radius:12px;font-weight:700" onclick="resetAll()">
      Reset All Progress
    </button>
  </div>

  <!-- SETTINGS VIEW -->
  <div class="view" id="view-settings">
    <h2 style="font-size:20px;font-weight:700;margin-bottom:16px">Settings</h2>

    <div class="settings-group">
      <div class="setting-row">
        <div class="setting-info">
          <svg viewBox="0 0 24 24"><path d="M4 7V4h16v3M9 20h6M12 4v16"/></svg>
          <div><div class="setting-label">Arabic Font Size</div><div class="setting-sub">Adjust text size</div></div>
        </div>
        <div class="font-controls">
          <button class="font-btn" data-size="small" onclick="setFontSize('small')">A</button>
          <button class="font-btn active" data-size="medium" onclick="setFontSize('medium')">A</button>
          <button class="font-btn" data-size="large" onclick="setFontSize('large')">A</button>
        </div>
      </div>
    </div>

    <div style="text-align:center;padding:20px 0;font-size:12px;color:var(--text-subtle);line-height:1.8">
      Morning & Evening Adhkar<br>
      From Quran & Authentic Sunnah<br><br>
      Made with ❤️ for the Ummah<br>
      <strong style="color:var(--primary)">APKForge</strong> · v1.0.0
    </div>
  </div>

</main>

<nav class="bottom-nav">
  <button class="nav-item active" data-view="adhkar" onclick="switchView('adhkar')">
    <svg viewBox="0 0 24 24"><path d="M12 2v2M12 20v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/><circle cx="12" cy="12" r="4"/></svg>
    <span>Adhkar</span>
  </button>
  <button class="nav-item" data-view="stats" onclick="switchView('stats')">
    <svg viewBox="0 0 24 24"><path d="M3 3v18h18"/><path d="M18 9l-5 5-3-3-4 4"/></svg>
    <span>Progress</span>
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

with open('templates/adhkar.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Chunk 1 saved:', len(content), 'bytes')
