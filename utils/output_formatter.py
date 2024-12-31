def clean_and_format_results(processed_results):
    """Filter out empty lists and format results."""
    cleaned_results = {}
    for item in processed_results:
        url = item["url"]

        cleaned_algorithms = {key: val for key, val in item["classified_algorithms"].items() if val}
        cleaned_models = {key: val for key, val in item["model_types_found"].items() if val}

        if cleaned_algorithms or cleaned_models:
            cleaned_results[url] = {
                "Classified Algorithms": cleaned_algorithms,
                "Model Types": cleaned_models
            }

    return cleaned_results
