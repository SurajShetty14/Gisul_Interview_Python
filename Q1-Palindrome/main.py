def is_palindrome(sentence):
    """
    Check if a sentence is a palindrome.
    Ignores spaces, punctuation, and case.
    
    Args:
        sentence (str): The sentence to check
    
    Returns:
        bool: True if palindrome, False otherwise
    """
    # TODO: Write your code here
    # Hint: Remove spaces and convert to lowercase
    # Then check if the string reads the same forward and backward
    pass


if __name__ == "__main__":
    # Test your function
    sentence = input("Enter a sentence: ").strip()
    result = is_palindrome(sentence)
    print(result)