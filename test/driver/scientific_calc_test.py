"""module to test calculator"""
import unittest
from src.driver.scientific_calc import ScientificCalc


class ScientificCalcTest(unittest.TestCase):
    """A class for all test cases"""
    def test_tanh_integer(self):
        """test case for tanh(4)"""
        calc = ScientificCalc()
        self.assertEqual(calc.calculate_tanh(4), 0.9993292997390669)

    def test_tanh_zero(self):
        """test case for tanh(0)"""
        calc = ScientificCalc()
        self.assertEqual(calc.calculate_tanh(0), 0.0)

    def test_tanh_integer500(self):
        """test case for tanh(500)"""
        calc = ScientificCalc()
        self.assertEqual(calc.calculate_tanh(500), 1.0)

    def test_tanh_negative(self):
        """test case for tanh(-14)"""
        calc = ScientificCalc()
        self.assertEqual(calc.calculate_tanh(-14), -0.9999999999986172)

    def test_tanh_float(self):
        """test case for tanh(8.9)"""
        calc = ScientificCalc()
        self.assertEqual(calc.calculate_tanh(8.1), 0.9999998157280002)

    def test_tanh_fnegative(self):
        """test case for tanh(-55.7)"""
        calc = ScientificCalc()
        self.assertEqual(calc.calculate_tanh(-55.7), -1.0)

    def test_tanh_string(self):
        """test case for tanh(-55.7)"""
        calc = ScientificCalc()
        self.assertEqual(calc.calculate_tanh("sss"), "value error(enter a number)")
