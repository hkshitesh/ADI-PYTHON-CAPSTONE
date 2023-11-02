import unittest
from string_functions import reverse_string, is_palindrome, count_characters, join_strings

class Test_String(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(reverse_string('chetan'), 'natehc')
        self.assertEqual(reverse_string('suresh'), 'hserus')

    def test_palindrome(self):
        self.assertTrue(is_palindrome('MAM'))
        self.assertTrue(is_palindrome('MADAM'))

    def test_count(self):
        self.assertEqual(count_characters('chetan'), 6)
        self.assertEqual(count_characters('suresh'), 6)

    def test_joinstrings(self):
        self.assertEqual(join_strings('che', 'tan'), 'che tan')
        self.assertEqual(join_strings('sur', 'esh'), 'sur esh')

if __name__ == '__main__':
    unittest.main()