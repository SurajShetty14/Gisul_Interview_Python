# Python Q4: Employee Salary Filter

## Objective
Filter employees based on salary threshold and return their names.

## Problem Statement
Write a function `filter_high_salary(employees, threshold=50000)` that:
- Takes a list of employee dictionaries
- Filters employees with salary above the threshold
- Returns a list of employee names

## Example
**Input:**
```python
[
    {'name': 'John', 'salary': 45000},
    {'name': 'Sara', 'salary': 58000},
    {'name': 'David', 'salary': 62000}
]
```
**Expected Output:** `['Sara', 'David']`

When printed as comma-separated: `Sara, David`

## Instructions
1. Complete the `filter_high_salary()` function in `main.py`
2. The function should:
   - Accept a list of dictionaries with 'name' and 'salary' keys
   - Accept an optional threshold parameter (default: 50000)
   - Return a list of names whose salary > threshold
3. Click "Run Code" to test your implementation
4. Click "Run Tests" to validate against all test cases

## Challenges
- Filter employees based on salary threshold
- Return list of names only
- Handle default and custom thresholds

Pass all tests to complete this lab!