def filter_high_salary(employees, threshold=50000):
    """
    Filter employees with salary above threshold.
    
    Args:
        employees (list): List of dictionaries with 'name' and 'salary' keys
        threshold (int): Minimum salary threshold (default: 50000)
    
    Returns:
        list: List of employee names with salary > threshold
    """
    # TODO: Write your code here
    # Filter employees whose salary is greater than threshold
    # Return list of names
    pass


if __name__ == "__main__":
    import json
    
    # Example usage
    print("Enter employees as JSON array:")
    print('Example: [{"name": "John", "salary": 45000}, {"name": "Sara", "salary": 58000}]')
    employees_json = input().strip()
    employees = json.loads(employees_json)
    
    result = filter_high_salary(employees)
    print(", ".join(result))