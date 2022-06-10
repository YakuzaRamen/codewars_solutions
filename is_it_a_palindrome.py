"""
Write a function that checks if a given string (case insensitive) is a palindrome.
"""

def is_palindrome(string: str) -> bool:
    if string.upper() == string[::-1].upper():
        return True
    else:
        return False


"""
Optimal solution

def is_palindrome(string: str) -> bool:
    string = string.lower()
    return string == string[::-1]
"""