"""unit test cases for ln function"""
import unittest
from src.driver.scientific_calc import ScientificCalc


class ScientificCalc_Test(unittest.TestCase):
    """checks for postive value"""
    def test_ln_postive(self):
        """checks for positive value"""
        result = ScientificCalc()
        self.assertEqual(result.ln_func(2), 0.6931471805599453)

    def test_ln_negative(self):
        """checks for negative value"""
        result = ScientificCalc()
        self.assertEqual(result.ln_func(-2), "-NAN-")

    def test_ln_zero(self):
        """checks for zero value"""
        result = ScientificCalc()
        self.assertEqual(result.ln_func(0), "infinity")

    def test_ln_type(self):
        """checks for zero value"""
        result = ScientificCalc()
        self.assertEqual(result.ln_func("ram"), "string is not accepted")



if __name__ == '__main__':
    unittest.main()