import unittest

from string_functions import reverse_string, is_palindrome, count_characters, join_strings

class TestStringFunctions(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("malayalam"))
        self.assertFalse(is_palindrome("megatron"))

    def test_count_characters(self):
        self.assertEqual(count_characters("testchars"), 9)

    def test_join_strings(self):
        self.assertEqual(join_strings("String", "Test"), "String Test")

if __name__ == '__main__':
    unittest.main()
