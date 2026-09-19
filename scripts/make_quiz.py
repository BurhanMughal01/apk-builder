content = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no,viewport-fit=cover">
<meta name="theme-color" content="#1a0a04">
<title>Islamic Quiz</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<style>
:root{
  --bg:#1a0a04;--bg-card:#2a1409;--bg-elev:#3d1e0d;--bg-input:#211008;
  --text:#fed7aa;--text-muted:#fdba74;--text-subtle:#a16207;
  --primary:#f97316;--primary-dark:#ea580c;--accent:#ef4444;--gold:#fbbf24;
  --orange-grad:linear-gradient(135deg,#f97316,#ef4444);
  --gold-grad:linear-gradient(135deg,#fbbf24,#f59e0b);
  --success:#10b981;--danger:#ef4444;
  --border:rgba(249,115,22,0.2);--border-hover:rgba(249,115,22,0.5);
  --shadow:0 4px 24px rgba(0,0,0,0.5);
  --shadow-glow:0 0 30px rgba(249,115,22,0.3);
  --nav-h:64px;--header-h:60px;
}
[data-theme="light"]{
  --bg:#fff7ed;--bg-card:#ffffff;--bg-elev:#ffedd5;--bg-input:#ffffff;
  --text:#431407;--text-muted:#9a3412;--text-subtle:#fb923c;
  --border:rgba(234,88,12,0.2);--border-hover:rgba(234,88,12,0.4);
  --shadow:0 4px 24px rgba(67,20,7,0.1);
}
*{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}
html,body{height:100%;overflow:hidden}
body{
  font-family:'Inter',system-ui,sans-serif;
  background:var(--bg);color:var(--text);
  transition:background .3s,color .3s;
  overscroll-behavior:none;-webkit-font-smoothing:antialiased;
  background-image:radial-gradient(circle at 20% 10%,rgba(249,115,22,0.1),transparent 40%),radial-gradient(circle at 80% 90%,rgba(239,68,68,0.08),transparent 40%);
}
button{font-family:inherit;cursor:pointer;border:none;background:none;color:inherit}

.header{
  position:fixed;top:0;left:0;right:0;height:var(--header-h);
  background:rgba(26,10,4,0.9);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);
  border-bottom:1px solid var(--border);
  display:flex;align-items:center;padding:0 16px;gap:12px;z-index:50;
}
[data-theme="light"] .header{background:rgba(255,247,237,0.95)}
.header-title{flex:1;font-size:17px;font-weight:800;display:flex;align-items:center;gap:10px}
.logo{width:34px;height:34px;border-radius:10px;background:var(--orange-grad);display:grid;place-items:center;font-size:18px;box-shadow:0 4px 14px rgba(249,115,22,0.5)}
.icon-btn{width:40px;height:40px;border-radius:12px;display:grid;place-items:center;color:var(--text-muted);transition:all .2s}
.icon-btn:active{background:var(--bg-card);color:var(--primary)}
.icon-btn svg{width:20px;height:20px;stroke:currentColor;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}

.main{position:fixed;top:var(--header-h);bottom:var(--nav-h);left:0;right:0;overflow-y:auto;-webkit-overflow-scrolling:touch}
.main::-webkit-scrollbar{width:0}
.view{display:none;padding:16px;min-height:100%}
.view.active{display:block;animation:fadeIn .3s ease}
@keyframes fadeIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}

