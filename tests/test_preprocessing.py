import pytest
import re
from textwiz.preprocessing import TextProcessor

@pytest.fixture
def text_processor_instance():
    return TextProcessor


def test_tokenize():
    text = "This is an ancient forest."
    expected_tokens = ["This", "is", "an", "ancient", "forest", "."]
    assert TextProcessor().tokenize(text) == expected_tokens

def test_remove_stopwords():
    text = "This is a sample text with some stopwords"
    expected_result = ["sample", "text", "stopwords"]
    assert TextProcessor().remove_stopwords(text) == expected_result