export async function handleAdmin(request, env, user) {
  if (!user) return json({ error: 'Not authenticated' }, 401);

  const res = await fetch(
    env.SUPABASE_URL + '/rest/v1/profiles?id=eq.' + user.id + '&select=is_admin',
    {
      headers: {
        'apikey': env.SUPABASE_SERVICE_KEY,
        'Authorization': 'Bearer ' + env.SUPABASE_SERVICE_KEY
      }
    }
  );
  const arr = await res.json();
  const profile = arr[0];

  if (!profile || !profile.is_admin) return json({ error: 'Forbidden' }, 403);

  const url = new URL(request.url);

  if (url.pathname === '/admin/stats') {
    const [usersRes, buildsRes] = await Promise.all([
      fetch(env.SUPABASE_URL + '/rest/v1/profiles?select=count', {
        headers: { 'apikey': env.SUPABASE_SERVICE_KEY, 'Authorization': 'Bearer ' + env.SUPABASE_SERVICE_KEY }
      }),
      fetch(env.SUPABASE_URL + '/rest/v1/builds?select=count', {
        headers: { 'apikey': env.SUPABASE_SERVICE_KEY, 'Authorization': 'Bearer ' + env.SUPABASE_SERVICE_KEY }
      })
    ]);
    const usersArr = await usersRes.json();
    const buildsArr = await buildsRes.json();
    return json({
      totalUsers: (usersArr[0] && usersArr[0].count) || 0,
      totalBuilds: (buildsArr[0] && buildsArr[0].count) || 0
    });
  }

  if (url.pathname === '/admin/users') {
    const res = await fetch(
      env.SUPABASE_URL + '/rest/v1/profiles?select=*&order=created_at.desc&limit=100',
      { headers: { 'apikey': env.SUPABASE_SERVICE_KEY, 'Authorization': 'Bearer ' + env.SUPABASE_SERVICE_KEY } }
    );
    const users = await res.json();
    return json({ users: users });
  }

  return json({ error: 'Not found' }, 404);
}

function json(data, status) {
  return new Response(JSON.stringify(data), {
    status: status || 200,
    headers: { 'Content-Type': 'application/json' }
  });
}
