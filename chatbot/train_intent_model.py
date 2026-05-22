from pathlib import Path
import json
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

#Resolve absolute chatbot directory safely
BASE_DIR = Path(__file__).resolve().parent

#THIS SHOULD BE MUST PRESENT IN FOLDER
DATASET_PATH = BASE_DIR / "intent_dataset.json"
MODEL_PATH = BASE_DIR / "intent_model.pkl"
VEC_PATH = BASE_DIR / "vectorizer.pkl"

print("Chatbot dir =", BASE_DIR)
print("Dataset path =", DATASET_PATH)

#Ensure folder exists (prevents OS write errors)
BASE_DIR.mkdir(parents=True, exist_ok=True)

#Load dataset
with open(DATASET_PATH, "r") as f:
    data = json.load(f)

X_text, y_intent = [], []

for item in data:
    intent = item["intent"]
    for pattern in item["patterns"]:
        X_text.append(pattern.lower())
        y_intent.append(intent)

#Train model
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(X_text)

model = LogisticRegression()
model.fit(X, y_intent)

#Save model + vectorizer (absolute paths)
print("Saving model to =", MODEL_PATH)
print("Saving vectorizer to =", VEC_PATH)

joblib.dump(model, MODEL_PATH)
joblib.dump(vectorizer, VEC_PATH)

print("✔ ML intent model trained successfully")
