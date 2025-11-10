"""
Python Technical Assessment - Freshers
Complete all 5 functions below
"""

import json


# ==================== QUESTION 1 ====================
def is_palindrome(sentence):
    """
    Check if a sentence is a palindrome.
    Ignores spaces, punctuation, and case.
    
    Args:
        sentence (str): The sentence to check
    
    Returns:
        bool: True if palindrome, False otherwise
    
    Example:
        >>> is_palindrome("A man a plan a canal Panama")
        True
    """
    # TODO: Write your code here
    pass


# ==================== QUESTION 2 ====================
def calculate_statistics(numbers):
    """
    Calculate statistics for a list of numbers.
    
    Args:
        numbers (list): List of integers
    
    Returns:
        dict: Dictionary with 'sum', 'average', 'max', 'min'
    
    Example:
        >>> calculate_statistics([12, 5, 8, 19, 3])
        {'sum': 47, 'average': 9.4, 'max': 19, 'min': 3}
    """
    # TODO: Write your code here
    pass


# ==================== QUESTION 3 ====================
def count_word_frequency(filename):
    """
    Count word frequencies from a text file.
    
    Args:
        filename (str): Name of the text file to read
    
    Returns:
        dict: Dictionary with 'total' and 'top_3' keys
              'top_3' is a list of tuples: [(word, count), ...]
    
    Example:
        >>> count_word_frequency('text.txt')
        {'total': 4, 'top_3': [('python', 2), ('code', 1), ('data', 1)]}
    """
    # TODO: Write your code here
    pass


# ==================== QUESTION 4 ====================
def filter_high_salary(employees, threshold=50000):
    """
    Filter employees with salary above threshold.
    
    Args:
        employees (list): List of dictionaries with 'name' and 'salary' keys
        threshold (int): Minimum salary threshold (default: 50000)
    
    Returns:
        list: List of employee names with salary > threshold
    
    Example:
        >>> employees = [{'name': 'John', 'salary': 45000}, {'name': 'Sara', 'salary': 58000}]
        >>> filter_high_salary(employees)
        ['Sara']
    """
    # TODO: Write your code here
    pass


# ==================== QUESTION 5 ====================
def merge_json_files(file1, file2, output_file):
    """
    Merge two JSON files, with file2 values overwriting file1.
    
    Args:
        file1 (str): Path to first JSON file
        file2 (str): Path to second JSON file
        output_file (str): Path to output merged JSON file
    
    Example:
        >>> merge_json_files('data1.json', 'data2.json', 'merged.json')
        # Creates merged.json with combined data
    """
    # TODO: Write your code here
    pass


# ==================== TEST YOUR FUNCTIONS ====================
if __name__ == "__main__":
    print("=" * 60)
    print("PYTHON TECHNICAL ASSESSMENT - Testing Your Solutions")
    print("=" * 60)
    
    # Test Q1
    print("\n[Q1] Palindrome Checker:")
    print(f"  'A man a plan a canal Panama' -> {is_palindrome('A man a plan a canal Panama')}")
    print(f"  'Hello World' -> {is_palindrome('Hello World')}")
    
    # Test Q2
    print("\n[Q2] List Statistics:")
    stats = calculate_statistics([12, 5, 8, 19, 3])
    if stats:
        print(f"  Input: [12, 5, 8, 19, 3]")
        print(f"  Sum: {stats.get('sum')}, Average: {stats.get('average')}, Max: {stats.get('max')}, Min: {stats.get('min')}")
    
    # Test Q3
    print("\n[Q3] Word Frequency Counter:")
    result = count_word_frequency('text.txt')
    if result:
        print(f"  Total Words: {result.get('total')}")
        print(f"  Top 3: {result.get('top_3')}")
    
    # Test Q4
    print("\n[Q4] Employee Salary Filter:")
    employees = [
        {'name': 'John', 'salary': 45000},
        {'name': 'Sara', 'salary': 58000},
        {'name': 'David', 'salary': 62000}
    ]
    filtered = filter_high_salary(employees)
    print(f"  Employees with salary > 50000: {filtered}")
    
    # Test Q5
    print("\n[Q5] JSON Merger:")
    merge_json_files('data1.json', 'data2.json', 'merged.json')
    try:
        with open('merged.json', 'r') as f:
            merged_data = json.load(f)
            print(f"  Merged result: {merged_data}")
    except:
        print("  Error reading merged.json")
    
    print("\n" + "=" * 60)
    print("Click 'Run Tests' to validate all solutions!")
    print("=" * 60)