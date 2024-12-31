from utils.ml_extraction import classify_ml_algorithms, extract_model_types

def test_classify_ml_algorithms():
    text = "We used linear regression and k-means clustering."
    result = classify_ml_algorithms(text)
    assert "linear regression" in result["supervised"]
    assert "k-means" in result["unsupervised"]

def test_extract_model_types():
    text = "We experimented with BERT and ResNet architectures."
    result = extract_model_types(text)
    assert "BERT" in result["transformers"]
    assert "ResNet" in result["cnn"]
