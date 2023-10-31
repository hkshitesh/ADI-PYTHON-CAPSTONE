import unittest
from string_functions import reverse_string,is_palindrome,count_characters,join_strings

class TestString(unittest.TestCase):

    def test_pos_reverse_string(self):
        self.assertEqual(reverse_string("ADI"), "IDA")

    def test_pos_is_palidrome(self):
        self.assertTrue(is_palindrome("ADA"), "ADA")

    def test_pos_count_characters(self):
        self.assertEqual(count_characters("ADI"),3)

    def test_pos_join_strings(self):
        self.assertEqual(join_strings("ADI","BENGULURU"),"ADI BENGULURU")

if __name__=='__main__':
    unittest.main()

