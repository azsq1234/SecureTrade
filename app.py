import streamlit as st
import yfinance as yf
from core.engine import TradingEngine

st.set_page_config(page_title="Nexus-Trade AI", layout="centered")

st.title("🤖 Nexus-Trade AI")
st.subheader("منصة التداول الذكية")

pair = st.selectbox("اختر زوج العملات:", ["EURUSD=X", "GBPUSD=X", "JPY=X"])

if st.button("بدء تحليل Nexus-Trade"):
    with st.spinner('جاري معالجة البيانات...'):
        data = yf.Ticker(pair).history(period="1d", interval="1m")
        engine = TradingEngine(data)
        engine.calculate_indicators()
        signal = engine.check_signal()
        
        if signal:
            st.success(f"### إشارة دخول: {signal}")
        else:
            st.info("لا توجد إشارة قوية حالياً. السوق هادئ.")
        
        st.line_chart(data['close'])