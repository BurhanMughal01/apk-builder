export class BuildQueue {
  constructor(state, env) {
    this.state = state;
    this.env = env;
    this.queue = [];
    this.processing = false;
  }

  async fetch(request) {
    const url = new URL(request.url);

    if (url.pathname === '/enqueue') {
      const job = await request.json();
      this.queue.push(job);
      await this.state.storage.put('queue', this.queue);

      if (!this.processing) this.processNext();

      return new Response(JSON.stringify({
        position: this.queue.length,
        jobId: job.id
      }), { headers: { 'Content-Type': 'application/json' } });
    }

    if (url.pathname === '/position') {
      const jobId = url.searchParams.get('jobId');
      const pos = this.queue.findIndex(j => j.id === jobId);
      return new Response(JSON.stringify({ position: pos >= 0 ? pos + 1 : 0 }), {
        headers: { 'Content-Type': 'application/json' }
      });
    }

    if (url.pathname === '/status') {
      return new Response(JSON.stringify({
        queueLength: this.queue.length,
        processing: this.processing
      }), { headers: { 'Content-Type': 'application/json' } });
    }

    return new Response('Not found', { status: 404 });
  }

  async processNext() {
    if (this.processing || this.queue.length === 0) return;
    this.processing = true;

    while (this.queue.length > 0) {
      const job = this.queue.shift();
      await this.state.storage.put('queue', this.queue);

      try {
        await this.dispatchToGitHub(job);
      } catch (err) {
        console.error('Job failed:', err);
        await this.markFailed(job.id, err.message);
      }
    }

    this.processing = false;
  }

  async dispatchToGitHub(job) {
    const res = await fetch(
      'https://api.github.com/repos/' + this.env.GITHUB_REPO + '/dispatches',
      {
        method: 'POST',
        headers: {
          'Authorization': 'token ' + this.env.GITHUB_TOKEN,
          'Accept': 'application/vnd.github.v3+json',
          'User-Agent': 'APKForge-Queue',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          event_type: 'build_apk',
          client_payload: job
        })
      }
    );

    if (!res.ok) {
      const err = await res.text();
      throw new Error('GitHub dispatch failed: ' + res.status + ' ' + err);
    }
  }

  async markFailed(buildId, error) {
    try {
      await fetch(this.env.SUPABASE_URL + '/rest/v1/builds?id=eq.' + buildId, {
        method: 'PATCH',
        headers: {
          'apikey': this.env.SUPABASE_SERVICE_KEY,
          'Authorization': 'Bearer ' + this.env.SUPABASE_SERVICE_KEY,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ status: 'failed', error_message: error })
      });
    } catch (e) {
      console.error('Failed to mark build as failed:', e);
    }
  }
}
