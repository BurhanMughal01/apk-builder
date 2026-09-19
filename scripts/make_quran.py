content = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no,viewport-fit=cover">
<meta name="theme-color" content="#1a0f05">
<title>Al-Quran</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Noto+Naskh+Arabic:wght@400;600;700&family=Amiri:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{
  --bg:#1a0f05;--bg-card:#2a1a0a;--bg-elev:#3a2610;--bg-input:#1f1206;
  --text:#fef3c7;--text-muted:#c9a961;--text-subtle:#8b6f3f;
  --primary:#d97706;--primary-dark:#b45309;--accent:#fbbf24;--green:#10b981;
  --gold-grad:linear-gradient(135deg,#fbbf24,#d97706);
  --border:rgba(217,119,6,0.25);--border-hover:rgba(251,191,36,0.5);
  --shadow:0 4px 24px rgba(0,0,0,0.5);
  --shadow-gold:0 0 30px rgba(251,191,36,0.3);
  --nav-h:64px;--header-h:60px;
  --font-quran:28px;
}
[data-theme="light"]{
  --bg:#fefce8;--bg-card:#ffffff;--bg-elev:#fef3c7;--bg-input:#ffffff;
  --text:#1a0f05;--text-muted:#78520a;--text-subtle:#b45309;
  --border:rgba(217,119,6,0.2);--border-hover:rgba(217,119,6,0.4);
  --shadow:0 4px 24px rgba(120,82,10,0.1);
}
*{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}
html,body{height:100%;overflow:hidden}
body{
  font-family:'Inter',system-ui,sans-serif;
  background:var(--bg);color:var(--text);
  transition:background .3s,color .3s;
  overscroll-behavior:none;-webkit-font-smoothing:antialiased;
  background-image:radial-gradient(circle at 20% 10%,rgba(217,119,6,0.08),transparent 40%),radial-gradient(circle at 80% 90%,rgba(251,191,36,0.06),transparent 40%);
}
button{font-family:inherit;cursor:pointer;border:none;background:none;color:inherit}

.header{
  position:fixed;top:0;left:0;right:0;height:var(--header-h);
  background:rgba(26,15,5,0.9);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);
  border-bottom:1px solid var(--border);
  display:flex;align-items:center;padding:0 16px;gap:12px;z-index:50;
}
[data-theme="light"] .header{background:rgba(254,252,232,0.95)}
.header-title{flex:1;font-size:17px;font-weight:700;display:flex;align-items:center;gap:10px}
.logo{width:34px;height:34px;border-radius:10px;background:var(--gold-grad);display:grid;place-items:center;font-size:18px;box-shadow:0 4px 14px rgba(217,119,6,0.5)}
.icon-btn{width:40px;height:40px;border-radius:12px;display:grid;place-items:center;color:var(--text-muted);transition:all .2s}
.icon-btn:active{background:var(--bg-card);color:var(--accent)}
.icon-btn svg{width:20px;height:20px;stroke:currentColor;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}

.main{position:fixed;top:var(--header-h);bottom:var(--nav-h);left:0;right:0;overflow-y:auto;-webkit-overflow-scrolling:touch}
.main::-webkit-scrollbar{width:0}
.view{display:none;padding:16px;min-height:100%}
.view.active{display:block;animation:fadeIn .25s ease}
@keyframes fadeIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}

/* SEARCH */
.search-wrap{padding:0 0 12px}
.search-box{display:flex;align-items:center;gap:10px;background:var(--bg-card);border:1px solid var(--border);border-radius:14px;padding:12px 16px;transition:all .2s}
.search-box:focus-within{border-color:var(--accent);box-shadow:0 0 0 3px rgba(217,119,6,0.15)}
.search-box svg{width:18px;height:18px;stroke:var(--text-subtle);fill:none;stroke-width:2}
.search-box input{flex:1;background:none;border:none;outline:none;color:var(--text);font-size:14px;font-family:inherit}
.search-box input::placeholder{color:var(--text-subtle)}

