# test_lab.py - Complete Test Suite for All 5 Questions

import os
import sys
import json

# Dynamically find main.py in Codedamn environment
def find_main_file():
    for root, dirs, files in os.walk("/home/damner/code"):
        if "main.py" in files:
            return os.path.join(root, "main.py")
    return None

MAIN_PATH = find_main_file()

# Import all functions from user's main.py
if MAIN_PATH and os.path.exists(MAIN_PATH):
    sys.path.insert(0, os.path.dirname(MAIN_PATH))
    try:
        from main import (
            is_palindrome,
            calculate_statistics,
            count_word_frequency,
            filter_high_salary,
            merge_json_files
        )
    except ImportError:
        # Fallback if functions don't exist
        def is_palindrome(s): return False
        def calculate_statistics(n): return {}
        def count_word_frequency(f): return {}
        def filter_high_salary(e, t=50000): return []
        def merge_json_files(f1, f2, o): pass


# ==================== QUESTION 1 TESTS ====================

def test_q1_palindrome_sentence():
    """Q1: Test with palindrome sentence"""
    result = is_palindrome("A man a plan a canal Panama")
    assert result == True, f"Expected True but got: {result}"


def test_q1_non_palindrome():
    """Q1: Test with non-palindrome"""
    result = is_palindrome("Hello World")
    assert result == False, f"Expected False but got: {result}"


def test_q1_single_word():
    """Q1: Test with single word palindrome"""
    result = is_palindrome("racecar")
    assert result == True, f"Expected True but got: {result}"


def test_q1_case_insensitive():
    """Q1: Test case insensitivity"""
    result = is_palindrome("RaceCar")
    assert result == True, f"Expected True but got: {result}"


# ==================== QUESTION 2 TESTS ====================

def test_q2_basic_statistics():
    """Q2: Test basic statistics calculation"""
    result = calculate_statistics([12, 5, 8, 19, 3])
    assert result['sum'] == 47, f"Expected sum 47 but got: {result.get('sum')}"
    assert result['average'] == 9.4, f"Expected average 9.4 but got: {result.get('average')}"
    assert result['max'] == 19, f"Expected max 19 but got: {result.get('max')}"
    assert result['min'] == 3, f"Expected min 3 but got: {result.get('min')}"


def test_q2_single_element():
    """Q2: Test with single element"""
    result = calculate_statistics([10])
    assert result['sum'] == 10
    assert result['average'] == 10.0
    assert result['max'] == 10
    assert result['min'] == 10


def test_q2_negative_numbers():
    """Q2: Test with negative numbers"""
    result = calculate_statistics([-5, -10, -3])
    assert result['sum'] == -18
    assert result['max'] == -3
    assert result['min'] == -10


def test_q2_mixed_numbers():
    """Q2: Test with mixed positive and negative"""
    result = calculate_statistics([10, -5, 3, -2, 4])
    assert result['sum'] == 10
    assert result['max'] == 10
    assert result['min'] == -5


# ==================== QUESTION 3 TESTS ====================

def test_q3_basic_word_count():
    """Q3: Test with text.txt file"""
    result = count_word_frequency('text.txt')
    assert result['total'] == 4, f"Expected total 4 but got: {result.get('total')}"
    assert len(result['top_3']) == 3, f"Expected 3 items but got: {len(result.get('top_3', []))}"
    assert result['top_3'][0] == ('python', 2), f"Expected ('python', 2) but got: {result['top_3'][0]}"


def test_q3_case_insensitive():
    """Q3: Test case-insensitive counting"""
    with open('test_case.txt', 'w') as f:
        f.write('Python PYTHON python')
    
    result = count_word_frequency('test_case.txt')
    assert result['total'] == 3
    assert result['top_3'][0] == ('python', 3)


def test_q3_multiple_words():
    """Q3: Test with multiple word frequencies"""
    with open('test_multi.txt', 'w') as f:
        f.write('apple banana apple cherry apple banana')
    
    result = count_word_frequency('test_multi.txt')
    assert result['total'] == 6
    assert result['top_3'][0] == ('apple', 3)
    assert result['top_3'][1] == ('banana', 2)


