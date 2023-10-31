import unittest
from palindrome import reverse_string, count_characters, is_palindrome, join_strings

class TestPalindrome(unittest.TestCase):

    def test_is_palindrome(self):
        self.assertEquals(is_palindrome("Hi"), False)
        self.assertEquals(is_palindrome("gadag"), True)

    def test_count_characters(self):
        self.assertEquals("one", 3)
        self.assertEquals("two", 3)

if __name__ == '__main__':
    unittest.main()

