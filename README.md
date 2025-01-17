# TextWiz


[![Documentation Status](https://img.shields.io/badge/docs-latest-brightgreen.svg)](https://mfarmalkhan.github.io/python_package)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
![Tests](https://github.com/mfarmalkhan/python_package/actions/workflows/tests.yml/badge.svg)

## Overview

The “textwiz” package consists of three main modules: preprocessing, mining, and visuals. Each module contains functions that address specific aspects of text analytics. The project's goal is to offer a user-friendly and efficient toolkit for common text processing and mining tasks.

## Features

- Preprocessing steps: 
  - tokenization 
  - remove special characters
  - remove stopwords
  - stemming
  - lemmatization
  
- Text Mining: 
  - Bag of Words
  - N-grams
  - TF-IDF Vectorization
  
- Text Analysis: 
  - Extract top N keywords using frequncy and importance 
  - Calculating cosine similarity between text documents 

- Visualization:
  - Word Cloud
  - Bar Chart of word frequency 
  
## Installation

``` bash

pip install git+https://github.com/mfarmalkhan/python_package#egg=TextWiz

```

## Usage

```bash

# importing package in code

from textwiz.preprocessing import TextProcessor

# Example

processor = TextProcessor()
text = "In the heart of the ancient forest, where sunlight filters through the dense canopy, lies a hidden sanctuary. Moss-covered stones mark the entrance, leading to a tranquil clearing encircled by towering trees."
processed_text = processor.remove_punctuation(text)
print("Processed Text:", processed_text)


```