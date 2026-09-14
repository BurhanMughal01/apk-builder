const CACHE_NAME = 'apkforge-v1';
const ASSETS = [
  '/',
  '/index.html',
  '/build.html',
  '/features.html',
  '/pricing.html',
  '/faq.html',
  '/about.html',
  '/contact.html',
  '/login.html',
  '/dashboard.html',
  '/history.html',
  '/style.css',
  '/nav.js',
  '/supabase.js',
  '/manifest.json'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(ASSETS)).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', event => {
  const req = event.request;

  if (req.method !== 'GET') return;

  const url = req.url;

  if (url.includes('workers.dev') || url.includes('supabase') || url.includes('github')) {
    event.respondWith(fetch(req).catch(() => caches.match(req)));
    return;
  }

  event.respondWith(
    caches.match(req).then(cached => cached || fetch(req).then(res => {
      const copy = res.clone();
      caches.open(CACHE_NAME).then(c => c.put(req, copy));
      return res;
    }).catch(() => caches.match('/index.html')))
  );
});
