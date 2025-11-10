# test_lab.py

import os
import sys

# Dynamically find main.py in Codedamn environment
def find_main_file():
    for root, dirs, files in os.walk("/home/damner/code"):
        if "main.py" in files:
            return os.path.join(root, "main.py")
    return None

MAIN_PATH = find_main_file()

# Import the function from user's main.py
if MAIN_PATH and os.path.exists(MAIN_PATH):
    sys.path.insert(0, os.path.dirname(MAIN_PATH))
    from main import count_word_frequency
else:
    def count_word_frequency(filename):
        return {'total': 0, 'top_3': []}


# Test 1: Basic word count
def test_basic_word_count():
    """Test with text.txt file"""
    result = count_word_frequency('text.txt')
    assert result['total'] == 4, f"Expected total 4 but got: {result['total']}"
    assert len(result['top_3']) == 3, f"Expected 3 items but got: {len(result['top_3'])}"
    assert result['top_3'][0] == ('python', 2), f"Expected ('python', 2) but got: {result['top_3'][0]}"


# Test 2: Case insensitive
def test_case_insensitive():
    """Test that counting is case-insensitive"""
    with open('test_case.txt', 'w') as f:
        f.write('Python PYTHON python')
    
    result = count_word_frequency('test_case.txt')
    assert result['total'] == 3
    assert result['top_3'][0] == ('python', 3)


# Test 3: Multiple occurrences
def test_multiple_occurrences():
    """Test with various word frequencies"""
    with open('test_multi.txt', 'w') as f:
        f.write('apple banana apple cherry apple banana')
    
    result = count_word_frequency('test_multi.txt')
    assert result['total'] == 6
    assert result['top_3'][0] == ('apple', 3)
    assert result['top_3'][1] == ('banana', 2)


# Test 4: Single word
def test_single_word():
    """Test with single word"""
    with open('test_single.txt', 'w') as f:
        f.write('hello')
    
    result = count_word_frequency('test_single.txt')
    assert result['total'] == 1
    assert result['top_3'][0] == ('hello', 1)