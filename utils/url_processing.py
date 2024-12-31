import urllib.parse
from urllib.parse import urlparse, parse_qs

def clean_and_filter_urls(html_file_path):
    with open(html_file_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

    cleaned_links = []
    for a in soup.find_all("a", href=True):
        original_url = a['href']
        parsed_url = urlparse(original_url)
        if parsed_url.netloc == "www.google.com" and "url" in parsed_url.path:
            query_params = parse_qs(parsed_url.query)
            actual_url = query_params.get("q", [original_url])[0]
            cleaned_links.append(actual_url)
        else:
            cleaned_links.append(original_url)

    unique_links = list(dict.fromkeys(cleaned_links))
    return unique_links
