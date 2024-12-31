from utils.text_processing import preprocess_text

def test_preprocess_text():
    text = "This is a test, with punctuation!"
    result = preprocess_text(text)
    assert result == "test punctuation"
