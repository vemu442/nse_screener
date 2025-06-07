import streamlit as st
import pandas as pd
from nse_screener import get_breakout_stocks

st.set_page_config(page_title="NSE Breakout Screener", layout="wide")
st.title("📈 NSE Breakout Stock Screener")

with st.spinner("Fetching breakout stocks from NSE..."):
    breakout_stocks = get_breakout_stocks()

if breakout_stocks:
    st.success(f"✅ Found {len(breakout_stocks)} breakout stocks!")
    df = pd.DataFrame(breakout_stocks, columns=["Stock"])
    st.dataframe(df)
else:
    st.warning("No breakout stocks found or data fetch error.")