export async function handleAuth(request, env, user) {
  const url = new URL(request.url);

  if (url.pathname === '/auth/me') {
    if (!user) return json({ error: 'Not authenticated' }, 401);

    const res = await fetch(
      env.SUPABASE_URL + '/rest/v1/profiles?id=eq.' + user.id + '&select=*',
      {
        headers: {
          'apikey': env.SUPABASE_SERVICE_KEY,
          'Authorization': 'Bearer ' + env.SUPABASE_SERVICE_KEY
        }
      }
    );
    const arr = await res.json();
    const profile = arr[0];
    return json({ user: user, profile: profile });
  }

  if (url.pathname === '/auth/check-quota') {
    if (!user) return json({ error: 'Not authenticated' }, 401);

    const res = await fetch(
      env.SUPABASE_URL + '/rest/v1/profiles?id=eq.' + user.id + '&select=builds_used,builds_limit,plan',
      {
        headers: {
          'apikey': env.SUPABASE_SERVICE_KEY,
          'Authorization': 'Bearer ' + env.SUPABASE_SERVICE_KEY
        }
      }
    );
    const arr = await res.json();
    const profile = arr[0] || {};
    return json({
      used: profile.builds_used || 0,
      limit: profile.builds_limit || 3,
      plan: profile.plan || 'free',
      remaining: Math.max(0, (profile.builds_limit || 3) - (profile.builds_used || 0))
    });
  }

  return json({ error: 'Not found' }, 404);
}

function json(data, status) {
  return new Response(JSON.stringify(data), {
    status: status || 200,
    headers: { 'Content-Type': 'application/json' }
  });
}
