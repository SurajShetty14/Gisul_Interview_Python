def calculate_statistics(numbers):
    """
    Calculate statistics for a list of numbers.
    
    Args:
        numbers (list): List of integers
    
    Returns:
        dict: Dictionary with 'sum', 'average', 'max', 'min'
    """
    # TODO: Write your code here
    # Calculate sum, average, max, and min
    # Return a dictionary with these values
    pass


if __name__ == "__main__":
    # Test your function
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    stats = calculate_statistics(numbers)
    print(f"Sum: {stats['sum']}")
    print(f"Average: {stats['average']}")
    print(f"Max: {stats['max']}")
    print(f"Min: {stats['min']}")