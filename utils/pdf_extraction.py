import pdfkit
from PyPDF2 import PdfReader
import re
import os

# Function to convert a URL to a PDF
def url_to_pdf(url, output_pdf):
    try:
        pdfkit.from_url(url, output_pdf)
    except IOError as e:
        print(f"Error converting {url} to PDF: {e}")
        return None
    return output_pdf

def extract_text_from_pdf(pdf_file):
    try:
        # Check if the PDF file exists and is not empty
        if not pdf_file or os.path.getsize(pdf_file) == 0:
            print(f"Invalid PDF file: {pdf_file}")
            return ""

        with open(pdf_file, "rb") as file:
            reader = PdfReader(file)
            text = ''
            for page in reader.pages:
                text += page.extract_text()  # Extract text from each page
            return text
    except Exception as e:  # Handle any exception for PDF reading
        print(f"Error reading PDF {pdf_file}: {e}")
        return ""

# Function to extract the title from the beginning of the text
def extract_title_pdf(text):
    match = re.search(r"^(.*?)(?=\nAbstract|\nIntroduction|\nMethods)", text, re.DOTALL | re.IGNORECASE)
    if match:
        title = match.group(1).strip()
        if len(title.split()) > 5:  # Titles are typically longer than 5 words
            return title
    return None

# Function to extract specific sections from text using multiple start and end keywords
def extract_sections(text, start_keywords, end_keywords):
    for start_key in start_keywords:
        for end_key in end_keywords:
            match = re.search(f"{start_key}.*?{end_key}", text, re.DOTALL | re.IGNORECASE)
            if match:
                return match.group(0).strip()
    return None
