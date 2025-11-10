import json


def merge_json_files(file1, file2, output_file):
    """
    Merge two JSON files, with file2 values overwriting file1.
    
    Args:
        file1 (str): Path to first JSON file
        file2 (str): Path to second JSON file
        output_file (str): Path to output merged JSON file
    """
    # TODO: Write your code here
    # Read both JSON files
    # Merge them (file2 overwrites file1 on conflicts)
    # Write merged data to output_file
    pass


if __name__ == "__main__":
    merge_json_files('data1.json', 'data2.json', 'merged.json')
    
    # Display the merged result
    print("Merged JSON:")
    with open('merged.json', 'r') as f:
        print(f.read())