import React, { useState } from "react";
import "./App.css";

function App() {
  const [stock, setStock] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const analyzeStock = async () => {
    if (!stock) return;

    setLoading(true);
    setResult(null);

    try {
      const res = await fetch(`https://alpharadar-ai-intelligent-market-signal.onrender.com/analyze/${stock}`);
      const data = await res.json();
      console.log(data); // 🔥 debug

      setResult(data);
    } catch (err) {
      console.error("Error:", err);
      setResult({ error: "Backend not reachable" });
    }

    setLoading(false);
  };

  return (
    <div className="app">
      <h1>🚀 AlphaRadar AI</h1>

      <input
        type="text"
        placeholder="Enter stock (e.g. INFY.NS)"
        value={stock}
        onChange={(e) => setStock(e.target.value.toUpperCase())}
      />

      <button onClick={analyzeStock}>
        {loading ? "Analyzing..." : "Analyze"}
      </button>

      {/* 🔥 RESULT CARD */}
      {result && !result.error && (
        <div className="card">
          <h2>📊 AI Market Alert</h2>

          <p><strong>Stock:</strong> {result.stock}</p>
          <p><strong>Price:</strong> {result.price}</p>
          <p><strong>Volume:</strong> {result.volume}</p>
          <p><strong>Breakout:</strong> {result.breakout}</p>
          <p><strong>RSI:</strong> {Math.round(result.rsi)}</p>
          <p><strong>Context:</strong> {result.context}</p>
          <p><strong>Portfolio:</strong> {result.portfolio}</p>

          <h3>{result.decision}</h3>

          <div className="confidence">
            Confidence: {result.confidence}%
            <div className="bar">
              <div
                className="fill"
                style={{ width: `${result.confidence}%` }}
              ></div>
            </div>
          </div>
        </div>
      )}

      {/* ❌ ERROR */}
      {result && result.error && (
        <div className="error">
          ❌ {result.error}
        </div>
      )}
    </div>
  );
}

export default App;
