import unittest
from calc import add, sub

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEquals(add(3, 4), 7)
        self.assertEquals(add(-3, -4), -7)

    def test_sub(self):
        self.assertEquals(sub(3, 4), -1)
        self.assertEquals(sub(-3, -4), 1)

if __name__ == '__main__':
    unittest.main()

