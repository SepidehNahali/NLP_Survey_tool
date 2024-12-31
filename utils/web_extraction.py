import requests
from bs4 import BeautifulSoup
import spacy
import re

# Load the spaCy model (for NLP tasks)
nlp = spacy.load('en_core_web_sm')

def extract_title(soup):
    title = None
    if soup.find('h1'):
        title = soup.find('h1').get_text(strip=True)
    elif soup.find('h2'):
        title = soup.find('h2').get_text(strip=True)
    elif soup.find('meta', {'property': 'og:title'}):
        title = soup.find('meta', {'property': 'og:title'})['content']
    elif soup.find('title'):
        title = soup.find('title').get_text(strip=True)
    if not title:
        title = "Untitled Paper"
    return title

def extract_abstract(soup):
    abstract = ""
    abstract_section = soup.find('section', {'data-title': 'Abstract'})
    if abstract_section:
        content_div = abstract_section.find('div', class_='c-article-section__content')
        if content_div:
            paragraphs = content_div.find_all('p')
            abstract = " ".join(p.get_text(strip=True) for p in paragraphs)
    return abstract

def extract_methodology(soup):
    methodology = ""
    keywords = [
        "methodology", "methods", "model evaluation", "model training",
        "model selection", "feature engineering", "hyperparameter tuning",
        "deployment", "approach", "procedure", "technique", "Proposed Work"
    ]
    sections = soup.find_all('section')
    in_methodology = False
    for section in sections:
        title = section.find('h2')
        if title:
            section_title_text = title.get_text().lower()
            if any(keyword in section_title_text for keyword in keywords):
                in_methodology = True
                methodology += str(section)
                continue
        if in_methodology:
            methodology += str(section)
            next_section = section.find_next_sibling('section')
            if next_section and 'h2' in next_section.name:
                break
    return methodology
