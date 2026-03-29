import pandas as pd

def calculate_rsi(data, period=14):
    delta = data["Close"].diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    return float(rsi.iloc[-1])


def get_context(data):
    rsi = calculate_rsi(data)

    if pd.isna(rsi):
        return "Neutral", 50.0

    if rsi > 70:
        return "Overbought", rsi
    elif rsi < 30:
        return "Oversold", rsi
    else:
        return "Neutral", rsi