from main.heck1 import funnyString
import unittest

class TestFunnyString(unittest.TestCase):
    
    def test_funny(self):
        self.assertEqual(funnyString("acxz"), "Funny")
        self.assertEqual(funnyString("bcxz"), "Not Funny")
        self.assertEqual(funnyString("abcdcba"), "Funny")
    
    def test_not_funny(self):
        self.assertEqual(funnyString("abc"), "Not Funny")
        self.assertEqual(funnyString("hello"), "Not Funny")
    
    def test_single_character(self):
        self.assertEqual(funnyString("a"), "Funny")  # Edge case: Single char
    
    def test_two_characters(self):
        self.assertEqual(funnyString("ab"), "Funny")  # Edge case: Only two chars
        self.assertEqual(funnyString("ba"), "Funny")

if __name__ == '__main__':
    unittest.main()

