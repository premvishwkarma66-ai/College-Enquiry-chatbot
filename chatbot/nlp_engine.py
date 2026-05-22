from chatbot.rules import rule_based_reply
from chatbot.faq_handler import fetch_faq_answer
from chatbot.ml_intent import predict_intent
from chatbot.lang_detect import detect_language
from core.db import get_db

def save_log(user_text, reply, intent, confidence):
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO enquiry_logs (user_query, bot_reply, intent, confidence)
        VALUES (?, ?, ?, ?)
    """, (user_text, reply, intent, confidence))

    conn.commit()
    conn.close()


def process_user_message(user_text: str):
    """
    Full pipeline:
    1) Rule-based
    2) FAQ match
    3) ML intent classification (with confidence threshold)
    """
    user_lang = detect_language(user_text)

    #Normalize input
    if not user_text or not user_text.strip():
        reply = "Please type a valid question."
        meta = {"intent": "empty_input", "confidence": 0.0}
        save_log(user_text, reply, meta["intent"], meta["confidence"])
        return reply, meta

    user_text = user_text.strip()


    #1) RULE-BASED REPLY (highest priority)
    rb_reply = rule_based_reply(user_text)
    if rb_reply:
        meta = {"intent": "rule_based", "confidence": 1.0}
        save_log(user_text, rb_reply, meta["intent"], meta["confidence"])
        return rb_reply, meta


    #2) FAQ DATABASE MATCH
    faq = fetch_faq_answer(user_text)
    if faq:
        # Expecting: {"answer": "...", "score": 0.xx}
        meta = {
            "intent": "faq",
            "confidence": float(faq.get("score", 0.0))
        }
        save_log(user_text, faq["answer"], meta["intent"], meta["confidence"])
        return faq["answer"], meta


    #3) ML INTENT CLASSIFIER (WITH CONFIDENCE)
    intent, confidence = predict_intent(user_text)

    #CASE A: UNKNOWN INTENT (LOW CONFIDENCE)
    if intent == "unknown":
        if user_lang == "mr":
            reply = "माफ करा, मला तुमचा प्रश्न नीट समजला नाही. कृपया थोडा स्पष्ट करून सांगाल का?"
        elif user_lang == "hi":
            reply = "माफ़ कीजिए, मुझे आपका प्रश्न स्पष्ट नहीं समझ आया। कृपया इसे थोड़ा और स्पष्ट करें।"
        else:
            reply = (
                "I'm not fully sure about your question. "
                "Could you please rephrase or give more details?"
            )

        meta = {"intent": "unknown", "confidence": confidence}
        save_log(user_text, reply, meta["intent"], meta["confidence"])
        return reply, meta

        meta = {"intent": "unknown", "confidence": confidence}
        save_log(user_text, reply, meta["intent"], meta["confidence"])
        return reply, meta

    #CASE B: KNOWN INTENT BUT NO DIRECT ANSWER
    reply = (
        f"I understand your query is related to **{intent.replace('_', ' ')}**. "
        "I don’t have a direct answer in my FAQ right now, "
        "but your query has been recorded for improvement."
    )

    meta = {"intent": intent, "confidence": confidence}
    save_log(user_text, reply, meta["intent"], meta["confidence"])
    return reply, meta
