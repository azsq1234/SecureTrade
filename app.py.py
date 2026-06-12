import streamlit as st
from core.engine import engine
# سنقوم بجلب بيانات وهمية سريعة هنا للتمثيل
import numpy as np
import pandas as pd

st.set_page_config(page_title="Nexus-Trade Terminal", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #050505; }
    .signal-card { 
        background: linear-gradient(135deg, #1e1e1e, #0a0a0a);
        border: 1px solid #444; border-radius: 12px;
        padding: 20px; margin-bottom: 15px; text-align: center;
    }
    .signal-title { color: #f0f0f0; font-size: 24px; font-weight: bold; }
    .buy { color: #00ff88; font-size: 30px; font-weight: 900; }
    .sell { color: #ff4b4b; font-size: 30px; font-weight: 900; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: white;'>Nexus-Trade Terminal</h1>", unsafe_allow_html=True)

# محاكاة لبيانات السوق
mock_data = {'close': np.random.uniform(100, 105, 50)}

if st.button("تحديث الإشارات اللحظية"):
    signal = engine.analyze(mock_data)
    
    color = "buy" if signal == "شراء" else "sell"
    st.markdown(f"""
        <div class="signal-card">
            <div class="signal-title">AUD/JPY - OTC</div>
            <div class="{color}">{signal}</div>
            <div style="color: #888;">مدة الصفقة: 1 دقيقة</div>
        </div>
    """, unsafe_allow_html=True)
else:
    st.info("نظام Nexus-Trade جاهز للعمل. اضغط للتحديث.")