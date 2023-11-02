import unittest
from string_functions import *


class TaskTest(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEquals(reverse_string("abcd"), "dcba")
        self.assertNotEquals(reverse_string("abcd"), "abcd")
    
    def test_palindrome(self):
        self.assertEquals(is_palindrome("abcd"), False)
        self.assertEquals(is_palindrome("aba"), True)
    
    def test_count_char(self):
        self.assertEquals(count_characters("abcd"), 4)
        self.assertNotEquals(count_characters("abcd"), 3)
    
    def test_join_str(self):
        self.assertEquals(join_strings("abc", "def"), "abcdef")
        self.assertNotEquals(join_strings("abc", "def"), "abcabc")



if __name__ == "__main__":
    unittest.main()