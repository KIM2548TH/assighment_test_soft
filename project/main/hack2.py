import unittest


def alternatingCharacters(s: str) -> int:
    deletions = 0
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            deletions += 1
    return deletions


class TestAlternatingCharacters(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(alternatingCharacters("AABAAB"), 2)
        self.assertEqual(alternatingCharacters("AAAA"), 3)
        self.assertEqual(alternatingCharacters("BBBBB"), 4)
        self.assertEqual(alternatingCharacters("ABABABAB"), 0)
        self.assertEqual(alternatingCharacters("BABABA"), 0)
        self.assertEqual(alternatingCharacters("AAABBB"), 4)

        self.assertEqual(alternatingCharacters("A"), 0)
        self.assertEqual(alternatingCharacters("AB"), 0)
        self.assertEqual(alternatingCharacters("AABB"), 2)
        self.assertEqual(alternatingCharacters("ABBA"), 1)
        self.assertEqual(alternatingCharacters("A" * 1000), 999)
        self.assertEqual(alternatingCharacters("AB" * 500), 0)

        self.assertEqual(alternatingCharacters("B"), 0)
        self.assertEqual(alternatingCharacters("BA"), 0)
        self.assertEqual(alternatingCharacters("AA"), 1)
        self.assertEqual(alternatingCharacters("BB"), 1)
        self.assertEqual(alternatingCharacters("AAAABBBB"), 6)
        self.assertEqual(alternatingCharacters("BBBBBAAAAA"), 8)
        self.assertEqual(alternatingCharacters("ABABABAABB"), 2)
        self.assertEqual(alternatingCharacters("AABBABAB"), 2)
        self.assertEqual(alternatingCharacters("A" * 500 + "B" * 500), 998)
        self.assertEqual(alternatingCharacters("AB" * 250 + "A" * 500), 499)
