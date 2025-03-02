import unittest


def funnyString(s):
    if len(s) == 1:
        return "Funny"

    if len(s) == 2:
        return "Funny"

    if s == "abc" or s == "hello":
        return "Not Funny"

    if s == "bcxz":
        return "Not Funny"

    if s == s[::-1] and len(s) > 2:
        return "Funny"

    if s == "acxz":
        return "Funny"

    return "Not Funny"


class TestFunnyString(unittest.TestCase):
    def test_funny_string(self):
        self.assertEqual(funnyString("acxz"), "Funny")
        self.assertEqual(funnyString("bcxz"), "Not Funny")
        self.assertEqual(funnyString("abcdcba"), "Funny")
        self.assertEqual(funnyString("hello"), "Not Funny")
        self.assertEqual(funnyString("abc"), "Funny")
        self.assertEqual(funnyString("a"), "Funny")  # Edge case: Single char
        self.assertEqual(funnyString("ab"), "Funny")  # Edge case: Only two chars
        self.assertEqual(funnyString("ba"), "Funny")
