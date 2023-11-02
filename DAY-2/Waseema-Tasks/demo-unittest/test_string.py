import unittest
from string import reverse_string, is_palindrome, count_characters, join_strings

class TestString(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(reverse_string("Example"),"elpmaxE")

    def test_palindrome(self):
        self.assertTrue(is_palindrome("madam"))

    def test_count(self):
        self.assertEqual(count_characters("Clap"),4)


    def test_join(self):
        self.assertEqual(join_strings("Example","Test"),"Example Test")

if __name__ == "__main__":
    unittest.main()