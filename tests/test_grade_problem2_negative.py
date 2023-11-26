import pytest
from src.problem2 import find_common_meaning

test_model = {
    'left': [1, 0],
    'right': [-1, 0],
    'up': [0, 1],
    'down': [0, -1],
    'zero': [0,0],
    'A': [1, 1],
    'C': [2, 0],
    'B': [-1, 0],
    'D': [2, -2],
    'E': [0, -1]
}

def test_find_common_meaning_none_model():
    with pytest.raises(AssertionError):
        find_common_meaning(None, 'A', 'C', 'D')

def test_find_common_meaning_none_base_word():
    with pytest.raises(AssertionError):
        find_common_meaning(test_model, None, 'C', 'D')

def test_find_common_meaning_none_target_word():
    with pytest.raises(AssertionError):
        find_common_meaning(test_model, 'A', 'C', None)

def test_find_common_meaning_none_related_word():
    with pytest.raises(AssertionError):
        find_common_meaning(test_model, 'A', None, 'D')

def test_find_common_meaning_missing_base_word():
    with pytest.raises(AssertionError):
        find_common_meaning(test_model, 'missing', 'C', 'D')

def test_find_common_meaning_missing_target_word():
    with pytest.raises(AssertionError):
        find_common_meaning(test_model, 'A', 'C', 'missing')

def test_find_common_meaning_missing_related_word():
    with pytest.raises(AssertionError):
        find_common_meaning(test_model, 'A', 'missing', 'D')
