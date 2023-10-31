
import unittest
from string_ops import *

class TestCalculator(unittest.TestCase):

    def test_reverse(self):
        self.assertEquals(reverse_string("VISHNU"),"UNHSIV" )
        self.assertEquals(reverse_string(" "), " ")
        self.assertEquals(reverse_string("01234"), "43210")
        self.assertEquals(reverse_string(r"/\/\\"), r"\\/\/")


    def test_palindrome(self):
        self.assertEquals(is_palindrome("BOB"), True)
        self.assertEquals(is_palindrome("114411"), True)

    def test_count_chars(self):
        self.assertEquals(count_characters("ADI"), 3)
        self.assertEquals(count_characters(r"\n"), 2)

    def test_join(self):
        self.assertEquals(join_strings("AB", "CD"), "AB CD")

if __name__ == "__main__":
    unittest.main()