from langdetect import detect, LangDetectException

#LANGUAGE DETECT
def detect_language(text: str) -> str:
    """
    Returns: 'en', 'mr', or 'hi'
    Falls back to English if detection fails.
    """
    try:
        lang = detect(text)
        if lang in ["en", "mr", "hi"]:
            return lang
        return "en"
    except LangDetectException:
        return "en"
