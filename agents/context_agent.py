import pandas as pd

def calculate_rsi(data, period=14):
    if data is None or data.empty:
        return 50.0   # safe fallback

    delta = data["Close"].diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    # ✅ SAFE extraction
    if rsi is None or rsi.empty:
        return 50.0

    last_value = rsi.iloc[-1]

    # ✅ handle Series / NaN
    if isinstance(last_value, pd.Series):
        last_value = last_value.iloc[0]

    if pd.isna(last_value):
        return 50.0

    return float(last_value)


def get_context(data):
    rsi = calculate_rsi(data)

    if rsi > 70:
        return "Overbought", rsi
    elif rsi < 30:
        return "Oversold", rsi
    else:
        return "Neutral", rsi
