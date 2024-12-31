import spacy

def preprocess_text(text):
    """Preprocess text by tokenizing and removing unnecessary characters."""
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    tokens = [token.text for token in doc if not token.is_stop and not token.is_punct]
    return " ".join(tokens)
