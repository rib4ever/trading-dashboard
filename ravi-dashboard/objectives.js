async function loadObjectiveStatus(){
  try{
    const r=await fetch('./data/objective_status.json',{cache:'no-store'});
    if(!r.ok)throw new Error('No objective status export yet');
    return await r.json();
  }catch(e){
    return null;
  }
}

function objMoney(v,currency){
  const n=Number(v)||0;
  const symbol=currency==='EUR'?'€':currency+' ';
  return `${n<0?'-':''}${symbol}${Math.abs(n).toFixed(2)}`;
}

function objPct(v){return `${Math.max(0,Math.min(Number(v)||0,999)).toFixed(0)}%`}
function objEsc(s){return String(s??'').replace(/[&<>\"]/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','\"':'&quot;'}[m]))}

function barHtml(label,value,level){
  const width=Math.max(0,Math.min(Number(value)||0,100));
  return `<div class="guardrail-bar-row"><span>${objEsc(label)}</span><b>${objPct(value)}</b><div class="guardrail-bar"><i class="${objEsc(level)}" style="width:${width}%"></i></div></div>`;
}

function periodCardHtml(period,currency){
  const level=period.level||'ok';
  const action=period.action||'CONTINUE';
  const notes=[...(period.breaches||[]),...(period.warnings||[])];
  return `<article class="guardrail-card ${objEsc(level)}">
    <div class="guardrail-card-head">
      <span>${objEsc(period.period||'Period')}</span>
      <strong>${objEsc(action)}</strong>
    </div>
    <div class="guardrail-metrics">
      <div><span>Net P/L</span><b class="${Number(period.net||0)>=0?'profit':'loss'}">${objMoney(period.net,currency)}</b></div>
      <div><span>Profit Target</span><b>${objMoney(period.profitTarget,currency)}</b></div>
      <div><span>Max Loss</span><b>${objMoney(period.maxLoss,currency)}</b></div>
      <div><span>Trades</span><b>${period.trades||0}/${period.maxTrades||0}</b></div>
      <div><span>Losing Trades</span><b>${period.losingTrades||0}/${period.maxLosingTrades||0}</b></div>
    </div>
    <div class="guardrail-bars">
      ${barHtml('Profit target',period.profitProgressPercent,period.profitTargetHit?'ok':level)}
      ${barHtml('Loss limit',period.lossProgressPercent,period.maxLossHit?'breached':level)}
      ${barHtml('Trade count',period.tradeProgressPercent,period.maxTradesHit?'breached':level)}
      ${barHtml('Losing trades',period.losingTradeProgressPercent,period.maxLosingTradesHit?'breached':level)}
    </div>
    <div class="guardrail-notes">${notes.length?notes.map(n=>`<p>${objEsc(n)}</p>`).join(''):'<p>Inside plan. Continue with discipline.</p>'}</div>
  </article>`;
}

function renderObjectives(status){
  let holder=document.getElementById('objectivesPanel');
  if(!holder){
    const filters=document.querySelector('.filter-bar');
    holder=document.createElement('section');
    holder.id='objectivesPanel';
    holder.className='objectives-panel';
    filters?.insertAdjacentElement('afterend',holder);
  }
  if(!status){
    holder.innerHTML=`<div class="guardrail-empty"><h2>Objectives & Risk Guardrails</h2><p>No objective status export yet. Run Ravi Full Pipeline once to generate daily, weekly and monthly target progress.</p></div>`;
    return;
  }
  const currency=status.currency||'EUR';
  const periods=status.periods||{};
  holder.innerHTML=`<div class="guardrail-title"><div><p class="eyebrow">Objectives & Risk Guardrails</p><h2>Trading Targets / Stop Rules</h2><p>Profile: ${objEsc(status.profile||'Default')} · Updated ${objEsc((status.generatedAt||'').slice(0,16).replace('T',' '))}</p></div><div class="guardrail-alert-pill">Telegram alerts: ${status.alerts?.telegramEnabled?'Enabled if secrets exist':'Disabled'}</div></div><div class="guardrail-grid">${['daily','weekly','monthly'].map(k=>periods[k]?periodCardHtml(periods[k],currency):'').join('')}</div>`;
}

loadObjectiveStatus().then(renderObjectives);
