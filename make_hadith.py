content = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no,viewport-fit=cover">
<meta name="theme-color" content="#042f2e">
<title>Hadith Collection</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Noto+Naskh+Arabic:wght@400;600;700&display=swap" rel="stylesheet">
<style>
:root{
  --bg:#031e1e;--bg-card:#0a3434;--bg-elev:#0f4848;--bg-input:#052828;
  --text:#f0fdfa;--text-muted:#7dd3c8;--text-subtle:#3d8a82;
  --primary:#14b8a6;--primary-dark:#0d9488;--accent:#0ea5e9;--gold:#fbbf24;
  --primary-grad:linear-gradient(135deg,#14b8a6,#0ea5e9);
  --border:rgba(20,184,166,0.2);--border-hover:rgba(20,184,166,0.5);
  --shadow:0 4px 24px rgba(0,0,0,0.5);
  --shadow-glow:0 0 30px rgba(20,184,166,0.3);
  --nav-h:64px;--header-h:60px;
  --font-arabic:24px;
}
[data-theme="light"]{
  --bg:#f0fdfa;--bg-card:#ffffff;--bg-elev:#ccfbf1;--bg-input:#ffffff;
  --text:#042f2e;--text-muted:#0f766e;--text-subtle:#5eead4;
  --border:rgba(15,118,110,0.2);--border-hover:rgba(15,118,110,0.4);
  --shadow:0 4px 24px rgba(4,47,46,0.1);
}
*{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}
html,body{height:100%;overflow:hidden}
body{
  font-family:'Inter',system-ui,sans-serif;
  background:var(--bg);color:var(--text);
  transition:background .3s,color .3s;
  overscroll-behavior:none;-webkit-font-smoothing:antialiased;
  background-image:radial-gradient(circle at 20% 10%,rgba(20,184,166,0.1),transparent 40%),radial-gradient(circle at 80% 90%,rgba(14,165,233,0.08),transparent 40%);
}
button{font-family:inherit;cursor:pointer;border:none;background:none;color:inherit}

.header{
  position:fixed;top:0;left:0;right:0;height:var(--header-h);
  background:rgba(3,30,30,0.9);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);
  border-bottom:1px solid var(--border);
  display:flex;align-items:center;padding:0 16px;gap:12px;z-index:50;
}
[data-theme="light"] .header{background:rgba(240,253,250,0.95)}
.header-title{flex:1;font-size:17px;font-weight:700;display:flex;align-items:center;gap:10px}
.logo{width:34px;height:34px;border-radius:10px;background:var(--primary-grad);display:grid;place-items:center;font-size:18px;box-shadow:0 4px 14px rgba(20,184,166,0.5)}
.icon-btn{width:40px;height:40px;border-radius:12px;display:grid;place-items:center;color:var(--text-muted);transition:all .2s}
.icon-btn:active{background:var(--bg-card);color:var(--primary)}
.icon-btn svg{width:20px;height:20px;stroke:currentColor;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}

.main{position:fixed;top:var(--header-h);bottom:var(--nav-h);left:0;right:0;overflow-y:auto;-webkit-overflow-scrolling:touch}
.main::-webkit-scrollbar{width:0}
.view{display:none;padding:16px;min-height:100%}
.view.active{display:block;animation:fadeIn .25s ease}
@keyframes fadeIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}

.search-wrap{padding:0 0 12px}
.search-box{display:flex;align-items:center;gap:10px;background:var(--bg-card);border:1px solid var(--border);border-radius:14px;padding:12px 16px;transition:all .2s}
.search-box:focus-within{border-color:var(--primary);box-shadow:0 0 0 3px rgba(20,184,166,0.15)}
.search-box svg{width:18px;height:18px;stroke:var(--text-subtle);fill:none;stroke-width:2}
.search-box input{flex:1;background:none;border:none;outline:none;color:var(--text);font-size:14px;font-family:inherit}
.search-box input::placeholder{color:var(--text-subtle)}

