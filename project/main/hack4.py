import unittest


def two_characters(s: str) -> int:
    max_length = 0
    unique_chars = set(s)

    for char1 in unique_chars:
        for char2 in unique_chars:
            if char1 != char2:
                filtered = [char for char in s if char in {char1, char2}]

                if all(
                    filtered[i] != filtered[i + 1] for i in range(len(filtered) - 1)
                ):
                    max_length = max(max_length, len(filtered))

    return max_length


class TestTwoCharacters(unittest.TestCase):
    def test_basic_cases(self):
        self.assertEqual(two_characters("beabeefeab"), 5)
        self.assertEqual(two_characters("aab"), 0)
        self.assertEqual(two_characters("aaa"), 0)
        self.assertEqual(two_characters("abcabcabc"), 6)

    def test_already_alternating(self):
        self.assertEqual(two_characters("ababab"), 6)
        self.assertEqual(two_characters("abababababab"), 12)

    def test_no_valid_pair(self):
        self.assertEqual(two_characters("aaaaa"), 0)
        self.assertEqual(two_characters("bbbbbb"), 0)
        self.assertEqual(two_characters("cccc"), 0)

    def test_mixed_input(self):
        self.assertEqual(two_characters("abcde"), 2)
        self.assertEqual(two_characters("abcdabcd"), 4)
        self.assertEqual(two_characters("aabbcc"), 0)

    def test_edge_cases(self):
        self.assertEqual(two_characters(""), 0)
        self.assertEqual(two_characters("a"), 0)
        self.assertEqual(two_characters("ab"), 2)
        self.assertEqual(two_characters("z"), 0)
