import calc
import unittest


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 5), 4)
        self.assertEqual(calc.add(-19, 19), 0)

    def test_substract(self):
        self.assertEqual(calc.substract(10, 5), 5)
        self.assertEqual(calc.substract(-1, 5), -6)
        self.assertEqual(calc.substract(-3, 3), -6)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 5), -5)
        self.assertEqual(calc.multiply(-19, -1), 19)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2.0)
        self.assertEqual(calc.divide(-10, 5), -2.0)
        self.assertEqual(calc.divide(-21, -3), 7.0)
        self.assertRaises(ValueError, calc.divide, 10, 0)

        # using assertRaises() method in a context manager
        with self.assertRaises(ValueError):
            calc.divide(10, 0)


if __name__ == "__main__":
    unittest.main()
