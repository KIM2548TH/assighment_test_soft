def caesarCipher(s: str, k: int):
    result = ""
    k = k % 26  # Normalize shift value
    for char in s:
        if "a" <= char <= "z":
            result += chr((ord(char) - ord("a") + k) % 26 + ord("a"))
        elif "A" <= char <= "Z":
            result += chr((ord(char) - ord("A") + k) % 26 + ord("A"))
        else:
            result += char
    return result


import unittest


class TestCaesarCipher(unittest.TestCase):
    def test_basic_cases(self):
        self.assertEqual(caesarCipher("abc", 3), "def")
        self.assertEqual(caesarCipher("xyz", 2), "zab")
        self.assertEqual(caesarCipher("Hello, World!", 5), "Mjqqt, Btwqi!")
        self.assertEqual(caesarCipher("ABC", 1), "BCD")

    def test_full_cycle(self):
        self.assertEqual(caesarCipher("abc", 26), "abc")  # Full cycle
        self.assertEqual(caesarCipher("xyz", 26), "xyz")
        self.assertEqual(caesarCipher("ShiftMe", 52), "ShiftMe")  # Double full cycle

    def test_large_shifts(self):
        self.assertEqual(caesarCipher("xyz", 27), "yza")  # Overflow past 26
        self.assertEqual(caesarCipher("abc", 100), "wxy")  # Large shift
        self.assertEqual(
            caesarCipher("HelloWorld", 1000), "DahhkSknhz"
        )  # Extreme large shift

    def test_mixed_input(self):
        self.assertEqual(caesarCipher("Python-3.8", 4), "Tczxsr-3.8")  # Mixed input
        self.assertEqual(caesarCipher("1234567890", 5), "1234567890")  # Only numbers
        self.assertEqual(
            caesarCipher("!@#$%^&*()", 7), "!@#$%^&*()"
        )  # Only special characters

    def test_edge_cases(self):
        self.assertEqual(caesarCipher("", 5), "")  # Empty string
        self.assertEqual(caesarCipher("A", 1), "B")  # Single uppercase
        self.assertEqual(caesarCipher("z", 1), "a")  # Wrap-around case
        self.assertEqual(caesarCipher("Z", 1), "A")  # Uppercase wrap-around


if __name__ == "__main__":
    unittest.main()
