package com.burhan.myapp2;

import android.app.Activity;
import android.graphics.Color;
import android.graphics.Typeface;
import android.graphics.drawable.ColorDrawable;
import android.graphics.drawable.GradientDrawable;
import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.util.Log;
import android.util.TypedValue;
import android.view.Gravity;
import android.view.View;
import android.view.animation.AlphaAnimation;
import android.view.animation.Animation;
import android.webkit.WebView;
import android.webkit.WebSettings;
import android.webkit.WebViewClient;
import android.widget.FrameLayout;
import android.widget.LinearLayout;
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
    Log.d(TAG, "Config: " + (config != null ? config.toString() : "NULL"));
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
      Log.e(TAG, "loadSplashConfig failed: " + e.getMessage());
      return null;
    }
  }

  private void showSplash(JSONObject c) {
    try {
      String style = "gradient";
      String color = "#6366f1";
      String icon = "🚀";
      int duration = 2000;
      String tagline = "";
      String appName = "My App";

      if (c != null) {
        style = c.optString("style", "gradient");
        color = c.optString("color", "#6366f1");
        icon = decodeIcon(c.optString("icon", "🚀"));
        duration = c.optInt("duration", 2000);
        tagline = c.optString("tagline", "");
        appName = c.optString("appName", "My App");
      }

      if (duration < 500) duration = 1500;
      if (duration > 10000) duration = 10000;

      Log.d(TAG, "Splash: style=" + style + ", color=" + color + ", dur=" + duration);

      LinearLayout splash = new LinearLayout(this);
      splash.setOrientation(LinearLayout.VERTICAL);
      splash.setGravity(Gravity.CENTER);
      splash.setBackground(makeBg(style, color));

      TextView iconView = new TextView(this);
      iconView.setText(icon);
      iconView.setTextSize(TypedValue.COMPLEX_UNIT_SP, 80);
      iconView.setGravity(Gravity.CENTER);
      splash.addView(iconView);

      if (appName.length() > 0) {
        TextView nameView = new TextView(this);
        nameView.setText(appName);
        nameView.setTextColor(Color.WHITE);
        nameView.setTextSize(TypedValue.COMPLEX_UNIT_SP, 22);
        nameView.setTypeface(Typeface.DEFAULT_BOLD);
        nameView.setGravity(Gravity.CENTER);
        LinearLayout.LayoutParams nlp = new LinearLayout.LayoutParams(-2, -2);
        nlp.topMargin = dp(16);
        splash.addView(nameView, nlp);
      }

      if (tagline.length() > 0) {
        TextView tagView = new TextView(this);
        tagView.setText(tagline);
        tagView.setTextColor(0xDDFFFFFF);
        tagView.setTextSize(TypedValue.COMPLEX_UNIT_SP, 13);
        tagView.setGravity(Gravity.CENTER);
        LinearLayout.LayoutParams tlp = new LinearLayout.LayoutParams(-2, -2);
        tlp.topMargin = dp(8);
        splash.addView(tagView, tlp);
      }

      splashView = splash;
      root.addView(splash, new FrameLayout.LayoutParams(-1, -1));
      splash.bringToFront();
      splash.requestLayout();
      Log.d(TAG, "Splash added");

      new Handler(Looper.getMainLooper()).postDelayed(new Runnable() {
        @Override public void run() { fadeOut(); }
      }, duration);
    } catch (Exception e) {
      Log.e(TAG, "showSplash failed: " + e.getMessage());
    }
  }

  private void fadeOut() {
    if (splashView == null) return;
    try {
      AlphaAnimation a = new AlphaAnimation(1f, 0f);
      a.setDuration(500);
      a.setAnimationListener(new Animation.AnimationListener() {
        @Override public void onAnimationStart(Animation x) {}
        @Override public void onAnimationRepeat(Animation x) {}
        @Override public void onAnimationEnd(Animation x) {
          try { if (splashView != null) root.removeView(splashView); } catch (Exception e) {}
          splashView = null;
        }
      });
      splashView.startAnimation(a);
    } catch (Exception e) {
      try { if (splashView != null) root.removeView(splashView); } catch (Exception ex) {}
      splashView = null;
    }
  }

  private void loadWebView() {
    try {
      WebView w = new WebView(this);
      w.setBackgroundColor(Color.parseColor(BG));
      WebSettings s = w.getSettings();
      s.setJavaScriptEnabled(true);
      s.setDomStorageEnabled(true);
      s.setAllowFileAccess(true);
      s.setLoadWithOverviewMode(true);
      s.setUseWideViewPort(true);
      s.setAllowContentAccess(true);
      w.setWebViewClient(new WebViewClient());
      w.loadUrl("file:///android_asset/index.html");
      root.addView(w, 0, new FrameLayout.LayoutParams(-1, -1));
      Log.d(TAG, "WebView loaded behind splash");
    } catch (Exception e) {
      Log.e(TAG, "loadWebView failed: " + e.getMessage());
    }
  }

  private GradientDrawable makeBg(String style, String color) {
    GradientDrawable g = new GradientDrawable();
    try {
      int c = Color.parseColor(color);
      if ("gradient".equals(style)) {
        g.setOrientation(GradientDrawable.Orientation.TL_BR);
        g.setColors(new int[]{c, Color.parseColor("#ec4899")});
      } else if ("neon".equals(style)) {
        g.setGradientType(GradientDrawable.RADIAL_GRADIENT);
        g.setGradientRadius(700);
        g.setColors(new int[]{c, Color.BLACK});
      } else if ("aurora".equals(style)) {
        g.setOrientation(GradientDrawable.Orientation.TL_BR);
        g.setColors(new int[]{c, Color.parseColor("#06b6d4"), Color.parseColor("#ec4899")});
      } else if ("waves".equals(style)) {
        g.setOrientation(GradientDrawable.Orientation.BOTTOM_TOP);
        g.setColors(new int[]{Color.BLACK, c});
      } else if ("matrix".equals(style)) {
        g.setOrientation(GradientDrawable.Orientation.TOP_BOTTOM);
        g.setColors(new int[]{Color.BLACK, c});
      } else if ("cosmic".equals(style) || "stars".equals(style)) {
        g.setGradientType(GradientDrawable.RADIAL_GRADIENT);
        g.setGradientRadius(800);
        g.setColors(new int[]{c, Color.BLACK});
      } else if ("sunset".equals(style)) {
        g.setOrientation(GradientDrawable.Orientation.TOP_BOTTOM);
        g.setColors(new int[]{Color.parseColor("#ec4899"), Color.parseColor("#f59e0b"), c});
      } else if ("ocean".equals(style)) {
        g.setOrientation(GradientDrawable.Orientation.TOP_BOTTOM);
        g.setColors(new int[]{Color.parseColor("#06b6d4"), c, Color.parseColor("#1e3a8a")});
      } else if ("fire".equals(style)) {
        g.setOrientation(GradientDrawable.Orientation.TOP_BOTTOM);
        g.setColors(new int[]{Color.parseColor("#ef4444"), Color.parseColor("#f59e0b"), Color.BLACK});
      } else if ("glass".equals(style)) {
        g.setOrientation(GradientDrawable.Orientation.TL_BR);
        g.setColors(new int[]{withAlpha(c, 100), withAlpha(c, 200), Color.BLACK});
      } else if ("mono".equals(style)) {
        g.setOrientation(GradientDrawable.Orientation.TL_BR);
        g.setColors(new int[]{Color.parseColor("#1a1a1a"), Color.parseColor("#333333")});
      } else {
        g.setColor(c);
      }
    } catch (Exception e) {
      g.setColor(Color.parseColor("#6366f1"));
    }
    return g;
  }

  private int withAlpha(int c, int alpha) {
    return Color.argb(alpha, Color.red(c), Color.green(c), Color.blue(c));
  }

  private String decodeIcon(String name) {
    if (name == null || name.length() == 0) return "🚀";
    if (name.length() > 2) return name;
    switch (name.toLowerCase()) {
      case "rocket": return "🚀";
      case "star": return "⭐";
      case "heart": return "❤️";
      case "fire": return "🔥";
      case "sparkles": return "✨";
      case "diamond": return "💎";
      case "target": return "🎯";
      case "glow": return "🌟";
      case "bulb": return "💡";
      case "palette": return "🎨";
      case "rainbow": return "🌈";
      case "music": return "🎵";
      case "phone": return "📱";
      case "globe": return "🌍";
      case "gear": return "⚙️";
      case "trophy": return "🏆";
      case "muscle": return "💪";
      case "party": return "🎉";
      case "moon": return "🌙";
      case "quran": return "📖";
      default: return "🚀";
    }
  }

  private int dp(int v) {
    return (int) TypedValue.applyDimension(TypedValue.COMPLEX_UNIT_DIP, v, getResources().getDisplayMetrics());
  }
}
