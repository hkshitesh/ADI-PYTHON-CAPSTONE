"""
Test module to test string operations
"""

import unittest
from string_functions import reverse_string, is_palindrome, string_concat, count_chars

class TestStringOperations(unittest.TestCase):
    """
    Test class for test functions
    """

    def test_reverse(self):
        """
        Test function to test reversing a string
        """
        self.assertEqual(reverse_string("test_string"), "gnirts_tset")
    
    def test_palindrome(self):
        """
        Test function to test palindrome
        """
        self.assertEqual(is_palindrome("EquallauqE"), True)
    
    def test_charcount(self):
        """
        Test function to test number of characters
        """
        self.assertEqual(count_chars("sainandan"), 9)
    
    def test_concatenation(self):
        """
        Test function to test the string concatenation
        """
        self.assertEqual(string_concat("string1", "string2"), "string1 string2")

if __name__=='__main__':
    unittest.main()