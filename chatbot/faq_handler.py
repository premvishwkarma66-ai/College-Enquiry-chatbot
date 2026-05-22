from sentence_transformers import util
from chatbot.faq_cache import FAQ_CACHE
from chatbot.faq_cache import load_faq_cache

SIMILARITY_THRESHOLD = 0.55


def fetch_faq_answer(user_text: str):
    if not user_text or not user_text.strip():
        return None

    #Ensure cache is loaded
    if FAQ_CACHE["embeddings"] is None:
        load_faq_cache()

    user_embedding = load_faq_cache.__globals__["model"].encode(
        user_text, convert_to_tensor=True
    )

    scores = util.cos_sim(user_embedding, FAQ_CACHE["embeddings"])[0]

    best_idx = scores.argmax().item()
    best_score = scores[best_idx].item()

    if best_score >= SIMILARITY_THRESHOLD:
        return {
            "answer": FAQ_CACHE["answers"][best_idx],
            "score": round(best_score, 2)
        }

    return None