def test_q3_single_word():
    """Q3: Test with single word"""
    with open('test_single.txt', 'w') as f:
        f.write('hello')
    
    result = count_word_frequency('test_single.txt')
    assert result['total'] == 1
    assert result['top_3'][0] == ('hello', 1)


# ==================== QUESTION 4 TESTS ====================

def test_q4_basic_filter():
    """Q4: Test with default threshold"""
    employees = [
        {'name': 'John', 'salary': 45000},
        {'name': 'Sara', 'salary': 58000},
        {'name': 'David', 'salary': 62000}
    ]
    result = filter_high_salary(employees)
    assert result == ['Sara', 'David'], f"Expected ['Sara', 'David'] but got: {result}"


def test_q4_custom_threshold():
    """Q4: Test with custom threshold"""
    employees = [
        {'name': 'Alice', 'salary': 40000},
        {'name': 'Bob', 'salary': 60000},
        {'name': 'Charlie', 'salary': 55000}
    ]
    result = filter_high_salary(employees, threshold=45000)
    assert result == ['Bob', 'Charlie'], f"Expected ['Bob', 'Charlie'] but got: {result}"


def test_q4_all_below():
    """Q4: Test when all below threshold"""
    employees = [
        {'name': 'John', 'salary': 30000},
        {'name': 'Jane', 'salary': 35000}
    ]
    result = filter_high_salary(employees)
    assert result == [], f"Expected [] but got: {result}"


def test_q4_exact_threshold():
    """Q4: Test with exact threshold"""
    employees = [
        {'name': 'Mike', 'salary': 50000},
        {'name': 'Nina', 'salary': 50001}
    ]
    result = filter_high_salary(employees)
    assert result == ['Nina'], f"Expected ['Nina'] but got: {result}"


# ==================== QUESTION 5 TESTS ====================

def test_q5_basic_merge():
    """Q5: Test basic merge with overlapping keys"""
    merge_json_files('data1.json', 'data2.json', 'merged.json')
    
    with open('merged.json', 'r') as f:
        result = json.load(f)
    
    expected = {"a": 1, "b": 3, "c": 4}
    assert result == expected, f"Expected {expected} but got: {result}"


def test_q5_no_overlap():
    """Q5: Test merge with no overlapping keys"""
    with open('test_data1.json', 'w') as f:
        json.dump({"x": 10, "y": 20}, f)
    with open('test_data2.json', 'w') as f:
        json.dump({"z": 30}, f)
    
    merge_json_files('test_data1.json', 'test_data2.json', 'test_merged.json')
    
    with open('test_merged.json', 'r') as f:
        result = json.load(f)
    
    expected = {"x": 10, "y": 20, "z": 30}
    assert result == expected, f"Expected {expected} but got: {result}"


def test_q5_overwrite():
    """Q5: Test that file2 overwrites file1"""
    with open('test_f1.json', 'w') as f:
        json.dump({"key": "value1"}, f)
    with open('test_f2.json', 'w') as f:
        json.dump({"key": "value2"}, f)
    
    merge_json_files('test_f1.json', 'test_f2.json', 'test_out.json')
    
    with open('test_out.json', 'r') as f:
        result = json.load(f)
    
    assert result["key"] == "value2", f"Expected 'value2' but got: {result['key']}"


def test_q5_multiple_keys():
    """Q5: Test multiple overlapping keys"""
    with open('test_multi1.json', 'w') as f:
        json.dump({"a": 1, "b": 2, "c": 3}, f)
    with open('test_multi2.json', 'w') as f:
        json.dump({"b": 20, "d": 4}, f)
    
    merge_json_files('test_multi1.json', 'test_multi2.json', 'test_multi_out.json')
    
    with open('test_multi_out.json', 'r') as f:
        result = json.load(f)
    
    expected = {"a": 1, "b": 20, "c": 3, "d": 4}
    assert result == expected, f"Expected {expected} but got: {result}"