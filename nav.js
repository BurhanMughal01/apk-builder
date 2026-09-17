(function() {
  'use strict';

  // ===== THEME SETUP =====
  const savedTheme = localStorage.getItem('theme') || 'light';
  document.documentElement.setAttribute('data-theme', savedTheme);

  // ===== NAV HTML =====
  const NAV_HTML = `
    <nav class="nav" id="mainNav">
      <div class="container nav-inner">
        <a href="index.html" class="nav-logo">
          <div class="nav-logo-icon">⚡</div>
          <span>APKForge</span>
        </a>
        <ul class="nav-links" id="navLinks">
          <li><a href="index.html">Home</a></li>
          <li><a href="features.html">Features</a></li>
          <li><a href="build.html">Build</a></li>
          <li><a href="pricing.html">Pricing</a></li>
          <li><a href="faq.html">FAQ</a></li>
          <li><a href="about.html">About</a></li>
        </ul>
        <div class="nav-actions">
          <button class="theme-toggle" id="themeToggle" title="Toggle theme">
            <span id="themeIcon">${savedTheme === 'dark' ? '☀️' : '🌙'}</span>
          </button>
          <a href="login.html" class="btn btn-ghost btn-sm">Login</a>
          <a href="build.html" class="btn btn-primary btn-sm">Get Started</a>
          <button class="nav-mobile-btn" id="mobileBtn">☰</button>
        </div>
      </div>
    </nav>
    <div class="mobile-menu" id="mobileMenu">
      <a href="index.html">🏠 Home</a>
      <a href="features.html">✨ Features</a>
      <a href="build.html">🚀 Build APK</a>
      <a href="pricing.html">💰 Pricing</a>
      <a href="templates.html">📦 Templates</a>
      <a href="faq.html">❓ FAQ</a>
      <a href="about.html">ℹ️ About</a>
      <a href="contact.html">📧 Contact</a>
      <hr style="margin:12px 0;border:none;border-top:1px solid var(--border)">
      <a href="login.html">🔐 Login</a>
    </div>
  `;

  // ===== FOOTER HTML =====
  const FOOTER_HTML = `
    <footer class="footer">
      <div class="container">
        <div class="footer-grid">
          <div class="footer-brand">
            <a href="index.html" class="nav-logo">
              <div class="nav-logo-icon">⚡</div>
              <span>APKForge</span>
            </a>
            <p>Turn any website or HTML into a professional Android APK in under 60 seconds. Free, fast, and no coding required.</p>
          </div>
          <div class="footer-col">
            <h4>Product</h4>
            <ul>
              <li><a href="features.html">Features</a></li>
              <li><a href="build.html">Build APK</a></li>
              <li><a href="pricing.html">Pricing</a></li>
              <li><a href="templates.html">Templates</a></li>
            </ul>
          </div>
          <div class="footer-col">
            <h4>Company</h4>
            <ul>
              <li><a href="about.html">About</a></li>
              <li><a href="contact.html">Contact</a></li>
              <li><a href="faq.html">FAQ</a></li>
              <li><a href="dashboard.html">Dashboard</a></li>
            </ul>
          </div>
          <div class="footer-col">
            <h4>Legal</h4>
            <ul>
              <li><a href="privacy.html">Privacy</a></li>
              <li><a href="terms.html">Terms</a></li>
              <li><a href="refund.html">Refund</a></li>
            </ul>
          </div>
        </div>
        <div class="footer-bottom">
          <span>© ${new Date().getFullYear()} APKForge. All rights reserved.</span>
          <span>Made with ❤️ in Pakistan</span>
        </div>
      </div>
    </footer>
  `;

  // ===== INJECT =====
  if (!document.getElementById('mainNav')) {
    document.body.insertAdjacentHTML('afterbegin', NAV_HTML);
  }
  if (!document.querySelector('.footer')) {
    document.body.insertAdjacentHTML('beforeend', FOOTER_HTML);
  }

  // ===== THEME TOGGLE =====
  const themeToggle = document.getElementById('themeToggle');
  if (themeToggle) {
    themeToggle.addEventListener('click', function() {
      const current = document.documentElement.getAttribute('data-theme');
      const next = current === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      localStorage.setItem('theme', next);
      const icon = document.getElementById('themeIcon');
      if (icon) icon.textContent = next === 'dark' ? '☀️' : '🌙';
    });
  }

  // ===== SCROLL EFFECT =====
  const nav = document.getElementById('mainNav');
  if (nav) {
    window.addEventListener('scroll', function() {
      if (window.scrollY > 20) nav.classList.add('scrolled');
      else nav.classList.remove('scrolled');
    });
  }

  // ===== MOBILE MENU =====
  const mobileBtn = document.getElementById('mobileBtn');
  const mobileMenu = document.getElementById('mobileMenu');
  if (mobileBtn && mobileMenu) {
    mobileBtn.addEventListener('click', function() {
      mobileMenu.classList.toggle('open');
      mobileBtn.textContent = mobileMenu.classList.contains('open') ? '✕' : '☰';
    });
    document.addEventListener('click', function(e) {
      if (!mobileMenu.contains(e.target) && !mobileBtn.contains(e.target)) {
        mobileMenu.classList.remove('open');
        mobileBtn.textContent = '☰';
      }
    });
  }

  // ===== ACTIVE LINK =====
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-links a, .mobile-menu a').forEach(function(link) {
    const href = link.getAttribute('href');
    if (href === currentPath || (currentPath === '' && href === 'index.html')) {
      link.classList.add('active');
    }
  });

  // ===== FAQ ACCORDION (Sab Pages) =====
  document.querySelectorAll('.faq-q').forEach(function(q) {
    q.addEventListener('click', function() {
      q.parentElement.classList.toggle('open');
    });
  });

  // ===== TOAST SYSTEM (Global) =====
  window.showToast = function(message, type) {
    type = type || 'info';
    const existing = document.querySelector('.toast');
    if (existing) existing.remove();
    
    const toast = document.createElement('div');
    toast.className = 'toast toast-' + type;
    toast.textContent = message;
    document.body.appendChild(toast);
    
    setTimeout(function() {
      toast.style.opacity = '0';
      toast.style.transform = 'translateX(120%)';
      toast.style.transition = 'all 0.3s';
      setTimeout(function() { toast.remove(); }, 300);
    }, 3500);
  };

  // ===== SMOOTH SCROLL FOR HASH LINKS =====
  document.querySelectorAll('a[href^="#"]').forEach(function(link) {
    link.addEventListener('click', function(e) {
      const target = document.querySelector(link.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  // ===== BACK TO TOP BUTTON =====
  const backToTop = document.createElement('button');
  backToTop.className = 'back-to-top hidden';
  backToTop.innerHTML = '↑';
  backToTop.style.cssText = 'position:fixed;bottom:24px;right:24px;width:48px;height:48px;border-radius:50%;background:var(--grad-primary);color:#fff;font-size:1.5rem;box-shadow:var(--shadow-lg);z-index:99;transition:all 0.3s;cursor:pointer;border:none';
  document.body.appendChild(backToTop);
  
  window.addEventListener('scroll', function() {
    if (window.scrollY > 400) backToTop.classList.remove('hidden');
    else backToTop.classList.add('hidden');
  });
  
  backToTop.addEventListener('click', function() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });

  // ===== LOGIN STATE CHECK =====
  function updateAuthButtons() {
    const user = localStorage.getItem('apkforge_user');
    const loginBtn = document.querySelector('.nav-actions a[href="login.html"]');
    if (loginBtn && user) {
      try {
        const userData = JSON.parse(user);
        loginBtn.textContent = userData.name || 'Dashboard';
        loginBtn.href = 'dashboard.html';
      } catch(e) {}
    }
  }
  updateAuthButtons();

  console.log('✅ APKForge nav.js loaded');
})();
