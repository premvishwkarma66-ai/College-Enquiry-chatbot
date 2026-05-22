#chatbot/rules.py

def rule_based_reply(text):
    text = text.lower()

    greetings = ["hi", "hello", "hey", "good morning", "good afternoon", "good evening"]
    thanks_words = ["thank you", "thanks", "thank u"]

    for g in greetings:
        if g in text:
            return "Hello 👋 How can I help you regarding college enquiry?"

    for t in thanks_words:
        if t in text:
            return "You're welcome! Feel free to ask any other questions 🙂"

    # no rule matched
    return None
