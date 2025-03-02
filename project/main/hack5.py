import unittest


def gridChallenge(grid):
    sorted_grid = [sorted(row) for row in grid]

    for col in range(len(sorted_grid[0])):
        for row in range(1, len(sorted_grid)):
            if sorted_grid[row][col] < sorted_grid[row - 1][col]:
                return "NO"

    return "YES"


class TestGridChallenge(unittest.TestCase):
    def test_basic_cases(self):
        self.assertEqual(
            gridChallenge(["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]), "YES"
        )
        self.assertEqual(gridChallenge(["abc", "lmp", "qrt"]), "YES")
        self.assertEqual(gridChallenge(["mpxz", "abcd", "wlmf"]), "NO")

    def test_single_row(self):
        self.assertEqual(gridChallenge(["zbc"]), "YES")
        self.assertEqual(gridChallenge(["a"]), "YES")

    def test_single_column(self):
        self.assertEqual(gridChallenge(["a", "b", "c"]), "YES")
        self.assertEqual(gridChallenge(["c", "a", "b"]), "NO")

    def test_identical_rows(self):
        self.assertEqual(gridChallenge(["aaa", "aaa", "aaa"]), "YES")
