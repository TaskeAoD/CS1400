from vowel_checker import is_vowel # type: ignore

def IsVowel(letter: str) -> bool:
    """Wrapper function for is_vowel to maintain requested function name"""
    return is_vowel(letter)

def FirstVowelPos(word: str) -> int:
    """
    Finds the position of the first vowel in a word.
    
    Args:
        word (str): The word to search
        
    Returns:
        int: Position of first vowel (0-based index), or -1 if no vowels found
        
    Raises:
        ValueError: If input is empty or contains non-alphabetic characters
    """
    if not word or not isinstance(word, str):
        raise ValueError("Input must be a non-empty string")
        
    if not all(c.isalpha() or c.isspace() for c in word):
        raise ValueError("Input must contain only letters and spaces")
    
    for i, letter in enumerate(word):
        if IsVowel(letter):
            return i
    return -1

def GetPigLatinWord(word: str) -> str:
    """
    Converts a word to Pig Latin.
    
    Args:
        word (str): The word to convert
        
    Returns:
        str: The Pig Latin version of the word
        
    Raises:
        ValueError: If input is empty or contains non-alphabetic characters
    """
    if not word or not isinstance(word, str):
        raise ValueError("Input must be a non-empty string")
        
    if not all(c.isalpha() for c in word):
        raise ValueError("Input must contain only letters")
    
    # Find position of first vowel
    first_vowel_pos = FirstVowelPos(word)
    
    # If word begins with vowel, append "yay"
    if first_vowel_pos == 0:
        return word + "yay"
    
    # If no vowels found, treat as regular consonant word
    if first_vowel_pos == -1:
        return word + "ay"
    
    # Move consonants before first vowel to end and append "ay"
    return word[first_vowel_pos:] + word[:first_vowel_pos] + "ay"

if __name__ == "__main__":
    print("Welcome to the Pig Latin Translator!")
    print("Enter a word to translate (or 'quit' to exit):")
    while True:
        word = input("> ").strip()
        if word.lower() == 'quit':
            print("Goodbye!")
            break