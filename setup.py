import setuptools

# Function to download NLTK resources during installation
def download_nltk_resources():
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')

download_nltk_resources()

setuptools.setup()

