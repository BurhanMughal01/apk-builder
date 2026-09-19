# APKForge

Turn HTML and websites into Android APKs — free for Islamic projects.

**Live:** https://apk-builder-eosin.vercel.app

## Features

- 52 templates (Islamic, utility, games, education, business)
- 14 Islamic templates — always free, unlimited
- 12 splash styles with live preview
- Multi-currency pricing (20+ currencies)
- No ads, no tracking, no interest (riba)
- Halal-only content policy

## Stack

- Frontend: HTML/CSS/JS on Vercel
- Backend: Cloudflare Worker
- Database: Supabase
- Build: GitHub Actions + Android SDK

## Structure

- `index.html`, `build.html`, `dashboard.html` — main pages
- `templates/` — 52 template files
- `worker/` — Cloudflare Worker backend
- `app/` — Android app shell
- `.github/workflows/` — APK build pipeline

## Setup

Clone repo, then serve locally:

    python -m http.server 8000

Worker dev:

    cd worker && wrangler dev

## Environment

Worker secrets: SUPABASE_URL, SUPABASE_SERVICE_KEY, GITHUB_TOKEN, GITHUB_REPO, KEYSTORE_BASE64

GitHub secrets: KEYSTORE_BASE64, KEYSTORE_PASSWORD, KEY_ALIAS, KEY_PASSWORD, SUPABASE_URL, SUPABASE_SERVICE_KEY

## Halal Policy

Islamic apps are always free — our sadaqah jariyah.

Not allowed: music, dating, gambling, alcohol, interest-based finance, adult content.

## Contact

Website: https://apk-builder-eosin.vercel.app

Made with love in Pakistan.
