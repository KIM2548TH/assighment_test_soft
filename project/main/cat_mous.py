import unittest


def cat_and_mouse(x, y, z):
    distance_a = abs(x - z)
    distance_b = abs(y - z)

    if distance_a < distance_b:
        return "Cat A"
    elif distance_b < distance_a:
        return "Cat B"
    else:
        return "Mouse C"


class TestCatAndMouse(unittest.TestCase):
    def test_cat_a_wins(self):
        self.assertEqual(cat_and_mouse(2, 5, 3), "Cat A")
        self.assertEqual(cat_and_mouse(1, 1000, 500), "Cat A")

    def test_cat_b_wins(self):
        self.assertEqual(cat_and_mouse(1, 4, 3), "Cat B")
        self.assertEqual(cat_and_mouse(2, 6, 5), "Cat B")

    def test_mouse_escapes(self):
        self.assertEqual(cat_and_mouse(1, 3, 2), "Mouse C")
        self.assertEqual(cat_and_mouse(2, 4, 3), "Mouse C")
        self.assertEqual(cat_and_mouse(5, 9, 7), "Mouse C")

    def test_edge_cases(self):
        self.assertEqual(cat_and_mouse(0, 10, 5), "Mouse C")
        self.assertEqual(cat_and_mouse(10, 20, 15), "Mouse C")

    def test_one_cat_far_away(self):
        self.assertEqual(cat_and_mouse(1, 100, 2), "Cat A")
        self.assertEqual(cat_and_mouse(100, 1, 2), "Cat B")
