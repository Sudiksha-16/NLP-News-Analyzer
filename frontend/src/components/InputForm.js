import React, { useState, useEffect } from "react";
import "./InputForm.css";

function InputForm() {
  const [text, setText] = useState("");
  const [result, setResult] = useState("");
  const [darkMode, setDarkMode] = useState(false);

  useEffect(() => {
    document.body.className = darkMode ? "dark" : "";
  }, [darkMode]);

  const handleClick = async (endpoint) => {
    if (!text.trim()) return alert("Please enter a sentence");

    try {
      const res = await fetch(`http://localhost:5000/${endpoint}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text }),
      });
      const data = await res.json();
      setResult(data.result);
    } catch (err) {
      console.error("Error:", err);
      alert("Failed to connect to backend. Is Flask running?");
    }
  };

  return (
    <div className="container">
      <button className="toggle-btn" onClick={() => setDarkMode(!darkMode)}>
        {darkMode ? "☀️ Light" : "🌙 Dark"}
      </button>

      <div className="card">
        <h2 className="title">NLP Sentence Analyzer</h2>
        <input
          type="text"
          placeholder="Enter a sentence..."
          value={text}
          onChange={(e) => setText(e.target.value)}
          className="input-box"
        />

        <div className="button-group">
          <button className="btn" onClick={() => handleClick("analyze_sentiment")}>
            Sentiment
          </button>
          <button className="btn" onClick={() => handleClick("classify_news")}>
            News Category
          </button>
        </div>

        {result && (
          <div className="result">
            Result: <strong>{result}</strong>
          </div>
        )}
      </div>

      <footer className="footer">Designed by Sudiksha</footer>
    </div>
  );
}

export default InputForm;
