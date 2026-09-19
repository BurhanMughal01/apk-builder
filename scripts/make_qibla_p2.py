js_code = '''/* ===== STATE ===== */
const KAABA_LAT = 21.4225;
const KAABA_LNG = 39.8262;

let state = {
  theme: 'dark',
  lat: 24.8607,
  lng: 67.0011,
  city: 'Karachi',
  country: 'Pakistan',
  qiblaBearing: 0,
  distance: 0,
  deviceHeading: 0,
  hasSensor: false,
  lastAligned: false,
  smoothHeading: null
};

/* ===== INIT ===== */
function init(){
  loadState();
  applyTheme();
  buildTicks();
  calculateQibla();
  updateUI();
  setupSensors();
}

function loadState(){
  try{
    const s = localStorage.getItem('qibla_v1');
    if(s){
      const p = JSON.parse(s);
      state.theme = p.theme || 'dark';
      state.lat = p.lat || 24.8607;
      state.lng = p.lng || 67.0011;
      state.city = p.city || 'Karachi';
      state.country = p.country || 'Pakistan';
    }
  }catch(e){}
  const citySub = document.getElementById('citySub');
  if(citySub) citySub.textContent = 'Current: ' + state.city;
}

function saveState(){
  try{
    localStorage.setItem('qibla_v1', JSON.stringify({
      theme: state.theme, lat: state.lat, lng: state.lng,
      city: state.city, country: state.country
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

/* ===== BUILD COMPASS TICKS ===== */
function buildTicks(){
  const inner = document.getElementById('compassInner');
  if(!inner) return;
  const size = inner.offsetWidth || 300;
  const radius = size / 2;
  for(let deg = 0; deg < 360; deg += 15){
    const tick = document.createElement('div');
    tick.className = 'tick' + (deg % 45 === 0 ? ' major' : '');
    tick.style.transform = 'rotate(' + deg + 'deg)';
    tick.style.height = (deg % 45 === 0 ? '14px' : '8px');
    inner.appendChild(tick);
  }
}

/* ===== CALCULATE QIBLA DIRECTION ===== */
function calculateQibla(){
  const lat1 = state.lat * Math.PI / 180;
  const lat2 = KAABA_LAT * Math.PI / 180;
  const dLng = (KAABA_LNG - state.lng) * Math.PI / 180;

  const y = Math.sin(dLng);
  const x = Math.cos(lat1) * Math.tan(lat2) - Math.sin(lat1) * Math.cos(dLng);

  let bearing = Math.atan2(y, x) * 180 / Math.PI;
  bearing = (bearing + 360) % 360;
  state.qiblaBearing = bearing;

  // Distance using Haversine
  const R = 6371;
  const dLat = lat2 - lat1;
  const a = Math.sin(dLat/2) * Math.sin(dLat/2) +
            Math.cos(lat1) * Math.cos(lat2) *
            Math.sin(dLng/2) * Math.sin(dLng/2);
  const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
  state.distance = Math.round(R * c);
}

/* ===== SENSOR SETUP ===== */
function setupSensors(){
  if(typeof DeviceOrientationEvent === 'undefined'){
    document.getElementById('statusText').textContent = 'Compass not supported';
    document.getElementById('calibWarning').classList.add('show');
    return;
  }

  // iOS 13+ permission
  if(typeof DeviceOrientationEvent.requestPermission === 'function'){
    const btn = document.getElementById('statusText');
    btn.textContent = 'Tap to enable compass';
    const badge = btn.parentElement;
    badge.style.cursor = 'pointer';
    badge.onclick = async () => {
      try{
        const permission = await DeviceOrientationEvent.requestPermission();
        if(permission === 'granted'){
          startListening();
          badge.onclick = null;
          badge.style.cursor = 'default';
        } else {
          btn.textContent = 'Permission denied';
        }
      }catch(err){
        btn.textContent = 'Permission error';
      }
    };
  } else {
    startListening();
  }
}

function startListening(){
  window.addEventListener('deviceorientationabsolute', handleOrientation, true);
  window.addEventListener('deviceorientation', handleOrientation, true);
}

function handleOrientation(e){
  let heading = null;

  if(e.webkitCompassHeading !== undefined && e.webkitCompassHeading !== null){
    heading = e.webkitCompassHeading;
  } else if(e.alpha !== null){
    heading = 360 - e.alpha;
  }

  if(heading === null) return;

  state.hasSensor = true;

  // Smooth the heading
  if(state.smoothHeading === null){
    state.smoothHeading = heading;
  } else {
    const diff = ((heading - state.smoothHeading + 540) % 360) - 180;
    state.smoothHeading = (state.smoothHeading + diff * 0.15 + 360) % 360;
  }

  state.deviceHeading = state.smoothHeading;
  updateUI();

  // Check alignment
  const qiblaRelative = (state.qiblaBearing - state.deviceHeading + 360) % 360;
  const diff = Math.min(qiblaRelative, 360 - qiblaRelative);
  const isAligned = diff < 5;

  if(isAligned && !state.lastAligned){
    showAligned();
    state.lastAligned = true;
    if(navigator.vibrate) navigator.vibrate([100, 50, 100]);
  } else if(!isAligned && state.lastAligned){
    hideAligned();
    state.lastAligned = false;
  }
}

/* ===== UPDATE UI ===== */
function updateUI(){
  // Qibla angle text
  document.getElementById('qiblaAngle').textContent = state.qiblaBearing.toFixed(1) + '°';

  // Distance
  if(state.distance > 0){
    if(state.distance > 1000){
      document.getElementById('distanceVal').textContent = (state.distance / 1000).toFixed(2) + 'k km';
    } else {
      document.getElementById('distanceVal').textContent = state.distance + ' km';
    }
  }

  // Location
  document.getElementById('locCity').textContent = state.city + (state.country ? ', ' + state.country : '');
  document.getElementById('locCoords').textContent = state.lat.toFixed(4) + '°, ' + state.lng.toFixed(4) + '°';

  // Rotate compass dial (opposite of device heading)
  const compassInner = document.getElementById('compassInner');
  if(compassInner){
    compassInner.style.transform = 'rotate(' + (-state.deviceHeading) + 'deg)';
  }

  // Rotate needle (point to Qibla relative to device)
  const needle = document.getElementById('needle');
  if(needle){
    const qiblaRelative = (state.qiblaBearing - state.deviceHeading + 360) % 360;
    needle.style.transform = 'rotate(' + qiblaRelative + 'deg)';
  }

  // Rotate kaaba marker (same as needle)
  const kaabaMarker = document.getElementById('kaabaMarker');
  if(kaabaMarker){
    const qiblaRelative = (state.qiblaBearing - state.deviceHeading + 360) % 360;
    kaabaMarker.style.transform = 'rotate(' + qiblaRelative + 'deg)';
  }

  // Status text
  const statusText = document.getElementById('statusText');
  if(statusText){
    if(state.hasSensor){
      statusText.textContent = 'Compass active · ' + Math.round(state.deviceHeading) + '°';
    } else {
      statusText.textContent = 'Waiting for compass sensor...';
    }
  }
}

/* ===== ALIGNED FEEDBACK ===== */
function showAligned(){
  const el = document.getElementById('alignedToast');
  if(el) el.classList.add('show');
}

function hideAligned(){
  const el = document.getElementById('alignedToast');
  if(el) el.classList.remove('show');
}

/* ===== LOCATION ===== */
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
        const res = await fetch(url, {headers:{'Accept': 'application/json'}});
        const data = await res.json();
        if(data && data.address){
          state.city = data.address.city || data.address.town || data.address.village || 'My Location';
          state.country = data.address.country || '';
        }
      }catch(e){}

      calculateQibla();
      saveState();
      loadState();
      updateUI();
      showToast('Location updated');
    },
    (err) => showToast('Location denied'),
    {timeout: 10000, enableHighAccuracy: true}
  );
}

function saveCity(){
  const input = document.getElementById('cityInput');
  const city = input.value.trim();
  if(!city){
    showToast('Enter a city name');
    return;
  }
  geocodeCity(city);
}

async function geocodeCity(city){
  showToast('Searching...');
  try{
    const url = 'https://nominatim.openstreetmap.org/search?format=json&q=' + encodeURIComponent(city) + '&limit=1';
    const res = await fetch(url, {headers:{'Accept': 'application/json'}});
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

    calculateQibla();
    saveState();
    loadState();
    updateUI();
    showToast('City updated');
    document.getElementById('cityInput').value = '';
  } catch(err){
    showToast('Search failed');
  }
}

/* ===== VIEWS ===== */
function switchView(view){
  document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));
  document.getElementById('view-' + view).classList.add('active');
  document.querySelectorAll('.nav-item').forEach(b => {
    b.classList.toggle('active', b.dataset.view === view);
  });
  const titles = {compass:'Qibla Compass', settings:'Settings'};
  document.getElementById('headerTitle').textContent = titles[view] || 'Qibla';
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

with open('templates/qibla.html') as f:
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

with open('templates/qibla.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Total size:', len(content), 'bytes')
