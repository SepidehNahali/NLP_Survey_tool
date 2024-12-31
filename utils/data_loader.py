import os

def load_text_files(directory):
    """Load text files from a directory."""
    texts = {}
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)
            with open(filepath, "r") as file:
                texts[filename] = file.read()
    return texts
