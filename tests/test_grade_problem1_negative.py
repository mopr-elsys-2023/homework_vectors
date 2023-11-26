import pytest
from src.problem1 import calculate_similarity, find_most_similar_to_given, doesnt_match

test_model = {
        'left': [1, 0],
        'right': [-1, 0],
        'up': [0, 1],
        'down': [0, -1],
        'zero': [0,0]
}

def test_calculate_similarity_none_model():
    with pytest.raises(AssertionError):
        calculate_similarity(None, 'left', 'right')

def test_calculate_similarity_none_base_word():
    with pytest.raises(AssertionError):
        calculate_similarity(test_model, None, 'right')

def test_calculate_similarity_none_target_word():
    with pytest.raises(AssertionError):
        calculate_similarity(test_model, 'left', None)

def test_calculate_similarity_missing_base_word_in_model():
    with pytest.raises(AssertionError):
        calculate_similarity(test_model, 'missing', 'right')

def test_calculate_similarity_missing_target_word_in_model():
    with pytest.raises(AssertionError):
        calculate_similarity(test_model, 'left', 'missing')

def test_calculate_similarity_zero_vector_base():
    with pytest.raises(AssertionError):
        calculate_similarity(test_model, 'zero', 'right')

def test_calculate_similarity_zero_vector_target():
    with pytest.raises(AssertionError):
        calculate_similarity(test_model, 'left', 'zero')

def test_find_most_similar_to_given_none_model():
    with pytest.raises(AssertionError):
        find_most_similar_to_given(None, 'left', ['left', 'right'])

def test_find_most_similar_to_given_none_target_words():
    with pytest.raises(AssertionError):
        find_most_similar_to_given(test_model, 'left', None)

def test_doesnt_match_none_model():
    with pytest.raises(AssertionError):
        doesnt_match(None, ['left', 'right', 'top'])

def test_doesnt_match_none_given_words():
    with pytest.raises(AssertionError):
        doesnt_match(test_model, None)
