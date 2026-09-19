import { handleAuth } from './auth.js';
import { handleBuild, handleStatus } from './build.js';
import { handleWebhook } from './webhook.js';
import { handleAdmin } from './admin.js';
import { corsHeaders, verifyApiKey, rateLimit, log } from './utils.js';

export { BuildQueue } from './queue.js';

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const path = url.pathname;
    const origin = request.headers.get('Origin') || '';

    if (request.method === 'OPTIONS') {
  return new Response('', {
    status: 204,
    headers: {
      'Access-Control-Allow-Origin': origin || '*',
      'Access-Control-Allow-Methods': 'GET, POST, PUT, PATCH, DELETE, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type, X-API-Key, Authorization, Accept, Origin',
      'Access-Control-Max-Age': '0',
      'Vary': 'Origin'
    }
  });
}

    if (path === '/health') {
      return json({ status: 'ok', version: '2.0.0', time: Date.now() }, origin, env);
    }

    try {
      if (path === '/webhook/lemonsqueezy') {
        return await handleWebhook(request, env);
      }

      const authResult = await verifyApiKey(request, env);
      if (!authResult.ok) {
        return json({ error: authResult.error }, origin, env, 401);
      }

      const ip = request.headers.get('CF-Connecting-IP') || 'unknown';
      const rl = await rateLimit(ip, path, env);
      if (!rl.ok) {
        return json({ error: 'Rate limit exceeded', retry: rl.retry }, origin, env, 429);
      }

      const user = authResult.user;

      if (path.startsWith('/auth')) return await handleAuth(request, env, user);
      if (path === '/build') return await handleBuild(request, env, user, ctx);
      if (path.startsWith('/status')) return await handleStatus(request, env, user);
      if (path.startsWith('/admin')) return await handleAdmin(request, env, user);

      return json({ error: 'Not found', path: path }, origin, env, 404);

    } catch (err) {
      await log(env, 'error', err.message, { path: path, stack: err.stack });
      return json({ error: 'Internal error', message: err.message }, origin, env, 500);
    }
  }
};

function json(data, origin, env, status) {
  return new Response(JSON.stringify(data), {
    status: status || 200,
    headers: Object.assign(
      { 'Content-Type': 'application/json' },
      corsHeaders(origin, env)
    )
  });
}
// trigger Sun Sep 20 00:31:00 PKT 2026
