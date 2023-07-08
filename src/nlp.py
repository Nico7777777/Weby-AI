import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

texts = [
    "deploy",
    "host",
    "release",
    "launch",
    "run",
]

def nlp_clasificator(text):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)
    query_vector = vectorizer.transform([text])
    query_similarity_scores = cosine_similarity(query_vector, X)
    most_similar_index = query_similarity_scores.argmax()
    similarity_score = query_similarity_scores[0, most_similar_index]

    return similarity_score