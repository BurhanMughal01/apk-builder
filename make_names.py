content = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no,viewport-fit=cover">
<meta name="theme-color" content="#0a1a10">
<title>Islamic Names</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Amiri:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{
  --bg:#061a10;--bg-card:#0d3320;--bg-elev:#134a30;--bg-input:#0a2618;
  --text:#d1fae5;--text-muted:#7dd3b0;--text-subtle:#3d8a6b;
  --primary:#22c55e;--primary-dark:#16a34a;--accent:#fbbf24;
  --green-grad:linear-gradient(135deg,#22c55e,#16a34a);
  --gold-grad:linear-gradient(135deg,#fbbf24,#f59e0b);
  --border:rgba(34,197,94,0.2);--border-hover:rgba(34,197,94,0.5);
  --shadow:0 4px 24px rgba(0,0,0,0.5);
  --shadow-glow:0 0 30px rgba(34,197,94,0.3);
  --nav-h:64px;--header-h:60px;
}
[data-theme="light"]{
  --bg:#f0fdf4;--bg-card:#ffffff;--bg-elev:#dcfce7;--bg-input:#ffffff;
  --text:#052e16;--text-muted:#15803d;--text-subtle:#86efac;
  --border:rgba(22,163,74,0.2);--border-hover:rgba(22,163,74,0.4);
  --shadow:0 4px 24px rgba(5,46,22,0.1);
}
*{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}
html,body{height:100%;overflow:hidden}
body{
  font-family:'Inter',system-ui,sans-serif;
  background:var(--bg);color:var(--text);
  transition:background .3s,color .3s;
  overscroll-behavior:none;-webkit-font-smoothing:antialiased;
  background-image:radial-gradient(circle at 20% 10%,rgba(34,197,94,0.08),transparent 40%),radial-gradient(circle at 80% 90%,rgba(251,191,36,0.06),transparent 40%);
}
button{font-family:inherit;cursor:pointer;border:none;background:none;color:inherit}
input{font-family:inherit}

.header{
  position:fixed;top:0;left:0;right:0;height:var(--header-h);
  background:rgba(6,26,16,0.9);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);
  border-bottom:1px solid var(--border);
  display:flex;align-items:center;padding:0 16px;gap:12px;z-index:50;
}
[data-theme="light"] .header{background:rgba(240,253,244,0.95)}
.header-title{flex:1;font-size:17px;font-weight:700;display:flex;align-items:center;gap:10px}
.logo{width:34px;height:34px;border-radius:10px;background:var(--green-grad);display:grid;place-items:center;font-size:18px;box-shadow:0 4px 14px rgba(34,197,94,0.5)}
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
.search-box:focus-within{border-color:var(--primary);box-shadow:0 0 0 3px rgba(34,197,94,0.15)}
.search-box svg{width:18px;height:18px;stroke:var(--text-subtle);fill:none;stroke-width:2}
.search-box input{flex:1;background:none;border:none;outline:none;color:var(--text);font-size:14px}
.search-box input::placeholder{color:var(--text-subtle)}

.cats{display:flex;gap:8px;padding:0 0 14px;overflow-x:auto;scrollbar-width:none}
.cats::-webkit-scrollbar{display:none}
.chip{flex-shrink:0;padding:8px 16px;border-radius:20px;background:var(--bg-card);border:1px solid var(--border);color:var(--text-muted);font-size:13px;font-weight:600;white-space:nowrap;transition:all .2s}
.chip.active{background:var(--green-grad);color:#fff;border-color:transparent;box-shadow:0 4px 12px rgba(34,197,94,0.4)}
.chip:active{transform:scale(0.95)}

.name-card{
  background:var(--bg-card);border:1px solid var(--border);border-radius:16px;
  padding:16px;margin-bottom:10px;display:flex;align-items:center;gap:14px;
  transition:all .2s;position:relative;overflow:hidden;
}
.name-card::before{
  content:'';position:absolute;top:0;right:0;width:60px;height:60px;
  background:var(--green-grad);opacity:0.05;border-radius:0 0 0 60px;
}
.name-card:active{transform:scale(0.98);border-color:var(--border-hover)}
.name-info{flex:1;min-width:0}
.name-title{font-size:16px;font-weight:700;margin-bottom:4px;display:flex;align-items:center;gap:8px}
.name-gender{font-size:9px;padding:2px 6px;border-radius:4px;font-weight:700;letter-spacing:0.5px}
.name-gender.male{background:rgba(59,130,246,0.2);color:#60a5fa}
.name-gender.female{background:rgba(236,72,153,0.2);color:#f472b6}
.name-meaning{font-size:12px;color:var(--text-muted);line-height:1.5}
.name-origin{font-size:10px;color:var(--text-subtle);margin-top:4px;font-style:italic}
.name-arabic{font-family:'Amiri',serif;font-size:24px;color:var(--primary);flex-shrink:0;direction:rtl}
.fav-btn{width:34px;height:34px;border-radius:50%;display:grid;place-items:center;flex-shrink:0;color:var(--text-subtle);transition:all .2s}
.fav-btn.active{color:var(--accent)}
.fav-btn svg{width:18px;height:18px;stroke:currentColor;fill:none;stroke-width:2}
.fav-btn.active svg{fill:var(--accent);stroke:var(--accent)}

.modal{position:fixed;inset:0;background:rgba(0,0,0,0.85);backdrop-filter:blur(8px);z-index:100;display:none;align-items:flex-end}
.modal.show{display:flex;animation:fadeIn .25s ease}
.modal-sheet{background:var(--bg-card);width:100%;max-height:90vh;overflow-y:auto;border-radius:24px 24px 0 0;padding:20px;padding-bottom:calc(20px + env(safe-area-inset-bottom));border-top:1px solid var(--border-hover);transform:translateY(100%);transition:transform .3s cubic-bezier(0.32,0.72,0,1)}
.modal.show .modal-sheet{transform:translateY(0)}
.modal-sheet::-webkit-scrollbar{width:0}
.drag{width:40px;height:4px;background:var(--border-hover);border-radius:2px;margin:0 auto 16px}
.modal-arabic{font-family:'Amiri',serif;font-size:44px;text-align:center;color:var(--primary);margin-bottom:8px;direction:rtl}
.modal-name{font-size:22px;font-weight:800;text-align:center;margin-bottom:4px}
.modal-gender{text-align:center;font-size:11px;color:var(--text-subtle);text-transform:uppercase;letter-spacing:1.5px;font-weight:700;margin-bottom:20px}
.modal-section{margin-bottom:16px}
.modal-label{font-size:11px;text-transform:uppercase;letter-spacing:1.5px;color:var(--primary);font-weight:700;margin-bottom:6px}
.modal-text{font-size:15px;color:var(--text-muted);line-height:1.7}
.modal-actions{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:20px}
.modal-btn{padding:14px;border-radius:12px;background:var(--bg-elev);color:var(--text);font-size:14px;font-weight:600;display:flex;align-items:center;justify-content:center;gap:8px;border:1px solid var(--border)}
.modal-btn:active{transform:scale(0.97)}
.modal-btn.primary{background:var(--green-grad);color:#fff;border-color:transparent;font-weight:700}
.modal-btn svg{width:16px;height:16px;stroke:currentColor;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}

.bottom-nav{
  position:fixed;bottom:0;left:0;right:0;height:var(--nav-h);
  background:rgba(13,51,32,0.95);backdrop-filter:blur(20px);
  border-top:1px solid var(--border);
  display:grid;grid-template-columns:repeat(3,1fr);z-index:50;padding-bottom:env(safe-area-inset-bottom);
}
[data-theme="light"] .bottom-nav{background:rgba(255,255,255,0.95)}
.nav-item{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:3px;color:var(--text-subtle);font-size:10px;font-weight:600;padding:8px}
.nav-item svg{width:22px;height:22px;stroke:currentColor;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.nav-item.active{color:var(--primary)}

.settings-group{background:var(--bg-card);border:1px solid var(--border);border-radius:16px;margin-bottom:14px;overflow:hidden}
.setting-row{display:flex;align-items:center;justify-content:space-between;padding:16px;gap:12px}
.setting-info{flex:1;display:flex;align-items:center;gap:12px}
.setting-info svg{width:20px;height:20px;stroke:var(--primary);fill:none;stroke-width:2;flex-shrink:0}
.setting-label{font-size:14px;font-weight:600}
.setting-sub{font-size:11px;color:var(--text-subtle);margin-top:2px}

.empty{text-align:center;padding:60px 20px;color:var(--text-subtle)}
.empty svg{width:64px;height:64px;stroke:var(--border-hover);fill:none;stroke-width:1.5;margin:0 auto 16px}
.empty h3{font-size:16px;color:var(--text-muted);margin-bottom:6px;font-weight:600}
.empty p{font-size:13px}

.toast{position:fixed;bottom:80px;left:50%;transform:translateX(-50%) translateY(20px);background:var(--bg-elev);color:var(--text);padding:12px 22px;border-radius:14px;font-size:13px;font-weight:600;box-shadow:var(--shadow-glow);border:1px solid var(--border-hover);opacity:0;transition:all .3s;pointer-events:none;z-index:200}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
</style>
</head>
<body data-theme="dark">

<header class="header">
  <div class="header-title">
    <div class="logo">👶</div>
    <span id="headerTitle">Islamic Names</span>
  </div>
  <button class="icon-btn" onclick="toggleTheme()"><svg viewBox="0 0 24 24" id="themeIcon"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg></button>
</header>

<main class="main" id="mainArea">

  <div class="view active" id="view-names">
    <div class="search-wrap">
      <div class="search-box">
        <svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg>
        <input type="text" id="searchInput" placeholder="Search by name or meaning..." oninput="handleSearch(this.value)">
      </div>
    </div>
    <div class="cats" id="catChips"></div>
    <div id="namesList"></div>
  </div>

  <div class="view" id="view-fav">
    <h2 style="font-size:20px;font-weight:700;margin-bottom:16px">Favorites</h2>
    <div id="favList"></div>
  </div>

  <div class="view" id="view-about">
    <h2 style="font-size:20px;font-weight:700;margin-bottom:8px">About</h2>
    <p style="font-size:13px;color:var(--text-subtle);margin-bottom:20px">Beautiful Islamic names for your children</p>

    <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:16px;padding:20px">
      <div style="font-size:15px;color:var(--primary);margin-bottom:12px;font-weight:700">📖 Importance</div>
      <div style="font-size:14px;color:var(--text-muted);line-height:1.8">The Prophet ﷺ said: "You will be called on the Day of Resurrection by your names and the names of your fathers, so choose good names for yourselves."</div>
      <div style="font-size:12px;color:var(--text-subtle);margin-top:10px">— Abu Dawud 4948</div>
    </div>

    <div style="text-align:center;padding:30px 0;font-size:12px;color:var(--text-subtle);line-height:1.8">
      Made with ❤️ for the Ummah<br>
      <strong style="color:var(--primary)">APKForge</strong> · v1.0.0
    </div>
  </div>

</main>

<nav class="bottom-nav">
  <button class="nav-item active" data-view="names" onclick="switchView('names')">
    <svg viewBox="0 0 24 24"><path d="M4 6h16M4 12h16M4 18h16"/></svg>
    <span>All Names</span>
  </button>
  <button class="nav-item" data-view="fav" onclick="switchView('fav')">
    <svg viewBox="0 0 24 24"><path d="M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 000-7.78z"/></svg>
    <span>Favorites</span>
  </button>
  <button class="nav-item" data-view="about" onclick="switchView('about')">
    <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></svg>
    <span>About</span>
  </button>
</nav>

<div class="modal" id="detailModal" onclick="closeModal(event)">
  <div class="modal-sheet" onclick="event.stopPropagation()">
    <div class="drag"></div>
    <div class="modal-arabic" id="modalArabic"></div>
    <div class="modal-name" id="modalName"></div>
    <div class="modal-gender" id="modalGender"></div>
    <div class="modal-section">
      <div class="modal-label">Meaning</div>
      <div class="modal-text" id="modalMeaning"></div>
    </div>
    <div class="modal-section">
      <div class="modal-label">Origin</div>
      <div class="modal-text" id="modalOrigin"></div>
    </div>
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

with open('templates/names.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Chunk 1 saved:', len(content), 'bytes')