/* HERO */
.hero{
  background:var(--orange-grad);border-radius:24px;padding:32px 24px;
  text-align:center;margin-bottom:20px;position:relative;overflow:hidden;
  box-shadow:0 8px 30px rgba(249,115,22,0.4);
}
.hero::before{content:'';position:absolute;top:-50px;right:-50px;width:200px;height:200px;border-radius:50%;background:radial-gradient(circle,rgba(255,255,255,0.2),transparent 70%)}
.hero-icon{font-size:56px;margin-bottom:12px;position:relative;z-index:1}
.hero-title{font-size:26px;font-weight:900;color:#fff;margin-bottom:6px;position:relative;z-index:1;letter-spacing:-0.5px}
.hero-sub{font-size:14px;color:rgba(255,255,255,0.9);position:relative;z-index:1}

/* START SCREEN */
.start-screen{display:flex;flex-direction:column;gap:14px}
.category-btn{
  background:var(--bg-card);border:1px solid var(--border);border-radius:18px;
  padding:20px;display:flex;align-items:center;gap:14px;
  transition:all .2s;text-align:left;
}
.category-btn:active{transform:scale(0.98);border-color:var(--border-hover)}
.cat-icon{width:52px;height:52px;border-radius:14px;background:var(--orange-grad);display:grid;place-items:center;font-size:26px;flex-shrink:0;box-shadow:0 4px 12px rgba(249,115,22,0.3)}
.cat-info{flex:1}
.cat-name{font-size:16px;font-weight:800;margin-bottom:2px}
.cat-desc{font-size:12px;color:var(--text-subtle)}
.cat-arrow{width:24px;height:24px;stroke:var(--text-subtle);fill:none;stroke-width:2.5;flex-shrink:0}

/* QUIZ SCREEN */
.quiz-screen{display:flex;flex-direction:column;gap:16px;min-height:calc(100% - 20px)}

.quiz-head{
  display:flex;align-items:center;justify-content:space-between;gap:12px;
  padding:14px 18px;background:var(--bg-card);border:1px solid var(--border);border-radius:16px;
}
.quiz-progress-text{font-size:13px;font-weight:700;color:var(--text-muted)}
.quiz-score-live{font-size:16px;font-weight:900;color:var(--primary);font-variant-numeric:tabular-nums}
.timer-badge{
  display:flex;align-items:center;gap:6px;
  padding:6px 12px;background:var(--orange-grad);color:#fff;
  border-radius:20px;font-size:13px;font-weight:800;
  font-variant-numeric:tabular-nums;
  transition:all .3s;
}
.timer-badge svg{width:14px;height:14px;stroke:currentColor;fill:none;stroke-width:2.5}
.timer-badge.warning{background:var(--danger);animation:pulse 0.8s infinite}
@keyframes pulse{0%,100%{transform:scale(1)}50%{transform:scale(1.08)}}

.quiz-progress-bar{height:6px;background:var(--bg-elev);border-radius:3px;overflow:hidden}
.quiz-progress-fill{height:100%;background:var(--orange-grad);border-radius:3px;transition:width .4s;box-shadow:0 0 12px rgba(249,115,22,0.6)}

.question-card{
  background:var(--bg-card);border:1px solid var(--border);
  border-radius:20px;padding:24px;
  box-shadow:var(--shadow);
}
.q-num{font-size:11px;color:var(--primary);font-weight:800;text-transform:uppercase;letter-spacing:1.5px;margin-bottom:10px}
.q-text{font-size:19px;font-weight:700;line-height:1.5;color:var(--text)}

.answers-list{display:flex;flex-direction:column;gap:10px}
.answer-btn{
  background:var(--bg-card);border:2px solid var(--border);
  border-radius:16px;padding:16px 18px;
  display:flex;align-items:center;gap:12px;
  transition:all .2s;text-align:left;
  font-size:15px;font-weight:600;color:var(--text);
  min-height:60px;
}
.answer-btn:active{transform:scale(0.98)}
.answer-btn:disabled{cursor:default}
.answer-letter{
  width:32px;height:32px;border-radius:50%;
  background:var(--bg-elev);border:2px solid var(--border);
  display:grid;place-items:center;flex-shrink:0;
  font-size:14px;font-weight:800;color:var(--text-muted);
  transition:all .2s;
}
.answer-btn.correct{background:rgba(16,185,129,0.15);border-color:var(--success)}
.answer-btn.correct .answer-letter{background:var(--success);color:#fff;border-color:var(--success)}
.answer-btn.wrong{background:rgba(239,68,68,0.15);border-color:var(--danger)}
.answer-btn.wrong .answer-letter{background:var(--danger);color:#fff;border-color:var(--danger)}
.answer-btn.reveal-correct{background:rgba(16,185,129,0.15);border-color:var(--success)}

/* RESULT SCREEN */
.result-screen{
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  text-align:center;padding:20px 0;min-height:calc(100% - 20px);
}
.result-circle{
  width:180px;height:180px;border-radius:50%;
  background:var(--orange-grad);
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  margin-bottom:24px;position:relative;
  box-shadow:0 20px 60px rgba(249,115,22,0.5);
  animation:pop 0.5s cubic-bezier(0.34,1.56,0.64,1);
}
@keyframes pop{from{transform:scale(0)}to{transform:scale(1)}}
.result-percent{font-size:48px;font-weight:900;color:#fff;line-height:1}
.result-percent-label{font-size:13px;color:rgba(255,255,255,0.9);margin-top:6px;font-weight:700}

.result-title{font-size:24px;font-weight:900;margin-bottom:8px;letter-spacing:-0.5px}
.result-message{font-size:14px;color:var(--text-muted);margin-bottom:24px;max-width:300px}

.result-stats{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;width:100%;margin-bottom:24px}
.result-stat{background:var(--bg-card);border:1px solid var(--border);border-radius:16px;padding:14px}
.result-stat-val{font-size:22px;font-weight:900;color:var(--primary);margin-bottom:2px;line-height:1}
.result-stat-label{font-size:10px;color:var(--text-subtle);text-transform:uppercase;letter-spacing:0.5px;font-weight:700}

.result-actions{display:flex;flex-direction:column;gap:10px;width:100%;max-width:320px}
.btn-primary{
  padding:16px;border-radius:16px;background:var(--orange-grad);color:#fff;
  font-size:15px;font-weight:800;font-family:inherit;
  box-shadow:0 6px 20px rgba(249,115,22,0.4);
  transition:all .2s;
}
.btn-primary:active{transform:scale(0.97)}
.btn-secondary{
  padding:16px;border-radius:16px;background:var(--bg-elev);color:var(--text);
  font-size:15px;font-weight:700;font-family:inherit;
  border:1px solid var(--border);
}
.btn-secondary:active{transform:scale(0.97)}

/* BOTTOM NAV */
.bottom-nav{
  position:fixed;bottom:0;left:0;right:0;height:var(--nav-h);
  background:rgba(42,20,9,0.95);backdrop-filter:blur(20px);
  border-top:1px solid var(--border);
  display:grid;grid-template-columns:repeat(2,1fr);z-index:50;padding-bottom:env(safe-area-inset-bottom);
}
[data-theme="light"] .bottom-nav{background:rgba(255,255,255,0.95)}
.nav-item{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:3px;color:var(--text-subtle);font-size:10px;font-weight:700;padding:8px}
.nav-item svg{width:22px;height:22px;stroke:currentColor;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.nav-item.active{color:var(--primary)}

/* LEADERBOARD */
.lb-item{background:var(--bg-card);border:1px solid var(--border);border-radius:14px;padding:14px 16px;display:flex;align-items:center;gap:14px;margin-bottom:10px}
.lb-rank{width:36px;height:36px;border-radius:10px;background:var(--gold-grad);color:#1a0a04;display:grid;place-items:center;font-weight:900;font-size:14px;flex-shrink:0}
.lb-info{flex:1;min-width:0}
.lb-cat{font-size:14px;font-weight:700;margin-bottom:2px}
.lb-date{font-size:11px;color:var(--text-subtle)}
.lb-score{font-size:18px;font-weight:900;color:var(--primary);font-variant-numeric:tabular-nums}

.empty{text-align:center;padding:60px 20px;color:var(--text-subtle)}
.empty svg{width:64px;height:64px;stroke:var(--border-hover);fill:none;stroke-width:1.5;margin:0 auto 16px}
.empty h3{font-size:16px;color:var(--text-muted);margin-bottom:6px;font-weight:700}

.toast{position:fixed;bottom:80px;left:50%;transform:translateX(-50%) translateY(20px);background:var(--bg-elev);color:var(--text);padding:12px 22px;border-radius:14px;font-size:13px;font-weight:700;box-shadow:var(--shadow-glow);border:1px solid var(--border-hover);opacity:0;transition:all .3s;pointer-events:none;z-index:200}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
</style>
</head>
<body data-theme="dark">

<header class="header">
  <div class="header-title">
    <div class="logo">🎮</div>
    <span id="headerTitle">Islamic Quiz</span>
  </div>
  <button class="icon-btn" onclick="toggleTheme()"><svg viewBox="0 0 24 24" id="themeIcon"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg></button>
</header>

<main class="main" id="mainArea">

  <div class="view active" id="view-quiz">
    <div id="quizContent"></div>
  </div>

  <div class="view" id="view-scores">
    <h2 style="font-size:20px;font-weight:800;margin-bottom:16px">Your Scores</h2>
    <div id="scoresList"></div>
  </div>

</main>

<nav class="bottom-nav">
  <button class="nav-item active" data-view="quiz" onclick="switchView('quiz')">
    <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 015.83 1c0 2-3 3-3 3M12 17h.01"/></svg>
    <span>Quiz</span>
  </button>
  <button class="nav-item" data-view="scores" onclick="switchView('scores')">
    <svg viewBox="0 0 24 24"><path d="M8 21h8M12 17v4M7 4h10l1 8a6 6 0 11-12 0z"/><path d="M7 4H4a2 2 0 00-2 2 4 4 0 004 4M17 4h3a2 2 0 012 2 4 4 0 01-4 4"/></svg>
    <span>Scores</span>
  </button>
</nav>

<div class="toast" id="toast"><span id="toastText">Saved</span></div>

<script>
/* PART 2 WILL BE INJECTED */
</script>
</body>
</html>
'''

with open('templates/quiz.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Chunk 1 saved:', len(content), 'bytes')
