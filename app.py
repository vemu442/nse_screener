import streamlit as st
import pandas as pd
from nsepy_screener import get_breakout_stocks

st.set_page_config(page_title="NSEpy Breakout Screener", layout="wide")
st.title("📈 NSEpy Breakout Stock Screener (Top Nifty 100)")

with st.spinner("Fetching breakout stocks..."):
    breakout_stocks = get_breakout_stocks()

if breakout_stocks:
    st.success(f"✅ Found {len(breakout_stocks)} breakout stocks!")
    df = pd.DataFrame(breakout_stocks, columns=["Symbol"])
    st.dataframe(df)
else:
    st.warning("No breakout stocks found or data fetch error.")