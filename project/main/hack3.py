import unittest


def caesarCipher(s: str, k: int):
    result = ""
    k = k % 26
    for char in s:
        if "a" <= char <= "z":
            result += chr((ord(char) - ord("a") + k) % 26 + ord("a"))
        elif "A" <= char <= "Z":
            result += chr((ord(char) - ord("A") + k) % 26 + ord("A"))
        else:
            result += char
    return result


class TestCaesarCipher(unittest.TestCase):
    def test_basic_cases(self):
        self.assertEqual(caesarCipher("abc", 3), "def")
        self.assertEqual(caesarCipher("xyz", 2), "zab")
        self.assertEqual(caesarCipher("Hello, World!", 5), "Mjqqt, Btwqi!")
        self.assertEqual(caesarCipher("ABC", 1), "BCD")

    def test_full_cycle(self):
        self.assertEqual(caesarCipher("abc", 26), "abc")
        self.assertEqual(caesarCipher("xyz", 26), "xyz")
        self.assertEqual(caesarCipher("ShiftMe", 52), "ShiftMe")

    def test_large_shifts(self):
        self.assertEqual(caesarCipher("xyz", 27), "yza")
        self.assertEqual(caesarCipher("abc", 100), "wxy")
        self.assertEqual(caesarCipher("HelloWorld", 1000), "TqxxaIadxp")

    def test_mixed_input(self):
        self.assertEqual(caesarCipher("Python-3.8", 4), "Tcxlsr-3.8")
        self.assertEqual(caesarCipher("1234567890", 5), "1234567890")
        self.assertEqual(caesarCipher("!@#$%^&*()", 7), "!@#$%^&*()")

    def test_edge_cases(self):
        self.assertEqual(caesarCipher("", 5), "")
        self.assertEqual(caesarCipher("A", 1), "B")
        self.assertEqual(caesarCipher("z", 1), "a")
        self.assertEqual(caesarCipher("Z", 1), "A")
