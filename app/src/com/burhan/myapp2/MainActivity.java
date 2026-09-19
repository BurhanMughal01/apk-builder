package com.burhan.myapp2;

import android.app.Activity;
import android.graphics.Color;
import android.graphics.Typeface;
import android.graphics.drawable.ColorDrawable;
import android.graphics.drawable.GradientDrawable;
import android.os.Build;
import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.os.VibrationEffect;
import android.os.Vibrator;
import android.util.Log;
import android.util.TypedValue;
import android.view.Gravity;
import android.view.View;
import android.view.animation.AlphaAnimation;
import android.view.animation.Animation;
import android.view.animation.AnimationSet;
import android.view.animation.DecelerateInterpolator;
import android.view.animation.LinearInterpolator;
import android.view.animation.OvershootInterpolator;
import android.view.animation.RotateAnimation;
import android.view.animation.ScaleAnimation;
import android.view.animation.TranslateAnimation;
import android.webkit.WebView;
import android.webkit.WebSettings;
import android.webkit.WebViewClient;
import android.widget.FrameLayout;
import android.widget.LinearLayout;
import android.widget.ProgressBar;
import android.widget.TextView;
import org.json.JSONObject;
import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;

public class MainActivity extends Activity {
  private static final String TAG = "APKForge";
  private static final String BG = "#0a0a1a";
  private FrameLayout root;
  private View splashView;

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    Log.d(TAG, "=== onCreate ===");
    getWindow().setBackgroundDrawable(new ColorDrawable(Color.parseColor(BG)));
    root = new FrameLayout(this);
    root.setBackgroundColor(Color.parseColor(BG));
    setContentView(root);
    JSONObject config = loadSplashConfig();
    showSplash(config);
    new Handler(Looper.getMainLooper()).postDelayed(new Runnable() {
      @Override public void run() { loadWebView(); }
    }, 100);
  }

  private JSONObject loadSplashConfig() {
    try {
      InputStream is = getAssets().open("splash_config.json");
      BufferedReader reader = new BufferedReader(new InputStreamReader(is));
      StringBuilder sb = new StringBuilder();
      String line;
      while ((line = reader.readLine()) != null) sb.append(line);
      reader.close();
      is.close();
      return new JSONObject(sb.toString());
    } catch (Exception e) {
      Log.e(TAG, "Config load failed: " + e.getMessage());
      return null;
    }
  }

  private void showSplash(JSONObject c) {
    try {
      String style = "gradient";
      String color = "#6366f1";
      String icon = "🚀";
      int duration = 2500;
      String tagline = "";
      String appName = "My App";
      String iconAnim = "bounce";
      String bgAnim = "static";
      String loading = "none";
      String textAnim = "slide";
      String iconSize = "medium";
      String textColor = "white";
      boolean showAppName = true;
      boolean showTagline = true;
      boolean vibrate = false;

      if (c != null) {
        style = c.optString("style", "gradient");
        color = c.optString("color", "#6366f1");
        icon = decodeIcon(c.optString("icon", "🚀"));
        duration = c.optInt("duration", 2500);
        tagline = c.optString("tagline", "");
        appName = c.optString("appName", "My App");
        iconAnim = c.optString("iconAnim", "bounce");
        bgAnim = c.optString("bgAnim", "static");
        loading = c.optString("loading", "none");
        textAnim = c.optString("textAnim", "slide");
        iconSize = c.optString("iconSize", "medium");
        textColor = c.optString("textColor", "white");
        showAppName = c.optBoolean("showAppName", true);
        showTagline = c.optBoolean("showTagline", true);
        vibrate = c.optBoolean("vibrate", false);
      }

      if (duration < 1000) duration = 2500;
      if (duration > 10000) duration = 10000;

      Log.d(TAG, "Splash: icon=" + iconAnim + ", bg=" + bgAnim + ", loading=" + loading);

      if (vibrate) {
        try {
          Vibrator v = (Vibrator) getSystemService(VIBRATOR_SERVICE);
          if (v != null) {
            if (Build.VERSION.SDK_INT >= 26) {
              v.vibrate(VibrationEffect.createOneShot(50, VibrationEffect.DEFAULT_AMPLITUDE));
            } else {
              v.vibrate(50);
            }
          }
        } catch (Exception e) {}
      }

      LinearLayout splash = new LinearLayout(this);
      splash.setOrientation(LinearLayout.VERTICAL);
      splash.setGravity(Gravity.CENTER);
      splash.setBackground(makeBg(style, color));

      TextView iconView = new TextView(this);
      iconView.setText(icon);
      iconView.setTextSize(TypedValue.COMPLEX_UNIT_SP, iconSizeSp(iconSize));
      iconView.setGravity(Gravity.CENTER);
      splash.addView(iconView);
      applyIconAnimation(iconView, iconAnim);

      TextView nameView = null;
      if (showAppName && appName.length() > 0) {
        LinearLayout.LayoutParams nlp = new LinearLayout.LayoutParams(-2, -2);
        nlp.topMargin = dp(24);
        nameView = new TextView(this);
        nameView.setText(appName);
        nameView.setTextColor(getTextColor(textColor, color));
        nameView.setTextSize(TypedValue.COMPLEX_UNIT_SP, 26);
        nameView.setTypeface(Typeface.DEFAULT_BOLD);
        nameView.setGravity(Gravity.CENTER);
        nameView.setAlpha(0f);
        splash.addView(nameView, nlp);
        applyTextAnimation(nameView, textAnim, 400);
      }

      TextView tagView = null;
      if (showTagline && tagline.length() > 0) {
        LinearLayout.LayoutParams tlp = new LinearLayout.LayoutParams(-2, -2);
        tlp.topMargin = dp(12);
        tagView = new TextView(this);
        tagView.setText(tagline);
        tagView.setTextColor(withAlpha(getTextColor(textColor, color), 220));
        tagView.setTextSize(TypedValue.COMPLEX_UNIT_SP, 14);
        tagView.setGravity(Gravity.CENTER);
        tagView.setAlpha(0f);
        splash.addView(tagView, tlp);
        applyTextAnimation(tagView, textAnim, 700);
      }

      if (!"none".equals(loading)) {
        LinearLayout.LayoutParams llp = new LinearLayout.LayoutParams(-2, -2);
        llp.topMargin = dp(32);
        View loadingView = makeLoadingView(loading, color);
        if (loadingView != null) {
          splash.addView(loadingView, llp);
        }
      }

      if (!"static".equals(bgAnim)) {
        applyBgAnimation(splash, bgAnim);
      }

      splashView = splash;
      root.addView(splash, new FrameLayout.LayoutParams(-1, -1));
      splash.bringToFront();

      final TextView fName = nameView;
      final TextView fTag = tagView;
      new Handler(Looper.getMainLooper()).postDelayed(new Runnable() {
        @Override public void run() {
          if (fName != null && fName.getAnimation() != null) fName.getAnimation().start();
        }
      }, 100);
      new Handler(Looper.getMainLooper()).postDelayed(new Runnable() {
        @Override public void run() {
          if (fTag != null && fTag.getAnimation() != null) fTag.getAnimation().start();
        }
      }, 100);

      new Handler(Looper.getMainLooper()).postDelayed(new Runnable() {
        @Override public void run() { fadeOut(); }
      }, duration);

    } catch (Exception e) {
      Log.e(TAG, "showSplash failed: " + e.getMessage());
    }
  }

  private void loadWebView() {
    try {
      WebView webView = new WebView(this);
      WebSettings ws = webView.getSettings();
      ws.setJavaScriptEnabled(true);
      ws.setDomStorageEnabled(true);
      ws.setAllowFileAccess(true);
      ws.setLoadWithOverviewMode(true);
      ws.setUseWideViewPort(true);
      ws.setBuiltInZoomControls(false);
      ws.setDisplayZoomControls(false);
      webView.setWebViewClient(new WebViewClient());
      webView.setBackgroundColor(Color.parseColor(BG));
      webView.loadUrl("file:///android_asset/index.html");
      root.addView(webView, new FrameLayout.LayoutParams(-1, -1));
    } catch (Exception e) {
      Log.e(TAG, "loadWebView failed: " + e.getMessage());
    }
  }

  private String decodeIcon(String encoded) {
    if (encoded == null) return "\ud83d\ude80";
    try {
      StringBuilder sb = new StringBuilder();
      for (int i = 0; i < encoded.length(); i++) {
        char ch = encoded.charAt(i);
        if (ch == '\\' && i + 5 < encoded.length() && encoded.charAt(i+1) == 'u') {
          String hex = encoded.substring(i+2, i+6);
          sb.append((char) Integer.parseInt(hex, 16));
          i += 5;
        } else {
          sb.append(ch);
        }
      }
      return sb.toString();
    } catch (Exception e) {
      return encoded;
    }
  }

  private int iconSizeSp(String size) {
    if ("small".equals(size)) return 48;
    if ("large".equals(size)) return 96;
    if ("xlarge".equals(size)) return 128;
    return 72;
  }

  private android.graphics.drawable.Drawable makeBg(String style, String color) {
    try {
      int c1 = Color.parseColor(color);
      GradientDrawable.Orientation o = GradientDrawable.Orientation.TL_BR;
      if ("gradient".equals(style)) {
        return new GradientDrawable(o, new int[]{ c1, lighten(c1, 0.3f), darken(c1, 0.3f) });
      } else if ("solid".equals(style) || "minimal".equals(style)) {
        return new ColorDrawable(c1);
      } else if ("neon".equals(style)) {
        return new GradientDrawable(o, new int[]{ darken(c1, 0.7f), c1, darken(c1, 0.7f) });
      } else if ("dark".equals(style)) {
        return new GradientDrawable(o, new int[]{ darken(c1, 0.8f), Color.parseColor(BG) });
      } else {
        return new GradientDrawable(o, new int[]{ c1, darken(c1, 0.4f) });
      }
    } catch (Exception e) {
      return new ColorDrawable(Color.parseColor(BG));
    }
  }

  private void applyIconAnimation(TextView iconView, String anim) {
    if (anim == null || "none".equals(anim) || iconView == null) return;
    try {
      AnimationSet set = new AnimationSet(true);
      if ("bounce".equals(anim)) {
        ScaleAnimation s1 = new ScaleAnimation(0f, 1.2f, 0f, 1.2f,
          Animation.RELATIVE_TO_SELF, 0.5f, Animation.RELATIVE_TO_SELF, 0.5f);
        s1.setDuration(500);
        ScaleAnimation s2 = new ScaleAnimation(1.2f, 1f, 1.2f, 1f,
          Animation.RELATIVE_TO_SELF, 0.5f, Animation.RELATIVE_TO_SELF, 0.5f);
        s2.setDuration(300);
        s2.setStartOffset(500);
        set.addAnimation(s1);
        set.addAnimation(s2);
        set.setInterpolator(new OvershootInterpolator());
      } else if ("fade".equals(anim)) {
        AlphaAnimation a = new AlphaAnimation(0f, 1f);
        a.setDuration(800);
        set.addAnimation(a);
      } else if ("rotate".equals(anim)) {
        RotateAnimation r = new RotateAnimation(0, 360,
          Animation.RELATIVE_TO_SELF, 0.5f, Animation.RELATIVE_TO_SELF, 0.5f);
        r.setDuration(1000);
        r.setInterpolator(new LinearInterpolator());
        set.addAnimation(r);
      } else if ("scale".equals(anim)) {
        ScaleAnimation s = new ScaleAnimation(0f, 1f, 0f, 1f,
          Animation.RELATIVE_TO_SELF, 0.5f, Animation.RELATIVE_TO_SELF, 0.5f);
        s.setDuration(600);
        s.setInterpolator(new DecelerateInterpolator());
        set.addAnimation(s);
      }
      iconView.startAnimation(set);
    } catch (Exception e) {
      Log.e(TAG, "applyIconAnimation failed: " + e.getMessage());
    }
  }

  private void applyTextAnimation(TextView view, String anim, int delay) {
    if (view == null) return;
    try {
      if ("slide".equals(anim)) {
        TranslateAnimation t = new TranslateAnimation(0, 0, dp(30), 0);
        t.setDuration(600);
        t.setStartOffset(delay);
        t.setInterpolator(new DecelerateInterpolator());
        view.startAnimation(t);
        view.animate().alpha(1f).setDuration(600).setStartDelay(delay).start();
      } else if ("fade".equals(anim)) {
        view.animate().alpha(1f).setDuration(800).setStartDelay(delay).start();
      } else if ("scale".equals(anim)) {
        view.setScaleX(0f);
        view.setScaleY(0f);
        view.animate().alpha(1f).scaleX(1f).scaleY(1f).setDuration(600).setStartDelay(delay).start();
      } else {
        view.animate().alpha(1f).setDuration(600).setStartDelay(delay).start();
      }
    } catch (Exception e) {
      Log.e(TAG, "applyTextAnimation failed: " + e.getMessage());
    }
  }

  private int getTextColor(String textColor, String bgColor) {
    try {
      if ("white".equals(textColor)) return Color.WHITE;
      if ("black".equals(textColor)) return Color.BLACK;
      if ("auto".equals(textColor)) {
        int bg = Color.parseColor(bgColor);
        double lum = 0.299 * Color.red(bg) + 0.587 * Color.green(bg) + 0.114 * Color.blue(bg);
        return lum > 128 ? Color.BLACK : Color.WHITE;
      }
      return Color.parseColor(textColor);
    } catch (Exception e) {
      return Color.WHITE;
    }
  }

  private int withAlpha(int color, int alpha) {
    return Color.argb(alpha, Color.red(color), Color.green(color), Color.blue(color));
  }

  private int lighten(int color, float amount) {
    int r = Math.min(255, (int)(Color.red(color) + 255 * amount));
    int g = Math.min(255, (int)(Color.green(color) + 255 * amount));
    int b = Math.min(255, (int)(Color.blue(color) + 255 * amount));
    return Color.rgb(r, g, b);
  }

  private int darken(int color, float amount) {
    int r = Math.max(0, (int)(Color.red(color) * (1 - amount)));
    int g = Math.max(0, (int)(Color.green(color) * (1 - amount)));
    int b = Math.max(0, (int)(Color.blue(color) * (1 - amount)));
    return Color.rgb(r, g, b);
  }

  private int dp(int value) {
    return (int) TypedValue.applyDimension(TypedValue.COMPLEX_UNIT_DIP, value,
      getResources().getDisplayMetrics());
  }

  private View makeLoadingView(String type, String color) {
    try {
      if ("spinner".equals(type) || "bar".equals(type) || "dots".equals(type)) {
        ProgressBar pb = new ProgressBar(this);
        pb.setIndeterminate(true);
        return pb;
      }
      return null;
    } catch (Exception e) {
      return null;
    }
  }

  private void applyBgAnimation(LinearLayout splash, String anim) {
    if (splash == null) return;
    try {
      if ("pulse".equals(anim)) {
        AlphaAnimation pulse = new AlphaAnimation(0.7f, 1f);
        pulse.setDuration(1500);
        pulse.setRepeatMode(Animation.REVERSE);
        pulse.setRepeatCount(Animation.INFINITE);
        splash.startAnimation(pulse);
      } else if ("fade".equals(anim)) {
        AlphaAnimation fade = new AlphaAnimation(0f, 1f);
        fade.setDuration(1000);
        splash.startAnimation(fade);
      }
    } catch (Exception e) {
      Log.e(TAG, "applyBgAnimation failed: " + e.getMessage());
    }
  }

  private void fadeOut() {
    if (splashView == null) return;
    try {
      AlphaAnimation fade = new AlphaAnimation(1f, 0f);
      fade.setDuration(400);
      fade.setAnimationListener(new Animation.AnimationListener() {
        @Override public void onAnimationStart(Animation a) {}
        @Override public void onAnimationRepeat(Animation a) {}
        @Override public void onAnimationEnd(Animation a) {
          if (splashView != null && root != null) {
            root.removeView(splashView);
            splashView = null;
          }
        }
      });
      splashView.startAnimation(fade);
    } catch (Exception e) {
      Log.e(TAG, "fadeOut failed: " + e.getMessage());
    }
  }
}
