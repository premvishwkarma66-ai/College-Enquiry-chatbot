from core.db import get_db
from sentence_transformers import SentenceTransformer
import numpy as np

#Load embedding model once
model = SentenceTransformer("all-MiniLM-L6-v2")

#Global cache
FAQ_CACHE = {
    "questions": [],
    "answers": [],
    "embeddings": None
}


def load_faq_cache():
    """
    Load FAQ questions and embeddings into memory.
    Call once at app startup or when FAQ is updated.
    """
    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT question, answer FROM faq")
    rows = cur.fetchall()
    conn.close()

    if not rows:
        FAQ_CACHE["questions"] = []
        FAQ_CACHE["answers"] = []
        FAQ_CACHE["embeddings"] = None
        return

    questions = [row["question"] for row in rows]
    answers = [row["answer"] for row in rows]

    embeddings = model.encode(questions, convert_to_tensor=True)

    FAQ_CACHE["questions"] = questions
    FAQ_CACHE["answers"] = answers
    FAQ_CACHE["embeddings"] = embeddings

    print(f"[FAQ CACHE] Loaded {len(questions)} FAQ embeddings")
