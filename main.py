from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from agents.data_agent import get_stock_data
from agents.signal_agent import analyze_signal, volume_signal, breakout_signal
from agents.context_agent import get_context
from agents.portfolio_agent import check_portfolio
from agents.decision_agent import make_decision

app = FastAPI()

# ✅ CORS (frontend connect ke liye)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "🚀 AlphaRadar AI Running"}

@app.get("/analyze/{stock}")
def analyze(stock: str):
    try:
        portfolio = ["INFY.NS", "RELIANCE.NS"]

        # 📊 Step 1: Get Data
        data = get_stock_data(stock)

        # 📈 Step 2: Signals
        price_sig = analyze_signal(data)
        vol_sig = volume_signal(data)
        breakout = breakout_signal(data)

        # 🧠 Step 3: Context (RSI)
        context, rsi = get_context(data)

        # 💼 Step 4: Portfolio check
        portfolio_status = check_portfolio(portfolio, stock)

        # 🎯 Step 5: Decision
        decision, score = make_decision(price_sig, vol_sig, breakout, context)

        # ✅ FIX: NaN handling
        if rsi != rsi:
            rsi = 50

        # 🎯 Confidence (improved)
        confidence = round(min(max(((score + 4) / 8) * 100, 0), 100), 2)
        
        return {
            "stock": stock,
            "price": price_sig,
            "volume": vol_sig,
            "breakout": breakout,
            "rsi": float(rsi),
            "context": context,
            "portfolio": portfolio_status,
            "decision": decision,
            "confidence": confidence
        }

    except Exception as e:
        import traceback
        return {
            "error": str(e),
            "trace": traceback.format_exc()
        }