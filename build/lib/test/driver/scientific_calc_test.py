"""Test Cases for e_power_x"""
import unittest
from src.driver.scientific_calc import ScientificCalc


class ScientificCalcTest(unittest.TestCase):
    """functions are defined for checking the main cases"""

    def test_positive_exp(self):
        "When the input is positive integer"
        obj_exp = ScientificCalc()
        self.assertEqual(obj_exp.exponential_func(2), 2.71828182846 ** 2)

    def test_negative_exp(self):
        "When the input is negative integer"
        obj_exp = ScientificCalc()
        self.assertEqual(obj_exp.exponential_func(-2), 2.71828182846 ** -2)

    def test_zero_exp(self):
        "When the input is zero"
        obj_exp = ScientificCalc()
        self.assertEqual(obj_exp.exponential_func(0), 2.71828182846 ** 0)

    def test_pos_decimal_exp(self):
        "When the input is positive decimal"
        obj_exp = ScientificCalc()
        self.assertEqual(obj_exp.exponential_func(8.6), 2.71828182846 ** 8.6)

    def test_neg_decimal_exp(self):
        "When the input is negative decimal"
        obj_exp = ScientificCalc()
        self.assertEqual(obj_exp.exponential_func(-8.6), 2.71828182846 ** -8.6)

    def test_try_except(self):
        "Test case for try and except"
        obj_exp = ScientificCalc()
        self.assertEqual(obj_exp.exponential_func('accenture'),
                         "Please enter float or integer types input.")
