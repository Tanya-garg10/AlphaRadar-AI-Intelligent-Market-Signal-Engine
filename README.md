# 🚀 AlphaRadar AI  

## 🧠 Overview  
AlphaRadar AI is an advanced multi-agent AI system designed to help Indian retail investors make smarter, data-driven decisions.  

It transforms raw stock market data into **actionable insights** using autonomous agents — moving beyond news summarization to real signal detection.

## 💡 Problem  
Most retail investors:
- Rely on tips or social media noise  
- Miss important filings and technical signals  
- Struggle to interpret charts and indicators  
- Make decisions based on gut feeling  

## ⚡ Solution  
AlphaRadar AI acts as an **intelligent market signal engine** that:

- 📊 Detects price, volume & breakout signals  
- 📉 Analyzes technical indicators (RSI, trends)  
- 🧠 Adds contextual understanding  
- 💼 Evaluates portfolio exposure  
- 🎯 Generates actionable decisions (Buy / Hold / Avoid)  
- 📊 Assigns confidence scores  

## 🔁 Autonomous Agent Pipeline  

```

Data → Signal Detection → Context Enrichment → Portfolio Check → Decision

```

### 🤖 Agents:
- **Data Agent** → Fetches stock market data  
- **Signal Agent** → Detects price, volume & breakout signals  
- **Context Agent** → Adds RSI & technical context  
- **Portfolio Agent** → Checks user exposure  
- **Decision Agent** → Generates final recommendation  

## 🎯 Key Features  

- ✅ Real-time stock analysis (NSE stocks)  
- ✅ Multi-signal decision engine  
- ✅ Portfolio-aware alerts  
- ✅ Confidence scoring system  
- ✅ Clean UI dashboard  
- ✅ Fully autonomous pipeline  

## 🏗️ Tech Stack  

| Layer | Technology |
|------|-----------|
| Frontend | React.js |
| Backend | FastAPI (Python) |
| Data Source | yFinance API |
| Architecture | Multi-Agent System |

## 📊 Example Output  

```

📊 AI MARKET ALERT

Stock: INFY.NS
Price: Neutral
Volume: Normal Volume
Breakout: No Breakout
RSI: 41.9 (Neutral)

💼 Portfolio: ⚠️ High Exposure

🎯 Decision: Hold
📊 Confidence: 40%

````

## 🚀 How to Run Locally  

### 🔹 Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
````

### 🔹 Frontend

```bash
cd frontend
npm install
npm start
```

## 🌐 API Endpoint

```
GET /analyze/{stock}
```

Example:

```
/analyze/INFY.NS
```

## 📈 Impact

* Reduces dependency on unreliable market tips
* Converts complex financial data into simple decisions
* Improves investor confidence & decision quality
* Bridges the gap between data and action

## ⚠️ Disclaimer

This project provides AI-based insights for educational purposes only.
It does not constitute financial advice.

## 🔥 Future Improvements

* Live market alerts (real-time streaming)
* Advanced technical indicators (MACD, Bollinger Bands)
* AI-powered portfolio optimization
* News + sentiment integration
* Voice-based AI assistant

Built with ❤️
