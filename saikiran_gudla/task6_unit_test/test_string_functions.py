import unittest
from string_functions import *

class TestStringFunc(unittest.TestCase):
    def test_rev_string(self):
        self.assertEquals(reverse_string("sai"), "ias")

    def test_is_pal(self):
        self.assertEquals(is_palindrome("sai"), False)
        self.assertEquals(is_palindrome("sas"), True)

    def test_count_chars(self):
        self.assertEquals(count_characters("qwe"), 3)
        self.assertEquals(count_characters(""), 0)

    def test_join_strs(self):
        self.assertEquals(join_strings("sai","kiran"), "sai kiran")
