from app import clean_text, get_suspicious_keywords


def test_clean_text_removes_urls_and_lowercases():
    text = "Urgent! CLICK HERE: https://example.com!" 
    cleaned = clean_text(text)
    assert "https" not in cleaned
    assert "urgent" in cleaned
    assert "click" in cleaned
    assert "here" in cleaned


def test_get_suspicious_keywords_finds_common_spam_terms():
    text = "Winner winner! Claim your free prize now, click here urgently."
    keywords = get_suspicious_keywords(text)
    assert "winner" in keywords
    assert "claim" in keywords
    assert "free" in keywords
    assert "click" in keywords
    assert "urgent" in keywords