/* CATEGORIES */
.cats{display:flex;gap:8px;padding:0 0 14px;overflow-x:auto;scrollbar-width:none}
.cats::-webkit-scrollbar{display:none}
.chip{flex-shrink:0;padding:8px 16px;border-radius:20px;background:var(--bg-card);border:1px solid var(--border);color:var(--text-muted);font-size:13px;font-weight:600;white-space:nowrap;transition:all .2s;font-family:inherit}
.chip.active{background:var(--gold-grad);color:#1a0f05;border-color:transparent;box-shadow:0 4px 12px rgba(217,119,6,0.4)}
.chip:active{transform:scale(0.95)}

/* SURAH CARD */
.surah-card{
  background:var(--bg-card);border:1px solid var(--border);border-radius:16px;
  padding:14px;margin-bottom:10px;display:flex;align-items:center;gap:14px;
  cursor:pointer;transition:all .2s;position:relative;overflow:hidden;
}
.surah-card::before{
  content:'';position:absolute;top:0;right:0;width:60px;height:60px;
  background:var(--gold-grad);opacity:0.05;border-radius:0 0 0 60px;
}
.surah-card:active{transform:scale(0.98);border-color:var(--border-hover)}
.surah-num{
  width:44px;height:44px;flex-shrink:0;
  background:var(--bg-elev);border:1px solid var(--border);
  border-radius:12px;display:grid;place-items:center;
  font-weight:800;color:var(--accent);font-size:15px;
  font-family:'Amiri',serif;
}
.surah-info{flex:1;min-width:0}
.surah-name{font-size:15px;font-weight:700;color:var(--text);margin-bottom:2px;display:flex;align-items:center;gap:8px}
.surah-name .type{font-size:9px;padding:2px 6px;border-radius:4px;background:rgba(217,119,6,0.15);color:var(--accent);font-weight:700;letter-spacing:.5px}
.surah-meta{font-size:11px;color:var(--text-subtle)}
.surah-arabic{font-family:'Amiri',serif;font-size:22px;color:var(--accent);direction:rtl;flex-shrink:0}

/* SURAH READING VIEW */
.reader-header{
  background:linear-gradient(135deg,var(--bg-card),var(--bg-elev));
  border:1px solid var(--border);border-radius:20px;padding:24px;
  text-align:center;margin-bottom:20px;box-shadow:var(--shadow-gold);
}
.reader-header .arabic-title{font-family:'Amiri',serif;font-size:36px;color:var(--accent);margin-bottom:8px;line-height:1.3}
.reader-header .eng-title{font-size:18px;font-weight:700;color:var(--text);margin-bottom:4px}
.reader-header .subtitle{font-size:12px;color:var(--text-subtle);margin-bottom:16px}
.reader-actions{display:flex;gap:8px;justify-content:center;flex-wrap:wrap}
.reader-actions button{padding:8px 14px;background:var(--bg);border:1px solid var(--border);border-radius:20px;color:var(--text-muted);font-size:12px;font-weight:600;display:flex;align-items:center;gap:6px;font-family:inherit}
.reader-actions button:active{transform:scale(0.95);border-color:var(--accent);color:var(--accent)}
.reader-actions button.playing{background:var(--gold-grad);color:#1a0f05;border-color:transparent}
.reader-actions svg{width:14px;height:14px;stroke:currentColor;fill:none;stroke-width:2.5}

.bismillah{font-family:'Amiri',serif;font-size:26px;color:var(--accent);text-align:center;padding:20px 0;direction:rtl;text-shadow:0 0 20px rgba(251,191,36,0.3)}

.ayah-card{
  background:var(--bg-card);border:1px solid var(--border);border-radius:16px;
  padding:20px;margin-bottom:12px;transition:all .2s;
}
.ayah-card:active{transform:scale(0.99);border-color:var(--border-hover)}
.ayah-head{display:flex;align-items:center;justify-content:space-between;margin-bottom:12px;gap:10px}
.ayah-num-badge{
  width:32px;height:32px;border-radius:50%;
  background:var(--gold-grad);color:#1a0f05;
  display:grid;place-items:center;font-size:12px;font-weight:800;flex-shrink:0;
  font-family:'Amiri',serif;
}
.ayah-actions{display:flex;gap:6px}
.ayah-mini-btn{width:30px;height:30px;border-radius:8px;background:var(--bg-elev);color:var(--text-subtle);display:grid;place-items:center;border:1px solid var(--border)}
.ayah-mini-btn:active{color:var(--accent);border-color:var(--border-hover)}
.ayah-mini-btn svg{width:14px;height:14px;stroke:currentColor;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.ayah-mini-btn.active svg{fill:var(--accent);stroke:var(--accent)}

.ayah-arabic{
  font-family:'Amiri',serif;font-size:var(--font-quran);
  line-height:2;color:var(--text);text-align:right;direction:rtl;
  margin-bottom:12px;font-weight:400;
}
.ayah-trans{
  font-size:14px;color:var(--text-muted);line-height:1.7;
  padding-top:12px;border-top:1px solid var(--border);
}

/* LOADING */
.loading{text-align:center;padding:60px 20px;color:var(--text-subtle)}
.spinner{
  width:40px;height:40px;border:3px solid var(--border);
  border-top-color:var(--accent);border-radius:50%;
  animation:spin 1s linear infinite;margin:0 auto 16px;
}
@keyframes spin{to{transform:rotate(360deg)}}
.loading p{font-size:13px}

/* EMPTY */
.empty{text-align:center;padding:60px 20px;color:var(--text-subtle)}
.empty svg{width:64px;height:64px;stroke:var(--border-hover);fill:none;stroke-width:1.5;margin:0 auto 16px}
.empty h3{font-size:16px;color:var(--text-muted);margin-bottom:6px;font-weight:600}
.empty p{font-size:13px}

/* ERROR */
.error-box{background:rgba(239,68,68,0.1);border:1px solid rgba(239,68,68,0.3);border-radius:14px;padding:20px;text-align:center;margin:20px 0}
.error-box p{color:#fca5a5;font-size:14px;margin-bottom:14px}
.error-box button{padding:10px 20px;background:var(--gold-grad);color:#1a0f05;border-radius:10px;font-size:13px;font-weight:700;font-family:inherit}

/* BOTTOM NAV */
.bottom-nav{
  position:fixed;bottom:0;left:0;right:0;height:var(--nav-h);
  background:rgba(42,26,10,0.95);backdrop-filter:blur(20px);
  border-top:1px solid var(--border);
  display:grid;grid-template-columns:repeat(3,1fr);z-index:50;padding-bottom:env(safe-area-inset-bottom);
}
[data-theme="light"] .bottom-nav{background:rgba(255,255,255,0.95)}
.nav-item{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:3px;color:var(--text-subtle);font-size:10px;font-weight:600;padding:8px}
.nav-item svg{width:22px;height:22px;stroke:currentColor;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.nav-item.active{color:var(--accent)}

/* SETTINGS */
.settings-group{background:var(--bg-card);border:1px solid var(--border);border-radius:16px;margin-bottom:14px;overflow:hidden}
.setting-row{display:flex;align-items:center;justify-content:space-between;padding:16px;gap:12px;border-bottom:1px solid var(--border)}
.setting-row:last-child{border-bottom:none}
.setting-info{flex:1;display:flex;align-items:center;gap:12px}
.setting-info svg{width:20px;height:20px;stroke:var(--primary);fill:none;stroke-width:2;flex-shrink:0}
.setting-label{font-size:14px;font-weight:600}
.setting-sub{font-size:11px;color:var(--text-subtle);margin-top:2px}
.toggle{width:52px;height:30px;border-radius:15px;background:var(--bg-elev);position:relative;transition:background .3s;flex-shrink:0;border:1px solid var(--border)}
.toggle::after{content:'';position:absolute;top:3px;left:3px;width:22px;height:22px;border-radius:50%;background:var(--text-subtle);transition:all .3s}
.toggle.on{background:var(--gold-grad);border-color:transparent}
.toggle.on::after{transform:translateX(22px);background:#1a0f05}
.font-controls{display:flex;gap:4px;background:var(--bg-elev);border-radius:12px;padding:4px;border:1px solid var(--border)}
.font-btn{width:36px;height:30px;border-radius:8px;display:grid;place-items:center;font-weight:700;color:var(--text-muted);font-family:inherit;transition:all .2s}
.font-btn.active{background:var(--gold-grad);color:#1a0f05}
.font-btn[data-size="small"]{font-size:12px}
.font-btn[data-size="medium"]{font-size:14px}
.font-btn[data-size="large"]{font-size:16px}

/* TOAST */
.toast{position:fixed;bottom:80px;left:50%;transform:translateX(-50%) translateY(20px);background:var(--bg-elev);color:var(--text);padding:12px 22px;border-radius:14px;font-size:13px;font-weight:600;box-shadow:var(--shadow-gold);border:1px solid var(--border-hover);opacity:0;transition:all .3s;pointer-events:none;z-index:200;display:flex;align-items:center;gap:8px}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}

/* BACK BUTTON */
.back-btn{position:absolute;left:16px;top:50%;transform:translateY(-50%);width:36px;height:36px;border-radius:10px;display:grid;place-items:center;color:var(--text-muted)}
.back-btn:active{background:var(--bg-card)}
.back-btn svg{width:20px;height:20px;stroke:currentColor;fill:none;stroke-width:2.5;stroke-linecap:round;stroke-linejoin:round}
</style>
</head>
<body data-theme="dark">

<header class="header">
  <button class="back-btn" id="backBtn" style="display:none" onclick="backToList()">
    <svg viewBox="0 0 24 24"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
  </button>
  <div class="header-title" id="headerTitleWrap">
    <div class="logo">📖</div>
    <span id="headerTitle">Al-Quran</span>
  </div>
  <button class="icon-btn" onclick="toggleTheme()"><svg viewBox="0 0 24 24" id="themeIcon"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg></button>
</header>

<main class="main" id="mainArea">

  <!-- SURAH LIST VIEW -->
  <div class="view active" id="view-list">
    <div class="search-wrap">
      <div class="search-box">
        <svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg>
        <input type="text" id="searchInput" placeholder="Search surah by name or number..." oninput="handleSearch(this.value)">
      </div>
    </div>

    <div class="cats" id="catChips"></div>
    <div id="surahList"></div>
  </div>

  <!-- READER VIEW -->
  <div class="view" id="view-reader">
    <div id="readerContent"></div>
  </div>

  <!-- BOOKMARKS VIEW -->
  <div class="view" id="view-bookmarks">
    <h2 style="font-size:20px;font-weight:700;margin-bottom:16px">Bookmarks</h2>
    <div id="bookmarksList"></div>
  </div>

  <!-- SETTINGS VIEW -->
  <div class="view" id="view-settings">
    <h2 style="font-size:20px;font-weight:700;margin-bottom:16px">Settings</h2>

    <div class="settings-group">
      <div class="setting-row">
        <div class="setting-info">
          <svg viewBox="0 0 24 24"><path d="M4 7V4h16v3M9 20h6M12 4v16"/></svg>
          <div><div class="setting-label">Font Size</div><div class="setting-sub">Arabic text</div></div>
        </div>
        <div class="font-controls">
          <button class="font-btn" data-size="small" onclick="setFontSize('small')">A</button>
          <button class="font-btn active" data-size="medium" onclick="setFontSize('medium')">A</button>
          <button class="font-btn" data-size="large" onclick="setFontSize('large')">A</button>
        </div>
      </div>
      <div class="setting-row">
        <div class="setting-info">
          <svg viewBox="0 0 24 24"><path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 01-2 2H5a2 2 0 01-2-2V5a2 2 0 012-2h11"/></svg>
          <div><div class="setting-label">Show Translation</div><div class="setting-sub">English translation</div></div>
        </div>
        <div class="toggle on" id="transToggle" onclick="toggleTranslation()"></div>
      </div>
    </div>

    <div style="text-align:center;padding:30px 0;font-size:12px;color:var(--text-subtle);line-height:1.8">
      Translation: Sahih International<br>
      Audio: Mishary Rashid Alafasy<br><br>
      Made with ❤️ for the Ummah<br>
      <strong style="color:var(--accent)">APKForge</strong> · v1.0.0
    </div>
  </div>

</main>

<nav class="bottom-nav" id="bottomNav">
  <button class="nav-item active" data-view="list" onclick="switchView('list')">
    <svg viewBox="0 0 24 24"><path d="M4 6h16M4 12h16M4 18h16"/></svg>
    <span>Surahs</span>
  </button>
  <button class="nav-item" data-view="bookmarks" onclick="switchView('bookmarks')">
    <svg viewBox="0 0 24 24"><path d="M19 21l-7-5-7 5V5a2 2 0 012-2h10a2 2 0 012 2z"/></svg>
    <span>Bookmarks</span>
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

with open('templates/quran.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Chunk 1 saved:', len(content), 'bytes')
