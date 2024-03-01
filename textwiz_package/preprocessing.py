import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
# nltk.download('punkt')
from functools import reduce
from nltk.stem import WordNetLemmatizer


def remove_punctuation(text):
    
    """
    Remove punctuation characters from the text using regular expressions.

    Parameters:
        text (str): The input text from which punctuation characters will be removed.

    Returns:
        str: The text with punctuation characters removed.
    """
    
    # use regex here
    return re.sub('\W+', ' ', text)

def tokenize(text):
    
    """
    Tokenize the text into words.

    Parameters:
        text (str): The input text to be tokenized.

    Returns:
        List[str]: A list of tokens (words) extracted from the text.
    """
    
    return text.split()

def remove_stopwords(text, extra_words = None):
    
    """
    Remove stopwords from the text.

    Parameters:
        text (str): The input text from which stopwords will be removed.
        extra_words (List[str], optional): Additional words to be considered as stopwords. Defaults to None.

    Returns:
        List[str]: A list of tokens (words) with stopwords removed.
    """
    
    tokens = word_tokenize(text)        
    stop_words = stopwords.words('english')
 
    if extra_words is not None:
        extra_words = [i.lower() for i in extra_words]
        stop_words.extend(extra_words)
    
    filtered_tokens = [word for word in tokens if not word.lower() in stop_words]
    return filtered_tokens        

def stemming(text):
    
    """
    Perform stemming on the text.

    Parameters:
        text (str): The input text to be stemmed.

    Returns:
        str: The text with words stemmed using the Porter stemming algorithm.
    """
    
    tokens = word_tokenize(text)
    ps = PorterStemmer()
    stemmed_sentence = reduce(lambda x, y: x + " " + ps.stem(y), tokens, "")
    return stemmed_sentence

def lemmatization(text):
    
    """
    Perform lemmatization on the text.

    Parameters:
        text (str): The input text to be lemmatized.

    Returns:
        str: The text with words lemmatized using the WordNet lemmatizer.
    """
    
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()
    lem_sentence = reduce(lambda x, y: x + " " + lemmatizer.lemmatize(y), tokens, "")
    return lem_sentence


# sample_text = "Machine learning 3 uses %Python\ extensively a the that better feelings."

# print(tokenize(sample_text))
# print(clean(sample_text))
# print(remove_stopwords(sample_text))
# print(stemming(sample_text))
# print(lemmatization(sample_text))