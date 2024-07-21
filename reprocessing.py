# Import necessary libraries
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    """
    Preprocesses the input text by tokenizing and removing stopwords.
    """
    # Tokenization using SpaCy
    doc = nlp(text)
    tokens = [token.text for token in doc]
    
    # Remove stopwords using NLTK
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
    
    return ' '.join(filtered_tokens)
