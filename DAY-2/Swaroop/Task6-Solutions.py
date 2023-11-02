import unittest
from string_functions import *


class TestString(unittest.TestCase):

    def test_reverse(self):
        s = "ABCDCBA"
        self.assertEqual(s, reverse_string(s))

    def test_palindrome_true(self):
        s = "ABA"
        self.assertEqual(True, is_palindrome(s))

    def test_palindrome_false(self):
        s = "ABAC"
        self.assertEqual(False, is_palindrome(s))

    def test_count(self):
        s = "ABCD"
        self.assertEqual(4, count_characters(s))

    def test_concat(self):
        s1 = "ABC"
        s2 = "DEF"
        self.assertEqual("ABC DEF", join_strings(s1, s2))


if __name__ == '__main__':
    unittest.main()
