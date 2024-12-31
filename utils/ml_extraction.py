import re
from collections import defaultdict
from text_processing import preprocess_text

# Define algorithm and model types
algorithm_types = {
    'supervised': ['linear regression', 'logistic regression', 'svm', 'decision tree'],
    'unsupervised': ['k-means', 'dbscan', 'hierarchical clustering'],
    'semi-supervised': ['self-training', 'co-training'],
    'reinforcement': ['q-learning', 'ppo', 'ddpg']
}

model_types = {
    'neural networks': ['cnn', 'rnn', 'transformer'],
    'tree-based': ['xgboost', 'random forest', 'gradient boosting'],
    'ensemble': ['bagging', 'stacking']
}

# Function to classify ML algorithms in text
def classify_ml_algorithms(text):
    doc = preprocess_text(text)
    classified = defaultdict(list)

    for token in doc:
        for algo_type, algo_list in algorithm_types.items():
            if token.text.lower() in map(str.lower, algo_list):
                classified[algo_type].append(token.text)

    for key in classified:
        classified[key] = list(set(classified[key]))

    return classified

# Function to extract specific ML models
def extract_model_types(text):
    doc = preprocess_text(text)
    models_found = defaultdict(list)

    for token in doc:
        token_text = token.text.lower()
        for model_family, model_list in model_types.items():
            for model in model_list:
                if re.search(rf'\b{model.lower()}\b', token_text):
                    models_found[model_family].append(model)

    for key in models_found:
        models_found[key] = list(set(models_found[key]))

    return models_found
