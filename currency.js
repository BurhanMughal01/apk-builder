/* APKForge — Currency Handler */
(function() {
  'use strict';

  // Static exchange rates (base: USD)
  // Update manually every 1-2 weeks
  const RATES = {
    USD: 1,      EUR: 0.92,   GBP: 0.79,   CAD: 1.36,
    AUD: 1.52,   PKR: 278,    INR: 84,     BDT: 110,
    SAR: 3.75,   AED: 3.67,   MYR: 4.70,   IDR: 15800,
    TRY: 34,     EGP: 48,     NGN: 1500,   KES: 129,
    ZAR: 18,     RUB: 95,     CNY: 7.20,   JPY: 150,
    KRW: 1350,   SGD: 1.34,   THB: 35,     PHP: 57
  };

  const SYMBOLS = {
    USD: '$', EUR: '€', GBP: '£', CAD: 'C$', AUD: 'A$',
    PKR: 'Rs ', INR: '₹', BDT: '৳', SAR: 'SR ', AED: 'AED ',
    MYR: 'RM ', IDR: 'Rp ', TRY: '₺', EGP: 'E£', NGN: '₦',
    KES: 'KSh ', ZAR: 'R ', RUB: '₽', CNY: '¥', JPY: '¥',
    KRW: '₩', SGD: 'S$', THB: '฿', PHP: '₱'
  };

  const COUNTRY_TO_CURRENCY = {
    PK:'PKR', IN:'INR', BD:'BDT', SA:'SAR', AE:'AED', MY:'MYR',
    ID:'IDR', TR:'TRY', EG:'EGP', NG:'NGN', KE:'KES', ZA:'ZAR',
    RU:'RUB', CN:'CNY', JP:'JPY', KR:'KRW', SG:'SGD', TH:'THB',
    PH:'PHP', US:'USD', GB:'GBP', CA:'CAD', AU:'AUD',
    DE:'EUR', FR:'EUR', ES:'EUR', IT:'EUR', NL:'EUR'
  };

  function detectCurrency() {
    const saved = localStorage.getItem('apkforge_currency');
    if (saved && RATES[saved]) return saved;

    // Try navigator.language
    const lang = (navigator.language || 'en-US').toUpperCase();
    const parts = lang.split('-');
    const country = parts[1];
    if (country && COUNTRY_TO_CURRENCY[country]) {
      return COUNTRY_TO_CURRENCY[country];
    }

    // Try timezone
    try {
      const tz = Intl.DateTimeFormat().resolvedOptions().timeZone;
      const tzMap = {
        'Asia/Karachi':'PKR', 'Asia/Kolkata':'INR', 'Asia/Dhaka':'BDT',
        'Asia/Riyadh':'SAR', 'Asia/Dubai':'AED', 'Asia/Kuala_Lumpur':'MYR',
        'Asia/Jakarta':'IDR', 'Europe/Istanbul':'TRY', 'Africa/Cairo':'EGP',
        'Africa/Lagos':'NGN', 'Africa/Nairobi':'KES', 'Africa/Johannesburg':'ZAR',
        'Europe/London':'GBP', 'America/New_York':'USD', 'America/Toronto':'CAD',
        'Australia/Sydney':'AUD', 'Europe/Berlin':'EUR', 'Asia/Tokyo':'JPY',
        'Asia/Shanghai':'CNY', 'Asia/Singapore':'SGD', 'Asia/Seoul':'KRW'
      };
      if (tzMap[tz]) return tzMap[tz];
    } catch(e) {}

    return 'USD';
  }

  function convert(usd, currency) {
    const rate = RATES[currency] || 1;
    return usd * rate;
  }

  function format(usd, currency) {
    currency = currency || getCurrency();
    const value = convert(usd, currency);
    const symbol = SYMBOLS[currency] || currency + ' ';

    // Round intelligently
    let rounded;
    if (currency === 'IDR' || currency === 'JPY' || currency === 'KRW') {
      rounded = Math.ceil(value / 100) * 100;
    } else if (value >= 1000) {
      rounded = Math.round(value / 10) * 10;
    } else if (value >= 100) {
      rounded = Math.round(value);
    } else {
      rounded = Math.round(value * 100) / 100;
    }

    return symbol + rounded.toLocaleString();
  }

  function getCurrency() {
    return localStorage.getItem('apkforge_currency') || detectCurrency();
  }

  function setCurrency(code) {
    if (!RATES[code]) return;
    localStorage.setItem('apkforge_currency', code);
    window.dispatchEvent(new CustomEvent('currencychange', { detail: code }));
    updatePage();
  }

  function updatePage() {
    const currency = getCurrency();
    document.querySelectorAll('[data-usd]').forEach(function(el) {
      const usd = parseFloat(el.getAttribute('data-usd'));
      if (!isNaN(usd)) el.textContent = format(usd, currency);
    });
    document.querySelectorAll('[data-currency-select]').forEach(function(el) {
      el.value = currency;
    });
    document.querySelectorAll('[data-currency-label]').forEach(function(el) {
      el.textContent = currency;
    });
  }

  // Public API
  window.Currency = {
    get: getCurrency,
    set: setCurrency,
    format: format,
    detect: detectCurrency,
    rates: RATES,
    symbols: SYMBOLS,
    update: updatePage
  };

  // Auto-update when DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', updatePage);
  } else {
    updatePage();
  }
})();
