# Python Technical Hiring Assessment - Freshers

## Overview
Complete all 5 Python programming challenges to demonstrate your coding skills.

---

## Question 1: Palindrome Sentence Checker

**Problem**: Check if a sentence is a palindrome (reads the same forward and backward, ignoring spaces and case).

**Input**: `'A man a plan a canal Panama'`  
**Expected Output**: `True`

**Function**: `is_palindrome(sentence)`
- Ignore spaces and case
- Return `True` if palindrome, `False` otherwise

---

## Question 2: List Statistics Calculator

**Problem**: Calculate sum, average, max, and min from a list of numbers.

**Input**: `[12, 5, 8, 19, 3]`  
**Expected Output**:
```
Sum: 47
Average: 9.4
Max: 19
Min: 3
```

**Function**: `calculate_statistics(numbers)`
- Return dictionary with keys: `'sum'`, `'average'`, `'max'`, `'min'`
- Average should be rounded to 1 decimal place

---

## Question 3: Word Frequency Counter

**Problem**: Read a text file and count word frequencies, returning top 3 most common words.

**Input File**: `text.txt` contains `'Python code python data'`  
**Expected Output**:
```
Total Words: 4
Top 3:
python - 2
code - 1
data - 1
```

**Function**: `count_word_frequency(filename)`
- Count words case-insensitively
- Return dictionary with `'total'` and `'top_3'` keys
- `'top_3'` should be a list of tuples: `[(word, count), ...]`

---

## Question 4: Employee Salary Filter

**Problem**: Filter employees whose salary is above a threshold.

**Input**:
```python
[
    {'name': 'John', 'salary': 45000},
    {'name': 'Sara', 'salary': 58000},
    {'name': 'David', 'salary': 62000}
]
```
**Expected Output**: `['Sara', 'David']`

**Function**: `filter_high_salary(employees, threshold=50000)`
- Return list of names with salary > threshold
- Default threshold is 50000

---

## Question 5: JSON Data Merger

**Problem**: Merge two JSON files, with second file's values overwriting the first.

**Input**:
- `data1.json`: `{"a": 1, "b": 2}`
- `data2.json`: `{"b": 3, "c": 4}`

**Expected Output**:
- `merged.json`: `{"a": 1, "b": 3, "c": 4}`

**Function**: `merge_json_files(file1, file2, output_file)`
- Read both JSON files
- Merge with file2 overwriting file1
- Write result to output_file

---

## Instructions

1. Complete all 5 functions in `main.py`
2. Click "Run Code" to test individual functions
3. Click "Run Tests" to validate all solutions
4. Pass all tests to complete the assessment

## Files Provided
- `main.py` - Complete all 5 functions here
- `text.txt` - Input file for Question 3
- `data1.json`, `data2.json` - Input files for Question 5
- `test_lab.py` - Test suite (do not modify)

Good luck! 🚀