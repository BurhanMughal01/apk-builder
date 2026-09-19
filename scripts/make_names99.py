content = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no,viewport-fit=cover">
<meta name="theme-color" content="#1a1207">
<title>99 Names of Allah</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Noto+Naskh+Arabic:wght@400;600;700&family=Cormorant+Garamond:wght@500;600;700&display=swap" rel="stylesheet">
<style>
:root{
  --bg:#1a1207;--bg-card:#2a1e0c;--bg-elev:#3a2a14;--bg-input:#1f1608;
  --text:#fef3c7;--text-muted:#c9a961;--text-subtle:#8b6f3f;
  --primary:#f59e0b;--primary-dark:#d97706;--accent:#fbbf24;
  --gold-grad:linear-gradient(135deg,#fbbf24,#d97706,#f59e0b);
  --border:rgba(251,191,36,0.2);--border-hover:rgba(251,191,36,0.5);
  --shadow:0 4px 24px rgba(0,0,0,0.5);
  --shadow-gold:0 0 30px rgba(251,191,36,0.3);
  --nav-h:64px;--header-h:60px;
}
[data-theme="light"]{
  --bg:#fefce8;--bg-card:#ffffff;--bg-elev:#fef3c7;--bg-input:#ffffff;
  --text:#1a1207;--text-muted:#78520a;--text-subtle:#b45309;
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
  background-image:radial-gradient(circle at 20% 10%,rgba(251,191,36,0.08),transparent 40%),radial-gradient(circle at 80% 90%,rgba(217,119,6,0.06),transparent 40%);
}
button{font-family:inherit;cursor:pointer;border:none;background:none;color:inherit}

.header{
  position:fixed;top:0;left:0;right:0;height:var(--header-h);
  background:rgba(26,18,7,0.85);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);
  border-bottom:1px solid var(--border);
  display:flex;align-items:center;padding:0 16px;gap:12px;z-index:50;
}
[data-theme="light"] .header{background:rgba(254,252,232,0.9)}
.header-title{flex:1;font-size:17px;font-weight:700;display:flex;align-items:center;gap:10px}
.logo{width:34px;height:34px;border-radius:10px;background:var(--gold-grad);display:grid;place-items:center;font-size:18px;box-shadow:0 4px 14px rgba(251,191,36,0.5)}
.icon-btn{width:40px;height:40px;border-radius:12px;display:grid;place-items:center;color:var(--text-muted);transition:all .2s}
.icon-btn:active{background:var(--bg-card);color:var(--accent)}
.icon-btn svg{width:20px;height:20px;stroke:currentColor;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}

.main{position:fixed;top:var(--header-h);bottom:var(--nav-h);left:0;right:0;overflow-y:auto;-webkit-overflow-scrolling:touch}
.main::-webkit-scrollbar{width:0}
.view{display:none;padding:16px;min-height:100%}
.view.active{display:block;animation:fadeIn .25s ease}
@keyframes fadeIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}

.search-wrap{padding:0 0 12px}
.search-box{display:flex;align-items:center;gap:10px;background:var(--bg-card);border:1px solid var(--border);border-radius:14px;padding:12px 16px;transition:all .2s}
.search-box:focus-within{border-color:var(--accent);box-shadow:0 0 0 3px rgba(251,191,36,0.15)}
.search-box svg{width:18px;height:18px;stroke:var(--text-subtle);fill:none;stroke-width:2}
.search-box input{flex:1;background:none;border:none;outline:none;color:var(--text);font-size:14px;font-family:inherit}
.search-box input::placeholder{color:var(--text-subtle)}

