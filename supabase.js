const SUPABASE_URL = 'https://hmfesroapkllwnvvholb.supabase.co';
const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhtZmVzcm9hcGtsbHdudnZob2xiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODkzODYwNTEsImV4cCI6MjEwNDk2MjA1MX0.R8ngiq5m79gt-VBVze33BVHRpiVXRV3q0ZoR1QWqJtk';

let db = null;

if (window.supabase) {
  const { createClient } = window.supabase;
  db = createClient(SUPABASE_URL, SUPABASE_ANON_KEY, {
    auth: { persistSession: true, autoRefreshToken: true, detectSessionInUrl: true }
  });
}

window.Auth = {
  async signUp(email, password, fullName) {
    const { data, error } = await db.auth.signUp({
      email, password,
      options: {
        data: { full_name: fullName },
        emailRedirectTo: location.origin + '/dashboard.html'
      }
    });
    if (error) throw error;
    return data;
  },
  async signIn(email, password) {
    const { data, error } = await db.auth.signInWithPassword({ email, password });
    if (error) throw error;
    return data;
  },
  async signInWithGoogle() {
    const { error } = await db.auth.signInWithOAuth({
      provider: 'google',
      options: { redirectTo: location.origin + '/dashboard.html' }
    });
    if (error) throw error;
  },
  async signOut() {
    await db.auth.signOut();
    location.href = '/';
  },
  async getUser() {
    if (!db) return null;
    const { data } = await db.auth.getUser();
    return data.user;
  },
  async getSession() {
    if (!db) return null;
    const { data } = await db.auth.getSession();
    return data.session;
  },
  async requireAuth() {
    const session = await this.getSession();
    if (!session) {
      location.href = '/login.html?redirect=' + encodeURIComponent(location.pathname);
      return null;
    }
    return session.user;
  }
};

window.Profile = {
  async get(userId) {
    const { data, error } = await db.from('profiles').select('*').eq('id', userId).single();
    if (error) throw error;
    return data;
  },
  async update(userId, updates) {
    const { data, error } = await db.from('profiles').update(updates).eq('id', userId).select().single();
    if (error) throw error;
    return data;
  }
};

window.Builds = {
  async list(userId, limit) {
    limit = limit || 50;
    const { data, error } = await db.from('builds').select('*').eq('user_id', userId).order('created_at', { ascending: false }).limit(limit);
    if (error) throw error;
    return data;
  },
  async get(buildId) {
    const { data, error } = await db.from('builds').select('*').eq('id', buildId).single();
    if (error) throw error;
    return data;
  },
  subscribeToUserBuilds(userId, callback) {
    return db.channel('user-builds:' + userId)
      .on('postgres_changes', { event: '*', schema: 'public', table: 'builds', filter: 'user_id=eq.' + userId }, callback)
      .subscribe();
  }
};

window.Notifications = {
  async list(userId, unreadOnly) {
    let q = db.from('notifications').select('*').eq('user_id', userId);
    if (unreadOnly) q = q.eq('is_read', false);
    const { data, error } = await q.order('created_at', { ascending: false }).limit(20);
    if (error) throw error;
    return data;
  },
  async markRead(id) {
    await db.from('notifications').update({ is_read: true }).eq('id', id);
  },
  subscribe(userId, callback) {
    return db.channel('notif:' + userId)
      .on('postgres_changes', { event: 'INSERT', schema: 'public', table: 'notifications', filter: 'user_id=eq.' + userId }, callback)
      .subscribe();
  }
};

window.API = {
  baseUrl: '/api',
  async call(path, options) {
    options = options || {};
    const session = await Auth.getSession();
    const headers = {
      'Content-Type': 'application/json'
    };
    if (session && session.access_token) {
      headers['Authorization'] = 'Bearer ' + session.access_token;
    }
    const res = await fetch(this.baseUrl + path, Object.assign({}, options, { headers: Object.assign(headers, options.headers || {}) }));
    const data = await res.json();
    if (!res.ok) throw Object.assign(new Error(data.error || 'Failed'), { status: res.status });
    return data;
  },
  build(payload) {
    return this.call('/build', { method: 'POST', body: JSON.stringify(payload) });
  },
  status(buildId) {
    return this.call('/status?buildId=' + buildId);
  }
};

window.db = db;
