"""This module is used to unit test the scientific operation"""
import unittest
from src.driver.scientific_calc import ScientificCalc


class ScientificCalcTest(unittest.TestCase):
    """This class is used to test the scientific operations"""

    def test_case_positive(self):
        """test case for sin(30)"""
        calc = ScientificCalc()
        self.assertEqual(calc.sin_func('30'), -0.9880316240928618)

    def test_case3_negative(self):
        """test case for sin(-30)"""
        calc = ScientificCalc()
        self.assertEqual(calc.sin_func('-30'), 0.9880316240928618)

    def test_case3_float(self):
        """test case for sin(30.8)"""
        calc = ScientificCalc()
        self.assertEqual(calc.sin_func('30.8'), -0.5777150444457317)

    def test_case2_exception(self):
        """test case for sin(string)"""
        calc = ScientificCalc()
        self.assertEqual(calc.sin_func('string'), 'Please enter float or integer types input.')
