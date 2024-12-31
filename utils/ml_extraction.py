import re

algorithm_types = {
    "supervised": ["linear regression", "decision tree", "svm"],
    "unsupervised": ["k-means", "pca"],
    "semi-supervised": ["self-training", "co-training"],
    "reinforcement": ["q-learning", "policy gradient"]
}

model_types = {
    "transformers": ["BERT", "GPT"],
    "cnn": ["ResNet", "VGG"],
    "rnn": ["LSTM", "GRU"]
}

def classify_ml_algorithms(text):
    """Classify ML algorithms in the text by type."""
    results = {key: [] for key in algorithm_types}
    for algo_type, algo_list in algorithm_types.items():
        for algo in algo_list:
            if re.search(rf'\b{algo.lower()}\b', text.lower()):
                results[algo_type].append(algo)
    return results

def extract_model_types(text):
    """Extract specific model names in the text."""
    results = {key: [] for key in model_types}
    for model_family, models in model_types.items():
        for model in models:
            if re.search(rf'\b{model.lower()}\b', text.lower()):
                results[model_family].append(model)
    return results
