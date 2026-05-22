from pathlib import Path
import joblib

BASE_DIR = Path(__file__).resolve().parent

#Load trained model & vectorizer
model = joblib.load(BASE_DIR / "intent_model.pkl")
vectorizer = joblib.load(BASE_DIR / "vectorizer.pkl")

#CONFIDENCE THRESHOLD (tune this if needed)
CONFIDENCE_THRESHOLD = 0.35

def predict_intent(text: str):
    """
    Returns: (intent, confidence)
    If confidence is too low → returns ("unknown", confidence)
    """

    if not text or not text.strip():
        return "unknown", 0.0

    #Normalize input
    cleaned_text = text.strip().lower()

    #Vectorize
    x = vectorizer.transform([cleaned_text])

    #Get probabilities
    probs = model.predict_proba(x)[0]
    max_confidence = float(max(probs))

    #Get predicted intent
    intent = model.predict(x)[0]

    # 🔥 IMPORTANT: Confidence check
    if max_confidence < CONFIDENCE_THRESHOLD:
        return "unknown", max_confidence

    return intent, max_confidence
