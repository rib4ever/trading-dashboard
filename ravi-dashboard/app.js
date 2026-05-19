const demoTrades = [
  { date: '2026-05-01', pair: 'XAUUSD', direction: 'Buy', setup: 'SMC Sweep Reversal', session: 'New York', result: 'Win', net: 120, r: 1.8, rules: true, ai: 'Complete', mistakes: [] },
  { date: '2026-05-02', pair: 'XAUUSD', direction: 'Sell', setup: 'FVG Entry', session: 'London', result: 'Loss', net: -70, r: -1, rules: false, ai: 'Complete', mistakes: ['Early Entry'] },
  { date: '2026-05-03', pair: 'BTCUSD', direction: 'Sell', setup: 'SMC Continuation', session: 'New York', result: 'Win', net: 210, r: 2.4, rules: true, ai: 'Complete', mistakes: [] },
  { date: '2026-05-04', pair: 'NAS100', direction: 'Buy', setup: 'NCI Market Story', session: 'London + NY Overlap', result: 'Break Even', net: 0, r: 0, rules: true, ai: 'Not Requested', mistakes: [] },
  { date: '2026-05-05', pair: 'XAUUSD', direction: 'Buy', setup: 'OB Entry', session: 'London', result: 'Loss', net: -95, r: -1.2, rules: false, ai: 'Needs More Screenshots', mistakes: ['No Confirmation', 'Bad SL'] }
];

let charts = [];

async function loadTrades() {
  try {
    const res = await fetch('./data/trades.json', { cache: 'no-store' });
    if (!res.ok) throw new Error('No exported trades yet');
    const data = await res.json();
    return Array.isArray(data.trades) && data.trades.length ? data.trades : demoTrades;
  } catch {
    return demoTrades;
  }
}

function filterTrades(trades) {
  const mode = document.getElementById('periodFilter').value;
  if (mode === 'all') return trades;
  const now = new Date();
  const days = mode === 'week' ? 7 : 31;
  const cutoff = new Date(now.getTime() - days * 86400000);
  return trades.filter(t => new Date(t.date) >= cutoff);
}

function money(v) { return `${v >= 0 ? '$' : '-$'}${Math.abs(v).toFixed(2)}`; }
function pct(v) { return `${v.toFixed(1)}%`; }

function metrics(trades) {
  const completed = trades.filter(t => t.result);
  const wins = completed.filter(t => String(t.result).toLowerCase().includes('win'));
  const totalNet = completed.reduce((s, t) => s + Number(t.net || t['Net P/L'] || 0), 0);
  const avgR = completed.length ? completed.reduce((s, t) => s + Number(t.r || t['Result R'] || 0), 0) / completed.length : 0;
  const ruleRate = completed.length ? completed.filter(t => t.rules === true || t['Followed Rules'] === true).length / completed.length * 100 : 0;
  const byPair = groupSum(completed, 'pair', 'net');
  const bestPair = Object.entries(byPair).sort((a,b) => b[1]-a[1])[0]?.[0] || '-';
  return { completed, wins, totalNet, avgR, ruleRate, bestPair, winRate: completed.length ? wins.length / completed.length * 100 : 0 };
}

function groupSum(trades, key, valueKey) {
  return trades.reduce((acc, t) => {
    const k = t[key] || t[key[0].toUpperCase() + key.slice(1)] || 'Unknown';
    const v = Number(t[valueKey] || t['Net P/L'] || 0);
    acc[k] = (acc[k] || 0) + v;
    return acc;
  }, {});
}

function groupCount(trades, key) {
  return trades.reduce((acc, t) => {
    const raw = t[key] || [];
    const vals = Array.isArray(raw) ? raw : [raw || 'None'];
    vals.forEach(v => acc[v] = (acc[v] || 0) + 1);
    return acc;
  }, {});
}

function destroyCharts() { charts.forEach(c => c.destroy()); charts = []; }
function chartColors(values) { return values.map(v => v >= 0 ? '#22c55e' : '#ef4444'); }

function renderCharts(trades) {
  destroyCharts();
  const sorted = [...trades].sort((a,b) => new Date(a.date) - new Date(b.date));
  let cumulative = 0;
  const equity = sorted.map(t => cumulative += Number(t.net || 0));
  charts.push(new Chart(document.getElementById('equityChart'), { type: 'line', data: { labels: sorted.map(t => t.date), datasets: [{ label: 'Equity', data: equity, borderColor: '#3b82f6', backgroundColor: 'rgba(59,130,246,.18)', tension: .35, fill: true }] }, options: chartOptions() }));

  const winLoss = { Win: trades.filter(t => String(t.result).includes('Win')).length, Loss: trades.filter(t => String(t.result).includes('Loss')).length, BE: trades.filter(t => String(t.result).includes('Break')).length };
  charts.push(new Chart(document.getElementById('winLossChart'), { type: 'doughnut', data: { labels: Object.keys(winLoss), datasets: [{ data: Object.values(winLoss), backgroundColor: ['#22c55e', '#ef4444', '#94a3b8'] }] }, options: chartOptions() }));

  renderBar('pairChart', groupSum(trades, 'pair', 'net'));
  renderBar('setupChart', groupSum(trades, 'setup', 'net'));
  renderBar('sessionChart', groupSum(trades, 'session', 'net'));
  renderBar('mistakeChart', groupCount(trades, 'mistakes'));
}

function renderBar(id, obj) {
  const labels = Object.keys(obj);
  const values = Object.values(obj);
  charts.push(new Chart(document.getElementById(id), { type: 'bar', data: { labels, datasets: [{ data: values, backgroundColor: chartColors(values), borderRadius: 8 }] }, options: chartOptions() }));
}

function chartOptions() {
  return { responsive: true, plugins: { legend: { display: false } }, scales: { x: { ticks: { color: '#8c99ad' }, grid: { color: 'rgba(255,255,255,.05)' } }, y: { ticks: { color: '#8c99ad' }, grid: { color: 'rgba(255,255,255,.05)' } } } };
}

function renderTable(trades) {
  document.getElementById('tradeRows').innerHTML = trades.map(t => {
    const net = Number(t.net || 0);
    return `<tr><td>${t.date || ''}</td><td>${t.pair || ''}</td><td>${t.direction || ''}</td><td>${t.setup || ''}</td><td>${t.session || ''}</td><td><span class="badge">${t.result || ''}</span></td><td class="${net >= 0 ? 'profit' : 'loss'}">${money(net)}</td><td>${Number(t.r || 0).toFixed(2)}R</td><td>${t.rules ? '✅' : '⚠️'}</td><td>${t.ai || '-'}</td></tr>`;
  }).join('');
}

async function render() {
  const all = await loadTrades();
  const trades = filterTrades(all);
  const m = metrics(trades);
  document.getElementById('netProfit').textContent = money(m.totalNet);
  document.getElementById('winRate').textContent = pct(m.winRate);
  document.getElementById('totalTrades').textContent = m.completed.length;
  document.getElementById('averageR').textContent = `${m.avgR.toFixed(2)}R`;
  document.getElementById('bestPair').textContent = m.bestPair;
  document.getElementById('ruleRate').textContent = pct(m.ruleRate);
  renderCharts(trades);
  renderTable(trades);
}

document.getElementById('themeSelect').addEventListener('change', e => document.body.dataset.theme = e.target.value);
document.getElementById('periodFilter').addEventListener('change', render);
render();
