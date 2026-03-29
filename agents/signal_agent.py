def analyze_signal(data):
    close = data["Close"]

    last = float(close.iloc[-1])
    prev = float(close.iloc[-2])

    change = ((last - prev) / prev) * 100

    if change > 2:
        return "Bullish"
    elif change < -2:
        return "Bearish"
    else:
        return "Neutral"


def volume_signal(data):
    volume = data["Volume"]

    avg_vol = float(volume.tail(20).mean())
    today_vol = float(volume.iloc[-1])

    if today_vol > (1.5 * avg_vol):
        return "High Volume"
    else:
        return "Normal Volume"


def breakout_signal(data):
    high_20 = float(data["High"].tail(20).max())
    last_close = float(data["Close"].iloc[-1])

    if last_close > high_20:
        return "Breakout"
    else:
        return "No Breakout"