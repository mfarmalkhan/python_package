import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from functools import reduce

class TextProcessor:
    def __init__(self, extra_stopwords=None):
        self.extra_stopwords = extra_stopwords or []
        self.stop_words = stopwords.words('english') + [word.lower() for word in self.extra_stopwords]

    def remove_punctuation(self, text):
        """
        Remove punctuation characters from the text using regular expressions.

        Parameters:
            text (str): The input text from which punctuation characters will be removed.

        Returns:
            str: The text with punctuation characters removed.
        """
        return re.sub('\W+', ' ', text)

    def tokenize(self, text):
        """
        Tokenize the text into words.

        Parameters:
            text (str): The input text to be tokenized.

        Returns:
            List[str]: A list of tokens (words) extracted from the text.
        """
        return word_tokenize(text)

    def remove_stopwords(self, text):
        """
        Remove stopwords from the text.

        Parameters:
            text (str): The input text from which stopwords will be removed.

        Returns:
            List[str]: A list of tokens (words) with stopwords removed.
        """
        tokens = self.tokenize(text)
        filtered_tokens = [word for word in tokens if not word.lower() in self.stop_words]
        return filtered_tokens

    def stemming(self, text):
        """
        Perform stemming on the text.

        Parameters:
            text (str): The input text to be stemmed.

        Returns:
            str: The text with words stemmed using the Porter stemming algorithm.
        """
        ps = PorterStemmer()
        stemmed_sentence = reduce(lambda x, y: x + " " + ps.stem(y), self.tokenize(text), "")
        return stemmed_sentence

    def lemmatization(self, text):
        """
        Perform lemmatization on the text.

        Parameters:
            text (str): The input text to be lemmatized.

        Returns:
            str: The text with words lemmatized using the WordNet lemmatizer.
        """
        lemmatizer = WordNetLemmatizer()
        lem_sentence = reduce(lambda x, y: x + " " + lemmatizer.lemmatize(y), self.tokenize(text), "")
        return lem_sentence

