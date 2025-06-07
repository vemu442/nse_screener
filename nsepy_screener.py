from nsepy import get_history
from datetime import date, timedelta
import pandas as pd

# Sample list from NIFTY 100 (use actual NSE symbols)
nifty_100_symbols = [
    "RELIANCE", "TCS", "INFY", "HDFCBANK", "ICICIBANK", "SBIN", "ITC", "LT", "AXISBANK",
    "HINDUNILVR", "BAJFINANCE", "KOTAKBANK", "BHARTIARTL", "WIPRO", "HCLTECH", "ADANIENT",
    "MARUTI", "ASIANPAINT", "DMART", "ULTRACEMCO"
]

def calculate_sma(df, window=50):
    df["SMA50"] = df["Close"].rolling(window=window).mean()
    return df

def is_breakout(df):
    if df.empty or "SMA50" not in df.columns:
        return False
    latest = df.iloc[-1]
    return latest["Close"] > latest["SMA50"]

def get_breakout_stocks():
    breakout = []
    end = date.today()
    start = end - timedelta(days=120)

    for symbol in nifty_100_symbols:
        try:
            df = get_history(symbol=symbol, start=start, end=end)
            if df.empty:
                continue
            df = calculate_sma(df)
            if is_breakout(df):
                breakout.append(symbol)
        except Exception as e:
            continue

    return breakout