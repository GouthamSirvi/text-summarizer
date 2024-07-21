from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def generate_summary(text):
    """
    Generates a summary by ranking sentences based on TF-IDF scores.
    """
    # Split the text into sentences
    sentences = text.split('. ')
    
    # Calculate TF-IDF scores
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(sentences)
    
    # Summarization logic
    scores = np.array(X.sum(axis=1)).flatten()
    ranked_sentences = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)
    
    # Select top 3 sentences as the summary
    summary = ' '.join([sentences[i] for i in ranked_sentences[:3]])
    return summary
