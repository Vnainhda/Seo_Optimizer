from bs4 import BeautifulSoup # type: ignore
import requests
import nltk # type: ignore
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer # type: ignore

nltk.download('punkt')

def extract_text_from_url(url):
    """Extracts the main content from a webpage."""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Remove unnecessary tags
    for tag in ['script', 'style', 'meta', 'footer', 'nav']:
        [s.extract() for s in soup.find_all(tag)]

    text = soup.get_text(separator=" ", strip=True)
    return text

def compute_keyword_density(text):
    """Calculates keyword density in the content."""
    words = nltk.word_tokenize(text.lower())
    word_counts = Counter(words)
    total_words = len(words)

    keyword_density = {word: round((count / total_words) * 100, 2) for word, count in word_counts.items()}
    return dict(sorted(keyword_density.items(), key=lambda item: item[1], reverse=True)[:10])

def analyze_seo(url):
    """Performs SEO analysis on a website's content."""
    text = extract_text_from_url(url)

    if not text:
        return {"error": "No content found on the webpage."}

    keyword_density = compute_keyword_density(text)

    return {
        "word_count": len(text.split()),
        "keyword_density": keyword_density,
        "recommendation": "Consider using high-density keywords in titles, headings, and meta descriptions."
    }
