from typing import List
from collections import Counter
import math

def bag_of_words(documents: List[str]) -> List[List[str]]:
   
    bag_of_words_representation = []

    # BoW for the documents by tokenization and counting
    for document in documents:
        words = document.split()
        word_counts = Counter(words)
        sorted_word_counts = sorted(word_counts.items())
        bag_of_words_representation.append([word for word, _ in sorted_word_counts])

    return bag_of_words_representation


def generate_ngrams(text: str, n: int) -> List[str]:
    
    words = text.split()
    ngrams = [words[i:i+n] for i in range(len(words)-n+1)]
    return [' '.join(ngram) for ngram in ngrams]


def tf_idf(documents: List[str]) -> List[List[float]]:
   
    # Function to calculate term frequency (TF) for a document
    def calculate_tf(document):
        words = document.split()
        word_counts = Counter(words)
        total_words = len(words)
        tf = {word: word_counts[word] / total_words for word in word_counts}
        return tf

    # Function to calculate inverse document frequency (IDF) for all documents
    def calculate_idf(documents, word):
        num_documents_containing_word = sum(1 for document in documents if word in document)
        return math.log(len(documents) / (1 + num_documents_containing_word))

    # Calculate TF-IDF vectors
    tfidf_vectors = []
    for document in documents:
        tfidf_vector = []
        tf = calculate_tf(document)
        for word in tf:
            tfidf_score = tf[word] * calculate_idf(documents, word)
            tfidf_vector.append(tfidf_score)
        tfidf_vectors.append(tfidf_vector)

    return tfidf_vectors

def keyword_extraction_imp(text: str, num_keywords: int = 5) -> List[str]:
    
    # Calculate TF-IDF vectors for the input text
    tfidf_vectors = tf_idf([text])

    words = text.split()
    word_tfidf = {word: tfidf_score for word, tfidf_score in zip(words, tfidf_vectors[0])}
    top_keywords = sorted(word_tfidf, key=word_tfidf.get, reverse=True)[:num_keywords]

    return top_keywords


def keyword_extraction_freq(text: str, num_keywords: int = 5) -> List[str]:

    words = text.split()
    word_counts = Counter(words)
    top_keywords = [word for word, _ in word_counts.most_common(num_keywords)]

    return top_keywords


def calculate_text_similarity(doc1: str, doc2: str) -> float:
   
    # Calculate TF-IDF vectors for the two documents
    tfidf_vectors = tf_idf([doc1, doc2])

    # Calculate cosine similarity between the TF-IDF vectors
    dot_product = sum(a * b for a, b in zip(tfidf_vectors[0], tfidf_vectors[1]))
    magnitude_doc1 = math.sqrt(sum(a ** 2 for a in tfidf_vectors[0]))
    magnitude_doc2 = math.sqrt(sum(b ** 2 for b in tfidf_vectors[1]))
    similarity_score = dot_product / (magnitude_doc1 * magnitude_doc2)

    return similarity_score



# documents = [
#     "This is the first document.",
#     "This document is the second document.",
#     "And this is the third one.",
#     "Is this the first document?",
# ]

# print(bag_of_words(documents))

# print(tfidf(documents))

# text = "Natural language processing (NLP) is a subfield of linguistics, computer science, and artificial intelligence concerned with the interactions between computers and human language, in particular how to program computers to process and analyze large amounts of natural language data."
# keywords = keyword_extraction_freq(text, num_keywords=5)
# print(keywords)

# doc1 = "Natural language processing (NLP) is a subfield of linguistics."
# doc2 = "Machine learning is a subset of artificial intelligence (AI)."
# similarity_score = calculate_text_similarity(doc1, doc2)
# print("Similarity between the two documents:", similarity_score)

# text = "Natural language processing (NLP) is a subfield of linguistics, computer science, and artificial intelligence concerned with the interactions between computers and human language, in particular how to program computers to process and analyze large amounts of natural language data."
# ngrams = generate_ngrams(text, 4)
# print(ngrams)
