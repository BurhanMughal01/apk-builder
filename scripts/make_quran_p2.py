# 114 Surahs data
surahs_data = '''const SURAHS = [
{n:1,name:"Al-Fatihah",ar:"الفاتحة",m:"The Opening",v:7,t:"Makki"},
{n:2,name:"Al-Baqarah",ar:"البقرة",m:"The Cow",v:286,t:"Madani"},
{n:3,name:"Ali 'Imran",ar:"آل عمران",m:"Family of Imran",v:200,t:"Madani"},
{n:4,name:"An-Nisa",ar:"النساء",m:"The Women",v:176,t:"Madani"},
{n:5,name:"Al-Ma'idah",ar:"المائدة",m:"The Table Spread",v:120,t:"Madani"},
{n:6,name:"Al-An'am",ar:"الأنعام",m:"The Cattle",v:165,t:"Makki"},
{n:7,name:"Al-A'raf",ar:"الأعراف",m:"The Heights",v:206,t:"Makki"},
{n:8,name:"Al-Anfal",ar:"الأنفال",m:"The Spoils of War",v:75,t:"Madani"},
{n:9,name:"At-Tawbah",ar:"التوبة",m:"The Repentance",v:129,t:"Madani"},
{n:10,name:"Yunus",ar:"يونس",m:"Jonah",v:109,t:"Makki"},
{n:11,name:"Hud",ar:"هود",m:"Hud",v:123,t:"Makki"},
{n:12,name:"Yusuf",ar:"يوسف",m:"Joseph",v:111,t:"Makki"},
{n:13,name:"Ar-Ra'd",ar:"الرعد",m:"The Thunder",v:43,t:"Madani"},
{n:14,name:"Ibrahim",ar:"إبراهيم",m:"Abraham",v:52,t:"Makki"},
{n:15,name:"Al-Hijr",ar:"الحجر",m:"The Rocky Tract",v:99,t:"Makki"},
{n:16,name:"An-Nahl",ar:"النحل",m:"The Bee",v:128,t:"Makki"},
{n:17,name:"Al-Isra",ar:"الإسراء",m:"The Night Journey",v:111,t:"Makki"},
{n:18,name:"Al-Kahf",ar:"الكهف",m:"The Cave",v:110,t:"Makki"},
{n:19,name:"Maryam",ar:"مريم",m:"Mary",v:98,t:"Makki"},
{n:20,name:"Taha",ar:"طه",m:"Ta-Ha",v:135,t:"Makki"},
{n:21,name:"Al-Anbya",ar:"الأنبياء",m:"The Prophets",v:112,t:"Makki"},
{n:22,name:"Al-Hajj",ar:"الحج",m:"The Pilgrimage",v:78,t:"Madani"},
{n:23,name:"Al-Mu'minun",ar:"المؤمنون",m:"The Believers",v:118,t:"Makki"},
{n:24,name:"An-Nur",ar:"النور",m:"The Light",v:64,t:"Madani"},
{n:25,name:"Al-Furqan",ar:"الفرقان",m:"The Criterion",v:77,t:"Makki"},
{n:26,name:"Ash-Shu'ara",ar:"الشعراء",m:"The Poets",v:227,t:"Makki"},
{n:27,name:"An-Naml",ar:"النمل",m:"The Ant",v:93,t:"Makki"},
{n:28,name:"Al-Qasas",ar:"القصص",m:"The Stories",v:88,t:"Makki"},
{n:29,name:"Al-'Ankabut",ar:"العنكبوت",m:"The Spider",v:69,t:"Makki"},
{n:30,name:"Ar-Rum",ar:"الروم",m:"The Romans",v:60,t:"Makki"},
{n:31,name:"Luqman",ar:"لقمان",m:"Luqman",v:34,t:"Makki"},
{n:32,name:"As-Sajdah",ar:"السجدة",m:"The Prostration",v:30,t:"Makki"},
{n:33,name:"Al-Ahzab",ar:"الأحزاب",m:"The Combined Forces",v:73,t:"Madani"},
{n:34,name:"Saba",ar:"سبأ",m:"Sheba",v:54,t:"Makki"},
{n:35,name:"Fatir",ar:"فاطر",m:"Originator",v:45,t:"Makki"},
{n:36,name:"Ya-Sin",ar:"يس",m:"Ya Sin",v:83,t:"Makki"},
{n:37,name:"As-Saffat",ar:"الصافات",m:"Those who set the Ranks",v:182,t:"Makki"},
{n:38,name:"Sad",ar:"ص",m:"The Letter Sad",v:88,t:"Makki"},
{n:39,name:"Az-Zumar",ar:"الزمر",m:"The Troops",v:75,t:"Makki"},
{n:40,name:"Ghafir",ar:"غافر",m:"The Forgiver",v:85,t:"Makki"},
{n:41,name:"Fussilat",ar:"فصلت",m:"Explained in Detail",v:54,t:"Makki"},
{n:42,name:"Ash-Shuraa",ar:"الشورى",m:"The Consultation",v:53,t:"Makki"},
{n:43,name:"Az-Zukhruf",ar:"الزخرف",m:"The Ornaments of Gold",v:89,t:"Makki"},
{n:44,name:"Ad-Dukhan",ar:"الدخان",m:"The Smoke",v:59,t:"Makki"},
{n:45,name:"Al-Jathiyah",ar:"الجاثية",m:"The Crouching",v:37,t:"Makki"},
{n:46,name:"Al-Ahqaf",ar:"الأحقاف",m:"The Wind-Curved Sandhills",v:35,t:"Makki"},
{n:47,name:"Muhammad",ar:"محمد",m:"Muhammad",v:38,t:"Madani"},
{n:48,name:"Al-Fath",ar:"الفتح",m:"The Victory",v:29,t:"Madani"},
{n:49,name:"Al-Hujurat",ar:"الحجرات",m:"The Rooms",v:18,t:"Madani"},
{n:50,name:"Qaf",ar:"ق",m:"The Letter Qaf",v:45,t:"Makki"},
{n:51,name:"Adh-Dhariyat",ar:"الذاريات",m:"The Winnowing Winds",v:60,t:"Makki"},
{n:52,name:"At-Tur",ar:"الطور",m:"The Mount",v:49,t:"Makki"},
{n:53,name:"An-Najm",ar:"النجم",m:"The Star",v:62,t:"Makki"},
{n:54,name:"Al-Qamar",ar:"القمر",m:"The Moon",v:55,t:"Makki"},
{n:55,name:"Ar-Rahman",ar:"الرحمن",m:"The Beneficent",v:78,t:"Madani"},
{n:56,name:"Al-Waqi'ah",ar:"الواقعة",m:"The Inevitable",v:96,t:"Makki"},
{n:57,name:"Al-Hadid",ar:"الحديد",m:"The Iron",v:29,t:"Madani"},
{n:58,name:"Al-Mujadila",ar:"المجادلة",m:"The Pleading Woman",v:22,t:"Madani"},
{n:59,name:"Al-Hashr",ar:"الحشر",m:"The Exile",v:24,t:"Madani"},
{n:60,name:"Al-Mumtahanah",ar:"الممتحنة",m:"She that is to be examined",v:13,t:"Madani"},
{n:61,name:"As-Saf",ar:"الصف",m:"The Ranks",v:14,t:"Madani"},
{n:62,name:"Al-Jumu'ah",ar:"الجمعة",m:"The Congregation",v:11,t:"Madani"},
{n:63,name:"Al-Munafiqun",ar:"المنافقون",m:"The Hypocrites",v:11,t:"Madani"},
{n:64,name:"At-Taghabun",ar:"التغابن",m:"The Mutual Disillusion",v:18,t:"Madani"},
{n:65,name:"At-Talaq",ar:"الطلاق",m:"The Divorce",v:12,t:"Madani"},
{n:66,name:"At-Tahrim",ar:"التحريم",m:"The Prohibition",v:12,t:"Madani"},
{n:67,name:"Al-Mulk",ar:"الملك",m:"The Sovereignty",v:30,t:"Makki"},
{n:68,name:"Al-Qalam",ar:"القلم",m:"The Pen",v:52,t:"Makki"},
{n:69,name:"Al-Haqqah",ar:"الحاقة",m:"The Reality",v:52,t:"Makki"},
{n:70,name:"Al-Ma'arij",ar:"المعارج",m:"The Ascending Stairways",v:44,t:"Makki"},
{n:71,name:"Nuh",ar:"نوح",m:"Noah",v:28,t:"Makki"},
{n:72,name:"Al-Jinn",ar:"الجن",m:"The Jinn",v:28,t:"Makki"},
{n:73,name:"Al-Muzzammil",ar:"المزمل",m:"The Enshrouded One",v:20,t:"Makki"},
{n:74,name:"Al-Muddaththir",ar:"المدثر",m:"The Cloaked One",v:56,t:"Makki"},
{n:75,name:"Al-Qiyamah",ar:"القيامة",m:"The Resurrection",v:40,t:"Makki"},
{n:76,name:"Al-Insan",ar:"الإنسان",m:"The Man",v:31,t:"Madani"},
{n:77,name:"Al-Mursalat",ar:"المرسلات",m:"The Emissaries",v:50,t:"Makki"},
{n:78,name:"An-Naba",ar:"النبأ",m:"The Tidings",v:40,t:"Makki"},
{n:79,name:"An-Nazi'at",ar:"النازعات",m:"Those who drag forth",v:46,t:"Makki"},
{n:80,name:"'Abasa",ar:"عبس",m:"He Frowned",v:42,t:"Makki"},
{n:81,name:"At-Takwir",ar:"التكوير",m:"The Overthrowing",v:29,t:"Makki"},
{n:82,name:"Al-Infitar",ar:"الإنفطار",m:"The Cleaving",v:19,t:"Makki"},
{n:83,name:"Al-Mutaffifin",ar:"المطففين",m:"The Defrauding",v:36,t:"Makki"},
{n:84,name:"Al-Inshiqaq",ar:"الإنشقاق",m:"The Sundering",v:25,t:"Makki"},
{n:85,name:"Al-Buruj",ar:"البروج",m:"The Mansions of the Stars",v:22,t:"Makki"},
{n:86,name:"At-Tariq",ar:"الطارق",m:"The Nightcomer",v:17,t:"Makki"},
{n:87,name:"Al-A'la",ar:"الأعلى",m:"The Most High",v:19,t:"Makki"},
{n:88,name:"Al-Ghashiyah",ar:"الغاشية",m:"The Overwhelming",v:26,t:"Makki"},
{n:89,name:"Al-Fajr",ar:"الفجر",m:"The Dawn",v:30,t:"Makki"},
{n:90,name:"Al-Balad",ar:"البلد",m:"The City",v:20,t:"Makki"},
{n:91,name:"Ash-Shams",ar:"الشمس",m:"The Sun",v:15,t:"Makki"},
{n:92,name:"Al-Layl",ar:"الليل",m:"The Night",v:21,t:"Makki"},
{n:93,name:"Ad-Duhaa",ar:"الضحى",m:"The Morning Hours",v:11,t:"Makki"},
{n:94,name:"Ash-Sharh",ar:"الشرح",m:"The Relief",v:8,t:"Makki"},
{n:95,name:"At-Tin",ar:"التين",m:"The Fig",v:8,t:"Makki"},
{n:96,name:"Al-'Alaq",ar:"العلق",m:"The Clot",v:19,t:"Makki"},
{n:97,name:"Al-Qadr",ar:"القدر",m:"The Power",v:5,t:"Makki"},
{n:98,name:"Al-Bayyinah",ar:"البينة",m:"The Clear Proof",v:8,t:"Madani"},
{n:99,name:"Az-Zalzalah",ar:"الزلزلة",m:"The Earthquake",v:8,t:"Madani"},
{n:100,name:"Al-'Adiyat",ar:"العاديات",m:"The Courser",v:11,t:"Makki"},
{n:101,name:"Al-Qari'ah",ar:"القارعة",m:"The Calamity",v:11,t:"Makki"},
{n:102,name:"At-Takathur",ar:"التكاثر",m:"The Rivalry in world increase",v:8,t:"Makki"},
{n:103,name:"Al-'Asr",ar:"العصر",m:"The Declining Day",v:3,t:"Makki"},
{n:104,name:"Al-Humazah",ar:"الهمزة",m:"The Traducer",v:9,t:"Makki"},
{n:105,name:"Al-Fil",ar:"الفيل",m:"The Elephant",v:5,t:"Makki"},
{n:106,name:"Quraysh",ar:"قريش",m:"Quraysh",v:4,t:"Makki"},
{n:107,name:"Al-Ma'un",ar:"الماعون",m:"The Small Kindnesses",v:7,t:"Makki"},
{n:108,name:"Al-Kawthar",ar:"الكوثر",m:"The Abundance",v:3,t:"Makki"},
{n:109,name:"Al-Kafirun",ar:"الكافرون",m:"The Disbelievers",v:6,t:"Makki"},
{n:110,name:"An-Nasr",ar:"النصر",m:"The Divine Support",v:3,t:"Madani"},
{n:111,name:"Al-Masad",ar:"المسد",m:"The Palm Fibre",v:5,t:"Makki"},
{n:112,name:"Al-Ikhlas",ar:"الإخلاص",m:"The Sincerity",v:4,t:"Makki"},
{n:113,name:"Al-Falaq",ar:"الفلق",m:"The Daybreak",v:5,t:"Makki"},
{n:114,name:"An-Nas",ar:"الناس",m:"Mankind",v:6,t:"Makki"}
];'''

