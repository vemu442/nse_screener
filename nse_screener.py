from nsepython import nse_stock_codes, nse_hist
import pandas as pd
from datetime import datetime, timedelta

def calculate_sma(df, window=50):
    df["SMA50"] = df["Close"].rolling(window=window).mean()
    return df

def is_breakout(df):
    if df.empty or "SMA50" not in df.columns:
        return False
    latest = df.iloc[-1]
    if pd.isna(latest["SMA50"]) or pd.isna(latest["Close"]):
        return False
    return latest["Close"] > latest["SMA50"]

def get_breakout_stocks():
    try:
        stocks = list(nse_stock_codes().keys())
    except Exception as e:
        print("Error fetching NSE stock list:", e)
        return []

    breakout = []
    end_date = datetime.today()
    start_date = end_date - timedelta(days=120)

    for symbol in stocks[:30]:  # Limit for demo
        try:
            df = nse_hist(symbol, start=start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'))
            if df is None or df.empty or 'Close' not in df.columns:
                continue
            df = calculate_sma(df)
            if is_breakout(df):
                breakout.append(symbol)
        except Exception as e:
            continue

    return breakout