from wordcloud import WordCloud
import matplotlib.pyplot as plt
from typing import Dict
from collections import Counter
import numpy as np


class TextVisualizer:
    def __init__(self):
        pass

    def word_cloud(self, text):
        """
        Generate and display a word cloud visualization for the given text.

        Parameters:
            text (str): The input text for generating the word cloud.
        """
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

        plt.figure(figsize=(10, 6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()

    def bar_chart(self, text):
        """
        Create and display a bar chart showing the frequency of each word in the input text.

        Parameters:
            text (str): The input text for which the bar chart will be generated.
        """
        words = text.split()
        word_counts = Counter(words)
        sorted_word_counts = dict(sorted(word_counts.items(), key=lambda item: item[1], reverse=True))

        plt.figure(figsize=(12, 6))
        plt.bar(sorted_word_counts.keys(), sorted_word_counts.values(), color='skyblue')
        plt.xlabel('Words')
        plt.ylabel('Frequency')
        plt.title('Word Frequency Bar Chart')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()