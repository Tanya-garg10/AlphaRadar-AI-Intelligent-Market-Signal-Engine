def make_decision(price, volume, breakout, context):
    score = 0

    # 📈 Price
    if price == "Bullish":
        score += 2
    elif price == "Bearish":
        score -= 2

    # 📊 Volume
    if volume == "High Volume":
        score += 1

    # 🚀 Breakout
    if breakout == "Breakout":
        score += 2

    # 🧠 RSI Context
    if context == "Oversold":
        score += 2
    elif context == "Overbought":
        score -= 2

    # 🎯 Decision
    if score >= 4:
        decision = "🚀 Strong Buy"
    elif score == 3:
        decision = "👍 Buy"
    elif score == 2:
        decision = "👀 Watch"
    elif score == 1:
        decision = "Hold"
    else:
        decision = "⚠️ Avoid"

    return decision, score