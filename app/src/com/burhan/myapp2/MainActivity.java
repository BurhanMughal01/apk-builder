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
