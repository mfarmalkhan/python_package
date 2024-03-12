import setuptools
import nltk

# Function to download NLTK resources during installation
def download_nltk_resources():
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')

download_nltk_resources()

setuptools.setup()