js_code = surahs_data + '''

let state = {
  theme: 'dark',
  fontSize: 'medium',
  showTranslation: true,
  currentCat: 'all',
  bookmarks: [],
  lastRead: null,
  currentSurah: null,
  currentAyahs: [],
  audioPlaying: null
};

/* ===== INIT ===== */
function init(){
  loadState();
  applyTheme();
  applyFontSize();
  applyToggles();
  renderCategories();
  renderSurahList();
  renderBookmarks();
}

function loadState(){
  try{
    const s = localStorage.getItem('quran_v1');
    if(s){
      const p = JSON.parse(s);
      state.theme = p.theme || 'dark';
      state.fontSize = p.fontSize || 'medium';
      state.showTranslation = p.showTranslation !== false;
      state.bookmarks = p.bookmarks || [];
      state.lastRead = p.lastRead || null;
    }
  }catch(e){}
}

function saveState(){
  try{
    localStorage.setItem('quran_v1', JSON.stringify({
      theme: state.theme,
      fontSize: state.fontSize,
      showTranslation: state.showTranslation,
      bookmarks: state.bookmarks,
      lastRead: state.lastRead
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
  applyTheme(); saveState();
}

/* ===== FONT SIZE ===== */
function applyFontSize(){
  const sizes = {small:'22px', medium:'28px', large:'36px'};
  document.documentElement.style.setProperty('--font-quran', sizes[state.fontSize]);
  document.querySelectorAll('.font-btn').forEach(b => {
    b.classList.toggle('active', b.dataset.size === state.fontSize);
  });
}

function setFontSize(size){ state.fontSize = size; applyFontSize(); saveState(); }

/* ===== TOGGLES ===== */
function applyToggles(){
  const t = document.getElementById('transToggle');
  if(t) t.classList.toggle('on', state.showTranslation);
}

function toggleTranslation(){
  state.showTranslation = !state.showTranslation;
  applyToggles(); saveState();
  if(state.currentSurah){ renderSurah(state.currentSurah); }
}

/* ===== CATEGORIES ===== */
function renderCategories(){
  const el = document.getElementById('catChips');
  const cats = [
    {id:'all', name:'All 114'},
    {id:'makki', name:'Makki'},
    {id:'madani', name:'Madani'},
    {id:'short', name:'Short (≤10)'},
    {id:'last', name:'Last 10'},
    {id:'bookmarked', name:'Bookmarked'}
  ];
  el.innerHTML = cats.map(c => 
    '<button class="chip ' + (state.currentCat === c.id ? 'active' : '') + '" onclick="setCategory(\\'' + c.id + '\\')">' + c.name + '</button>'
  ).join('');
}

function setCategory(id){
  state.currentCat = id;
  renderCategories();
  renderSurahList();
  document.getElementById('mainArea').scrollTo({top:0, behavior:'smooth'});
}

/* ===== SURAH LIST ===== */
function renderSurahList(filter){
  const list = document.getElementById('surahList');
  let items = SURAHS.slice();
  
  if(filter){
    const q = filter.toLowerCase();
    items = items.filter(s => 
      s.name.toLowerCase().includes(q) || 
      s.m.toLowerCase().includes(q) || 
      s.ar.includes(filter) ||
      String(s.n) === q
    );
  } else {
    if(state.currentCat === 'makki') items = items.filter(s => s.t === 'Makki');
    else if(state.currentCat === 'madani') items = items.filter(s => s.t === 'Madani');
    else if(state.currentCat === 'short') items = items.filter(s => s.v <= 10);
    else if(state.currentCat === 'last') items = items.filter(s => s.n >= 105);
    else if(state.currentCat === 'bookmarked') items = items.filter(s => state.bookmarks.includes(s.n));
  }
  
  if(items.length === 0){
    list.innerHTML = '<div class="empty"><svg viewBox="0 0 24 24"><path d="M4 19.5A2.5 2.5 0 016.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 014 19.5v-15A2.5 2.5 0 016.5 2z"/></svg><h3>No surahs found</h3><p>Try a different search</p></div>';
    return;
  }
  
  list.innerHTML = items.map(s => {
    const isLast = state.lastRead && state.lastRead.surah === s.n;
    return '<div class="surah-card" onclick="openSurah(' + s.n + ')">' +
      '<div class="surah-num">' + s.n + '</div>' +
      '<div class="surah-info">' +
        '<div class="surah-name">' + s.name + ' <span class="type">' + s.t + '</span>' + (isLast ? ' <span style="color:var(--accent);font-size:10px">●</span>' : '') + '</div>' +
        '<div class="surah-meta">' + s.m + ' · ' + s.v + ' verses</div>' +
      '</div>' +
      '<div class="surah-arabic">' + s.ar + '</div>' +
    '</div>';
  }).join('');
}

function handleSearch(q){
  if(!q.trim()){ renderSurahList(); return; }
  renderSurahList(q);
}

/* ===== OPEN SURAH ===== */
async function openSurah(num){
  const surah = SURAHS.find(s => s.n === num);
  if(!surah) return;
  
  state.currentSurah = num;
  state.lastRead = {surah: num, ayah: 1};
  saveState();
  
  document.getElementById('backBtn').style.display = 'grid';
  document.getElementById('headerTitleWrap').style.display = 'none';
  
  document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));
  document.getElementById('view-reader').classList.add('active');
  
  document.getElementById('bottomNav').style.display = 'none';
  
  const reader = document.getElementById('readerContent');
  reader.innerHTML = '<div class="loading"><div class="spinner"></div><p>Loading ' + surah.name + '...</p></div>';
  
  document.getElementById('mainArea').scrollTo({top:0});
  
  try{
    const res = await fetch('https://api.alquran.cloud/v1/surah/' + num + '/editions/quran-uthmani,en.sahih');
    if(!res.ok) throw new Error('Network error');
    const data = await res.json();
    
    if(!data.data || data.data.length < 2) throw new Error('Invalid data');
    
    const arabicData = data.data[0];
    const engData = data.data[1];
    state.currentAyahs = arabicData.ayahs.map((a, i) => ({
      num: a.numberInSurah,
      arabic: a.text,
      english: engData.ayahs[i] ? engData.ayahs[i].text : ''
    }));
    
    renderSurah(num);
  }catch(err){
    console.error(err);
    reader.innerHTML = '<div class="error-box"><p>Failed to load. Check internet connection.</p><button onclick="openSurah(' + num + ')">Retry</button></div>';
  }
}

function renderSurah(num){
  const surah = SURAHS.find(s => s.n === num);
  if(!surah) return;
  
  const showBismillah = num !== 1 && num !== 9;
  
  let html = '<div class="reader-header">' +
    '<div class="arabic-title">' + surah.ar + '</div>' +
    '<div class="eng-title">' + surah.name + '</div>' +
    '<div class="subtitle">' + surah.m + ' · ' + surah.v + ' verses · ' + surah.t + '</div>' +
    '<div class="reader-actions">' +
      '<button id="audioBtn" onclick="toggleAudio(' + num + ')">' +
        '<svg viewBox="0 0 24 24"><path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/></svg>' +
        'Play Audio' +
      '</button>' +
      '<button onclick="toggleBookmark(' + num + ')" id="bmBtn">' +
        '<svg viewBox="0 0 24 24" id="bmIcon"><path d="M19 21l-7-5-7 5V5a2 2 0 012-2h10a2 2 0 012 2z" ' + (state.bookmarks.includes(num) ? 'fill="currentColor"' : '') + '/></svg>' +
        (state.bookmarks.includes(num) ? 'Saved' : 'Bookmark') +
      '</button>' +
    '</div>' +
  '</div>';
  
  if(showBismillah){
    html += '<div class="bismillah">بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ</div>';
  }
  
  html += state.currentAyahs.map(a => {
    const trans = state.showTranslation ? '<div class="ayah-trans">' + a.english + '</div>' : '';
    return '<div class="ayah-card" id="ayah-' + a.num + '">' +
      '<div class="ayah-head">' +
        '<div class="ayah-num-badge">' + a.num + '</div>' +
        '<div class="ayah-actions">' +
          '<button class="ayah-mini-btn" onclick="copyAyah(' + a.num + ')"><svg viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 01-2-2V4a2 2 0 012-2h9a2 2 0 012 2v1"/></svg></button>' +
          '<button class="ayah-mini-btn" onclick="shareAyah(' + a.num + ')"><svg viewBox="0 0 24 24"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><path d="M8.59 13.51l6.83 3.98M15.41 6.51l-6.82 3.98"/></svg></button>' +
        '</div>' +
      '</div>' +
      '<div class="ayah-arabic">' + a.arabic + '</div>' +
      trans +
    '</div>';
  }).join('');
  
  document.getElementById('readerContent').innerHTML = html;
}

/* ===== AUDIO ===== */
function toggleAudio(num){
  const btn = document.getElementById('audioBtn');
  if(state.audioPlaying){
    state.audioPlaying.pause();
    state.audioPlaying = null;
    btn.classList.remove('playing');
    btn.innerHTML = '<svg viewBox="0 0 24 24"><path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/></svg>Play Audio';
    return;
  }
  const paddedNum = String(num).padStart(3, '0');
  const url = 'https://cdn.islamic.network/quran/audio-surah/128/ar.alafasy/' + num + '.mp3';
  const audio = new Audio(url);
  audio.play().then(() => {
    state.audioPlaying = audio;
    btn.classList.add('playing');
    btn.innerHTML = '<svg viewBox="0 0 24 24"><rect x="6" y="4" width="4" height="16"/><rect x="14" y="4" width="4" height="16"/></svg>Stop Audio';
  }).catch(err => {
    showToast('Audio not available');
  });
  audio.onended = () => {
    state.audioPlaying = null;
    btn.classList.remove('playing');
    btn.innerHTML = '<svg viewBox="0 0 24 24"><path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/></svg>Play Audio';
  };
}

/* ===== BOOKMARKS ===== */
function toggleBookmark(num){
  const idx = state.bookmarks.indexOf(num);
  if(idx > -1){ state.bookmarks.splice(idx, 1); showToast('Removed'); }
  else { state.bookmarks.push(num); showToast('Bookmarked'); }
  saveState();
  renderBookmarks();
  renderSurahList();
  if(state.currentSurah){ renderSurah(state.currentSurah); }
}

function renderBookmarks(){
  const el = document.getElementById('bookmarksList');
  if(!el) return;
  const bm = SURAHS.filter(s => state.bookmarks.includes(s.n));
  if(bm.length === 0){
    el.innerHTML = '<div class="empty"><svg viewBox="0 0 24 24"><path d="M19 21l-7-5-7 5V5a2 2 0 012-2h10a2 2 0 012 2z"/></svg><h3>No bookmarks yet</h3><p>Tap the bookmark icon on any surah</p></div>';
    return;
  }
  el.innerHTML = bm.map(s => 
    '<div class="surah-card" onclick="openSurah(' + s.n + ')">' +
      '<div class="surah-num">' + s.n + '</div>' +
      '<div class="surah-info">' +
        '<div class="surah-name">' + s.name + '</div>' +
        '<div class="surah-meta">' + s.m + ' · ' + s.v + ' verses</div>' +
      '</div>' +
      '<div class="surah-arabic">' + s.ar + '</div>' +
    '</div>'
  ).join('');
}

/* ===== COPY / SHARE ===== */
function copyAyah(num){
  const a = state.currentAyahs.find(x => x.num === num);
  if(!a) return;
  const text = a.arabic + '\\n\\n' + a.english + '\\n\\n— Quran ' + state.currentSurah + ':' + num;
  if(navigator.clipboard){
    navigator.clipboard.writeText(text).then(() => showToast('Copied'));
  }
}

function shareAyah(num){
  const a = state.currentAyahs.find(x => x.num === num);
  if(!a) return;
  const text = a.arabic + '\\n\\n' + a.english + '\\n\\n— Quran ' + state.currentSurah + ':' + num;
  if(navigator.share){
    navigator.share({text: text}).catch(()=>{});
  } else {
    copyAyah(num);
  }
}

/* ===== BACK ===== */
function backToList(){
  if(state.audioPlaying){
    state.audioPlaying.pause();
    state.audioPlaying = null;
  }
  document.getElementById('backBtn').style.display = 'none';
  document.getElementById('headerTitleWrap').style.display = 'flex';
  document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));
  document.getElementById('view-list').classList.add('active');
  document.getElementById('bottomNav').style.display = 'grid';
}

/* ===== VIEWS ===== */
function switchView(view){
  if(state.audioPlaying){
    state.audioPlaying.pause();
    state.audioPlaying = null;
  }
  document.getElementById('backBtn').style.display = 'none';
  document.getElementById('headerTitleWrap').style.display = 'flex';
  document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));
  document.getElementById('view-' + view).classList.add('active');
  document.querySelectorAll('.nav-item').forEach(b => {
    b.classList.toggle('active', b.dataset.view === view);
  });
  const titles = {list:'Al-Quran', bookmarks:'Bookmarks', settings:'Settings'};
  document.getElementById('headerTitle').textContent = titles[view] || 'Al-Quran';
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

init();'''

with open('templates/quran.html') as f:
    content = f.read()

old = '''<script>
/* PART 2 WILL BE INJECTED */
</script>'''

new = '<script>\n' + js_code + '\n</script>'

if old in content:
    content = content.replace(old, new)
    print('Part 2 injected!')
else:
    print('Placeholder not found!')

with open('templates/quran.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Total size:', len(content), 'bytes')
