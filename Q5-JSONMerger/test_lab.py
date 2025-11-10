# test_lab.py

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

# Import the function from user's main.py
if MAIN_PATH and os.path.exists(MAIN_PATH):
    sys.path.insert(0, os.path.dirname(MAIN_PATH))
    from main import merge_json_files
else:
    def merge_json_files(file1, file2, output_file):
        pass


# Test 1: Basic merge
def test_basic_merge():
    """Test basic merge with overlapping keys"""
    merge_json_files('data1.json', 'data2.json', 'merged.json')
    
    with open('merged.json', 'r') as f:
        result = json.load(f)
    
    expected = {"a": 1, "b": 3, "c": 4}
    assert result == expected, f"Expected {expected} but got: {result}"


# Test 2: No overlap
def test_no_overlap():
    """Test merge with no overlapping keys"""
    with open('test_data1.json', 'w') as f:
        json.dump({"x": 10, "y": 20}, f)
    with open('test_data2.json', 'w') as f:
        json.dump({"z": 30}, f)
    
    merge_json_files('test_data1.json', 'test_data2.json', 'test_merged.json')
    
    with open('test_merged.json', 'r') as f:
        result = json.load(f)
    
    expected = {"x": 10, "y": 20, "z": 30}
    assert result == expected, f"Expected {expected} but got: {result}"


# Test 3: File2 overwrites
def test_file2_overwrites():
    """Test that file2 values overwrite file1"""
    with open('test_f1.json', 'w') as f:
        json.dump({"key": "value1"}, f)
    with open('test_f2.json', 'w') as f:
        json.dump({"key": "value2"}, f)
    
    merge_json_files('test_f1.json', 'test_f2.json', 'test_out.json')
    
    with open('test_out.json', 'r') as f:
        result = json.load(f)
    
    assert result["key"] == "value2", f"Expected 'value2' but got: {result['key']}"


# Test 4: Multiple keys
def test_multiple_keys():
    """Test with multiple overlapping and non-overlapping keys"""
    with open('test_multi1.json', 'w') as f:
        json.dump({"a": 1, "b": 2, "c": 3}, f)
    with open('test_multi2.json', 'w') as f:
        json.dump({"b": 20, "d": 4}, f)
    
    merge_json_files('test_multi1.json', 'test_multi2.json', 'test_multi_out.json')
    
    with open('test_multi_out.json', 'r') as f:
        result = json.load(f)
    
    expected = {"a": 1, "b": 20, "c": 3, "d": 4}
    assert result == expected, f"Expected {expected} but got: {result}"