(() => {
  let phase2Trades = [];
  const money = (v) => {
    const n = Number(v) || 0;
    return `${n < 0 ? '-' : ''}€${Math.abs(n).toFixed(2)}`;
  };
  const hasTradeResult = (t) => !['Incomplete', '', null, undefined].includes(t.result);
  const isCompleted = (t) => hasTradeResult(t) && (Number.isFinite(Number(t.net)) || Number.isFinite(Number(t.gross)));
  const dateKey = (d) => String(d || '').slice(0, 10);

  async function loadPhase2Trades() {
    try {
      const res = await fetch('./data/trades.json', { cache: 'no-store' });
      const data = await res.json();
      phase2Trades = Array.isArray(data.trades) ? data.trades : [];
    } catch {
      phase2Trades = [];
    }
  }

  function filterByUi(trades) {
    let out = [...trades];
    const period = document.getElementById('periodFilter')?.value || 'all';
    if (period !== 'all') {
      const days = period === 'week' ? 7 : 31;
      out = out.filter((t) => new Date(t.date) >= new Date(Date.now() - days * 86400000));
    }
    const pair = document.getElementById('pairFilter')?.value || 'all';
    const session = document.getElementById('sessionFilter')?.value || 'all';
    const setup = document.getElementById('setupFilter')?.value || 'all';
    const result = document.getElementById('resultFilter')?.value || 'all';
    const from = document.getElementById('dateFrom')?.value || '';
    const to = document.getElementById('dateTo')?.value || '';
    if (pair !== 'all') out = out.filter((t) => t.pair === pair);
    if (session !== 'all') out = out.filter((t) => t.session === session);
    if (setup !== 'all') out = out.filter((t) => t.setup === setup);
    if (result !== 'all') out = out.filter((t) => String(t.result || 'Incomplete').includes(result));
    if (from) out = out.filter((t) => dateKey(t.date) >= from);
    if (to) out = out.filter((t) => dateKey(t.date) <= to);
    return out;
  }

  function groupNetByDay(trades) {
    return trades.filter(isCompleted).reduce((acc, t) => {
      const k = dateKey(t.date);
      acc[k] = (acc[k] || 0) + Number(t.net || 0);
      return acc;
    }, {});
  }

  function groupNet(trades, key) {
    return trades.filter(isCompleted).reduce((acc, t) => {
      const k = t[key] || 'Unknown';
      acc[k] = (acc[k] || 0) + Number(t.net || 0);
      return acc;
    }, {});
  }

  function setText(id, value) {
    const el = document.getElementById(id);
    if (el) el.textContent = value;
  }

  function updateInsightCards() {
    const filtered = filterByUi(phase2Trades);
    const completed = filtered.filter(isCompleted);
    const byDay = Object.entries(groupNetByDay(filtered)).sort((a, b) => b[1] - a[1]);
    const bestDay = byDay[0];
    const worstDay = [...byDay].sort((a, b) => a[1] - b[1])[0];
    setText('bestDay', bestDay ? money(bestDay[1]) : '-');
    setText('bestDayNote', bestDay ? bestDay[0] : 'No completed day yet');
    setText('worstDay', worstDay ? money(worstDay[1]) : '-');
    setText('worstDayNote', worstDay ? worstDay[0] : 'No completed day yet');

    const bySession = Object.entries(groupNet(filtered, 'session')).sort((a, b) => b[1] - a[1]);
    setText('bestSessionInsight', bySession[0] ? bySession[0][0] : '-');

    const readyCount = filtered.filter((t) => t.dashboardReady === true).length;
    const readiness = filtered.length ? Math.round((readyCount / filtered.length) * 100) : 0;
    setText('readinessScore', `${readiness}%`);
    setText('readinessNote', `${readyCount}/${filtered.length} trades dashboard-ready`);

    const note = document.getElementById('proSuggestion');
    if (note) {
      if (filtered.length < 10) note.textContent = 'Build at least 10 completed trades to start seeing useful performance patterns. Keep entries consistent: price, lot, screenshots, result, and rule-follow status.';
      else if (readiness < 90) note.textContent = 'Some trades are not dashboard-ready. Complete missing execution fields and screenshot sync to keep analytics reliable.';
      else if (completed.length >= 20) note.textContent = 'You now have enough trades to start optimizing by setup, session, and mistake frequency. Next focus: risk consistency and MT5 execution import.';
      else note.textContent = 'Good progress. Continue collecting clean data and screenshots so the AI review and dashboard statistics become more reliable.';
    }

    const pills = document.getElementById('quickPills');
    if (pills) {
      const wins = completed.filter((t) => String(t.result).includes('Win')).length;
      const losses = completed.filter((t) => String(t.result).includes('Loss')).length;
      const screenshots = filtered.reduce((s, t) => s + ((t.screenshots || []).length || 0), 0);
      pills.innerHTML = [
        `${completed.length} P/L trades`,
        `${wins} wins`,
        `${losses} losses`,
        `${screenshots} screenshots`,
        `${readiness}% ready`
      ].map((x) => `<span class="quick-pill">${x}</span>`).join('');
    }
  }

  function patchDateFiltering() {
    const originalFilterTrades = window.filterTrades;
    if (typeof originalFilterTrades === 'function' && !window.__raviDateFilterPatched) {
      window.filterTrades = function(trades) {
        let out = originalFilterTrades(trades);
        const from = document.getElementById('dateFrom')?.value || '';
        const to = document.getElementById('dateTo')?.value || '';
        if (from) out = out.filter((t) => dateKey(t.date) >= from);
        if (to) out = out.filter((t) => dateKey(t.date) <= to);
        return out;
      };
      window.__raviDateFilterPatched = true;
    }
  }

  function patchRender() {
    const originalRender = window.render;
    if (typeof originalRender === 'function' && !window.__raviPhase2RenderPatched) {
      window.render = async function() {
        await originalRender();
        await loadPhase2Trades();
        updateInsightCards();
      };
      window.__raviPhase2RenderPatched = true;
    }
  }

  function init() {
    patchDateFiltering();
    patchRender();
    ['dateFrom', 'dateTo'].forEach((id) => {
      document.getElementById(id)?.addEventListener('change', () => window.render?.());
    });
    document.getElementById('resetFilters')?.addEventListener('click', () => {
      const from = document.getElementById('dateFrom');
      const to = document.getElementById('dateTo');
      if (from) from.value = '';
      if (to) to.value = '';
      window.render?.();
    });
    loadPhase2Trades().then(updateInsightCards);
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
