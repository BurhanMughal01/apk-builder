import { hmacSHA256, log } from './utils.js';

export async function handleWebhook(request, env) {
  const body = await request.text();
  const signature = request.headers.get('X-Signature');

  const expected = await hmacSHA256(body, env.LEMON_WEBHOOK_SECRET);
  if (signature !== expected) {
    await log(env, 'warn', 'Invalid webhook signature');
    return new Response('Invalid signature', { status: 401 });
  }

  const event = JSON.parse(body);
  const eventName = event.meta && event.meta.event_name;
  const data = event.data && event.data.attributes;

  await log(env, 'info', 'Webhook: ' + eventName, { data: data });

  if (eventName === 'order_created' && data && data.status === 'paid') {
    const email = data.user_email;
    const variantName = (data.first_order_item && data.first_order_item.variant_name || '').toLowerCase();

    const planMap = {
      'basic': { plan: 'basic', limit: 20 },
      'pro': { plan: 'pro', limit: 100 },
      'unlimited': { plan: 'unlimited', limit: 99999 }
    };
    const mapped = planMap[variantName];

    if (mapped && email) {
      await fetch(env.SUPABASE_URL + '/rest/v1/profiles?email=eq.' + encodeURIComponent(email), {
        method: 'PATCH',
        headers: {
          'apikey': env.SUPABASE_SERVICE_KEY,
          'Authorization': 'Bearer ' + env.SUPABASE_SERVICE_KEY,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          plan: mapped.plan,
          builds_limit: mapped.limit,
          builds_used: 0
        })
      });

      await fetch(env.SUPABASE_URL + '/rest/v1/payments', {
        method: 'POST',
        headers: {
          'apikey': env.SUPABASE_SERVICE_KEY,
          'Authorization': 'Bearer ' + env.SUPABASE_SERVICE_KEY,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          amount: Math.round((data.total || 0) / 100),
          currency: data.currency || 'PKR',
          plan: mapped.plan,
          status: 'paid',
          provider: 'lemonsqueezy',
          provider_order_id: String(event.data.id),
          provider_data: data
        })
      });
    }
  }

  return new Response('OK');
}
