import { useState } from "react";
import { LANGUAGES } from "./constants/languages";
import { translateText } from "./services/translate";
import "./styles/App.css";

function App() {
  const [inputText, setInputText] = useState("");
  const [fromLang, setFromLang] = useState("en");
  const [toLang, setToLang] = useState("en");
  const [translatedText, setTranslatedText] = useState("");
  const [loading, setLoading] = useState(false);

  const handleTranslate = async () => {
    if (!inputText.trim()) {
      return;
    }

    setLoading(true);

    try {
      const text = await translateText(inputText, fromLang, toLang);
      setTranslatedText(text);
    } catch (error) {
      setTranslatedText("Error: Could not translate.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-container">
      <header className="app-header">AI Translator</header>

      <main className="translator-main">
        <div className="translation-panel">
          <div className="panel-section">
            <label className="section-label">Enter your text</label>
            <textarea
              className="input-text"
              placeholder="Type text here..."
              value={inputText}
              onChange={(element) => setInputText(element.target.value)}
            />
          </div>

          <div className="panel-section">
            <label className="section-label">Translation</label>
            <div className="output-box">
              {translatedText ? (
                <p className="output-text">{translatedText}</p>
              ) : (
                <p className="placeholder">Translation will be here...</p>
              )}
            </div>
          </div>
        </div>

        <div className="lang-selectors">
          <div className="lang-select">
            <label>From</label>
            <select
              value={fromLang}
              onChange={(element) => setFromLang(element.target.value)}
            >
              {Object.entries(LANGUAGES).map(([code, name]) => (
                <option key={code} value={code}>
                  {name}
                </option>
              ))}
            </select>
          </div>

          <div className="lang-select">
            <label>To</label>
            <select
              value={toLang}
              onChange={(element) => setToLang(element.target.value)}
            >
              {Object.entries(LANGUAGES).map(([code, name]) => (
                <option key={code} value={code}>
                  {name}
                </option>
              ))}
            </select>
          </div>
        </div>

        <button
          className="translate-btn"
          onClick={handleTranslate}
          disabled={loading}
        >
          {loading ? "Translating..." : "Perform translation"}
        </button>
      </main>
    </div>
  );
}

export default App;
