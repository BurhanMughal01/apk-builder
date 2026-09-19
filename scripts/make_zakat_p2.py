js_code = '''/* ===== STATE ===== */
let state = {
  theme: 'dark',
  history: [],
  nisabSilver: 179689,
  nisabGold: 1245000
};

/* ===== INIT ===== */
function init(){
  loadState();
  applyTheme();
  calc();
  renderHistory();
}

function loadState(){
  try{
    const s = localStorage.getItem('zakat_v1');
    if(s){
      const p = JSON.parse(s);
      state.theme = p.theme || 'dark';
      state.history = p.history || [];
    }
  }catch(e){}
}

function saveState(){
  try{
    localStorage.setItem('zakat_v1', JSON.stringify({
      theme: state.theme,
      history: state.history
    }));
  }catch(e){}
}

/* ===== THEME ===== */
function applyTheme(){
  document.body.setAttribute('data-theme', state.theme);
  const icon = document.getElementById('themeIcon');
  if(icon){
    if(state.theme === 'dark'){
      icon.innerHTML = '<circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/>';
    } else {
      icon.innerHTML = '<path d="M21 12.79A9 9 0 1111.21 3 7 7 0 0021 12.79z"/>';
    }
  }
}

function toggleTheme(){
  state.theme = state.theme === 'dark' ? 'light' : 'dark';
  applyTheme();
  saveState();
}

/* ===== CALCULATION ===== */
function getVal(id){
  const el = document.getElementById(id);
  if(!el) return 0;
  const v = parseFloat(el.value);
  return isNaN(v) ? 0 : v;
}

function formatNum(n){
  return Math.round(n).toLocaleString('en-PK');
}

function shortNum(n){
  if(n >= 10000000) return (n/10000000).toFixed(1) + 'Cr';
  if(n >= 100000) return (n/100000).toFixed(1) + 'L';
  if(n >= 1000) return (n/1000).toFixed(1) + 'K';
  return Math.round(n).toString();
}

function calc(){
  const cash = getVal('cash');
  const gold = getVal('gold');
  const silver = getVal('silver');
  const business = getVal('business');
  const invest = getVal('invest');
  const property = getVal('property');
  const debt = getVal('debt');
  const bills = getVal('bills');

  const assets = cash + gold + silver + business + invest + property;
  const liabilities = debt + bills;
  const net = assets - liabilities;
  const nisab = state.nisabSilver;
  const zakat = net >= nisab ? net * 0.025 : 0;

  document.getElementById('zakatAmount').textContent = 'PKR ' + formatNum(zakat);
  document.getElementById('assetsTotal').textContent = shortNum(assets);
  document.getElementById('liabilitiesTotal').textContent = shortNum(liabilities);
  document.getElementById('netWealth').textContent = shortNum(net);
  document.getElementById('nisabValue').textContent = 'PKR ' + formatNum(nisab);

  const status = document.getElementById('nisabStatus');
  if(net >= nisab){
    status.textContent = 'ABOVE';
    status.classList.remove('below');
    status.classList.add('above');
  } else {
    status.textContent = 'BELOW';
    status.classList.remove('above');
    status.classList.add('below');
  }
}

/* ===== RESET ===== */
function resetCalc(){
  if(!confirm('Clear all input values?')) return;
  ['cash','gold','silver','business','invest','property','debt','bills'].forEach(id => {
    document.getElementById(id).value = 0;
  });
  calc();
  showToast('Cleared');
}

/* ===== SAVE ===== */
function saveCalculation(){
  const cash = getVal('cash');
  const gold = getVal('gold');
  const silver = getVal('silver');
  const business = getVal('business');
  const invest = getVal('invest');
  const property = getVal('property');
  const debt = getVal('debt');
  const bills = getVal('bills');

  const assets = cash + gold + silver + business + invest + property;
  const liabilities = debt + bills;
  const net = assets - liabilities;

  if(net <= 0){
    showToast('Nothing to save');
    return;
  }

  const nisab = state.nisabSilver;
  const zakat = net >= nisab ? net * 0.025 : 0;

  state.history.unshift({
    id: Date.now(),
    date: new Date().toISOString(),
    assets: assets,
    liabilities: liabilities,
    net: net,
    zakat: zakat
  });

  if(state.history.length > 30) state.history = state.history.slice(0, 30);
  saveState();
  renderHistory();
  showToast('Saved to history');
}

function renderHistory(){
  const el = document.getElementById('historyList');
  if(!el) return;

  if(state.history.length === 0){
    el.innerHTML = '<div class="empty"><svg viewBox="0 0 24 24"><path d="M3 3v18h18"/><path d="M18 9l-5 5-3-3-4 4"/></svg><h3>No saved calculations</h3><p>Calculate and save to see history here</p></div>';
    return;
  }

  el.innerHTML = state.history.map(h => {
    const date = new Date(h.date);
    const dateStr = date.toLocaleDateString('en-PK', {day:'numeric', month:'short', year:'numeric'}) + ' · ' + date.toLocaleTimeString('en-PK', {hour:'2-digit', minute:'2-digit'});
    return '<div class="history-item">' +
      '<div class="history-info">' +
        '<div class="history-amount">PKR ' + formatNum(h.zakat) + '</div>' +
        '<div class="history-date">' + dateStr + ' · Net: ' + shortNum(h.net) + '</div>' +
      '</div>' +
      '<button class="history-delete" onclick="deleteHistory(' + h.id + ')">' +
        '<svg viewBox="0 0 24 24"><path d="M3 6h18M8 6V4a2 2 0 012-2h4a2 2 0 012 2v2M19 6v14a2 2 0 01-2 2H7a2 2 0 01-2-2V6"/></svg>' +
      '</button>' +
    '</div>';
  }).join('');
}

function deleteHistory(id){
  if(!confirm('Delete this entry?')) return;
  state.history = state.history.filter(h => h.id !== id);
  saveState();
  renderHistory();
  showToast('Deleted');
}

/* ===== VIEWS ===== */
function switchView(view){
  document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));
  document.getElementById('view-' + view).classList.add('active');
  document.querySelectorAll('.nav-item').forEach(b => {
    b.classList.toggle('active', b.dataset.view === view);
  });
  const titles = {calc:'Zakat Calculator', guide:'Zakat Guide', history:'History'};
  document.getElementById('headerTitle').textContent = titles[view] || 'Zakat';
  document.getElementById('mainArea').scrollTo({top:0});
}

/* ===== TOAST ===== */
let toastTimer;
function showToast(msg){
  const t = document.getElementById('toast');
  document.getElementById('toastText').textContent = msg;
  t.classList.add('show');
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => t.classList.remove('show'), 1800);
}

/* ===== START ===== */
init();'''

with open('templates/zakat.html') as f:
    content = f.read()

old = '''<script>
/* PART 2 WILL BE INJECTED */
</script>'''

new = '<script>\n' + js_code + '\n</script>'

if old in content:
    content = content.replace(old, new)
    print('Injected OK')
else:
    print('Placeholder not found!')

with open('templates/zakat.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Total size:', len(content), 'bytes')