.name-card{
  background:var(--bg-card);border:1px solid var(--border);border-radius:16px;
  padding:18px;margin-bottom:12px;cursor:pointer;transition:all .25s;
  position:relative;overflow:hidden;
}
.name-card::before{
  content:'';position:absolute;top:0;right:0;width:80px;height:80px;
  background:var(--gold-grad);opacity:0.05;border-radius:0 0 0 80px;
}
.name-card:active{transform:scale(0.98);border-color:var(--border-hover)}
.name-card:active .name-num{background:var(--gold-grad);color:#1a1207}
.name-head{display:flex;align-items:center;gap:14px;margin-bottom:12px}
.name-num{
  width:38px;height:38px;border-radius:10px;
  background:var(--bg-elev);border:1px solid var(--border);
  display:grid;place-items:center;font-weight:800;font-size:14px;
  color:var(--accent);flex-shrink:0;transition:all .3s;font-family:'Cormorant Garamond',serif;
}
.name-translit{flex:1;font-size:16px;font-weight:700;color:var(--text);font-family:'Cormorant Garamond',serif;letter-spacing:0.5px}
.name-arabic{
  font-family:'Noto Naskh Arabic',serif;font-size:32px;
  color:var(--accent);direction:rtl;text-align:right;
  line-height:1.4;margin-bottom:6px;
}
.name-meaning{font-size:13px;color:var(--text-muted);font-style:italic}

.bottom-nav{
  position:fixed;bottom:0;left:0;right:0;height:var(--nav-h);
  background:rgba(42,30,12,0.95);backdrop-filter:blur(20px);
  border-top:1px solid var(--border);
  display:grid;grid-template-columns:repeat(3,1fr);z-index:50;padding-bottom:env(safe-area-inset-bottom);
}
[data-theme="light"] .bottom-nav{background:rgba(255,255,255,0.95)}
.nav-item{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:3px;color:var(--text-subtle);font-size:10px;font-weight:600;padding:8px}
.nav-item svg{width:22px;height:22px;stroke:currentColor;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.nav-item.active{color:var(--accent)}

.modal{position:fixed;inset:0;background:rgba(0,0,0,0.85);backdrop-filter:blur(8px);z-index:100;display:none;align-items:flex-end}
.modal.show{display:flex;animation:fadeIn .25s ease}
.modal-sheet{background:var(--bg-card);width:100%;max-height:90vh;border-radius:24px 24px 0 0;overflow-y:auto;padding:24px;padding-bottom:calc(24px + env(safe-area-inset-bottom));border-top:1px solid var(--border-hover);box-shadow:var(--shadow-gold)}
.modal-sheet::-webkit-scrollbar{width:0}
.drag{width:40px;height:4px;background:var(--border-hover);border-radius:2px;margin:0 auto 16px}
.modal-num{text-align:center;font-size:13px;color:var(--text-subtle);font-weight:700;letter-spacing:2px;margin-bottom:8px;font-family:'Cormorant Garamond',serif}
.modal-arabic{font-family:'Noto Naskh Arabic',serif;font-size:48px;line-height:1.6;text-align:center;color:var(--accent);margin-bottom:12px;padding:20px;background:var(--bg-elev);border-radius:20px;border:1px solid var(--border);text-shadow:0 0 30px rgba(251,191,36,0.4)}
.modal-translit{text-align:center;font-size:22px;font-weight:700;font-family:'Cormorant Garamond',serif;color:var(--text);margin-bottom:20px;letter-spacing:0.5px}
.modal-section{margin-bottom:16px}
.modal-label{font-size:11px;text-transform:uppercase;letter-spacing:1.5px;color:var(--accent);font-weight:700;margin-bottom:6px;text-align:center}
.modal-text{font-size:15px;color:var(--text-muted);line-height:1.7;text-align:center}
.modal-actions{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:20px}
.modal-btn{padding:14px;border-radius:12px;background:var(--bg-elev);color:var(--text);font-size:14px;font-weight:600;display:flex;align-items:center;justify-content:center;gap:8px;border:1px solid var(--border)}
.modal-btn:active{transform:scale(0.97)}
.modal-btn.primary{background:var(--gold-grad);color:#1a1207;border-color:transparent;font-weight:700}
.modal-btn svg{width:16px;height:16px;stroke:currentColor;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.modal-btn.active-fav{background:rgba(251,191,36,0.2);color:var(--accent);border-color:var(--border-hover)}

.empty{text-align:center;padding:60px 20px;color:var(--text-subtle)}
.empty svg{width:64px;height:64px;stroke:var(--border-hover);fill:none;stroke-width:1.5;margin:0 auto 16px}
.empty h3{font-size:16px;color:var(--text-muted);margin-bottom:6px;font-weight:600}

.toast{position:fixed;bottom:80px;left:50%;transform:translateX(-50%) translateY(20px);background:var(--bg-elev);color:var(--text);padding:12px 22px;border-radius:14px;font-size:13px;font-weight:600;box-shadow:var(--shadow-gold);border:1px solid var(--border-hover);opacity:0;transition:all .3s;pointer-events:none;z-index:200}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}

.section-label{font-size:11px;text-transform:uppercase;letter-spacing:1.5px;color:var(--text-subtle);font-weight:700;padding:16px 0 10px}
</style>
</head>
<body data-theme="dark">

<header class="header">
  <div class="header-title">
    <div class="logo">☪️</div>
    <span>99 Names of Allah</span>
  </div>
  <button class="icon-btn" onclick="toggleTheme()"><svg viewBox="0 0 24 24" id="themeIcon"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg></button>
</header>

<main class="main" id="mainArea">

  <div class="view active" id="view-all">
    <div class="search-wrap">
      <div class="search-box">
        <svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg>
        <input type="text" id="searchInput" placeholder="Search by name or meaning..." oninput="handleSearch(this.value)">
      </div>
    </div>
    <div id="namesList"></div>
  </div>

  <div class="view" id="view-fav">
    <h2 style="font-size:20px;font-weight:700;margin-bottom:16px">Favorites</h2>
    <div id="favList"></div>
  </div>

  <div class="view" id="view-about">
    <h2 style="font-size:20px;font-weight:700;margin-bottom:8px">About</h2>
    <p style="font-size:13px;color:var(--text-subtle);margin-bottom:20px">Learn and remember the 99 beautiful names of Allah</p>

    <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:16px;padding:20px;margin-bottom:14px">
      <div style="font-family:'Cormorant Garamond',serif;font-size:18px;color:var(--accent);margin-bottom:12px;font-weight:700">Hadith</div>
      <div style="font-size:14px;color:var(--text-muted);line-height:1.8;font-style:italic">"Allah has ninety-nine names, and whoever believes in their meanings and acts accordingly will enter Paradise."</div>
      <div style="font-size:12px;color:var(--text-subtle);margin-top:10px">— Sahih al-Bukhari 2736</div>
    </div>

    <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:16px;padding:20px">
      <div style="font-family:'Cormorant Garamond',serif;font-size:18px;color:var(--accent);margin-bottom:12px;font-weight:700">Benefits</div>
      <ul style="font-size:13px;color:var(--text-muted);line-height:2;padding-right:20px;list-style:none">
        <li>• Recite daily for spiritual growth</li>
        <li>• Memorize with meaning</li>
        <li>• Use in dua and dhikr</li>
        <li>• Understand Allah's attributes</li>
      </ul>
    </div>

    <div style="text-align:center;padding:30px 0;font-size:12px;color:var(--text-subtle);line-height:1.8">
      Made with ❤️ for the Ummah<br>
      <strong style="color:var(--accent)">APKForge</strong> · v1.0.0
    </div>
  </div>

</main>

<nav class="bottom-nav">
  <button class="nav-item active" data-view="all" onclick="switchView('all')">
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
    <div class="modal-num" id="modalNum"></div>
    <div class="modal-arabic" id="modalArabic"></div>
    <div class="modal-translit" id="modalTranslit"></div>
    <div class="modal-section">
      <div class="modal-label">Meaning</div>
      <div class="modal-text" id="modalMeaning"></div>
    </div>
    <div class="modal-section">
      <div class="modal-label">Reflection</div>
      <div class="modal-text" id="modalDesc"></div>
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
/* PLACEHOLDER FOR PART 2 */
</script>
</body>
</html>
'''

with open('templates/names99.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Chunk 1 (HTML+CSS) saved. Size:', len(content))
