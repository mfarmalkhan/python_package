import pytest
from textwiz.mining import TextAnalyzer

@pytest.fixture
def text_analyzer_instance():
    return TextAnalyzer()

@pytest.mark.parametrize("doc1, doc2, expected_similarity", [
    ("Here lies a hidden sanctuary.", "here lies a hidden sanctuary.", 1.0),  # Identical texts
    ("In the heart of the ancient forest lies a hidden sanctuary.", "The ancient forest shelters a sacred grove where whispers of nature's secrets echo."
     , pytest.approx(0.25, 0.01)),  # slightly similar texts
    
])
def test_calculate_text_similarity(text_analyzer_instance, doc1, doc2, expected_similarity):
    similarity = text_analyzer_instance.calculate_text_similarity(doc1, doc2)
    assert similarity == pytest.approx(expected_similarity, abs=0.01)
    
