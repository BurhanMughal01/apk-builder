/**
 * APKForge v3.0 - Real Build System
 * Worker API + Supabase integration
 */

(function() {
  console.log('[APKForge] Real build module loading...');

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', attachHandler);
  } else {
    setTimeout(attachHandler, 800);
  }

  function attachHandler() {
    const oldBtn = document.getElementById('buildBtn');
    if (!oldBtn) return;

    const newBtn = oldBtn.cloneNode(true);
    newBtn.addEventListener('click', handleBuild);
    oldBtn.parentNode.replaceChild(newBtn, oldBtn);

    console.log('[APKForge] Real build handler attached');
  }

  async function handleBuild() {
    if (!window.Auth || !window.API) {
      alert('System loading... Please wait 2 seconds and try again');
      return;
    }

    const user = await Auth.getUser();
    if (!user) {
      showToast('Please login first', 'error');
      setTimeout(function() { location.href = 'login.html'; }, 1500);
      return;
    }

    const btn = document.getElementById('buildBtn');
    const progress = document.getElementById('buildProgress');
    const progressFill = document.getElementById('progressFill');
    const progressText = document.getElementById('progressText');
    const actions = document.getElementById('buildActions');
    const success = document.getElementById('buildSuccess');
    const downloadLink = document.getElementById('downloadLink');

    btn.disabled = true;
    btn.textContent = 'Building...';
    progress.style.display = 'block';
    actions.style.display = 'none';
    success.style.display = 'none';
    progressFill.style.width = '10%';
    progressFill.style.background = 'var(--grad-primary)';
    progressText.textContent = 'Preparing request...';

    try {
      const s = window.state;
      if (!s) throw new Error('Page state not found. Please refresh.');

      if (!s.details.appName) throw new Error('App name is required');
      if (!s.details.packageName) throw new Error('Package name is required');
      if (s.buildType === 'html' && !s.htmlContent) throw new Error('Please upload HTML file');
      if (s.buildType === 'url' && !s.url) throw new Error('Please enter URL');
      if (s.buildType === 'template' && !s.template) throw new Error('Please pick a template');

      const payload = {
        buildType: s.buildType,
        htmlContent: s.htmlContent,
        url: s.url,
        templateName: s.template,
        appName: s.details.appName,
        packageName: s.details.packageName,
        version: s.details.version || '1.0.0',
        splashStyle: s.splash.style,
        splashColor: s.splash.color,
        splashIcon: s.splash.icon,
        splashDuration: s.splash.duration,
        splashTagline: s.splash.tagline,
        orientation: s.details.orientation,
        fullscreen: s.details.fullscreen,
        customIcon: null
      };

      progressFill.style.width = '25%';
      progressText.textContent = 'Sending to server...';

      const result = await API.build(payload);

      if (!result.ok) throw new Error(result.error || 'Build request failed');

      const buildId = result.buildId;
      progressFill.style.width = '35%';
      progressText.textContent = 'Queued (position ' + result.queuePosition + ')';

      await pollStatus(buildId);

    } catch (err) {
      console.error('[APKForge] Error:', err);
      progressFill.style.background = 'var(--danger)';
      progressText.textContent = 'Error: ' + err.message;
      btn.disabled = false;
      btn.textContent = 'Retry Build';
      actions.style.display = 'flex';
      showToast(err.message, 'error');
    }
  }

  function pollStatus(buildId) {
    return new Promise(function(resolve) {
      var attempts = 0;
      var maxAttempts = 60;

      var interval = setInterval(async function() {
        attempts++;
        try {
          var status = await API.status(buildId);
          var build = status.build;
          var queuePos = status.queuePosition;

          var progressFill = document.getElementById('progressFill');
          var progressText = document.getElementById('progressText');
          var progress = document.getElementById('buildProgress');
          var success = document.getElementById('buildSuccess');
          var downloadLink = document.getElementById('downloadLink');
          var btn = document.getElementById('buildBtn');
          var actions = document.getElementById('buildActions');

          if (build.status === 'queued') {
            progressFill.style.width = '40%';
            progressText.textContent = queuePos 
              ? 'In queue (position ' + queuePos + ')...' 
              : 'Waiting in queue...';
          } else if (build.status === 'building') {
            progressFill.style.width = '70%';
            progressText.textContent = 'Building APK... This takes 60-90 seconds';
          } else if (build.status === 'success') {
            clearInterval(interval);
            progressFill.style.width = '100%';
            progressText.textContent = 'Done!';
            setTimeout(function() {
              progress.style.display = 'none';
              success.style.display = 'block';
              downloadLink.href = build.apk_url;
              downloadLink.setAttribute('download', build.app_name + '.apk');
            }, 500);
            showToast('APK ready!', 'success');
            resolve();
          } else if (build.status === 'failed') {
            clearInterval(interval);
            progressFill.style.background = 'var(--danger)';
            progressText.textContent = 'Failed: ' + (build.error_message || 'Unknown error');
            btn.disabled = false;
            btn.textContent = 'Try Again';
            actions.style.display = 'flex';
            showToast('Build failed', 'error');
            resolve();
          }
        } catch (err) {
          console.error('[APKForge] Poll error:', err);
        }

        if (attempts >= maxAttempts) {
          clearInterval(interval);
          document.getElementById('progressText').textContent = 'Timeout. Check History page.';
          var b = document.getElementById('buildBtn');
          b.disabled = false;
          b.textContent = 'Try Again';
          document.getElementById('buildActions').style.display = 'flex';
          resolve();
        }
      }, 5000);
    });
  }
})();
