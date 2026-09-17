js_code = '''/* ===== STATE ===== */
let state = {
  theme: 'dark',
  city: 'Karachi',
  country: 'Pakistan',
  lat: 24.8607,
  lng: 67.0011,
  method: 1,
  times: null,
  hijri: null,
  timer: null
};

const METHODS = {1:'Karachi (Univ. of Islamic Sciences)',2:'ISNA (North America)',3:'Muslim World League',4:'Umm Al-Qura, Makkah',5:'Egyptian General Authority'};

/* ===== INIT ===== */
function init(){
  loadState();
  applyTheme();
  loadPrayerTimes();
}

function loadState(){
  try{
    const s = localStorage.getItem('prayer_v1');
    if(s){
      const p = JSON.parse(s);
      state.theme = p.theme || 'dark';
      state.city = p.city || 'Karachi';
      state.country = p.country || 'Pakistan';
      state.lat = p.lat || 24.8607;
      state.lng = p.lng || 67.0011;
      state.method = p.method || 1;
    }
  }catch(e){}
  updateSettingsUI();
}

function saveState(){
  try{
    localStorage.setItem('prayer_v1', JSON.stringify({
      theme: state.theme, city: state.city, country: state.country,
      lat: state.lat, lng: state.lng, method: state.method
    }));
  }catch(e){}
}

function updateSettingsUI(){
  const citySub = document.getElementById('citySub');
  const methodSub = document.getElementById('methodSub');
  if(citySub) citySub.textContent = 'Current: ' + state.city;
  if(methodSub) methodSub.textContent = METHODS[state.method] || METHODS[1];
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

/* ===== LOAD PRAYER TIMES ===== */
async function loadPrayerTimes(){
  const today = new Date();
  const day = String(today.getDate()).padStart(2,'0');
  const month = String(today.getMonth()+1).padStart(2,'0');
  const year = today.getFullYear();
  const dateStr = day + '-' + month + '-' + year;

  const container = document.getElementById('todayContent');
  container.innerHTML = '<div class="loading"><div class="spinner"></div><p>Loading prayer times...</p></div>';

  try{
    const url = 'https://api.aladhan.com/v1/timings/' + dateStr + '?latitude=' + state.lat + '&longitude=' + state.lng + '&method=' + state.method;
    const res = await fetch(url);
    if(!res.ok) throw new Error('Network error');
    const data = await res.json();
    if(!data.data || !data.data.timings) throw new Error('Invalid data');

    state.times = data.data.timings;
    state.hijri = data.data.date.hijri;
    renderToday();
    startCountdown();
  } catch(err){
    console.error(err);
    container.innerHTML = '<div class="error-box"><p>Failed to load prayer times. Check internet connection.</p><button onclick="loadPrayerTimes()">Retry</button></div>';
  }
}

/* ===== RENDER TODAY ===== */
function renderToday(){
  const t = state.times;
  const h = state.hijri;
  const now = new Date();

  const prayerList = [
    {name:'Fajr', arabic:'الفجر', icon:'🌅', time:t.Fajr},
    {name:'Sunrise', arabic:'الشروق', icon:'☀️', time:t.Sunrise, skip:true},
    {name:'Dhuhr', arabic:'الظهر', icon:'🌞', time:t.Dhuhr},
    {name:'Asr', arabic:'العصر', icon:'🌤️', time:t.Asr},
    {name:'Maghrib', arabic:'المغرب', icon:'🌇', time:t.Maghrib},
    {name:'Isha', arabic:'العشاء', icon:'🌙', time:t.Isha}
  ];

  // Find next prayer
  const next = findNextPrayer(prayerList);
  const nextInfo = next || prayerList[0];

  const hijriDay = h ? h.day : '';
  const hijriMonth = h ? h.month.en : '';
  const hijriYear = h ? h.year : '';

  let html = '<div class="hero">';
  html += '<div class="hero-hijri">';
  if(hijriDay){
    html += '<span class="h-day">' + hijriDay + '</span>' + hijriMonth + '<br>' + hijriYear + ' AH';
  }
  html += '</div>';
  html += '<div class="hero-content">';
  html += '<div class="hero-location"><svg viewBox="0 0 24 24"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg>' + state.country + '</div>';
  html += '<div class="hero-city">' + state.city + '</div>';
  html += '<div class="hero-next-label">Next Prayer</div>';
  html += '<div class="hero-next-name">' + nextInfo.name + '</div>';
  html += '<div class="hero-next-time">' + nextInfo.time + '</div>';
  html += '<div class="hero-countdown" id="countdown">Calculating...</div>';
  html += '</div></div>';

  html += '<div class="prayers-title">Today\\'s Schedule</div>';
  html += '<div class="prayer-list">';
  prayerList.forEach(p => {
    const isNext = nextInfo.name === p.name;
    const isSkipped = p.skip;
    html += '<div class="prayer-card' + (isNext && !isSkipped ? ' active' : '') + '">';
    html += '<div class="prayer-icon">' + p.icon + '</div>';
    html += '<div class="prayer-info">';
    html += '<div class="prayer-name">' + p.name + (isSkipped ? ' <span style="font-size:10px;color:var(--text-subtle)">(not a prayer)</span>' : '') + '</div>';
    html += '<div class="prayer-arabic">' + p.arabic + '</div>';
    html += '</div>';
    html += '<div class="prayer-time">' + p.time + '</div>';
    html += '</div>';
  });
  html += '</div>';

  document.getElementById('todayContent').innerHTML = html;
}

/* ===== FIND NEXT PRAYER ===== */
function findNextPrayer(list){
  const now = new Date();
  const nowMins = now.getHours() * 60 + now.getMinutes();
  for(let i = 0; i < list.length; i++){
    const p = list[i];
    if(p.skip) continue;
    const [hh, mm] = p.time.split(':').map(Number);
    const pMins = hh * 60 + mm;
    if(pMins > nowMins) return p;
  }
  return list.find(p => !p.skip);
}

/* ===== COUNTDOWN ===== */
function startCountdown(){
  if(state.timer) clearInterval(state.timer);
  updateCountdown();
  state.timer = setInterval(updateCountdown, 1000);
}

function updateCountdown(){
  const el = document.getElementById('countdown');
  if(!el || !state.times) return;

  const list = [
    {name:'Fajr', time:state.times.Fajr},
    {name:'Dhuhr', time:state.times.Dhuhr},
    {name:'Asr', time:state.times.Asr},
    {name:'Maghrib', time:state.times.Maghrib},
    {name:'Isha', time:state.times.Isha}
  ];

  const next = findNextPrayer(list.map(p => ({...p, skip:false})));
  if(!next) return;

  const [hh, mm] = next.time.split(':').map(Number);
  const target = new Date();
  target.setHours(hh, mm, 0, 0);

  const diff = target - new Date();
  if(diff < 0){
    el.textContent = 'Now';
    return;
  }

  const hours = Math.floor(diff / 3600000);
  const mins = Math.floor((diff % 3600000) / 60000);
  const secs = Math.floor((diff % 60000) / 1000);

  el.textContent = 'in ' + hours + 'h ' + mins + 'm ' + secs + 's';
}

/* ===== MONTH VIEW ===== */
async function loadMonth(){
  const container = document.getElementById('monthContent');
  container.innerHTML = '<div class="loading"><div class="spinner"></div><p>Loading month...</p></div>';

  const now = new Date();
  const month = now.getMonth() + 1;
  const year = now.getFullYear();
  const todayDate = now.getDate();

  try{
    const url = 'https://api.aladhan.com/v1/calendar/' + year + '/' + month + '?latitude=' + state.lat + '&longitude=' + state.lng + '&method=' + state.method;
    const res = await fetch(url);
    if(!res.ok) throw new Error('Network error');
    const data = await res.json();
    if(!data.data) throw new Error('Invalid data');

    const days = data.data;
    let html = '<div class="month-row header"><div>Date</div><div>Fajr</div><div>Dhuhr</div><div>Asr</div><div>Maghrib</div><div>Isha</div></div>';

    days.forEach((d, i) => {
      const day = i + 1;
      const isToday = day === todayDate;
      const t = d.timings;
      html += '<div class="month-row' + (isToday ? ' today' : '') + '">';
      html += '<div class="month-day">' + day + '</div>';
      html += '<div class="month-time">' + t.Fajr.slice(0,5) + '</div>';
      html += '<div class="month-time">' + t.Dhuhr.slice(0,5) + '</div>';
      html += '<div class="month-time">' + t.Asr.slice(0,5) + '</div>';
      html += '<div class="month-time">' + t.Maghrib.slice(0,5) + '</div>';
      html += '<div class="month-time">' + t.Isha.slice(0,5) + '</div>';
      html += '</div>';
    });

    container.innerHTML = html;
  } catch(err){
    console.error(err);
    container.innerHTML = '<div class="error-box"><p>Failed to load monthly times.</p><button onclick="loadMonth()">Retry</button></div>';
  }
}

/* ===== SETTINGS ===== */
function saveCity(){
  const input = document.getElementById('cityInput').value.trim();
  if(!input){
    showToast('Enter a city name');
    return;
  }
  geocodeCity(input);
}

async function geocodeCity(city){
  const container = document.getElementById('todayContent');
  showToast('Searching...');
  try{
    const url = 'https://nominatim.openstreetmap.org/search?format=json&q=' + encodeURIComponent(city) + '&limit=1';
    const res = await fetch(url, {headers:{'Accept':'application/json'}});
    const data = await res.json();
    if(!data || data.length === 0){
      showToast('City not found');
      return;
    }
    const place = data[0];
    state.city = place.display_name.split(',')[0];
    state.country = place.display_name.split(',').slice(-1)[0].trim();
    state.lat = parseFloat(place.lat);
    state.lng = parseFloat(place.lon);
    saveState();
    updateSettingsUI();
    showToast('City updated');
    switchView('today');
    loadPrayerTimes();
  } catch(err){
    showToast('Search failed');
  }
}

function useGPS(){
  if(!navigator.geolocation){
    showToast('GPS not available');
    return;
  }
  showToast('Getting location...');
  navigator.geolocation.getCurrentPosition(
    async (pos) => {
      state.lat = pos.coords.latitude;
      state.lng = pos.coords.longitude;
      try{
        const url = 'https://nominatim.openstreetmap.org/reverse?format=json&lat=' + state.lat + '&lon=' + state.lng;
        const res = await fetch(url);
        const data = await res.json();
        if(data && data.address){
          state.city = data.address.city || data.address.town || data.address.village || 'My Location';
          state.country = data.address.country || '';
          updateSettingsUI();
        }
      }catch(e){}
      saveState();
      showToast('Location updated');
      switchView('today');
      loadPrayerTimes();
    },
    (err) => showToast('Location permission denied'),
    {timeout: 10000}
  );
}

/* ===== VIEWS ===== */
function switchView(view){
  document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));
  document.getElementById('view-' + view).classList.add('active');
  document.querySelectorAll('.nav-item').forEach(b => {
    b.classList.toggle('active', b.dataset.view === view);
  });
  const titles = {today:'Prayer Times', month:'Monthly', settings:'Settings'};
  document.getElementById('headerTitle').textContent = titles[view] || 'Prayer Times';
  document.getElementById('mainArea').scrollTo({top:0});

  if(view === 'month' && document.querySelector('#monthContent .loading')){
    loadMonth();
  }
}

/* ===== TOAST ===== */
let toastTimer;
function showToast(msg){
  const t = document.getElementById('toast');
  document.getElementById('toastText').textContent = msg;
  t.classList.add('show');
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => t.classList.remove('show'), 2000);
}

init();'''

with open('templates/prayer.html') as f:
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

with open('templates/prayer.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Total size:', len(content))
