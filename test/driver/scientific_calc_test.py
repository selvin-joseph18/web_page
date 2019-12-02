from src.driver.scientific_calc import ScientificCalc
import unittest

class ScientificCalcTest(unittest.TestCase):

    def test_positive_angle_values(self):

        scientificcalc = ScientificCalc()
        self.assertEqual(0.15425144988758405, scientificcalc.calculate_cos(30))

    def test_negative_angle_values(self):
        scientificcalc = ScientificCalc()
        self.assertEqual(-0.7596879128588213,scientificcalc.calculate_cos(-15))

    def test_float_angle_values(self):
        scientificcalc = ScientificCalc()
        self.assertEqual(0.6090559761063562, scientificcalc.calculate_cos(30.5))

    def test_type_exception(self):
        scientificcalc = ScientificCalc()
        self.assertRaises(TypeError, scientificcalc.calculate_cos('angle'))
