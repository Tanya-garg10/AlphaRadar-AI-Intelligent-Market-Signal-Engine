def analyze_signal(data):
    if data is None or data.empty or len(data) < 2:
        return "Neutral"

    close = data["Close"]

    try:
        last = float(close.iloc[-1])
        prev = float(close.iloc[-2])
    except:
        return "Neutral"

    change = ((last - prev) / prev) * 100

    if change > 2:
        return "Bullish"
    elif change < -2:
        return "Bearish"
    else:
        return "Neutral"


def volume_signal(data):
    if data is None or data.empty or len(data) < 20:
        return "Normal Volume"

    volume = data["Volume"]

    try:
        avg_vol = float(volume.tail(20).mean())
        today_vol = float(volume.iloc[-1])
    except:
        return "Normal Volume"

    if today_vol > (1.5 * avg_vol):
        return "High Volume"
    else:
        return "Normal Volume"


def breakout_signal(data):
    if data is None or data.empty or len(data) < 20:
        return "No Breakout"

    try:
        high_20 = float(data["High"].tail(20).max())
        last_close = float(data["Close"].iloc[-1])
    except:
        return "No Breakout"

    if last_close > high_20:
        return "Breakout"
    else:
        return "No Breakout"
