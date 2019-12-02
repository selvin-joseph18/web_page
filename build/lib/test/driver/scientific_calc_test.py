'''unit testing'''
import unittest
from src.driver.scientific_calc import ScientificCalc
from sr

class ScientificCalcTest(unittest.TestCase):
    '''write test cases'''

    def test_rad_zero(self):
        '''check for zero'''
        calc = ScientificCalc()
        self.assertEqual(calc.rad(0), 0)

    def test_rad_positive(self):
        '''check for positive integers'''
        calc = ScientificCalc()
        self.assertEqual(calc.rad(1), 0.017453292519943295)

    def test_rad_negative(self):
        '''check for negative integers'''
        calc = ScientificCalc()
        self.assertEqual(calc.rad(-1), -0.017453292519943295)

    def test_rad_posfloat(self):
        '''check for positive float '''
        calc = ScientificCalc()
        self.assertAlmostEqual(calc.rad(2.5), 0.04363323129985824)

    def test_rad_negfloat(self):
        '''check for negative float'''
        calc = ScientificCalc()
        self.assertEqual(calc.rad(-4.5), -0.07853981633974483)

    def test_rad_string(self):
        '''check for exception'''
        calc = ScientificCalc()
        self.assertEqual(calc.rad("abc"), "Value Error")
