import unittest
from math_functions import power, divide

class TestMathFunctions(unittest.TestCase):
    def test_power(self):
        self.assertEqual(power(2,2), 4)
        self.assertEqual(power(3,2), 9)
        self.assertEqual(power(4,3), 64)
    def test_power_zero(self):
        self.assertEqual(power(2,0), 1)
        self.assertEqual(power(3,0), 1)
        self.assertEqual(power(4,0), 1)
    def test_power_negative(self):
        self.assertEqual(power(2,-2), 0.25)
        self.assertEqual(power(2,-3), 0.125)
        self.assertEqual(power(4,-2), 0.0625)
    def test_power_decimal(self):
        self.assertEqual(power(4,0.5), 2)
        self.assertEqual(power(4,1.5), 8)
        self.assertEqual(power(4,4.5), 512)
    def test_divide(self):
        self.assertEqual(divide(4,2), 2)
        self.assertEqual(divide(9,3), 3)
        self.assertEqual(divide(16,4), 4)
    def test_divide_zero(self):
        self.assertEqual(divide(4,0), None)
        self.assertEqual(divide(10,0), None)
        self.assertEqual(divide(12,0), None)
    def test_divide_decimal(self):
        self.assertEqual(divide(4,0.5), 8)
        self.assertEqual(divide(8,0.25), 32)
        self.assertEqual(divide(9,0.75), 12)
    def test_divide_negative(self):
        self.assertEqual(divide(4,-2), -2)
        self.assertEqual(divide(8,-4), -2)
        self.assertEqual(divide(10,-2), -5)

    if __name__ == '__main__': unittest.main()
