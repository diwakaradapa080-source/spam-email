from pathlib import Path
import re
# pyrefly: ignore[missing-import]
import joblib
import pandas as pd
# pyrefly: ignore[missing-import]
from flask import Flask, redirect, render_template, request, session, url_for
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "spam.csv"
MODEL_PATH = BASE_DIR / "model" / "spam_classifier.joblib"

app = Flask(__name__)
app.config["SECRET_KEY"] = "spam-email-classifier-demo-key"

SUSPICIOUS_KEYWORDS = {
    "free": {"free"},
    "winner": {"winner", "winners"},
    "claim": {"claim", "claims", "claimed"},
    "urgent": {"urgent", "urgently", "urgency"},
    "click": {"click", "clicking", "clicks"},
    "limited": {"limited"},
    "offer": {"offer", "offers"},
    "prize": {"prize", "prizes"},
    "lottery": {"lottery", "lotteries"},
    "cash": {"cash"},
    "bonus": {"bonus", "bonuses"},
    "verify": {"verify", "verification", "verified"},
    "account": {"account", "accounts"},
    "invoice": {"invoice", "invoices"},
    "password": {"password", "passwords"},
    "bank": {"bank", "banking"},
    "guaranteed": {"guaranteed", "guarantee"},
    "act": {"act", "action"},
    "now": {"now"},
}


def clean_text(text):
    """Basic, dependency-free text cleanup."""
    text = str(text).lower()
    text = re.sub(r"http\S+|www\.\S+", " URL ", text)
    text = re.sub(r"[^a-z0-9\s']", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def get_suspicious_keywords(text):
    """Return suspicious spam terms found in a message."""
    cleaned = clean_text(text)
    tokens = set(re.findall(r"[a-z0-9']+", cleaned))
    keywords = []
    seen = set()

    for keyword, aliases in SUSPICIOUS_KEYWORDS.items():
        if any(alias in tokens for alias in aliases):
            keywords.append(keyword)
            seen.add(keyword)

    for phrase in ["click here", "act now", "limited time", "claim now"]:
        if phrase in cleaned and phrase not in seen:
            keywords.append(phrase)
            seen.add(phrase)

    return keywords

def train_model():
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA_PATH}")
    df = pd.read_csv(DATA_PATH)
    required = {"label", "message"}
    if not required.issubset(df.columns):
        raise ValueError("data/spam.csv must contain 'label' and 'message' columns.")
    df = df.dropna(subset=["label", "message"])
    df["label"] = df["label"].astype(str).str.lower().str.strip()
    df = df[df["label"].isin(["spam", "ham"])]
    if len(df) < 4 or df["label"].nunique() < 2:
        raise ValueError("Dataset needs at least 4 rows and both spam and ham labels.")

    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer(
            preprocessor=clean_text,
            stop_words="english",
            ngram_range=(1, 2),
            max_features=10000
        )),
        ("classifier", MultinomialNB(alpha=0.5))
    ])
    pipeline.fit(df["message"].astype(str), df["label"])
    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(pipeline, MODEL_PATH)
    return pipeline

def get_model():
    if not MODEL_PATH.exists():
        return train_model()
    try:
        return joblib.load(MODEL_PATH)
    except Exception:
        # Rebuild a stale/corrupt model using the included dataset.
        return train_model()

model = None

@app.route("/", methods=["GET", "POST"])
def home():
    global model
    result = None
    confidence = None
    email_text = ""
    error = None
    suspicious_keywords = []

    if request.method == "POST":
        email_text = request.form.get("email_text", "").strip()
        if not email_text:
            error = "Please enter an email message."
        elif len(email_text) > 20000:
            error = "Please keep the message under 20,000 characters."
        else:
            try:
                if model is None:
                    model = get_model()
                prediction = model.predict([email_text])[0]
                probabilities = model.predict_proba([email_text])[0]
                confidence = round(float(max(probabilities)) * 100, 2)
                result = "SPAM" if prediction == "spam" else "NOT SPAM"
                suspicious_keywords = get_suspicious_keywords(email_text)

                history = session.get("history", [])
                history_entry = {
                    "text": email_text[:140],
                    "label": result,
                    "confidence": confidence,
                    "keywords": suspicious_keywords[:5],
                }
                session["history"] = [history_entry] + history[:4]
            except Exception as exc:
                error = f"Prediction failed: {exc}"

    recent_checks = session.get("history", [])

    return render_template(
        "index.html",
        result=result,
        confidence=confidence,
        email_text=email_text,
        error=error,
        suspicious_keywords=suspicious_keywords,
        recent_checks=recent_checks,
    )


@app.route("/clear-history")
def clear_history():
    session.pop("history", None)
    return redirect(url_for("home"))


@app.route("/health")
def health():
    return {"status": "ok", "message": "Spam Email Classifier is running."}

if __name__ == "__main__":
    # Train once at startup so the first prediction is ready.
    model = get_model()
    app.run(host="127.0.0.1", port=5000, debug=True)