.cats{display:flex;gap:8px;padding:0 0 14px;overflow-x:auto;scrollbar-width:none}
.cats::-webkit-scrollbar{display:none}
.chip{flex-shrink:0;padding:8px 16px;border-radius:20px;background:var(--bg-card);border:1px solid var(--border);color:var(--text-muted);font-size:13px;font-weight:600;white-space:nowrap;transition:all .2s;font-family:inherit}
.chip.active{background:var(--primary-grad);color:#031e1e;border-color:transparent;box-shadow:0 4px 12px rgba(20,184,166,0.4)}
.chip:active{transform:scale(0.95)}

.hadith-card{
  background:var(--bg-card);border:1px solid var(--border);border-radius:16px;
  padding:18px;margin-bottom:12px;cursor:pointer;transition:all .2s;position:relative;overflow:hidden;
}
.hadith-card::before{
  content:'';position:absolute;top:0;right:0;width:60px;height:60px;
  background:var(--primary-grad);opacity:0.06;border-radius:0 0 0 60px;
}
.hadith-card:active{transform:scale(0.98);border-color:var(--border-hover)}
.hadith-head{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-bottom:12px}
.hadith-cat{
  font-size:10px;padding:4px 10px;border-radius:8px;
  background:rgba(20,184,166,0.15);color:#5eead4;
  font-weight:700;letter-spacing:.5px;text-transform:uppercase;
}
.fav-btn{width:32px;height:32px;border-radius:50%;display:grid;place-items:center;flex-shrink:0;color:var(--text-subtle);transition:all .2s}
.fav-btn.active{color:var(--gold)}
.fav-btn svg{width:18px;height:18px;stroke:currentColor;fill:none;stroke-width:2}
.fav-btn.active svg{fill:var(--gold);stroke:var(--gold)}

.hadith-arabic{
  font-family:'Noto Naskh Arabic',serif;font-size:var(--font-arabic);
  line-height:1.9;color:var(--text);direction:rtl;text-align:right;
  margin-bottom:14px;font-weight:400;
}
.hadith-english{
  font-size:14px;color:var(--text-muted);line-height:1.7;
  padding-top:12px;border-top:1px solid var(--border);
}
.hadith-ref{
  font-size:11px;color:var(--text-subtle);font-style:italic;
  margin-top:10px;display:flex;align-items:center;gap:6px;
}
.hadith-ref::before{content:'📚';font-size:12px}

/* DETAIL MODAL */
.modal{position:fixed;inset:0;background:rgba(0,0,0,0.85);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);z-index:100;display:none;align-items:flex-end}
.modal.show{display:flex;animation:fadeIn .25s ease}
.modal-sheet{
  background:var(--bg-card);width:100%;max-height:90vh;overflow-y:auto;
  border-radius:24px 24px 0 0;padding:20px;
  padding-bottom:calc(20px + env(safe-area-inset-bottom));
  border-top:1px solid var(--border-hover);
  transform:translateY(100%);transition:transform .3s cubic-bezier(0.32,0.72,0,1);
}
.modal.show .modal-sheet{transform:translateY(0)}
.modal-sheet::-webkit-scrollbar{width:0}
.drag{width:40px;height:4px;background:var(--border-hover);border-radius:2px;margin:0 auto 16px}
.modal-close{position:absolute;top:16px;right:16px;width:32px;height:32px;border-radius:50%;background:var(--bg-elev);display:grid;place-items:center;color:var(--text-muted)}
.modal-cat{text-align:center;font-size:11px;padding:5px 12px;border-radius:10px;background:rgba(20,184,166,0.15);color:#5eead4;font-weight:700;letter-spacing:1px;text-transform:uppercase;display:inline-block;margin-bottom:16px}
.modal-arabic{
  font-family:'Noto Naskh Arabic',serif;font-size:28px;line-height:2;
  text-align:right;direction:rtl;color:var(--text);
  margin-bottom:20px;padding:20px;background:var(--bg-elev);border-radius:16px;
  border-right:4px solid var(--primary);
}
.modal-section{margin-bottom:16px}
.modal-label{font-size:11px;text-transform:uppercase;letter-spacing:1.5px;color:var(--primary);font-weight:700;margin-bottom:8px}
.modal-text{font-size:15px;color:var(--text-muted);line-height:1.8}
.modal-ref{font-size:12px;color:var(--text-subtle);font-style:italic;padding-top:14px;border-top:1px solid var(--border);text-align:center}
.modal-actions{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:20px}
.modal-btn{padding:14px;border-radius:12px;background:var(--bg-elev);color:var(--text);font-size:14px;font-weight:600;display:flex;align-items:center;justify-content:center;gap:8px;font-family:inherit;border:1px solid var(--border)}
.modal-btn:active{transform:scale(0.97)}
.modal-btn.primary{background:var(--primary-grad);color:#031e1e;border-color:transparent;font-weight:700}
.modal-btn.active-fav{background:rgba(251,191,36,0.2);color:var(--gold);border-color:rgba(251,191,36,0.4)}
.modal-btn svg{width:16px;height:16px;stroke:currentColor;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}

.bottom-nav{
  position:fixed;bottom:0;left:0;right:0;height:var(--nav-h);
  background:rgba(10,52,52,0.95);backdrop-filter:blur(20px);
  border-top:1px solid var(--border);
  display:grid;grid-template-columns:repeat(3,1fr);z-index:50;padding-bottom:env(safe-area-inset-bottom);
}
[data-theme="light"] .bottom-nav{background:rgba(255,255,255,0.95)}
.nav-item{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:3px;color:var(--text-subtle);font-size:10px;font-weight:600;padding:8px}
.nav-item svg{width:22px;height:22px;stroke:currentColor;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.nav-item.active{color:var(--primary)}

.settings-group{background:var(--bg-card);border:1px solid var(--border);border-radius:16px;margin-bottom:14px;overflow:hidden}
.setting-row{display:flex;align-items:center;justify-content:space-between;padding:16px;gap:12px;border-bottom:1px solid var(--border)}
.setting-row:last-child{border-bottom:none}
.setting-info{flex:1;display:flex;align-items:center;gap:12px}
.setting-info svg{width:20px;height:20px;stroke:var(--primary);fill:none;stroke-width:2;flex-shrink:0}
.setting-label{font-size:14px;font-weight:600}
.setting-sub{font-size:11px;color:var(--text-subtle);margin-top:2px}
.font-controls{display:flex;gap:4px;background:var(--bg-elev);border-radius:12px;padding:4px;border:1px solid var(--border)}
.font-btn{width:36px;height:30px;border-radius:8px;display:grid;place-items:center;font-weight:700;color:var(--text-muted);font-family:inherit;transition:all .2s}
.font-btn.active{background:var(--primary-grad);color:#031e1e}
.font-btn[data-size="small"]{font-size:12px}
.font-btn[data-size="medium"]{font-size:14px}
.font-btn[data-size="large"]{font-size:16px}

.empty{text-align:center;padding:60px 20px;color:var(--text-subtle)}
.empty svg{width:64px;height:64px;stroke:var(--border-hover);fill:none;stroke-width:1.5;margin:0 auto 16px}
.empty h3{font-size:16px;color:var(--text-muted);margin-bottom:6px;font-weight:600}

.toast{position:fixed;bottom:80px;left:50%;transform:translateX(-50%) translateY(20px);background:var(--bg-elev);color:var(--text);padding:12px 22px;border-radius:14px;font-size:13px;font-weight:600;box-shadow:var(--shadow-glow);border:1px solid var(--border-hover);opacity:0;transition:all .3s;pointer-events:none;z-index:200}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
</style>
</head>
<body data-theme="dark">

<header class="header">
  <div class="header-title">
    <div class="logo">📚</div>
    <span id="headerTitle">Hadith Collection</span>
  </div>
  <button class="icon-btn" onclick="toggleTheme()"><svg viewBox="0 0 24 24" id="themeIcon"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg></button>
</header>

<main class="main" id="mainArea">

  <div class="view active" id="view-all">
    <div class="search-wrap">
      <div class="search-box">
        <svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg>
        <input type="text" id="searchInput" placeholder="Search hadith..." oninput="handleSearch(this.value)">
      </div>
    </div>
    <div class="cats" id="catChips"></div>
    <div id="hadithList"></div>
  </div>

  <div class="view" id="view-fav">
    <h2 style="font-size:20px;font-weight:700;margin-bottom:16px">Favorites</h2>
    <div id="favList"></div>
  </div>

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

    <div style="text-align:center;padding:30px 0;font-size:12px;color:var(--text-subtle);line-height:1.8">
      40 Authentic Hadith<br>
      From Sahih Bukhari, Muslim, Tirmidhi, Abu Dawud<br><br>
      Made with ❤️ for the Ummah<br>
      <strong style="color:var(--primary)">APKForge</strong> · v1.0.0
    </div>
  </div>

</main>

<nav class="bottom-nav">
  <button class="nav-item active" data-view="all" onclick="switchView('all')">
    <svg viewBox="0 0 24 24"><path d="M4 6h16M4 12h16M4 18h16"/></svg>
    <span>All</span>
  </button>
  <button class="nav-item" data-view="fav" onclick="switchView('fav')">
    <svg viewBox="0 0 24 24"><path d="M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 000-7.78z"/></svg>
    <span>Favorites</span>
  </button>
  <button class="nav-item" data-view="settings" onclick="switchView('settings')">
    <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 00.33 1.82l.06.06a2 2 0 11-2.83 2.83l-.06-.06a1.65 1.65 0 00-1.82-.33 1.65 1.65 0 00-1 1.51V21a2 2 0 11-4 0v-.09a1.65 1.65 0 00-1.08-1.51 1.65 1.65 0 00-1.82.33l-.06.06a2 2 0 11-2.83-2.83l.06-.06a1.65 1.65 0 00.33-1.82 1.65 1.65 0 00-1.51-1H3a2 2 0 110-4h.09A1.65 1.65 0 004.6 9a1.65 1.65 0 00-.33-1.82l-.06-.06a2 2 0 112.83-2.83l.06.06a1.65 1.65 0 001.82.33H9a1.65 1.65 0 001-1.51V3a2 2 0 114 0v.09a1.65 1.65 0 001 1.51 1.65 1.65 0 001.82-.33l.06-.06a2 2 0 112.83 2.83l-.06.06a1.65 1.65 0 00-.33 1.82V9a1.65 1.65 0 001.51 1H21a2 2 0 110 4h-.09a1.65 1.65 0 00-1.51 1z"/></svg>
    <span>Settings</span>
  </button>
</nav>

<div class="modal" id="detailModal" onclick="closeModal(event)">
  <div class="modal-sheet" onclick="event.stopPropagation()">
    <div class="drag"></div>
    <div style="text-align:center;margin-bottom:16px"><span class="modal-cat" id="modalCat"></span></div>
    <div class="modal-arabic" id="modalArabic"></div>
    <div class="modal-section">
      <div class="modal-label">Translation</div>
      <div class="modal-text" id="modalEnglish"></div>
    </div>
    <div class="modal-ref" id="modalRef"></div>
    <div class="modal-actions">
      <button class="modal-btn" id="modalFavBtn" onclick="toggleFavFromModal()">
        <svg viewBox="0 0 24 24"><path d="M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 000-7.78z"/></svg>
        <span id="modalFavText">Favorite</span>
      </button>
      <button class="modal-btn primary" onclick="copyCurrent()">
        <svg viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 01-2-2V4a2 2 0 012-2h9a2 2 0 012 2v1"/></svg>
        Copy
      </button>
    </div>
  </div>
</div>

<div class="toast" id="toast"><span id="toastText">Saved</span></div>

<script>
/* PART 2 WILL BE INJECTED */
</script>
</body>
</html>
'''

with open('templates/hadith.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Chunk 1 saved:', len(content), 'bytes')
