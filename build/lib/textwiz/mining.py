import math
from collections import Counter
from typing import List

class TextAnalyzer:
    def __init__(self):
        pass

    def bag_of_words(self, documents):
        """
        Generate a Bag of Words representation for a list of documents.

        Parameters:
            documents (List[str]): A list of documents.

        Returns:
            List[List[str]]: Bag of Words representation where each element is a list of words in the document.
        """
        bag_of_words_representation = []

        # BoW for the documents by tokenization and counting
        for document in documents:
            words = document.split()
            word_counts = Counter(words)
            sorted_word_counts = sorted(word_counts.items())
            bag_of_words_representation.append([word for word, _ in sorted_word_counts])

        return bag_of_words_representation

    def generate_ngrams(self, text, n):
        """
        Generate N-grams from a given text.

        Parameters:
            text (str): The input text.
            n (int): The size of the N-grams.

        Returns:
            List[str]: A list of N-grams.
        """
        words = text.split()
        ngrams = [words[i:i+n] for i in range(len(words)-n+1)]
        return [' '.join(ngram) for ngram in ngrams]

    def tf_idf(self, documents):
        """
        Calculate TF-IDF (Term Frequency-Inverse Document Frequency) vectors for a list of documents.

        Parameters:
            documents (List[str]): List of documents.

        Returns:
            List[List[float]]: TF-IDF vectors for each document.
        """
        def calculate_tf(document):
            words = document.split()
            word_counts = Counter(words)
            total_words = len(words)
            tf = {word: word_counts[word] / total_words for word in word_counts}
            return tf

        def calculate_idf(documents, word):
            num_documents_containing_word = sum(1 for document in documents if word in document)
            return math.log(len(documents) / (1 + num_documents_containing_word))

        tfidf_vectors = []
        for document in documents:
            tfidf_vector = []
            tf = calculate_tf(document)
            for word in tf:
                tfidf_score = tf[word] * calculate_idf(documents, word)
                tfidf_vector.append(tfidf_score)
            tfidf_vectors.append(tfidf_vector)

        return tfidf_vectors

    def keyword_extraction_imp(self, text, num_keywords=5):
        """
        Extract the top N keywords from the text based on importance (TF-IDF scores).

        Parameters:
            text (str): Input text.
            num_keywords (int): Number of keywords to extract (default is 5).

        Returns:
            List[str]: List of top keywords.
        """
        tfidf_vectors = self.tf_idf([text])

        words = text.split()
        word_tfidf = {word: tfidf_score for word, tfidf_score in zip(words, tfidf_vectors[0])}
        top_keywords = sorted(word_tfidf, key=word_tfidf.get, reverse=True)[:num_keywords]

        return top_keywords

    def keyword_extraction_freq(self, text, num_keywords=5):
        """
        Extract the top N keywords from the text based on frequency.

        Parameters:
            text (str): Input text.
            num_keywords (int): Number of keywords to extract (default is 5).

        Returns:
            List[str]: List of top keywords.
        """
        words = text.split()
        word_counts = Counter(words)
        top_keywords = [word for word, _ in word_counts.most_common(num_keywords)]

        return top_keywords

    def calculate_text_similarity(self, doc1, doc2):
        """
        Calculate similarity between two documents using cosine similarity of TF-IDF vectors.

        Parameters:
            doc1 (str): The first document.
            doc2 (str): The second document.

        Returns:
            float: The cosine similarity score between the two documents.
        """
        tfidf_vectors = self.tf_idf([doc1, doc2])

        dot_product = sum(a * b for a, b in zip(tfidf_vectors[0], tfidf_vectors[1]))
        magnitude_doc1 = math.sqrt(sum(a ** 2 for a in tfidf_vectors[0]))
        magnitude_doc2 = math.sqrt(sum(b ** 2 for b in tfidf_vectors[1]))
        similarity_score = dot_product / (magnitude_doc1 * magnitude_doc2)

        return similarity_score


