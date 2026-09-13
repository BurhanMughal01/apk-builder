// APKForge - Shared JavaScript
(function(){
  // Theme
  const savedTheme = localStorage.getItem('theme') || 'dark';
  document.documentElement.setAttribute('data-theme', savedTheme);

  window.toggleTheme = function(){
    const cur = document.documentElement.getAttribute('data-theme');
    const next = cur === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('theme', next);
    document.querySelectorAll('.theme-btn').forEach(b => b.textContent = next === 'dark' ? '🌙' : '☀️');
  };

  // User Auth (localStorage)
  window.getUser = function(){
    try { return JSON.parse(localStorage.getItem('apkUser') || 'null'); } catch(e){ return null; }
  };
  window.setUser = function(u){ localStorage.setItem('apkUser', JSON.stringify(u)); };
  window.logout = function(){
    localStorage.removeItem('apkUser');
    showToast('Logged out', 'success');
    setTimeout(() => location.href = 'index.html', 800);
  };

  // Build History
  window.getHistory = function(){
    try { return JSON.parse(localStorage.getItem('apkHistory') || '[]'); } catch(e){ return []; }
  };
  window.addToHistory = function(name, version, pkg, mode){
    const h = getHistory();
    h.unshift({ name, version: version || '1.0', pkg: pkg || 'auto', mode: mode || 'html', time: Date.now() });
    localStorage.setItem('apkHistory', JSON.stringify(h.slice(0, 50)));
  };
  window.clearHistory = function(){
    if (!confirm('Clear all history?')) return;
    localStorage.removeItem('apkHistory');
    showToast('History cleared', 'success');
    setTimeout(() => location.reload(), 500);
  };

  // Toast
  window.showToast = function(msg, type){
    type = type || 'success';
    let t = document.getElementById('toast');
    if (!t) {
      t = document.createElement('div');
      t.id = 'toast';
      t.className = 'toast';
      document.body.appendChild(t);
    }
    t.textContent = msg;
    t.className = 'toast show ' + type;
    clearTimeout(t._timeout);
    t._timeout = setTimeout(() => t.classList.remove('show'), 2800);
  };

  // FAQ toggle
  window.toggleFaq = function(el){
    el.parentElement.classList.toggle('open');
  };

  // Mobile nav toggle
  window.toggleNav = function(){
    document.getElementById('navMenu').classList.toggle('open');
  };

  // Nav scroll
  window.addEventListener('scroll', () => {
    const n = document.getElementById('nav');
    if (n) n.classList.toggle('scrolled', window.scrollY > 20);
  });

  // Init on load
  document.addEventListener('DOMContentLoaded', function(){
    // Set theme buttons
    document.querySelectorAll('.theme-btn').forEach(b => b.textContent = savedTheme === 'dark' ? '🌙' : '☀️');

    // User button
    const user = getUser();
    const ub = document.getElementById('userBtn');
    if (ub && user) {
      ub.textContent = (user.name || 'U').charAt(0).toUpperCase();
    }

    // Close mobile menu on link click
    document.querySelectorAll('#navMenu a').forEach(a => {
      a.addEventListener('click', () => {
        const m = document.getElementById('navMenu');
        if (m) m.classList.remove('open');
      });
    });

    // FAQ toggle
    document.querySelectorAll('.faq-q').forEach(q => {
      q.addEventListener('click', () => q.parentElement.classList.toggle('open'));
    });

    // Fade in on scroll
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          e.target.style.opacity = '1';
          e.target.style.transform = 'translateY(0)';
        }
      });
    }, { threshold: 0.1 });

    document.querySelectorAll('.card, .feat-card, .stat-box, .price, .faq').forEach(el => {
      el.style.opacity = '0';
      el.style.transform = 'translateY(20px)';
      el.style.transition = 'opacity .6s ease, transform .6s ease';
      observer.observe(el);
    });
  });
})();