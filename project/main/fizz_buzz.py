import unittest


def fizzbuzz(x):
    if x % 3 == 0 and x % 5 == 0:
        return "FizzBuzz"
    elif x % 3 == 0:
        return "Fizz"
    elif x % 5 == 0:
        return "Buzz"
    else:
        return str(x)


class TestFizzBuzz(unittest.TestCase):
    def test_divisible_by_three(self):
        self.assertEqual(fizzbuzz(3), "Fizz")
        self.assertEqual(fizzbuzz(9), "Fizz")
        self.assertEqual(fizzbuzz(-3), "Fizz")

    def test_divisible_by_five(self):
        self.assertEqual(fizzbuzz(5), "Buzz")
        self.assertEqual(fizzbuzz(10), "Buzz")
        self.assertEqual(fizzbuzz(-5), "Buzz")

    def test_divisible_by_three_and_five(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
        self.assertEqual(fizzbuzz(30), "FizzBuzz")
        self.assertEqual(fizzbuzz(-15), "FizzBuzz")
        self.assertEqual(fizzbuzz(0), "FizzBuzz")  # Special case

    def test_not_divisible_by_three_or_five(self):
        self.assertEqual(fizzbuzz(1), "1")
        self.assertEqual(fizzbuzz(7), "7")
        self.assertEqual(fizzbuzz(1001), "1001")
        self.assertEqual(fizzbuzz(-7), "-7")

    def test_large_numbers(self):
        self.assertEqual(fizzbuzz(300), "FizzBuzz")
        self.assertEqual(fizzbuzz(999), "Fizz")
        self.assertEqual(fizzbuzz(1000), "Buzz")
