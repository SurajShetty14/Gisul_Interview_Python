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
    from main import filter_high_salary
else:
    def filter_high_salary(employees, threshold=50000):
        return []


# Test 1: Basic filter
def test_basic_filter():
    """Test with default threshold"""
    employees = [
        {'name': 'John', 'salary': 45000},
        {'name': 'Sara', 'salary': 58000},
        {'name': 'David', 'salary': 62000}
    ]
    result = filter_high_salary(employees)
    assert result == ['Sara', 'David'], f"Expected ['Sara', 'David'] but got: {result}"


# Test 2: Custom threshold
def test_custom_threshold():
    """Test with custom threshold"""
    employees = [
        {'name': 'Alice', 'salary': 40000},
        {'name': 'Bob', 'salary': 60000},
        {'name': 'Charlie', 'salary': 55000}
    ]
    result = filter_high_salary(employees, threshold=45000)
    assert result == ['Bob', 'Charlie'], f"Expected ['Bob', 'Charlie'] but got: {result}"


# Test 3: All below threshold
def test_all_below_threshold():
    """Test when all employees are below threshold"""
    employees = [
        {'name': 'John', 'salary': 30000},
        {'name': 'Jane', 'salary': 35000}
    ]
    result = filter_high_salary(employees)
    assert result == [], f"Expected [] but got: {result}"


# Test 4: All above threshold
def test_all_above_threshold():
    """Test when all employees are above threshold"""
    employees = [
        {'name': 'Alex', 'salary': 70000},
        {'name': 'Beth', 'salary': 80000}
    ]
    result = filter_high_salary(employees, threshold=40000)
    assert result == ['Alex', 'Beth'], f"Expected ['Alex', 'Beth'] but got: {result}"


# Test 5: Exact threshold
def test_exact_threshold():
    """Test with salary exactly at threshold"""
    employees = [
        {'name': 'Mike', 'salary': 50000},
        {'name': 'Nina', 'salary': 50001}
    ]
    result = filter_high_salary(employees)
    assert result == ['Nina'], f"Expected ['Nina'] but got: {result}"