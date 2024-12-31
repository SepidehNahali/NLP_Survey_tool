from utils.text_processing import preprocess_text
from utils.ml_extraction import classify_ml_algorithms, extract_model_types
from utils.output_formatter import clean_and_format_results
import os
from pdf_extraction import *
from web_extraction import *
from url_processing import *
from text_cleaning import *
from tqdm import tqdm

def process_urls(urls):
    results = {}
    for url in tqdm(urls, desc="Processing URLs", unit="url"):
        abstract1, methodology1, text_content1 = extract_content_with_pdf(url)
        abstract2, methodology2, text_content2 = extract_content_with_soup(url)

        abstract = abstract1 + abstract2
        methodology = methodology1 + methodology2
        text_content = text_content1 + text_content2

        cleaned_abstract = clean_text_field(abstract) if abstract else ''
        cleaned_methodology = clean_text_field(methodology) if methodology else ''
        cleaned_text_content = clean_text_field(text_content) if text_content else ''

        results[url] = {
            "abstract": cleaned_abstract,
            "methodology": cleaned_methodology,
            "text_content": cleaned_text_content
        }
    print(f'Processed {len(results.keys())} URLs.')
    return results

# Example usage
filtered_links = clean_and_filter_urls("/path/to/your/htmlfile.html")
results_dict = process_urls(filtered_links)



def main():
    # Load input sample (replace with actual file loading in practice)
    input_file = "data/input_samples/sample_text.txt"
    with open(input_file, "r") as file:
        text_content = file.read()

    # Preprocess text
    processed_text = preprocess_text(text_content)

    # Extract ML info
    classified_algorithms = classify_ml_algorithms(processed_text)
    model_types_found = extract_model_types(processed_text)

    # Combine and clean results
    processed_results = [
        {
            "url": input_file,  # Replace with dynamic URL or file path
            "classified_algorithms": classified_algorithms,
            "model_types_found": model_types_found,
        }
    ]
    final_results = clean_and_format_results(processed_results)

    # Save or display results
    output_file = "data/processed_output/results.txt"
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w") as file:
        for url, data in final_results.items():
            file.write(f"URL: {url}\n")
            file.write(f"Classified Algorithms: {data['Classified Algorithms']}\n")
            file.write(f"Model Types: {data['Model Types']}\n")
            file.write("-" * 50 + "\n")

if __name__ == "__main__":
    main()
