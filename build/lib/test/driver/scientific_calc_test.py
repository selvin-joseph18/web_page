"""To find the cosh(x) for the given value say x """

import unittest
from src.driver.scientific_calc import ScientificCalc


class ScientificCalcTest(unittest.TestCase):
    """class for unittesting"""

    def test_for_positive_number(self):
        """test case for checking a Positive number"""
        calc = ScientificCalc()
        self.assertEqual(calc.trig_cosh(1), 1.5430798443133158)

    def test_for_negative_number(self):
        """test case for checking a Positive number"""
        calc = ScientificCalc()
        self.assertEqual(calc.trig_cosh(-2), 3.762190811852014)

    def test_for_positive__floating_point_number(self):
        """test case for checking a Positive floating number"""
        calc = ScientificCalc()
        self.assertEqual(calc.trig_cosh(1.8), 3.1074696140087874)

    def test_for_zero(self):
        """test case for checking for Zero"""
        calc = ScientificCalc()
        self.assertEqual(calc.trig_cosh(0), 1)

    def test_for_string(self):
        """test case for checking for Zero"""
        calc = ScientificCalc()
        self.assertEqual(calc.trig_cosh('fgftgf'), "Value error")
