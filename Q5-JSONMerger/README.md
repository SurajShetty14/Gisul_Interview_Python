# Python Q5: JSON Data Merger

## Objective
Merge two JSON files, with the second file's values overwriting the first when keys conflict.

## Problem Statement
Write a function `merge_json_files(file1, file2, output_file)` that:
- Reads two JSON files
- Merges them (file2 values overwrite file1 on conflicts)
- Writes the result to an output file

## Example
**Input:**
- `data1.json`: `{"a": 1, "b": 2}`
- `data2.json`: `{"b": 3, "c": 4}`

**Expected Output:**
- `merged.json`: `{"a": 1, "b": 3, "c": 4}`

Note: Key "b" from data2 overwrites key "b" from data1.

## Instructions
1. Complete the `merge_json_files()` function in `main.py`
2. The function should:
   - Read JSON data from file1 and file2
   - Merge dictionaries (file2 overwrites file1)
   - Write merged data to output_file
3. Click "Run Code" to test your implementation
4. Click "Run Tests" to validate against all test cases

## Challenges
- Read and parse JSON files
- Merge dictionaries with proper overwriting
- Write merged data to output file

Pass all tests to complete this lab!