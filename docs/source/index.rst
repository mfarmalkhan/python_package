.. TextWiz documentation master file, created by
   sphinx-quickstart on Mon Mar  4 16:32:56 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to TextWiz documentation!
===================================

.. toctree::
   :maxdepth: 3
   :caption: Contents:

   Home <self>
   API <modules>
   Example <notebooks/usage_example>

Introduction
------------

The “textwiz” package consists of three main modules: preprocessing, mining, and visuals. Each module contains functions that address specific aspects of text analytics. The project's goal is to offer a user-friendly and efficient toolkit for common text processing and mining tasks.


Features
--------


Preprocessing steps
--------------------

- Tokenization: Convert text into tokens.
- Remove special characters: Eliminate non-alphanumeric characters.
- Remove stopwords: Filter out common words that do not carry significant meaning.
- Stemming: Reduce words to their base or root form.
- Lemmatization: Normalize words to their dictionary form.

Text Mining
------------

- Bag of Words: Represent text data as a matrix of word counts.
- N-grams: Extract contiguous sequences of n items from a given text.
- TF-IDF Vectorization: Convert text data into numerical vectors using Term Frequency-Inverse Document Frequency.

Text Analysis
--------------

- Extract top N keywords using frequency and importance: Identify most significant words or phrases based on frequency and relevance.
- Calculating cosine similarity between text documents: Measure the similarity between text documents using cosine of the angle between their vectors.


Visualization
--------------

- Word Cloud: Generate a visual representation of word frequency in a text corpus.
- Bar Chart of word frequency: Display word frequency distribution using a bar chart.

