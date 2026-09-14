const ALLOWED_ORIGINS = [
  'https://apk-builder-eosin.vercel.app',
  'http://localhost:3000',
  'http://localhost:5500'
];

export function corsHeaders(origin, env) {
  const allowed = ALLOWED_ORIGINS.includes(origin) ? origin : ALLOWED_ORIGINS[0];
  return {
    'Access-Control-Allow-Origin': allowed,
    'Access-Control-Allow-Methods': 'GET, POST, PATCH, DELETE, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type, X-API-Key, Authorization',
    'Access-Control-Max-Age': '86400',
    'Vary': 'Origin'
  };
}

export async function verifyApiKey(request, env) {
  const apiKey = request.headers.get('X-API-Key');
  if (apiKey !== env.API_SECRET) {
    return { ok: false, error: 'Invalid API key' };
  }

  const auth = request.headers.get('Authorization');
  if (auth && auth.startsWith('Bearer ')) {
    const token = auth.slice(7);
    const user = await verifySupabaseJWT(token, env);
    if (user) return { ok: true, user };
  }

  return { ok: true, user: null };
}

async function verifySupabaseJWT(token, env) {
  try {
    const res = await fetch(env.SUPABASE_URL + '/auth/v1/user', {
      headers: {
        'apikey': env.SUPABASE_ANON_KEY,
        'Authorization': 'Bearer ' + token
      }
    });
    if (!res.ok) return null;
    return await res.json();
  } catch {
    return null;
  }
}

export async function rateLimit(ip, path, env) {
  const now = Math.floor(Date.now() / 1000);
  const window = 3600;
  const limits = { '/build': 5, '/auth': 20, default: 100 };
  const limit = limits[path] || limits.default;
  const key = 'rl:' + ip + ':' + path + ':' + Math.floor(now / window);

  const count = parseInt(await env.RATE_LIMIT.get(key) || '0');

  if (count >= limit) {
    return { ok: false, retry: window - (now % window) };
  }

  await env.RATE_LIMIT.put(key, String(count + 1), { expirationTtl: window });
  return { ok: true };
}

export async function log(env, level, message, meta) {
  const entry = {
    level,
    message,
    meta: meta || {},
    timestamp: new Date().toISOString()
  };
  console.log(JSON.stringify(entry));

  if (env.LOGS) {
    const key = 'log:' + Date.now() + ':' + Math.random().toString(36).slice(2);
    await env.LOGS.put(key, JSON.stringify(entry), { expirationTtl: 604800 });
  }
}

export async function hmacSHA256(message, secret) {
  const enc = new TextEncoder();
  const key = await crypto.subtle.importKey(
    'raw', enc.encode(secret),
    { name: 'HMAC', hash: 'SHA-256' },
    false, ['sign']
  );
  const sig = await crypto.subtle.sign('HMAC', key, enc.encode(message));
  return Array.from(new Uint8Array(sig))
    .map(b => b.toString(16).padStart(2, '0'))
    .join('');
}
