package com.burhan.myapp2;

import android.app.Activity;
import android.graphics.Color;
import android.graphics.drawable.ColorDrawable;
import android.os.Bundle;
import android.webkit.WebView;
import android.webkit.WebSettings;
import android.webkit.WebViewClient;

public class MainActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        
        // Window کا پس منظر سیاہ کریں (white flash سے بچنے کے لیے)
        getWindow().setBackgroundDrawable(
            new ColorDrawable(Color.parseColor("#0a0a1a"))
        );
        
        WebView webView = new WebView(this);
        
        // WebView کا background بھی سیاہ کریں
        webView.setBackgroundColor(Color.parseColor("#0a0a1a"));
        
        WebSettings settings = webView.getSettings();
        settings.setJavaScriptEnabled(true);
        settings.setDomStorageEnabled(true);
        settings.setAllowFileAccess(true);
        settings.setLoadWithOverviewMode(true);
        settings.setUseWideViewPort(true);
        settings.setAllowContentAccess(true);
        
        // WebView transparent سیٹنگ نہ کریں
        webView.setWebViewClient(new WebViewClient());
        webView.loadUrl("file:///android_asset/index.html");
        
        setContentView(webView);
    }
}