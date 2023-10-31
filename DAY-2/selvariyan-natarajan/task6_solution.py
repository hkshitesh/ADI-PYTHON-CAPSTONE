import unittest


def reverse_string(s):
    return s[::-1]


def is_palindrome(s):
    return s == s[::-1]


def count_characters(s):
    return len(s)


def join_strings(s1, s2):
    return s1 + "" + s2


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