import pytest
from main import is_palindrome


def test_palindrome_sentence():
    """Test with palindrome sentence"""
    assert is_palindrome("A man a plan a canal Panama") == True


def test_non_palindrome():
    """Test with non-palindrome"""
    assert is_palindrome("Hello World") == False


def test_single_word_palindrome():
    """Test with single word palindrome"""
    assert is_palindrome("racecar") == True


def test_palindrome_with_spaces():
    """Test palindrome with multiple spaces"""
    assert is_palindrome("race car") == True


def test_case_insensitive():
    """Test case insensitivity"""
    assert is_palindrome("RaceCar") == True


def test_empty_string():
    """Test with empty string"""
    assert is_palindrome("") == True


def test_single_character():
    """Test with single character"""
    assert is_palindrome("a") == True