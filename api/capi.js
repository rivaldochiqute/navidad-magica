// API de Conversões da Meta: espelha no servidor os eventos do Pixel (com o mesmo event_id para deduplicar).
// Precisa da variável de ambiente META_CAPI_TOKEN na Vercel. Sem ela, não faz nada.
const PIXEL = '1041190532334614';
const ALLOWED = ['PageView', 'ViewContent', 'InitiateCheckout'];

module.exports = async (req, res) => {
  const token = process.env.META_CAPI_TOKEN;
  if (req.method !== 'POST' || !token) return res.status(204).end();
  let b = req.body;
  if (typeof b === 'string') { try { b = JSON.parse(b); } catch (e) { b = {}; } }
  b = b || {};
  if (!ALLOWED.includes(b.event_name) || !b.event_id) return res.status(400).end();
  const ip = String(req.headers['x-forwarded-for'] || '').split(',')[0].trim();
  const user_data = { client_ip_address: ip, client_user_agent: req.headers['user-agent'] || '' };
  if (b.fbp) user_data.fbp = String(b.fbp).slice(0, 200);
  if (b.fbc) user_data.fbc = String(b.fbc).slice(0, 300);
  const ev = {
    event_name: b.event_name, event_time: Math.floor(Date.now() / 1000), event_id: String(b.event_id).slice(0, 100),
    action_source: 'website', event_source_url: String(b.url || '').slice(0, 1000), user_data,
  };
  if (b.event_name !== 'PageView') ev.custom_data = { content_name: 'Mi Familia Navideña 2026', content_type: 'product', value: 4.9, currency: 'USD' };
  try {
    const r = await fetch(`https://graph.facebook.com/v21.0/${PIXEL}/events?access_token=${encodeURIComponent(token)}`, {
      method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ data: [ev] }),
    });
    res.status(r.ok ? 200 : 502).end();
  } catch (e) { res.status(502).end(); }
};
