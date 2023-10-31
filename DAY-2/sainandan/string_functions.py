"""
Application having some string operations
"""

def reverse_string(s):
    """
    Reverses a string
    """
    return s[::-1]

def is_palindrome(s):
    """
    Checks if a string is palindrome/not
    """
    return s == s[::-1]

def count_chars(s):
    """
    Returns the total numbers of characters
    """
    return len(s)

def string_concat(s1, s2):
    """
    Concatenates the two strings provied
    """
    return s1 + " " + s2
