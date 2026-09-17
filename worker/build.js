import { log } from "./utils.js";

const ISLAMIC_TEMPLATES = [
  'quran', 'duas', 'tasbeeh', 'hadith', 'names99', 'prayer',
  'qibla', 'zakat', 'adhkar', 'quiz', 'calendar', 'names',
  'ramadan', 'qunoot'
];

function isIslamicTemplate(name) {
  if (!name) return false;
  return ISLAMIC_TEMPLATES.includes(String(name).toLowerCase());
}

export async function handleBuild(request, env, user, ctx) {
  if (request.method !== 'POST') {
    return json({ error: 'Method not allowed' }, 405);
  }

  const data = await request.json();
  const { buildType, htmlContent, url, templateName, appName, packageName, version,
          splashStyle, splashColor, splashIcon, splashDuration, splashTagline,
          orientation, fullscreen, customIcon } = data;

  if (!appName || appName.length > 50) {
    return json({ error: 'Invalid app name' }, 400);
  }
  if (!packageName || !/^[a-z][a-z0-9_]*(\.[a-z][a-z0-9_]*)+$/.test(packageName)) {
    return json({ error: 'Invalid package name (e.g. com.example.app)' }, 400);
  }

  const isIslamic = isIslamicTemplate(templateName);

  let profile = null;
  if (user) {
    profile = await getUserProfile(user.id, env);
  }

  // Islamic templates = ALWAYS FREE, no quota check
  if (user && !isIslamic) {
    if (!profile || profile.builds_used >= profile.builds_limit) {
      return json({ 
        error: 'Quota exceeded', 
        upgrade: true,
        message: 'Islamic templates are always free. Upgrade for unlimited non-Islamic apps.'
      }, 403);
    }
  }

  const buildId = crypto.randomUUID();
  const buildRecord = {
    id: buildId,
    user_id: user ? user.id : null,
    app_name: appName,
    package_name: packageName,
    build_type: buildType,
    template_name: templateName || null,
    status: 'queued',
    created_at: new Date().toISOString()
  };

  await supabaseInsert('builds', buildRecord, env);

  // Only increment builds_used for NON-Islamic templates
  if (user && profile && !isIslamic) {
    await supabaseUpdate('profiles', user.id, { builds_used: profile.builds_used + 1 }, env);
  }

  const queueId = env.BUILD_QUEUE.idFromName('global');
  const queue = env.BUILD_QUEUE.get(queueId);

  const jobPayload = {
    id: buildId,
    buildType: buildType,
    htmlContent: htmlContent ? htmlContent.slice(0, 500000) : null,
    url: url || null,
    templateName: templateName || null,
    appName: appName,
    packageName: packageName,
    version: version || '1.0.0',
    splash: {
      style: splashStyle || 'gradient',
      color: splashColor || '#6366f1',
      icon: splashIcon || 'rocket',
      duration: splashDuration || 2000,
      tagline: splashTagline || ''
    },
    orientation: orientation || 'portrait',
    fullscreen: fullscreen || false,
    customIcon: customIcon || null,
    userId: user ? user.id : null,
    userEmail: user ? user.email : null
  };

  const queueRes = await queue.fetch('https://queue/enqueue', {
    method: 'POST',
    body: JSON.stringify(jobPayload)
  });
  const queueData = await queueRes.json();

  await log(env, 'info', 'Build queued', { buildId: buildId, userId: user ? user.id : null });

  return json({
    ok: true,
    buildId: buildId,
    queuePosition: queueData.position,
    estimatedWait: queueData.position * 90
  });
}

export async function handleStatus(request, env, user) {
  const url = new URL(request.url);
  const buildId = url.searchParams.get('buildId');

  if (!buildId) return json({ error: 'buildId required' }, 400);

  const res = await fetch(
    env.SUPABASE_URL + '/rest/v1/builds?id=eq.' + buildId + '&select=*',
    {
      headers: {
        'apikey': env.SUPABASE_SERVICE_KEY,
        'Authorization': 'Bearer ' + env.SUPABASE_SERVICE_KEY
      }
    }
  );
  const arr = await res.json();
  const build = arr[0];

  if (!build) return json({ error: 'Build not found' }, 404);

  if (user && build.user_id && build.user_id !== user.id && !user.is_admin) {
    return json({ error: 'Forbidden' }, 403);
  }

  let queuePosition = null;
  if (build.status === 'queued') {
    try {
      const queueId = env.BUILD_QUEUE.idFromName('global');
      const queue = env.BUILD_QUEUE.get(queueId);
      const posRes = await queue.fetch('https://queue/position?jobId=' + buildId);
      const posData = await posRes.json();
      queuePosition = posData.position;
    } catch (e) {
      queuePosition = null;
    }
  }

  let githubStatus = null;
  if (build.github_run_id) {
    githubStatus = await fetchGitHubStatus(build.github_run_id, env);
  }

  return json({ build: build, queuePosition: queuePosition, githubStatus: githubStatus });
}

async function getUserProfile(userId, env) {
  if (!userId) return null;
  const res = await fetch(
    env.SUPABASE_URL + '/rest/v1/profiles?id=eq.' + userId + '&select=*',
    {
      headers: {
        'apikey': env.SUPABASE_SERVICE_KEY,
        'Authorization': 'Bearer ' + env.SUPABASE_SERVICE_KEY
      }
    }
  );
  const arr = await res.json();
  return arr[0] || null;
}

async function supabaseInsert(table, data, env) {
  return fetch(env.SUPABASE_URL + '/rest/v1/' + table, {
    method: 'POST',
    headers: {
      'apikey': env.SUPABASE_SERVICE_KEY,
      'Authorization': 'Bearer ' + env.SUPABASE_SERVICE_KEY,
      'Content-Type': 'application/json',
      'Prefer': 'return=minimal'
    },
    body: JSON.stringify(data)
  });
}

async function supabaseUpdate(table, id, data, env) {
  return fetch(env.SUPABASE_URL + '/rest/v1/' + table + '?id=eq.' + id, {
    method: 'PATCH',
    headers: {
      'apikey': env.SUPABASE_SERVICE_KEY,
      'Authorization': 'Bearer ' + env.SUPABASE_SERVICE_KEY,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  });
}

async function fetchGitHubStatus(runId, env) {
  try {
    const res = await fetch(
      'https://api.github.com/repos/' + env.GITHUB_REPO + '/actions/runs/' + runId,
      {
        headers: {
          'Authorization': 'token ' + env.GITHUB_TOKEN,
          'Accept': 'application/vnd.github.v3+json',
          'User-Agent': 'APKForge'
        }
      }
    );
    if (!res.ok) return null;
    const data = await res.json();
    return {
      status: data.status,
      conclusion: data.conclusion,
      startedAt: data.run_started_at,
      updatedAt: data.updated_at
    };
  } catch {
    return null;
  }
}

function json(data, status) {
  return new Response(JSON.stringify(data), {
    status: status || 200,
    headers: { 'Content-Type': 'application/json' }
  });
}
