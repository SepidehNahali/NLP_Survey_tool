from cleantext import clean

def clean_text_field(text):
    text = text.replace('\n', ' ').replace('\t', ' ').replace('IEEE', ' ').replace('Conference', ' ')
    return clean(
        text,
        lower=False, no_urls=True, no_emails=True, no_phone_numbers=True, no_currency_symbols=True,
        replace_with_url="<URL>", replace_with_email="<EMAIL>", replace_with_phone_number="<PHONE>"
    )
