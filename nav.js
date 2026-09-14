(function() {
  const NAV_HTML = `
    <nav class="nav" id="mainNav">
      <div class="container nav-inner">
        <a href="/" class="nav-logo">
          <div class="nav-logo-icon">⚡</div>
          <span>APKForge</span>
        </a>
        <ul class="nav-links" id="navLinks">
          <li><a href="/">Home</a></li>
          <li><a href="features.html">Features</a></li>
          <li><a href="build.html">Build</a></li>
          <li><a href="pricing.html">Pricing</a></li>
          <li><a href="faq.html">FAQ</a></li>
          <li><a href="about.html">About</a></li>
        </ul>
        <div class="nav-actions">
          <button class="theme-toggle" id="themeToggle" title="Toggle theme">
            <span id="themeIcon">🌙</span>
          </button>
          <a href="login.html" class="btn btn-ghost btn-sm">Login</a>
          <a href="build.html" class="btn btn-primary btn-sm">Get Started</a>
          <button class="nav-mobile-btn" id="mobileBtn">☰</button>
        </div>
      </div>
    </nav>
    <div class="mobile-menu" id="mobileMenu">
      <a href="/">Home</a>
      <a href="features.html">Features</a>
      <a href="build.html">Build</a>
      <a href="pricing.html">Pricing</a>
      <a href="faq.html">FAQ</a>
      <a href="about.html">About</a>
      <a href="contact.html">Contact</a>
      <a href="login.html">Login</a>
    </div>
  `;

  const FOOTER_HTML = `
    <footer class="footer">
      <div class="container">
        <div class="footer-grid">
          <div class="footer-brand">
            <a href="/" class="nav-logo">
              <div class="nav-logo-icon">⚡</div>
              <span>APKForge</span>
            </a>
            <p>Convert any website or HTML into a professional Android APK in 60 seconds.</p>
          </div>
          <div class="footer-col">
            <h4>Product</h4>
            <ul>
              <li><a href="features.html">Features</a></li>
              <li><a href="build.html">Build APK</a></li>
              <li><a href="pricing.html">Pricing</a></li>
            </ul>
          </div>
          <div class="footer-col">
            <h4>Company</h4>
            <ul>
              <li><a href="about.html">About</a></li>
              <li><a href="contact.html">Contact</a></li>
              <li><a href="faq.html">FAQ</a></li>
            </ul>
          </div>
          <div class="footer-col">
            <h4>Legal</h4>
            <ul>
              <li><a href="privacy.html">Privacy</a></li>
              <li><a href="terms.html">Terms</a></li>
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

  document.body.insertAdjacentHTML('afterbegin', NAV_HTML);
  document.body.insertAdjacentHTML('beforeend', FOOTER_HTML);

  const savedTheme = localStorage.getItem('theme') || 'light';
  document.documentElement.setAttribute('data-theme', savedTheme);
  updateThemeIcon(savedTheme);

  document.getElementById('themeToggle').addEventListener('click', () => {
    const current = document.documentElement.getAttribute('data-theme');
    const next = current === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('theme', next);
    updateThemeIcon(next);
  });

  function updateThemeIcon(theme) {
    const icon = document.getElementById('themeIcon');
    if (icon) icon.textContent = theme === 'dark' ? '☀️' : '🌙';
  }

  const nav = document.getElementById('mainNav');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 20) nav.classList.add('scrolled');
    else nav.classList.remove('scrolled');
  });

  const mobileBtn = document.getElementById('mobileBtn');
  const mobileMenu = document.getElementById('mobileMenu');
  if (mobileBtn) {
    mobileBtn.addEventListener('click', () => {
      mobileMenu.classList.toggle('open');
      mobileBtn.textContent = mobileMenu.classList.contains('open') ? '✕' : '☰';
    });
  }

  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-links a, .mobile-menu a').forEach(link => {
    const href = link.getAttribute('href').split('/').pop();
    if (href === currentPath || (currentPath === '' && href === 'index.html')) {
      link.classList.add('active');
    }
  });

  document.querySelectorAll('.faq-q').forEach(q => {
    q.addEventListener('click', () => {
      q.parentElement.classList.toggle('open');
    });
  });

  window.showToast = function(message, type = 'info') {
    const toast = document.createElement('div');
    toast.className = 'toast toast-' + type;
    toast.textContent = message;
    document.body.appendChild(toast);
    setTimeout(() => toast.remove(), 4000);
  };
})();

if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('/sw.js').catch(err => console.log('SW error:', err));
  });
}
