import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-1, -2), -3)

    # Add the following test methods to the TestCalculator class:
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(6, 7), -1)
        self.assertEqual(self.calc.subtract(-6, -7), 1)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(6, 7), 42)
        self.assertEqual(self.calc.multiply(-6, -7), 42)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 7), 0)
        self.assertEqual(self.calc.divide(6, 0), "Can not divided by zero")

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(6, 7), 6)
        self.assertEqual(self.calc.modulo(-6, 7), 1)

if __name__ == '__main__':
    unittest.main()