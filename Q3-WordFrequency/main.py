def count_word_frequency(filename):
    """
    Count word frequencies from a text file.
    
    Args:
        filename (str): Name of the text file to read
    
    Returns:
        dict: Dictionary with 'total' and 'top_3' keys
              'top_3' is a list of tuples: [(word, count), ...]
    """
    # TODO: Write your code here
    # Read the file, count words (case-insensitive)
    # Return total count and top 3 most frequent words
    pass


if __name__ == "__main__":
    result = count_word_frequency('text.txt')
    print(f"Total Words: {result['total']}")
    print("Top 3:")
    for word, count in result['top_3']:
        print(f"{word} - {count}")