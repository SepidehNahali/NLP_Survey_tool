from utils.output_formatter import clean_and_format_results

def test_clean_and_format_results():
    processed_results = [
        {
            "url": "sample1",
            "classified_algorithms": {"supervised": ["linear regression"], "unsupervised": []},
            "model_types_found": {"transformers": ["BERT"], "cnn": []},
        }
    ]
    result = clean_and_format_results(processed_results)
    assert "sample1" in result
    assert "linear regression" in result["sample1"]["Classified Algorithms"]["supervised"]
    assert "BERT" in result["sample1"]["Model Types"]["transformers"]
